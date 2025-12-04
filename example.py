import dora_client
from dora_client.models.asset_kind import AssetKind  # noqa: E501
from dora_client.models import *
from dora_client.rest import ApiException
from dora_client import Configuration
import json
import pprint
from websocket import WebSocketApp
import threading
import logging


TOKEN = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjNzQ5NTFmNjBhMDE0NzE3ZjFlMzA4ZDZiMjgwZjQ4ZjFlODhmZGEiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiU2FpIEt1bWFyIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FDZzhvY0lCUmU5My00cndwMXNBMFJ3RmhESGdudDFhblo4bExNNlkyYjdPUUlWbXBKRjJSdz1zOTYtYyIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9kb3JhLWFscGhhLWRldiIsImF1ZCI6ImRvcmEtYWxwaGEtZGV2IiwiYXV0aF90aW1lIjoxNzY0ODM5MTg3LCJ1c2VyX2lkIjoia1lmNXRqaTBMRlRVamNnUVdIYVF4YjkzZlBBMiIsInN1YiI6ImtZZjV0amkwTEZUVWpjZ1FXSGFReGI5M2ZQQTIiLCJpYXQiOjE3NjQ4NDY2ODUsImV4cCI6MTc2NDg1MDI4NSwiZW1haWwiOiJzYWlAZG9yYS50ZWNoIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZ29vZ2xlLmNvbSI6WyIxMDU0MjE1MTMwNjIzMDg1MTU1OTMiXSwiZW1haWwiOlsic2FpQGRvcmEudGVjaCJdfSwic2lnbl9pbl9wcm92aWRlciI6Imdvb2dsZS5jb20iLCJ0ZW5hbnQiOiJkb3JhLXVpLTE2Y3NhIn19.EQyUSmEHHOr2EvAomt6sycIg-gsUhcTYVL0HEULwVlgTsa-Pwc0wd3ljmKIdmetUvrG5byl_D9LW5WZ7XYy90mAnkZhECe537WaJvE79a6PaBgr_dumTVBOueQ3-ZX45Dqh5gDJ_bTBsZk0Mtn5FopzzFYCdpG4GOu_EUjZNCv1K08HrbkIjpx3V-zNunydJ3BqzJvrvOUn0Vsq8WNDzh1PDeC904Prs2lw25vQkACFIY0hGJ5uGaTfaL9VZbIV36yHt54znQb0O8tRLXpCShFPTygw3OQK6qqjqHA4x5Ja9jaRV-7Pv-uXtmFFTvL7divxD-Jf8NoZkX31WV-EERw"


# configuration for connecting the dora api
config = Configuration()
config.host = "https://dora-dev.fly.dev/"
config.debug = False

# init api client
api_client = dora_client.ApiClient(configuration=config)
api_client.default_headers["Authorization"] = f"Bearer {TOKEN}"

# create an instance of the API class
api_instance = dora_client.DefaultApi(api_client=api_client)


def init_logger():
    logger = logging.getLogger("main_logger")
    logger.setLevel(logging.INFO)

    # Stream handler to output to terminal in plain text
    stream_handler = logging.StreamHandler()
    stream_formatter = logging.Formatter(
        '[%(asctime)s][%(levelname)s][%(name)s]: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    stream_handler.setFormatter(stream_formatter)
    logger.addHandler(stream_handler)

    return logger


def print_local(data: any):
    pprint.pprint(data, indent=4)


class RealTimeWebsocket(threading.Thread):
    host = None
    token = None

    def __init__(self, logger: any, host: str, url: str, token: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.host = f'{host}{url}?token={token}'
        self.logger = logger
        self.logger.info(f"streaming url :{self.host}")
        self.token = token
        self.ws = WebSocketApp(
            url=self.host,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
            on_open=self.on_open,
        )

    def on_message(self, ws, message):
        if message == "PONG":
            return
        try:
            message = json.loads(message)
            self.logger.info(message)
        except Exception as e:
            self.logger.error(f"error on on_message {e}")
            return

    def on_error(self, ws, error):
        self.logger.error(
            f"error while init real time price feed client host {error}")
        self._running = False
        ws.close()

    def on_close(self, ws, close_status_code, close_msg):
        self.logger.error(
            f"closed due to {close_status_code} and msg : {close_msg}")
        self._running = False

    def on_open(self, ws):
        pass

    def run(self):
        try:
            self.ws.run_forever()
        except KeyboardInterrupt:
            self.logger.error("WebSocket closed by user interrupt")
        finally:
            self._running = False


try:
    logger = init_logger()

    # we can get the orderbook id by below list of orderbooks or we can get from website
    order_book_id = "019a3b42-e73d-7bc8-83ad-044e9b4f8f97"
    # r: ListOrderBooksResponse = api_instance.list_order_books()
    # data = r.get("data", [])
    # for i in range(len(data)):
    #     order_book_id = data[i].get("order_book_id")
    #     logger.info(f"getting the order_book :{order_book_id}")
    #     or_resp: GetOrderBookResponse = api_instance.get_orderbook_by_id(
    #         order_book_id=order_book_id)
    #     logger.info(or_resp)

    # r: ListAssetsResponse = api_instance.list_assets()
    # data = r.get("data", [])
    # for i in range(len(data)):
    #     id = data[i].get("id")
    #     or_resp: GetOrderBookResponse = api_instance.get_asset_by_id(id)
    #     logger.info(or_resp)
    # user_config_resp: GetUserConfigResponse = api_instance.get_user_config_self()
    # logger.info(user_config_resp)

    user_positions_resp: UserBalanceResponse = api_instance.get_ledger_balances_self()
    user_position = user_positions_resp.get("data", {})
    balances = user_position.get("balances", [])
    position_id = None
    order_amount = 100.0
    for i in range(0, len(balances)):
        if float(balances[i]["available"]) > order_amount:
            position_id = balances[i]["id"]
            break

    logger.info(
        f"creating market order on order_book: {order_book_id} with position_id: {position_id} and order_amount :{order_amount}")

    order_req: CreateOrderRequest = CreateOrderRequest(
        quantity="10",
        inverse_leverage='1',
        kind=OrderKind.MARKET,
        side=Side.BUY,
        position_id=position_id,
        order_book_id=order_book_id
    )
    coresp: CreateOrderResponse = api_instance.create_order(order_req)
    logger.info(f"buy order id :{coresp.get("data", {}).get("order_id")}")

    logger.info("Selling buy quantity with market order")
    sell_order_req: CreateOrderRequest = CreateOrderRequest(
        quantity="10",
        inverse_leverage='1',
        kind=OrderKind.MARKET,
        side=Side.SELL,
        position_id=position_id,
        order_book_id=order_book_id,
    )
    coresp: CreateOrderResponse = api_instance.create_order(sell_order_req)
    logger.info(f"sell order id :{coresp.get("data", {}).get("order_id")}")
    # prices_stream = RealTimeWebsocket(
    #     logger, config.host.replace("https://", "wss://").replace("fly.dev", "fly.dev:8085"), "v1/prices/stream", TOKEN)
    # prices_stream.start()
    # try:
    #     while True:
    #         pass
    #         time.sleep(0.1)
    # except KeyboardInterrupt:
    #     logger.info("Shutting down...")
except ApiException as e:
    if e.body:
        try:
            error_json = json.loads(e.body.decode(
                'utf-8') if isinstance(e.body, bytes) else e.body)
            logger.info(json.dumps(error_json, indent=2))
        except Exception as parse_exc:
            logger.error("Failed to parse error body as JSON:", parse_exc)
            logger.error(e.body)
except Exception as e:
    logger.error("Exception when calling : %s\n" % e)
