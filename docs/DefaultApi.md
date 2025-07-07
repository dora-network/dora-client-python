# dora_client.DefaultApi

All URIs are relative to *https://localhost:8080/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_all_open_orders**](DefaultApi.md#cancel_all_open_orders) | **DELETE** /orders | Cancel all open orders
[**cancel_order_by_id**](DefaultApi.md#cancel_order_by_id) | **DELETE** /orders/{order_id} | Cancel an order by ID
[**create_order**](DefaultApi.md#create_order) | **POST** /orders | Create a new order
[**delete_user**](DefaultApi.md#delete_user) | **DELETE** /user/{id} | Delete user by ID
[**get_all_asset_prices**](DefaultApi.md#get_all_asset_prices) | **GET** /price | Get the current price of all assets
[**get_asset_by_id**](DefaultApi.md#get_asset_by_id) | **GET** /assets/{id} | Get asset by ID
[**get_asset_price**](DefaultApi.md#get_asset_price) | **GET** /price/asset/{asset_id} | Get the current price of an asset
[**get_candle_data**](DefaultApi.md#get_candle_data) | **GET** /charts/candle/{orderbook} | Get candlestick data for an orderbook
[**get_coupons_by_asset_id**](DefaultApi.md#get_coupons_by_asset_id) | **GET** /assets/{id}/coupons | Get coupons for a bond asset
[**get_l3_depth**](DefaultApi.md#get_l3_depth) | **GET** /orderbooks/{id}/orders | Get all open orders for a specific orderbook (L3 market depth)
[**get_l3_depth_0**](DefaultApi.md#get_l3_depth_0) | **GET** /orderbooks/{id}/L3 | Get all open orders for a specific orderbook (L3 market depth)
[**get_ledger_balances_self**](DefaultApi.md#get_ledger_balances_self) | **GET** /ledger/balances/self | Get your own available, locked, and borrowed assets
[**get_ledger_interest_self**](DefaultApi.md#get_ledger_interest_self) | **GET** /ledger/interest/self | Get your own interest
[**get_ledger_module**](DefaultApi.md#get_ledger_module) | **GET** /ledger/module | Get the entire module object, including unborrowed leverage assets and total leverage trackers
[**get_ledger_module_by_asset**](DefaultApi.md#get_ledger_module_by_asset) | **GET** /ledger/module/{asset_id} | Get the module object for a single asset ID
[**get_ledger_positions_self**](DefaultApi.md#get_ledger_positions_self) | **GET** /ledger/positions/self | Get your own positions
[**get_ledger_value_self**](DefaultApi.md#get_ledger_value_self) | **GET** /ledger/value/self | Get your own available, locked, and borrowed USD value; and realized and unrealized PnL
[**get_order_by_id**](DefaultApi.md#get_order_by_id) | **GET** /orders/{order_id} | Get order by ID
[**get_orderbook_by_id**](DefaultApi.md#get_orderbook_by_id) | **GET** /orderbooks/{id} | Get orderbook by ID
[**get_orderbook_depth**](DefaultApi.md#get_orderbook_depth) | **GET** /orderbooks/{id}/depth | Get the aggregated price levels for a specific orderbook (L2 market depth)
[**get_orderbook_depth_0**](DefaultApi.md#get_orderbook_depth_0) | **GET** /orderbooks/{id}/L2 | Get the aggregated price levels for a specific orderbook (L2 market depth)
[**get_orderbook_summary**](DefaultApi.md#get_orderbook_summary) | **GET** /orderbooks/{id}/summary | Get summary of an orderbook
[**get_orderbook_top**](DefaultApi.md#get_orderbook_top) | **GET** /orderbooks/{id}/top | Get the top price levels for a specific orderbook (L1 market depth)
[**get_orderbook_top_0**](DefaultApi.md#get_orderbook_top_0) | **GET** /orderbooks/{id}/L1 | Get the top price levels for a specific orderbook (L1 market depth)
[**get_pool_price**](DefaultApi.md#get_pool_price) | **GET** /price/pool/{pool_id} | Get the current price of a pool
[**get_trade_by_id**](DefaultApi.md#get_trade_by_id) | **GET** /trade/{id} | Get a trade by ID
[**get_trades**](DefaultApi.md#get_trades) | **GET** /trade | Get a filtered, paginated list of trades
[**get_transaction_by_id**](DefaultApi.md#get_transaction_by_id) | **GET** /transactions/{id} | Get a transaction by ID
[**get_transactions**](DefaultApi.md#get_transactions) | **GET** /transactions | Get a filtered, paginated list of transactions
[**get_user_by_id**](DefaultApi.md#get_user_by_id) | **GET** /user/{id} | Get user by ID
[**get_user_ledger_stream**](DefaultApi.md#get_user_ledger_stream) | **GET** /user/{id}/ledger/stream | Get a snapshot of user&#x27;s ledger updates since a specific time, and opens a stream for further updates
[**get_user_orders_stream**](DefaultApi.md#get_user_orders_stream) | **GET** /user/{id}/orders/stream | Get a snapshot of user&#x27;s order updates since a specific time, and opens a stream for further updates
[**get_user_transactions_stream**](DefaultApi.md#get_user_transactions_stream) | **GET** /user/{id}/transactions/stream | Get a snapshot of user&#x27;s executed transactions since a specific time, and opens a stream for further updates
[**ledger_deposit**](DefaultApi.md#ledger_deposit) | **POST** /ledger/deposit | Deposit assets into your account from the outside world
[**ledger_withdraw**](DefaultApi.md#ledger_withdraw) | **POST** /ledger/withdraw | Withdraw assets from your account to the outside world
[**leverage_borrow**](DefaultApi.md#leverage_borrow) | **POST** /leverage/borrow | Directly borrow assets
[**leverage_isolate_collateral**](DefaultApi.md#leverage_isolate_collateral) | **POST** /leverage/isolate_collateral | Create an isolated position by transferring collateral to the position from the user&#x27;s global collateral
[**leverage_isolate_position**](DefaultApi.md#leverage_isolate_position) | **POST** /leverage/isolate_position | Create an isolated position using all collateral, supplied_collateral, and borrows from the user&#x27;s global position
[**leverage_repay**](DefaultApi.md#leverage_repay) | **POST** /leverage/repay | Repay borrowed assets
[**leverage_supply**](DefaultApi.md#leverage_supply) | **POST** /leverage/supply | Supply leverage for a specific asset
[**leverage_unite**](DefaultApi.md#leverage_unite) | **POST** /leverage/unite | Combines all isolated positions into a single global position
[**leverage_withdraw**](DefaultApi.md#leverage_withdraw) | **POST** /leverage/withdraw | Withdraw leverage for a specific asset
[**liquidity_add**](DefaultApi.md#liquidity_add) | **POST** /liquidity/pool/{pool_id}/add | Add liquidity to a pool
[**liquidity_subtract**](DefaultApi.md#liquidity_subtract) | **POST** /liquidity/pool/{pool_id}/subtract | Subtract liquidity from a pool
[**list_assets**](DefaultApi.md#list_assets) | **GET** /assets | List assets
[**list_order_books**](DefaultApi.md#list_order_books) | **GET** /orderbooks | List order books
[**list_orders**](DefaultApi.md#list_orders) | **GET** /orders | List all orders
[**stream_asset_prices**](DefaultApi.md#stream_asset_prices) | **GET** /price/stream | Get a snapshot of asset prices from a specific date and open a stream for real-time updates
[**stream_candle_data**](DefaultApi.md#stream_candle_data) | **GET** /charts/candle/stream/{orderbook} | Get a snapshot of candlestick data from date provided, and open a stream for real-time updates
[**stream_order_book_balances**](DefaultApi.md#stream_order_book_balances) | **GET** /orderbooks/{id}/stream/balances | Get a snapshot of base and quote balances for an order book and open a stream for real-time updates
[**stream_orderbook_open_orders**](DefaultApi.md#stream_orderbook_open_orders) | **GET** /orderbooks/{id}/stream/open | Get a snapshot of open orders in an order book and open a stream for real-time updates
[**stream_trades**](DefaultApi.md#stream_trades) | **GET** /trade/stream | Get a snapshot of trades from a specific date and open a stream for real-time updates
[**update_user_config**](DefaultApi.md#update_user_config) | **PUT** /user/{id}/config | Update user configuration by ID
[**verify_user**](DefaultApi.md#verify_user) | **PUT** /user/{id}/verify | Verify a user by ID

# **cancel_all_open_orders**
> InlineResponse20015 cancel_all_open_orders()

Cancel all open orders

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()

try:
    # Cancel all open orders
    api_response = api_instance.cancel_all_open_orders()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->cancel_all_open_orders: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_order_by_id**
> InlineResponse204 cancel_order_by_id(order_id)

Cancel an order by ID

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
order_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Cancel an order by ID
    api_response = api_instance.cancel_order_by_id(order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->cancel_order_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | [**str**](.md)|  | 

### Return type

[**InlineResponse204**](InlineResponse204.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_order**
> OrderId create_order(body)

Create a new order

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
body = dora_client.CreateOrderRequest() # CreateOrderRequest | 

try:
    # Create a new order
    api_response = api_instance.create_order(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateOrderRequest**](CreateOrderRequest.md)|  | 

### Return type

[**OrderId**](OrderId.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> InlineResponse2004 delete_user(id)

Delete user by ID

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Delete user by ID
    api_response = api_instance.delete_user(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_asset_prices**
> InlineResponse20028 get_all_asset_prices()

Get the current price of all assets

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()

try:
    # Get the current price of all assets
    api_response = api_instance.get_all_asset_prices()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_all_asset_prices: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_by_id**
> InlineResponse2001 get_asset_by_id(id)

Get asset by ID

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Get asset by ID
    api_response = api_instance.get_asset_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_asset_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_price**
> InlineResponse20029 get_asset_price(asset_id)

Get the current price of an asset

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Get the current price of an asset
    api_response = api_instance.get_asset_price(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_asset_price: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | [**str**](.md)|  | 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_candle_data**
> InlineResponse20017 get_candle_data(orderbook, start=start, end=end, resolution=resolution)

Get candlestick data for an orderbook

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
orderbook = 'orderbook_example' # str | 
start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
resolution = 'resolution_example' # str |  (optional)

try:
    # Get candlestick data for an orderbook
    api_response = api_instance.get_candle_data(orderbook, start=start, end=end, resolution=resolution)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_candle_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orderbook** | **str**|  | 
 **start** | **datetime**|  | [optional] 
 **end** | **datetime**|  | [optional] 
 **resolution** | **str**|  | [optional] 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coupons_by_asset_id**
> InlineResponse2002 get_coupons_by_asset_id(id, start=start, end=end, page=page, limit=limit)

Get coupons for a bond asset

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
page = 1 # int |  (optional) (default to 1)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get coupons for a bond asset
    api_response = api_instance.get_coupons_by_asset_id(id, start=start, end=end, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_coupons_by_asset_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **start** | **datetime**|  | [optional] 
 **end** | **datetime**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_l3_depth**
> InlineResponse2006 get_l3_depth(id)

Get all open orders for a specific orderbook (L3 market depth)

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Get all open orders for a specific orderbook (L3 market depth)
    api_response = api_instance.get_l3_depth(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_l3_depth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_l3_depth_0**
> InlineResponse2006 get_l3_depth_0(id)

Get all open orders for a specific orderbook (L3 market depth)

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Get all open orders for a specific orderbook (L3 market depth)
    api_response = api_instance.get_l3_depth_0(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_l3_depth_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ledger_balances_self**
> InlineResponse20021 get_ledger_balances_self()

Get your own available, locked, and borrowed assets

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()

try:
    # Get your own available, locked, and borrowed assets
    api_response = api_instance.get_ledger_balances_self()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_ledger_balances_self: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ledger_interest_self**
> InlineResponse20023 get_ledger_interest_self()

Get your own interest

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()

try:
    # Get your own interest
    api_response = api_instance.get_ledger_interest_self()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_ledger_interest_self: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ledger_module**
> InlineResponse20018 get_ledger_module()

Get the entire module object, including unborrowed leverage assets and total leverage trackers

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()

try:
    # Get the entire module object, including unborrowed leverage assets and total leverage trackers
    api_response = api_instance.get_ledger_module()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_ledger_module: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ledger_module_by_asset**
> InlineResponse20019 get_ledger_module_by_asset(asset_id)

Get the module object for a single asset ID

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Get the module object for a single asset ID
    api_response = api_instance.get_ledger_module_by_asset(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_ledger_module_by_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | [**str**](.md)|  | 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ledger_positions_self**
> InlineResponse20020 get_ledger_positions_self()

Get your own positions

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()

try:
    # Get your own positions
    api_response = api_instance.get_ledger_positions_self()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_ledger_positions_self: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ledger_value_self**
> InlineResponse20022 get_ledger_value_self()

Get your own available, locked, and borrowed USD value; and realized and unrealized PnL

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()

try:
    # Get your own available, locked, and borrowed USD value; and realized and unrealized PnL
    api_response = api_instance.get_ledger_value_self()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_ledger_value_self: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_by_id**
> InlineResponse20016 get_order_by_id(order_id)

Get order by ID

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
order_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Get order by ID
    api_response = api_instance.get_order_by_id(order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_order_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | [**str**](.md)|  | 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orderbook_by_id**
> InlineResponse20010 get_orderbook_by_id(id)

Get orderbook by ID

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Get orderbook by ID
    api_response = api_instance.get_orderbook_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_orderbook_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orderbook_depth**
> InlineResponse20011 get_orderbook_depth(id)

Get the aggregated price levels for a specific orderbook (L2 market depth)

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Get the aggregated price levels for a specific orderbook (L2 market depth)
    api_response = api_instance.get_orderbook_depth(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_orderbook_depth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orderbook_depth_0**
> InlineResponse20011 get_orderbook_depth_0(id)

Get the aggregated price levels for a specific orderbook (L2 market depth)

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Get the aggregated price levels for a specific orderbook (L2 market depth)
    api_response = api_instance.get_orderbook_depth_0(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_orderbook_depth_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orderbook_summary**
> InlineResponse20013 get_orderbook_summary(id)

Get summary of an orderbook

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Get summary of an orderbook
    api_response = api_instance.get_orderbook_summary(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_orderbook_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orderbook_top**
> InlineResponse20012 get_orderbook_top(id)

Get the top price levels for a specific orderbook (L1 market depth)

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Get the top price levels for a specific orderbook (L1 market depth)
    api_response = api_instance.get_orderbook_top(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_orderbook_top: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orderbook_top_0**
> InlineResponse20012 get_orderbook_top_0(id)

Get the top price levels for a specific orderbook (L1 market depth)

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Get the top price levels for a specific orderbook (L1 market depth)
    api_response = api_instance.get_orderbook_top_0(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_orderbook_top_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pool_price**
> InlineResponse20030 get_pool_price(pool_id)

Get the current price of a pool

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
pool_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Get the current price of a pool
    api_response = api_instance.get_pool_price(pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_pool_price: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | [**str**](.md)|  | 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trade_by_id**
> InlineResponse20027 get_trade_by_id(id)

Get a trade by ID

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Get a trade by ID
    api_response = api_instance.get_trade_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_trade_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trades**
> InlineResponse20026 get_trades(pools=pools, user_ids=user_ids, start=start, end=end, page=page, limit=limit)

Get a filtered, paginated list of trades

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
pools = ['pools_example'] # list[str] |  (optional)
user_ids = ['user_ids_example'] # list[str] |  (optional)
start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
page = 1 # int |  (optional) (default to 1)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get a filtered, paginated list of trades
    api_response = api_instance.get_trades(pools=pools, user_ids=user_ids, start=start, end=end, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_trades: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pools** | [**list[str]**](str.md)|  | [optional] 
 **user_ids** | [**list[str]**](str.md)|  | [optional] 
 **start** | **datetime**|  | [optional] 
 **end** | **datetime**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_by_id**
> InlineResponse20025 get_transaction_by_id(id)

Get a transaction by ID

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Get a transaction by ID
    api_response = api_instance.get_transaction_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_transaction_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions**
> InlineResponse2008 get_transactions(pools=pools, user_ids=user_ids, tx_kinds=tx_kinds, start=start, end=end, page=page, limit=limit)

Get a filtered, paginated list of transactions

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
pools = ['pools_example'] # list[str] |  (optional)
user_ids = ['user_ids_example'] # list[str] |  (optional)
tx_kinds = ['tx_kinds_example'] # list[str] |  (optional)
start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
page = 1 # int |  (optional) (default to 1)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get a filtered, paginated list of transactions
    api_response = api_instance.get_transactions(pools=pools, user_ids=user_ids, tx_kinds=tx_kinds, start=start, end=end, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pools** | [**list[str]**](str.md)|  | [optional] 
 **user_ids** | [**list[str]**](str.md)|  | [optional] 
 **tx_kinds** | [**list[str]**](str.md)|  | [optional] 
 **start** | **datetime**|  | [optional] 
 **end** | **datetime**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_id**
> InlineResponse2003 get_user_by_id(id)

Get user by ID

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Get user by ID
    api_response = api_instance.get_user_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_user_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_ledger_stream**
> InlineResponse2007 get_user_ledger_stream(id, since=since)

Get a snapshot of user's ledger updates since a specific time, and opens a stream for further updates

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
since = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    # Get a snapshot of user's ledger updates since a specific time, and opens a stream for further updates
    api_response = api_instance.get_user_ledger_stream(id, since=since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_user_ledger_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **since** | **datetime**|  | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_orders_stream**
> InlineResponse2006 get_user_orders_stream(id, since=since, orderbook_ids=orderbook_ids)

Get a snapshot of user's order updates since a specific time, and opens a stream for further updates

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
since = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
orderbook_ids = ['orderbook_ids_example'] # list[str] |  (optional)

try:
    # Get a snapshot of user's order updates since a specific time, and opens a stream for further updates
    api_response = api_instance.get_user_orders_stream(id, since=since, orderbook_ids=orderbook_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_user_orders_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **since** | **datetime**|  | [optional] 
 **orderbook_ids** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_transactions_stream**
> InlineResponse2008 get_user_transactions_stream(id, since=since)

Get a snapshot of user's executed transactions since a specific time, and opens a stream for further updates

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
since = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    # Get a snapshot of user's executed transactions since a specific time, and opens a stream for further updates
    api_response = api_instance.get_user_transactions_stream(id, since=since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_user_transactions_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **since** | **datetime**|  | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ledger_deposit**
> InlineResponse201 ledger_deposit(body)

Deposit assets into your account from the outside world

TODO: finish this when implementation has been completed

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
body = dora_client.FundUserRequest() # FundUserRequest | 

try:
    # Deposit assets into your account from the outside world
    api_response = api_instance.ledger_deposit(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ledger_deposit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FundUserRequest**](FundUserRequest.md)|  | 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ledger_withdraw**
> InlineResponse201 ledger_withdraw(body)

Withdraw assets from your account to the outside world

TODO: Finish this when implementation has been completed

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
body = dora_client.FundUserRequest() # FundUserRequest | 

try:
    # Withdraw assets from your account to the outside world
    api_response = api_instance.ledger_withdraw(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ledger_withdraw: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FundUserRequest**](FundUserRequest.md)|  | 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leverage_borrow**
> InlineResponse2013 leverage_borrow(body)

Directly borrow assets

TODO: Finish this when implementation has been completed

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
body = NULL # dict | 

try:
    # Directly borrow assets
    api_response = api_instance.leverage_borrow(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->leverage_borrow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict**](dict.md)|  | 

### Return type

[**InlineResponse2013**](InlineResponse2013.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leverage_isolate_collateral**
> InlineResponse2014 leverage_isolate_collateral(body)

Create an isolated position by transferring collateral to the position from the user's global collateral

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
body = dora_client.IsolateCollateralRequest() # IsolateCollateralRequest | 

try:
    # Create an isolated position by transferring collateral to the position from the user's global collateral
    api_response = api_instance.leverage_isolate_collateral(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->leverage_isolate_collateral: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IsolateCollateralRequest**](IsolateCollateralRequest.md)|  | 

### Return type

[**InlineResponse2014**](InlineResponse2014.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leverage_isolate_position**
> InlineResponse2015 leverage_isolate_position(body)

Create an isolated position using all collateral, supplied_collateral, and borrows from the user's global position

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
body = dora_client.IsolatePositionRequest() # IsolatePositionRequest | 

try:
    # Create an isolated position using all collateral, supplied_collateral, and borrows from the user's global position
    api_response = api_instance.leverage_isolate_position(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->leverage_isolate_position: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IsolatePositionRequest**](IsolatePositionRequest.md)|  | 

### Return type

[**InlineResponse2015**](InlineResponse2015.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leverage_repay**
> InlineResponse2013 leverage_repay(body)

Repay borrowed assets

TODO: Finish this when implementation has been completed

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
body = NULL # dict | 

try:
    # Repay borrowed assets
    api_response = api_instance.leverage_repay(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->leverage_repay: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict**](dict.md)|  | 

### Return type

[**InlineResponse2013**](InlineResponse2013.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leverage_supply**
> InlineResponse2011 leverage_supply(body)

Supply leverage for a specific asset

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
body = dora_client.SupplyRequest() # SupplyRequest | 

try:
    # Supply leverage for a specific asset
    api_response = api_instance.leverage_supply(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->leverage_supply: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SupplyRequest**](SupplyRequest.md)|  | 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leverage_unite**
> InlineResponse20024 leverage_unite(body)

Combines all isolated positions into a single global position

TODO: Finish this when implementation has been completed

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
body = dora_client.UnitePositionRequest() # UnitePositionRequest | 

try:
    # Combines all isolated positions into a single global position
    api_response = api_instance.leverage_unite(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->leverage_unite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnitePositionRequest**](UnitePositionRequest.md)|  | 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leverage_withdraw**
> InlineResponse2012 leverage_withdraw(body)

Withdraw leverage for a specific asset

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
body = dora_client.WithdrawRequest() # WithdrawRequest | 

try:
    # Withdraw leverage for a specific asset
    api_response = api_instance.leverage_withdraw(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->leverage_withdraw: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WithdrawRequest**](WithdrawRequest.md)|  | 

### Return type

[**InlineResponse2012**](InlineResponse2012.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **liquidity_add**
> InlineResponse2016 liquidity_add(body, pool_id)

Add liquidity to a pool

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
body = dora_client.LiquidityRequest() # LiquidityRequest | 
pool_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Add liquidity to a pool
    api_response = api_instance.liquidity_add(body, pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->liquidity_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LiquidityRequest**](LiquidityRequest.md)|  | 
 **pool_id** | [**str**](.md)|  | 

### Return type

[**InlineResponse2016**](InlineResponse2016.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **liquidity_subtract**
> InlineResponse2016 liquidity_subtract(body, pool_id)

Subtract liquidity from a pool

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
body = dora_client.LiquidityRequest() # LiquidityRequest | 
pool_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Subtract liquidity from a pool
    api_response = api_instance.liquidity_subtract(body, pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->liquidity_subtract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LiquidityRequest**](LiquidityRequest.md)|  | 
 **pool_id** | [**str**](.md)|  | 

### Return type

[**InlineResponse2016**](InlineResponse2016.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_assets**
> InlineResponse200 list_assets(created_after=created_after, created_before=created_before, asset_kind=asset_kind, can_add_liquidity=can_add_liquidity, can_direct_borrow=can_direct_borrow, can_onboard=can_onboard, can_trade=can_trade, can_virtual_borrow=can_virtual_borrow, page=page, limit=limit)

List assets

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
created_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
asset_kind = 'asset_kind_example' # str | Asset kind (BOND, CURRENCY, INTEREST, POOL_SHARE) (optional)
can_add_liquidity = true # bool |  (optional)
can_direct_borrow = true # bool |  (optional)
can_onboard = true # bool |  (optional)
can_trade = true # bool |  (optional)
can_virtual_borrow = true # bool |  (optional)
page = 1 # int |  (optional) (default to 1)
limit = 100 # int |  (optional) (default to 100)

try:
    # List assets
    api_response = api_instance.list_assets(created_after=created_after, created_before=created_before, asset_kind=asset_kind, can_add_liquidity=can_add_liquidity, can_direct_borrow=can_direct_borrow, can_onboard=can_onboard, can_trade=can_trade, can_virtual_borrow=can_virtual_borrow, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created_after** | **datetime**|  | [optional] 
 **created_before** | **datetime**|  | [optional] 
 **asset_kind** | **str**| Asset kind (BOND, CURRENCY, INTEREST, POOL_SHARE) | [optional] 
 **can_add_liquidity** | **bool**|  | [optional] 
 **can_direct_borrow** | **bool**|  | [optional] 
 **can_onboard** | **bool**|  | [optional] 
 **can_trade** | **bool**|  | [optional] 
 **can_virtual_borrow** | **bool**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_order_books**
> InlineResponse2009 list_order_books(created_after=created_after, created_before=created_before, page=page, limit=limit)

List order books

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
created_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
page = 1 # int |  (optional) (default to 1)
limit = 100 # int |  (optional) (default to 100)

try:
    # List order books
    api_response = api_instance.list_order_books(created_after=created_after, created_before=created_before, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_order_books: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created_after** | **datetime**|  | [optional] 
 **created_before** | **datetime**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_orders**
> InlineResponse2006 list_orders(orderbook_id=orderbook_id, kind=kind, status=status, side=side, _from=_from, to=to, page=page, limit=limit)

List all orders

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
orderbook_id = ['orderbook_id_example'] # list[str] |  (optional)
kind = 'kind_example' # str |  (optional)
status = 'status_example' # str |  (optional)
side = 'side_example' # str |  (optional)
_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
page = 1 # int |  (optional) (default to 1)
limit = 100 # int |  (optional) (default to 100)

try:
    # List all orders
    api_response = api_instance.list_orders(orderbook_id=orderbook_id, kind=kind, status=status, side=side, _from=_from, to=to, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orderbook_id** | [**list[str]**](str.md)|  | [optional] 
 **kind** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **side** | **str**|  | [optional] 
 **_from** | **datetime**|  | [optional] 
 **to** | **datetime**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_asset_prices**
> InlineResponse20028 stream_asset_prices(since=since)

Get a snapshot of asset prices from a specific date and open a stream for real-time updates

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
since = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    # Get a snapshot of asset prices from a specific date and open a stream for real-time updates
    api_response = api_instance.stream_asset_prices(since=since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->stream_asset_prices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **datetime**|  | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_candle_data**
> InlineResponse20017 stream_candle_data(since=since, resolution=resolution)

Get a snapshot of candlestick data from date provided, and open a stream for real-time updates

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
since = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
resolution = 'resolution_example' # str |  (optional)

try:
    # Get a snapshot of candlestick data from date provided, and open a stream for real-time updates
    api_response = api_instance.stream_candle_data(since=since, resolution=resolution)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->stream_candle_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **datetime**|  | [optional] 
 **resolution** | **str**|  | [optional] 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_order_book_balances**
> InlineResponse20014 stream_order_book_balances(id, since=since)

Get a snapshot of base and quote balances for an order book and open a stream for real-time updates

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
since = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    # Get a snapshot of base and quote balances for an order book and open a stream for real-time updates
    api_response = api_instance.stream_order_book_balances(id, since=since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->stream_order_book_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **since** | **datetime**|  | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_orderbook_open_orders**
> InlineResponse2006 stream_orderbook_open_orders(id, since=since)

Get a snapshot of open orders in an order book and open a stream for real-time updates

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
since = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    # Get a snapshot of open orders in an order book and open a stream for real-time updates
    api_response = api_instance.stream_orderbook_open_orders(id, since=since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->stream_orderbook_open_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **since** | **datetime**|  | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_trades**
> TradeResponse stream_trades(since=since, orderbook_ids=orderbook_ids)

Get a snapshot of trades from a specific date and open a stream for real-time updates

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
since = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
orderbook_ids = ['orderbook_ids_example'] # list[str] |  (optional)

try:
    # Get a snapshot of trades from a specific date and open a stream for real-time updates
    api_response = api_instance.stream_trades(since=since, orderbook_ids=orderbook_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->stream_trades: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **datetime**|  | [optional] 
 **orderbook_ids** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**TradeResponse**](TradeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_config**
> InlineResponse2005 update_user_config(body, id)

Update user configuration by ID

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
body = dora_client.UpdateUserConfigRequest() # UpdateUserConfigRequest | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Update user configuration by ID
    api_response = api_instance.update_user_config(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_user_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateUserConfigRequest**](UpdateUserConfigRequest.md)|  | 
 **id** | [**str**](.md)|  | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_user**
> InlineResponse2005 verify_user(id)

Verify a user by ID

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Verify a user by ID
    api_response = api_instance.verify_user(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->verify_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

