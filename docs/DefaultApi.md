# dora_client.DefaultApi

All URIs are relative to *https://localhost:8084*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_all_open_orders**](DefaultApi.md#cancel_all_open_orders) | **DELETE** /v1/orders | Cancel all open orders, if user passes orderbook on query param it will cancel all orders on specific orderbook, admin can cancel user&#x27;s orders on specific orderbook
[**cancel_order_by_id**](DefaultApi.md#cancel_order_by_id) | **DELETE** /v1/orders/{order_id} | Cancel an order by ID
[**check_user_email_exists**](DefaultApi.md#check_user_email_exists) | **GET** /v1/user/exists | Check whether a user email exists
[**claim_leverage_get_accrued_interest**](DefaultApi.md#claim_leverage_get_accrued_interest) | **POST** /v1/leverage/accrued_interest/claim | Claim current accrued leverage interest for a specific user
[**close_isolated_position**](DefaultApi.md#close_isolated_position) | **POST** /v1/positions/close | Close isolated positions, repaying the borrowed
[**create_api_key_for_user**](DefaultApi.md#create_api_key_for_user) | **POST** /v1/user/apikey | Create apikey for a user
[**create_api_key_for_user_id**](DefaultApi.md#create_api_key_for_user_id) | **POST** /v1/user/{user_id}/apikey | Create apikey for a user
[**create_order**](DefaultApi.md#create_order) | **POST** /v1/orders | Create a new order
[**create_user**](DefaultApi.md#create_user) | **POST** /v1/integrators/user | Create a new user
[**delete_user**](DefaultApi.md#delete_user) | **DELETE** /v1/user/{user_id} | Delete user by ID
[**get_all_asset_prices**](DefaultApi.md#get_all_asset_prices) | **GET** /v1/price | Get the current price of all assets
[**get_api_keys_for_user_id**](DefaultApi.md#get_api_keys_for_user_id) | **GET** /v1/user/{user_id}/apikey | Get user&#x27;s api keys: admin or integrator only
[**get_asset_by_id**](DefaultApi.md#get_asset_by_id) | **GET** /v1/assets/{asset_id} | Get asset by ID
[**get_asset_price**](DefaultApi.md#get_asset_price) | **GET** /v1/price/asset/{asset_id} | Get the current price of an asset
[**get_asset_ytmby_id**](DefaultApi.md#get_asset_ytmby_id) | **GET** /v1/assets/{asset_id}/ytm | Get annualized yield to maturity for a bond asset
[**get_assets_stream**](DefaultApi.md#get_assets_stream) | **GET** /v1/assets/stream | Get all inserts or updates for assets
[**get_candle_data**](DefaultApi.md#get_candle_data) | **GET** /v1/charts/{order_book_id}/candle | Get candlestick data for an orderbook
[**get_coupon_payments_by_asset_id**](DefaultApi.md#get_coupon_payments_by_asset_id) | **GET** /v1/assets/{asset_id}/coupon_payments | Get coupon payments for a bond asset
[**get_l1_depth**](DefaultApi.md#get_l1_depth) | **GET** /v1/orderbooks/{order_book_id}/L1 | Get the top price levels for a specific orderbook (L1 market depth)
[**get_l2_depth**](DefaultApi.md#get_l2_depth) | **GET** /v1/orderbooks/{order_book_id}/L2 | Get the aggregated price levels for a specific orderbook (L2 market depth)
[**get_l3_depth**](DefaultApi.md#get_l3_depth) | **GET** /v1/orderbooks/{order_book_id}/L3 | Get all open orders for a specific orderbook (L3 market depth)
[**get_ledger_balances_self**](DefaultApi.md#get_ledger_balances_self) | **GET** /v1/ledger/balances/self | Get your own available, locked, and borrowed assets
[**get_ledger_interest_self**](DefaultApi.md#get_ledger_interest_self) | **GET** /v1/ledger/interest/self | Get your own interest
[**get_ledger_module**](DefaultApi.md#get_ledger_module) | **GET** /v1/ledger/module | Get the entire module object, including unborrowed leverage assets and total leverage trackers
[**get_ledger_module_by_asset**](DefaultApi.md#get_ledger_module_by_asset) | **GET** /v1/ledger/module/{asset_id} | Get the module object for a single asset ID
[**get_ledger_positions_self**](DefaultApi.md#get_ledger_positions_self) | **GET** /v1/ledger/positions/self | Get your own positions
[**get_ledger_value_self**](DefaultApi.md#get_ledger_value_self) | **GET** /v1/ledger/value/self | Get your own available, locked, and borrowed USD value; and realized and unrealized PnL
[**get_ledger_withdraw_requests_by_self**](DefaultApi.md#get_ledger_withdraw_requests_by_self) | **GET** /v1/ledger/withdraw/requests/self | Get all pending withdrawal requests for the logged in user
[**get_order_by_id**](DefaultApi.md#get_order_by_id) | **GET** /v1/orders/{order_id} | Get order by ID
[**get_orderbook_by_id**](DefaultApi.md#get_orderbook_by_id) | **GET** /v1/orderbooks/{order_book_id} | Get orderbook by ID
[**get_orderbook_depth**](DefaultApi.md#get_orderbook_depth) | **GET** /v1/orderbooks/{order_book_id}/depth | Get the aggregated price levels for a specific orderbook (L2 market depth)
[**get_orderbook_orders**](DefaultApi.md#get_orderbook_orders) | **GET** /v1/orderbooks/{order_book_id}/orders | Get all open orders for a specific orderbook (L3 market depth)
[**get_orderbook_stats**](DefaultApi.md#get_orderbook_stats) | **GET** /v1/orderbooks/{order_book_id}/stats | Get orderbook stats
[**get_orderbook_stats_stream**](DefaultApi.md#get_orderbook_stats_stream) | **GET** /v1/orderbooks/{order_book_id}/stats/stream | Orderbook stats stream
[**get_orderbook_summary**](DefaultApi.md#get_orderbook_summary) | **GET** /v1/orderbooks/{order_book_id}/summary | Get summary of an orderbook
[**get_orderbook_top**](DefaultApi.md#get_orderbook_top) | **GET** /v1/orderbooks/{order_book_id}/top | Get the top price levels for a specific orderbook (L1 market depth)
[**get_pl_for_self_by_account**](DefaultApi.md#get_pl_for_self_by_account) | **GET** /v1/pl/self | Get account-by-account PL breakdown for the logged in user
[**get_pool_price**](DefaultApi.md#get_pool_price) | **GET** /v1/price/pool/{pool_id} | Get the current price of a pool
[**get_trade_by_id**](DefaultApi.md#get_trade_by_id) | **GET** /v1/trades/{trade_id} | Get a trade by ID
[**get_trades**](DefaultApi.md#get_trades) | **GET** /v1/trades | Get a filtered, paginated list of trades
[**get_transaction_by_id**](DefaultApi.md#get_transaction_by_id) | **GET** /v1/transactions/{transaction_id} | Get a transaction by ID
[**get_transactions**](DefaultApi.md#get_transactions) | **GET** /v1/transactions | Get a filtered, paginated list of transactions
[**get_user_by_id**](DefaultApi.md#get_user_by_id) | **GET** /v1/user/{user_id} | Get user by ID (admin only)
[**get_user_coupon_payments_stream**](DefaultApi.md#get_user_coupon_payments_stream) | **GET** /v1/user/{user_id}/coupon_payments/stream | Stream user&#x27;s coupon payment accruals in real time
[**get_user_ledger_stream**](DefaultApi.md#get_user_ledger_stream) | **GET** /v1/user/{user_id}/ledger/stream | Get a snapshot of user&#x27;s ledger updates since a specific time, and opens a stream for further updates
[**get_user_order_updates_stream**](DefaultApi.md#get_user_order_updates_stream) | **GET** /v1/user/{user_id}/orders/{order_book_id}/updates/stream | Get a snapshot of user&#x27;s order updates for the given order book since a specific time, and opens a stream for further updates
[**get_user_orders_updates_stream_all**](DefaultApi.md#get_user_orders_updates_stream_all) | **GET** /v1/user/{user_id}/orders/all/updates/stream | Get a snapshot of user&#x27;s order updates across all order books since a specific time, and opens a stream for further updates
[**get_user_self**](DefaultApi.md#get_user_self) | **GET** /v1/user/self | Get user details for the authenticated user
[**get_user_transactions_stream**](DefaultApi.md#get_user_transactions_stream) | **GET** /v1/user/{user_id}/transactions/stream | Get a snapshot of user&#x27;s executed transactions since a specific time, and opens a stream for further updates
[**get_users_api_keys**](DefaultApi.md#get_users_api_keys) | **GET** /v1/user/apikey | Get user&#x27;s api keys
[**ledger_deposit**](DefaultApi.md#ledger_deposit) | **POST** /v1/ledger/deposit/{user_id} | Deposit assets into this user&#x27;s account from the outside world
[**ledger_withdraw**](DefaultApi.md#ledger_withdraw) | **POST** /v1/ledger/withdraw/{user_id} | Withdraw assets from this user to the outside world
[**ledger_withdraw_request**](DefaultApi.md#ledger_withdraw_request) | **POST** /v1/ledger/withdraw/requests/self | Initiate a withdrawal request for the logged in user to the outside world
[**leverage_get_accrued_interest_by_user**](DefaultApi.md#leverage_get_accrued_interest_by_user) | **GET** /v1/leverage/accrued_interest/self | Get current accrued leverage interest for the user
[**leverage_isolate_collateral**](DefaultApi.md#leverage_isolate_collateral) | **POST** /v1/leverage/isolate_collateral | Create an isolated position by transferring collateral to the position from the user&#x27;s global collateral
[**leverage_supply**](DefaultApi.md#leverage_supply) | **POST** /v1/leverage/supply | Supply leverage for a specific asset
[**leverage_unite**](DefaultApi.md#leverage_unite) | **POST** /v1/leverage/unite | Combines all isolated positions into a single global position
[**leverage_withdraw**](DefaultApi.md#leverage_withdraw) | **POST** /v1/leverage/withdraw | Withdraw leverage for a specific asset
[**liquidity_add**](DefaultApi.md#liquidity_add) | **POST** /v1/liquidity/pool/{pool_id}/add | Add liquidity to a pool
[**liquidity_subtract**](DefaultApi.md#liquidity_subtract) | **POST** /v1/liquidity/pool/{pool_id}/remove | Subtract liquidity from a pool
[**list_assets**](DefaultApi.md#list_assets) | **GET** /v1/assets | List assets
[**list_order_books**](DefaultApi.md#list_order_books) | **GET** /v1/orderbooks | List order books
[**list_orders**](DefaultApi.md#list_orders) | **GET** /v1/orders | List all orders
[**list_position_accounts_self**](DefaultApi.md#list_position_accounts_self) | **GET** /v1/user/self/position_accounts | List all position accounts for the authenticated user
[**pay_leverage_get_accrued_interest**](DefaultApi.md#pay_leverage_get_accrued_interest) | **POST** /v1/leverage/accrued_interest/pay | Pay current accrued leverage interest for a specific user
[**revoke_api_key_for_user**](DefaultApi.md#revoke_api_key_for_user) | **PUT** /v1/user/apikey/{key_id}/revoke | Revoke apikey for a user
[**revoke_api_key_for_user_id**](DefaultApi.md#revoke_api_key_for_user_id) | **PUT** /v1/user/{user_id}/apikey/{key_id}/revoke | Revoke apikey for a user: admin or integrator only
[**settle_leverage_accrued_interest**](DefaultApi.md#settle_leverage_accrued_interest) | **POST** /v1/leverage/accrued_interest/settle | Settle current accrued leverage interest for a specific user
[**stream_asset_prices**](DefaultApi.md#stream_asset_prices) | **GET** /v1/prices/stream | Stream real-time asset prices as map objects
[**stream_candle_data**](DefaultApi.md#stream_candle_data) | **GET** /v1/charts/{order_book_id}/candle/stream | Get a snapshot of candlestick data from date provided, and open a stream for real-time updates
[**stream_order_book_balances**](DefaultApi.md#stream_order_book_balances) | **GET** /v1/orderbooks/{order_book_id}/balances/stream | Get a snapshot of base and quote balances for an order book and open a stream for real-time updates
[**stream_orderbook_open_orders**](DefaultApi.md#stream_orderbook_open_orders) | **GET** /v1/orderbooks/{order_book_id}/open/stream | Get a snapshot of open orders in an order book and open a stream for real-time updates
[**stream_trades**](DefaultApi.md#stream_trades) | **GET** /v1/trades/{order_book_id}/stream | Get a snapshot of trades executed on the given order book from a specific date and open a stream for real-time updates
[**transfer_available_balances**](DefaultApi.md#transfer_available_balances) | **POST** /v1/positions/transfer_balances | Transfer available balance between a user&#x27;s accounts (e.g. global to isolated position)
[**update_user_config**](DefaultApi.md#update_user_config) | **PUT** /v1/user/{user_id}/config | Update user configuration by ID
[**update_user_config_self**](DefaultApi.md#update_user_config_self) | **PUT** /v1/user/config/self | Update user configuration for the authenticated user
[**validate_submit_order**](DefaultApi.md#validate_submit_order) | **POST** /v1/orders/validate | Validate submit order request data
[**verify_user**](DefaultApi.md#verify_user) | **PUT** /v1/user/{user_id}/verify | Verify a user by ID

# **cancel_all_open_orders**
> ListOrdersResponse cancel_all_open_orders(order_book_id=order_book_id, user_id=user_id, order_kind=order_kind)

Cancel all open orders, if user passes orderbook on query param it will cancel all orders on specific orderbook, admin can cancel user's orders on specific orderbook

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
order_book_id = NULL # dict |  (optional)
user_id = NULL # dict |  (optional)
order_kind = dora_client.OrderKind() # OrderKind |  (optional)

try:
    # Cancel all open orders, if user passes orderbook on query param it will cancel all orders on specific orderbook, admin can cancel user's orders on specific orderbook
    api_response = api_instance.cancel_all_open_orders(order_book_id=order_book_id, user_id=user_id, order_kind=order_kind)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->cancel_all_open_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_book_id** | [**dict**](.md)|  | [optional] 
 **user_id** | [**dict**](.md)|  | [optional] 
 **order_kind** | [**OrderKind**](.md)|  | [optional] 

### Return type

[**ListOrdersResponse**](ListOrdersResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_order_by_id**
> CancelOrderResponse cancel_order_by_id(order_id)

Cancel an order by ID

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
order_id = NULL # dict | 

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
 **order_id** | [**dict**](.md)|  | 

### Return type

[**CancelOrderResponse**](CancelOrderResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_user_email_exists**
> EmailExistsResponse check_user_email_exists(email)

Check whether a user email exists

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
email = NULL # dict | 

try:
    # Check whether a user email exists
    api_response = api_instance.check_user_email_exists(email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->check_user_email_exists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**dict**](.md)|  | 

### Return type

[**EmailExistsResponse**](EmailExistsResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **claim_leverage_get_accrued_interest**
> ClaimLeverageAccruedInterestResponse claim_leverage_get_accrued_interest(body)

Claim current accrued leverage interest for a specific user

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
body = dora_client.ClaimLeverageAccruedInterestRequest() # ClaimLeverageAccruedInterestRequest | 

try:
    # Claim current accrued leverage interest for a specific user
    api_response = api_instance.claim_leverage_get_accrued_interest(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->claim_leverage_get_accrued_interest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClaimLeverageAccruedInterestRequest**](ClaimLeverageAccruedInterestRequest.md)|  | 

### Return type

[**ClaimLeverageAccruedInterestResponse**](ClaimLeverageAccruedInterestResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **close_isolated_position**
> ClosePositionResponse close_isolated_position(body)

Close isolated positions, repaying the borrowed

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
body = dora_client.ClosePositionRequest() # ClosePositionRequest | 

try:
    # Close isolated positions, repaying the borrowed
    api_response = api_instance.close_isolated_position(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->close_isolated_position: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClosePositionRequest**](ClosePositionRequest.md)|  | 

### Return type

[**ClosePositionResponse**](ClosePositionResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_api_key_for_user**
> CreateAPIKeyResponse create_api_key_for_user(body)

Create apikey for a user

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
body = dora_client.CreateAPIKeyRequest() # CreateAPIKeyRequest | 

try:
    # Create apikey for a user
    api_response = api_instance.create_api_key_for_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_api_key_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAPIKeyRequest**](CreateAPIKeyRequest.md)|  | 

### Return type

[**CreateAPIKeyResponse**](CreateAPIKeyResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_api_key_for_user_id**
> CreateAPIKeyResponse create_api_key_for_user_id(body, user_id)

Create apikey for a user

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
body = dora_client.CreateAPIKeyRequest() # CreateAPIKeyRequest | 
user_id = NULL # dict | 

try:
    # Create apikey for a user
    api_response = api_instance.create_api_key_for_user_id(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_api_key_for_user_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAPIKeyRequest**](CreateAPIKeyRequest.md)|  | 
 **user_id** | [**dict**](.md)|  | 

### Return type

[**CreateAPIKeyResponse**](CreateAPIKeyResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_order**
> CreateOrderResponse create_order(body)

Create a new order

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
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

[**CreateOrderResponse**](CreateOrderResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> UserCreatedResponse create_user(body)

Create a new user

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
body = dora_client.CreateIntegratorUserRequest() # CreateIntegratorUserRequest | 

try:
    # Create a new user
    api_response = api_instance.create_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateIntegratorUserRequest**](CreateIntegratorUserRequest.md)|  | 

### Return type

[**UserCreatedResponse**](UserCreatedResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> UserDeletedResponse delete_user(user_id)

Delete user by ID

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
user_id = NULL # dict | 

try:
    # Delete user by ID
    api_response = api_instance.delete_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**dict**](.md)|  | 

### Return type

[**UserDeletedResponse**](UserDeletedResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_asset_prices**
> ListAssetPriceResponse get_all_asset_prices()

Get the current price of all assets

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))

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

[**ListAssetPriceResponse**](ListAssetPriceResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_keys_for_user_id**
> GetAPIKeyResponse get_api_keys_for_user_id(user_id)

Get user's api keys: admin or integrator only

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
user_id = NULL # dict | 

try:
    # Get user's api keys: admin or integrator only
    api_response = api_instance.get_api_keys_for_user_id(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_api_keys_for_user_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**dict**](.md)|  | 

### Return type

[**GetAPIKeyResponse**](GetAPIKeyResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_by_id**
> GetAssetByIDResponse get_asset_by_id(asset_id)

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
asset_id = NULL # dict | 

try:
    # Get asset by ID
    api_response = api_instance.get_asset_by_id(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_asset_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | [**dict**](.md)|  | 

### Return type

[**GetAssetByIDResponse**](GetAssetByIDResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_price**
> GetAssetPriceResponse get_asset_price(asset_id)

Get the current price of an asset

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
asset_id = NULL # dict | 

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
 **asset_id** | [**dict**](.md)|  | 

### Return type

[**GetAssetPriceResponse**](GetAssetPriceResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_ytmby_id**
> GetAssetYTMByIDResponse get_asset_ytmby_id(asset_id)

Get annualized yield to maturity for a bond asset

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
asset_id = NULL # dict | 

try:
    # Get annualized yield to maturity for a bond asset
    api_response = api_instance.get_asset_ytmby_id(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_asset_ytmby_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | [**dict**](.md)|  | 

### Return type

[**GetAssetYTMByIDResponse**](GetAssetYTMByIDResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assets_stream**
> StreamAssetsResponse get_assets_stream(since=since, until=until)

Get all inserts or updates for assets

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
since = NULL # dict |  (optional)
until = NULL # dict |  (optional)

try:
    # Get all inserts or updates for assets
    api_response = api_instance.get_assets_stream(since=since, until=until)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_assets_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | [**dict**](.md)|  | [optional] 
 **until** | [**dict**](.md)|  | [optional] 

### Return type

[**StreamAssetsResponse**](StreamAssetsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_candle_data**
> ListCandlesResponse get_candle_data(order_book_id, start=start, end=end, resolution=resolution)

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
order_book_id = NULL # dict | 
start = NULL # dict |  (optional)
end = NULL # dict |  (optional)
resolution = dora_client.CandleResolution() # CandleResolution |  (optional)

try:
    # Get candlestick data for an orderbook
    api_response = api_instance.get_candle_data(order_book_id, start=start, end=end, resolution=resolution)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_candle_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_book_id** | [**dict**](.md)|  | 
 **start** | [**dict**](.md)|  | [optional] 
 **end** | [**dict**](.md)|  | [optional] 
 **resolution** | [**CandleResolution**](.md)|  | [optional] 

### Return type

[**ListCandlesResponse**](ListCandlesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coupon_payments_by_asset_id**
> ListCouponPaymentsResponse get_coupon_payments_by_asset_id(asset_id)

Get coupon payments for a bond asset

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
asset_id = NULL # dict | 

try:
    # Get coupon payments for a bond asset
    api_response = api_instance.get_coupon_payments_by_asset_id(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_coupon_payments_by_asset_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | [**dict**](.md)|  | 

### Return type

[**ListCouponPaymentsResponse**](ListCouponPaymentsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_l1_depth**
> GetTopOfBookResponse get_l1_depth(order_book_id)

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
order_book_id = NULL # dict | 

try:
    # Get the top price levels for a specific orderbook (L1 market depth)
    api_response = api_instance.get_l1_depth(order_book_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_l1_depth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_book_id** | [**dict**](.md)|  | 

### Return type

[**GetTopOfBookResponse**](GetTopOfBookResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_l2_depth**
> ListOrderBookDepthResponse get_l2_depth(order_book_id)

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
order_book_id = NULL # dict | 

try:
    # Get the aggregated price levels for a specific orderbook (L2 market depth)
    api_response = api_instance.get_l2_depth(order_book_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_l2_depth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_book_id** | [**dict**](.md)|  | 

### Return type

[**ListOrderBookDepthResponse**](ListOrderBookDepthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_l3_depth**
> ListOrdersResponse get_l3_depth(order_book_id)

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
order_book_id = NULL # dict | 

try:
    # Get all open orders for a specific orderbook (L3 market depth)
    api_response = api_instance.get_l3_depth(order_book_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_l3_depth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_book_id** | [**dict**](.md)|  | 

### Return type

[**ListOrdersResponse**](ListOrdersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ledger_balances_self**
> UserBalanceResponse get_ledger_balances_self()

Get your own available, locked, and borrowed assets

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))

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

[**UserBalanceResponse**](UserBalanceResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ledger_interest_self**
> UserInterestResponse get_ledger_interest_self()

Get your own interest

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))

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

[**UserInterestResponse**](UserInterestResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ledger_module**
> LedgerModuleResponse get_ledger_module()

Get the entire module object, including unborrowed leverage assets and total leverage trackers

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))

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

[**LedgerModuleResponse**](LedgerModuleResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ledger_module_by_asset**
> LedgerModuleByAssetResponse get_ledger_module_by_asset(asset_id)

Get the module object for a single asset ID

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
asset_id = NULL # dict | 

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
 **asset_id** | [**dict**](.md)|  | 

### Return type

[**LedgerModuleByAssetResponse**](LedgerModuleByAssetResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ledger_positions_self**
> UserPositionResponse get_ledger_positions_self()

Get your own positions

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))

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

[**UserPositionResponse**](UserPositionResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ledger_value_self**
> UserValueResponse get_ledger_value_self()

Get your own available, locked, and borrowed USD value; and realized and unrealized PnL

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))

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

[**UserValueResponse**](UserValueResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ledger_withdraw_requests_by_self**
> AllWithdrawalInitiationsResponse get_ledger_withdraw_requests_by_self()

Get all pending withdrawal requests for the logged in user

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))

try:
    # Get all pending withdrawal requests for the logged in user
    api_response = api_instance.get_ledger_withdraw_requests_by_self()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_ledger_withdraw_requests_by_self: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AllWithdrawalInitiationsResponse**](AllWithdrawalInitiationsResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_by_id**
> GetOrderResponse get_order_by_id(order_id)

Get order by ID

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
order_id = NULL # dict | 

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
 **order_id** | [**dict**](.md)|  | 

### Return type

[**GetOrderResponse**](GetOrderResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orderbook_by_id**
> GetOrderBookResponse get_orderbook_by_id(order_book_id)

Get orderbook by ID

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
order_book_id = NULL # dict | 

try:
    # Get orderbook by ID
    api_response = api_instance.get_orderbook_by_id(order_book_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_orderbook_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_book_id** | [**dict**](.md)|  | 

### Return type

[**GetOrderBookResponse**](GetOrderBookResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orderbook_depth**
> ListOrderBookDepthResponse get_orderbook_depth(order_book_id)

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
order_book_id = NULL # dict | 

try:
    # Get the aggregated price levels for a specific orderbook (L2 market depth)
    api_response = api_instance.get_orderbook_depth(order_book_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_orderbook_depth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_book_id** | [**dict**](.md)|  | 

### Return type

[**ListOrderBookDepthResponse**](ListOrderBookDepthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orderbook_orders**
> ListOrdersResponse get_orderbook_orders(order_book_id)

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
order_book_id = NULL # dict | 

try:
    # Get all open orders for a specific orderbook (L3 market depth)
    api_response = api_instance.get_orderbook_orders(order_book_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_orderbook_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_book_id** | [**dict**](.md)|  | 

### Return type

[**ListOrdersResponse**](ListOrdersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orderbook_stats**
> GetOrderbookStatsResponse get_orderbook_stats(order_book_id)

Get orderbook stats

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
order_book_id = NULL # dict | 

try:
    # Get orderbook stats
    api_response = api_instance.get_orderbook_stats(order_book_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_orderbook_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_book_id** | [**dict**](.md)|  | 

### Return type

[**GetOrderbookStatsResponse**](GetOrderbookStatsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orderbook_stats_stream**
> OrderbookStats get_orderbook_stats_stream(order_book_id)

Orderbook stats stream

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
order_book_id = NULL # dict | 

try:
    # Orderbook stats stream
    api_response = api_instance.get_orderbook_stats_stream(order_book_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_orderbook_stats_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_book_id** | [**dict**](.md)|  | 

### Return type

[**OrderbookStats**](OrderbookStats.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orderbook_summary**
> GetOrderBookSummaryResponse get_orderbook_summary(order_book_id)

Get summary of an orderbook

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
order_book_id = NULL # dict | 

try:
    # Get summary of an orderbook
    api_response = api_instance.get_orderbook_summary(order_book_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_orderbook_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_book_id** | [**dict**](.md)|  | 

### Return type

[**GetOrderBookSummaryResponse**](GetOrderBookSummaryResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orderbook_top**
> GetTopOfBookResponse get_orderbook_top(order_book_id)

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
order_book_id = NULL # dict | 

try:
    # Get the top price levels for a specific orderbook (L1 market depth)
    api_response = api_instance.get_orderbook_top(order_book_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_orderbook_top: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_book_id** | [**dict**](.md)|  | 

### Return type

[**GetTopOfBookResponse**](GetTopOfBookResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pl_for_self_by_account**
> PLResponse get_pl_for_self_by_account()

Get account-by-account PL breakdown for the logged in user

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))

try:
    # Get account-by-account PL breakdown for the logged in user
    api_response = api_instance.get_pl_for_self_by_account()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_pl_for_self_by_account: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PLResponse**](PLResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pool_price**
> GetPoolPriceResponse get_pool_price(pool_id)

Get the current price of a pool

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
pool_id = NULL # dict | 

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
 **pool_id** | [**dict**](.md)|  | 

### Return type

[**GetPoolPriceResponse**](GetPoolPriceResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trade_by_id**
> TradeResponse get_trade_by_id(trade_id)

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
trade_id = NULL # dict | 

try:
    # Get a trade by ID
    api_response = api_instance.get_trade_by_id(trade_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_trade_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trade_id** | [**dict**](.md)|  | 

### Return type

[**TradeResponse**](TradeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trades**
> ListTradeResponse get_trades(order_book_ids=order_book_ids, user_ids=user_ids, start=start, end=end, page=page, limit=limit)

Get a filtered, paginated list of trades

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
order_book_ids = NULL # dict |  (optional)
user_ids = NULL # dict |  (optional)
start = NULL # dict |  (optional)
end = NULL # dict |  (optional)
page = 1 # dict |  (optional) (default to 1)
limit = 100 # dict |  (optional) (default to 100)

try:
    # Get a filtered, paginated list of trades
    api_response = api_instance.get_trades(order_book_ids=order_book_ids, user_ids=user_ids, start=start, end=end, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_trades: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_book_ids** | [**dict**](.md)|  | [optional] 
 **user_ids** | [**dict**](.md)|  | [optional] 
 **start** | [**dict**](.md)|  | [optional] 
 **end** | [**dict**](.md)|  | [optional] 
 **page** | [**dict**](.md)|  | [optional] [default to 1]
 **limit** | [**dict**](.md)|  | [optional] [default to 100]

### Return type

[**ListTradeResponse**](ListTradeResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_by_id**
> GetTransactionResponse get_transaction_by_id(transaction_id)

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
transaction_id = NULL # dict | 

try:
    # Get a transaction by ID
    api_response = api_instance.get_transaction_by_id(transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_transaction_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | [**dict**](.md)|  | 

### Return type

[**GetTransactionResponse**](GetTransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions**
> ListTransactionsResponse get_transactions(pools=pools, user_ids=user_ids, tx_kinds=tx_kinds, start=start, end=end, page=page, limit=limit)

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
pools = NULL # dict |  (optional)
user_ids = NULL # dict |  (optional)
tx_kinds = NULL # dict |  (optional)
start = NULL # dict |  (optional)
end = NULL # dict |  (optional)
page = 1 # dict |  (optional) (default to 1)
limit = 100 # dict |  (optional) (default to 100)

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
 **pools** | [**dict**](.md)|  | [optional] 
 **user_ids** | [**dict**](.md)|  | [optional] 
 **tx_kinds** | [**dict**](.md)|  | [optional] 
 **start** | [**dict**](.md)|  | [optional] 
 **end** | [**dict**](.md)|  | [optional] 
 **page** | [**dict**](.md)|  | [optional] [default to 1]
 **limit** | [**dict**](.md)|  | [optional] [default to 100]

### Return type

[**ListTransactionsResponse**](ListTransactionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_id**
> GetUserResponse get_user_by_id(user_id)

Get user by ID (admin only)

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
user_id = NULL # dict | 

try:
    # Get user by ID (admin only)
    api_response = api_instance.get_user_by_id(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_user_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**dict**](.md)|  | 

### Return type

[**GetUserResponse**](GetUserResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_coupon_payments_stream**
> StreamUserCouponPaymentsResponse get_user_coupon_payments_stream(user_id)

Stream user's coupon payment accruals in real time

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthQuery
configuration = dora_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
user_id = NULL # dict | 

try:
    # Stream user's coupon payment accruals in real time
    api_response = api_instance.get_user_coupon_payments_stream(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_user_coupon_payments_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**dict**](.md)|  | 

### Return type

[**StreamUserCouponPaymentsResponse**](StreamUserCouponPaymentsResponse.md)

### Authorization

[apiKeyAuthQuery](../README.md#apiKeyAuthQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_ledger_stream**
> StreamPositionsResponse get_user_ledger_stream(user_id)

Get a snapshot of user's ledger updates since a specific time, and opens a stream for further updates

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthQuery
configuration = dora_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
user_id = NULL # dict | 

try:
    # Get a snapshot of user's ledger updates since a specific time, and opens a stream for further updates
    api_response = api_instance.get_user_ledger_stream(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_user_ledger_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**dict**](.md)|  | 

### Return type

[**StreamPositionsResponse**](StreamPositionsResponse.md)

### Authorization

[apiKeyAuthQuery](../README.md#apiKeyAuthQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_order_updates_stream**
> StreamOrderUpdatesResponse get_user_order_updates_stream(user_id, order_book_id, since=since)

Get a snapshot of user's order updates for the given order book since a specific time, and opens a stream for further updates

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthQuery
configuration = dora_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
user_id = NULL # dict | 
order_book_id = NULL # dict | 
since = NULL # dict |  (optional)

try:
    # Get a snapshot of user's order updates for the given order book since a specific time, and opens a stream for further updates
    api_response = api_instance.get_user_order_updates_stream(user_id, order_book_id, since=since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_user_order_updates_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**dict**](.md)|  | 
 **order_book_id** | [**dict**](.md)|  | 
 **since** | [**dict**](.md)|  | [optional] 

### Return type

[**StreamOrderUpdatesResponse**](StreamOrderUpdatesResponse.md)

### Authorization

[apiKeyAuthQuery](../README.md#apiKeyAuthQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_orders_updates_stream_all**
> StreamOrderUpdatesResponse get_user_orders_updates_stream_all(user_id, since=since)

Get a snapshot of user's order updates across all order books since a specific time, and opens a stream for further updates

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthQuery
configuration = dora_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
user_id = NULL # dict | 
since = NULL # dict |  (optional)

try:
    # Get a snapshot of user's order updates across all order books since a specific time, and opens a stream for further updates
    api_response = api_instance.get_user_orders_updates_stream_all(user_id, since=since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_user_orders_updates_stream_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**dict**](.md)|  | 
 **since** | [**dict**](.md)|  | [optional] 

### Return type

[**StreamOrderUpdatesResponse**](StreamOrderUpdatesResponse.md)

### Authorization

[apiKeyAuthQuery](../README.md#apiKeyAuthQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_self**
> GetUserResponse get_user_self()

Get user details for the authenticated user

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))

try:
    # Get user details for the authenticated user
    api_response = api_instance.get_user_self()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_user_self: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetUserResponse**](GetUserResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_transactions_stream**
> StreamTransactionsResponse get_user_transactions_stream(user_id, since=since)

Get a snapshot of user's executed transactions since a specific time, and opens a stream for further updates

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthQuery
configuration = dora_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
user_id = NULL # dict | 
since = NULL # dict |  (optional)

try:
    # Get a snapshot of user's executed transactions since a specific time, and opens a stream for further updates
    api_response = api_instance.get_user_transactions_stream(user_id, since=since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_user_transactions_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**dict**](.md)|  | 
 **since** | [**dict**](.md)|  | [optional] 

### Return type

[**StreamTransactionsResponse**](StreamTransactionsResponse.md)

### Authorization

[apiKeyAuthQuery](../README.md#apiKeyAuthQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_api_keys**
> GetAPIKeyResponse get_users_api_keys()

Get user's api keys

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))

try:
    # Get user's api keys
    api_response = api_instance.get_users_api_keys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_users_api_keys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAPIKeyResponse**](GetAPIKeyResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ledger_deposit**
> FundUserResponse ledger_deposit(body, user_id)

Deposit assets into this user's account from the outside world

Deposit assets into this user's account from the outside world. Note that this does not interact with any external systems; it simply adds the amount to the user's available balance in the ledger. Actual transfer of assets must be handled separately.

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
body = dora_client.FundUserRequest() # FundUserRequest | 
user_id = NULL # dict | 

try:
    # Deposit assets into this user's account from the outside world
    api_response = api_instance.ledger_deposit(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ledger_deposit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FundUserRequest**](FundUserRequest.md)|  | 
 **user_id** | [**dict**](.md)|  | 

### Return type

[**FundUserResponse**](FundUserResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ledger_withdraw**
> FundUserResponse ledger_withdraw(body, user_id)

Withdraw assets from this user to the outside world

Withdraw assets from this user's account to the outside world. Note that this does not interact with any external systems; it simply deducts the amount from the user's available balance in the ledger. Actual transfer of assets must be handled separately.

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
body = dora_client.DefundUserRequest() # DefundUserRequest | 
user_id = NULL # dict | 

try:
    # Withdraw assets from this user to the outside world
    api_response = api_instance.ledger_withdraw(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ledger_withdraw: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DefundUserRequest**](DefundUserRequest.md)|  | 
 **user_id** | [**dict**](.md)|  | 

### Return type

[**FundUserResponse**](FundUserResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ledger_withdraw_request**
> WithdrawalInitiationResponse ledger_withdraw_request(body, user_id)

Initiate a withdrawal request for the logged in user to the outside world

Withdraw assets from the logged in user's account to the outside world. Note that this does not interact with any external systems; it simply deducts the amount from the user's available balance in the ledger. Actual transfer of assets must be handled separately.

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
body = dora_client.DefundUserRequest() # DefundUserRequest | 
user_id = NULL # dict | 

try:
    # Initiate a withdrawal request for the logged in user to the outside world
    api_response = api_instance.ledger_withdraw_request(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ledger_withdraw_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DefundUserRequest**](DefundUserRequest.md)|  | 
 **user_id** | [**dict**](.md)|  | 

### Return type

[**WithdrawalInitiationResponse**](WithdrawalInitiationResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leverage_get_accrued_interest_by_user**
> CurrentLeverageAccruedInterestResponse leverage_get_accrued_interest_by_user(position_id=position_id, asset_id=asset_id)

Get current accrued leverage interest for the user

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
position_id = NULL # dict |  (optional)
asset_id = NULL # dict |  (optional)

try:
    # Get current accrued leverage interest for the user
    api_response = api_instance.leverage_get_accrued_interest_by_user(position_id=position_id, asset_id=asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->leverage_get_accrued_interest_by_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **position_id** | [**dict**](.md)|  | [optional] 
 **asset_id** | [**dict**](.md)|  | [optional] 

### Return type

[**CurrentLeverageAccruedInterestResponse**](CurrentLeverageAccruedInterestResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leverage_isolate_collateral**
> IsolateCollateralResponse leverage_isolate_collateral(body)

Create an isolated position by transferring collateral to the position from the user's global collateral

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
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

[**IsolateCollateralResponse**](IsolateCollateralResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leverage_supply**
> SupplyResponse leverage_supply(body)

Supply leverage for a specific asset

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
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

[**SupplyResponse**](SupplyResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leverage_unite**
> UnitePositionResponse leverage_unite(body)

Combines all isolated positions into a single global position

Combines all isolated positions into a single global position

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
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

[**UnitePositionResponse**](UnitePositionResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leverage_withdraw**
> WithdrawResponse leverage_withdraw(body)

Withdraw leverage for a specific asset

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
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

[**WithdrawResponse**](WithdrawResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **liquidity_add**
> LiquidityResponse liquidity_add(body, pool_id)

Add liquidity to a pool

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
body = dora_client.LiquidityRequest() # LiquidityRequest | 
pool_id = NULL # dict | 

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
 **pool_id** | [**dict**](.md)|  | 

### Return type

[**LiquidityResponse**](LiquidityResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **liquidity_subtract**
> LiquidityResponse liquidity_subtract(body, pool_id)

Subtract liquidity from a pool

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
body = dora_client.LiquidityRequest() # LiquidityRequest | 
pool_id = NULL # dict | 

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
 **pool_id** | [**dict**](.md)|  | 

### Return type

[**LiquidityResponse**](LiquidityResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_assets**
> ListAssetsResponse list_assets(created_after=created_after, created_before=created_before, asset_kind=asset_kind, can_add_liquidity=can_add_liquidity, can_direct_borrow=can_direct_borrow, can_onboard=can_onboard, can_trade=can_trade, can_virtual_borrow=can_virtual_borrow, page=page, limit=limit)

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
created_after = NULL # dict |  (optional)
created_before = NULL # dict |  (optional)
asset_kind = dora_client.AssetKind() # AssetKind | Asset kind (BOND, CURRENCY, INTEREST, POOL_SHARE) (optional)
can_add_liquidity = NULL # dict |  (optional)
can_direct_borrow = NULL # dict |  (optional)
can_onboard = NULL # dict |  (optional)
can_trade = NULL # dict |  (optional)
can_virtual_borrow = NULL # dict |  (optional)
page = 1 # dict |  (optional) (default to 1)
limit = 100 # dict |  (optional) (default to 100)

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
 **created_after** | [**dict**](.md)|  | [optional] 
 **created_before** | [**dict**](.md)|  | [optional] 
 **asset_kind** | [**AssetKind**](.md)| Asset kind (BOND, CURRENCY, INTEREST, POOL_SHARE) | [optional] 
 **can_add_liquidity** | [**dict**](.md)|  | [optional] 
 **can_direct_borrow** | [**dict**](.md)|  | [optional] 
 **can_onboard** | [**dict**](.md)|  | [optional] 
 **can_trade** | [**dict**](.md)|  | [optional] 
 **can_virtual_borrow** | [**dict**](.md)|  | [optional] 
 **page** | [**dict**](.md)|  | [optional] [default to 1]
 **limit** | [**dict**](.md)|  | [optional] [default to 100]

### Return type

[**ListAssetsResponse**](ListAssetsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_order_books**
> ListOrderBooksResponse list_order_books(status=status, base_asset_id=base_asset_id, quote_asset_id=quote_asset_id, page=page, limit=limit)

List order books

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
status = dora_client.OrderBookStatus() # OrderBookStatus |  (optional)
base_asset_id = NULL # dict |  (optional)
quote_asset_id = NULL # dict |  (optional)
page = 1 # dict |  (optional) (default to 1)
limit = 100 # dict |  (optional) (default to 100)

try:
    # List order books
    api_response = api_instance.list_order_books(status=status, base_asset_id=base_asset_id, quote_asset_id=quote_asset_id, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_order_books: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**OrderBookStatus**](.md)|  | [optional] 
 **base_asset_id** | [**dict**](.md)|  | [optional] 
 **quote_asset_id** | [**dict**](.md)|  | [optional] 
 **page** | [**dict**](.md)|  | [optional] [default to 1]
 **limit** | [**dict**](.md)|  | [optional] [default to 100]

### Return type

[**ListOrderBooksResponse**](ListOrderBooksResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_orders**
> ListOrdersResponse list_orders(order_book_id=order_book_id, kind=kind, status=status, side=side, _from=_from, to=to, page=page, limit=limit)

List all orders

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
order_book_id = NULL # dict |  (optional)
kind = NULL # dict |  (optional)
status = NULL # dict |  (optional)
side = dora_client.Side() # Side |  (optional)
_from = NULL # dict |  (optional)
to = NULL # dict |  (optional)
page = 1 # dict |  (optional) (default to 1)
limit = 100 # dict |  (optional) (default to 100)

try:
    # List all orders
    api_response = api_instance.list_orders(order_book_id=order_book_id, kind=kind, status=status, side=side, _from=_from, to=to, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_book_id** | [**dict**](.md)|  | [optional] 
 **kind** | [**dict**](.md)|  | [optional] 
 **status** | [**dict**](.md)|  | [optional] 
 **side** | [**Side**](.md)|  | [optional] 
 **_from** | [**dict**](.md)|  | [optional] 
 **to** | [**dict**](.md)|  | [optional] 
 **page** | [**dict**](.md)|  | [optional] [default to 1]
 **limit** | [**dict**](.md)|  | [optional] [default to 100]

### Return type

[**ListOrdersResponse**](ListOrdersResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_position_accounts_self**
> ListPositionAccountsResponse list_position_accounts_self()

List all position accounts for the authenticated user

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))

try:
    # List all position accounts for the authenticated user
    api_response = api_instance.list_position_accounts_self()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_position_accounts_self: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListPositionAccountsResponse**](ListPositionAccountsResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_leverage_get_accrued_interest**
> PayLeverageAccruedInterestResponse pay_leverage_get_accrued_interest(body)

Pay current accrued leverage interest for a specific user

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
body = dora_client.PayLeverageAccruedInterestRequest() # PayLeverageAccruedInterestRequest | 

try:
    # Pay current accrued leverage interest for a specific user
    api_response = api_instance.pay_leverage_get_accrued_interest(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->pay_leverage_get_accrued_interest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PayLeverageAccruedInterestRequest**](PayLeverageAccruedInterestRequest.md)|  | 

### Return type

[**PayLeverageAccruedInterestResponse**](PayLeverageAccruedInterestResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_api_key_for_user**
> RevokeAPIKeyResponse revoke_api_key_for_user(key_id)

Revoke apikey for a user

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
key_id = NULL # dict | 

try:
    # Revoke apikey for a user
    api_response = api_instance.revoke_api_key_for_user(key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->revoke_api_key_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | [**dict**](.md)|  | 

### Return type

[**RevokeAPIKeyResponse**](RevokeAPIKeyResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_api_key_for_user_id**
> RevokeAPIKeyResponse revoke_api_key_for_user_id(user_id, key_id)

Revoke apikey for a user: admin or integrator only

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
user_id = NULL # dict | 
key_id = NULL # dict | 

try:
    # Revoke apikey for a user: admin or integrator only
    api_response = api_instance.revoke_api_key_for_user_id(user_id, key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->revoke_api_key_for_user_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**dict**](.md)|  | 
 **key_id** | [**dict**](.md)|  | 

### Return type

[**RevokeAPIKeyResponse**](RevokeAPIKeyResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settle_leverage_accrued_interest**
> SettleLeverageAccruedInterestResponse settle_leverage_accrued_interest(body)

Settle current accrued leverage interest for a specific user

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
body = dora_client.SettleLeverageAccruedInterestRequest() # SettleLeverageAccruedInterestRequest | 

try:
    # Settle current accrued leverage interest for a specific user
    api_response = api_instance.settle_leverage_accrued_interest(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->settle_leverage_accrued_interest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SettleLeverageAccruedInterestRequest**](SettleLeverageAccruedInterestRequest.md)|  | 

### Return type

[**SettleLeverageAccruedInterestResponse**](SettleLeverageAccruedInterestResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_asset_prices**
> StreamAssetPricesResponse stream_asset_prices(since=since, asset_id=asset_id)

Stream real-time asset prices as map objects

Opens a WebSocket stream for real-time asset price updates. First message contains all current prices, subsequent messages contain only changed prices. Data is sent as JSON objects keyed by asset ID.

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
since = NULL # dict |  (optional)
asset_id = NULL # dict |  (optional)

try:
    # Stream real-time asset prices as map objects
    api_response = api_instance.stream_asset_prices(since=since, asset_id=asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->stream_asset_prices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | [**dict**](.md)|  | [optional] 
 **asset_id** | [**dict**](.md)|  | [optional] 

### Return type

[**StreamAssetPricesResponse**](StreamAssetPricesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_candle_data**
> StreamCandlesResponse stream_candle_data(order_book_id, since=since, resolution=resolution)

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
order_book_id = NULL # dict | 
since = NULL # dict |  (optional)
resolution = dora_client.CandleResolution() # CandleResolution |  (optional)

try:
    # Get a snapshot of candlestick data from date provided, and open a stream for real-time updates
    api_response = api_instance.stream_candle_data(order_book_id, since=since, resolution=resolution)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->stream_candle_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_book_id** | [**dict**](.md)|  | 
 **since** | [**dict**](.md)|  | [optional] 
 **resolution** | [**CandleResolution**](.md)|  | [optional] 

### Return type

[**StreamCandlesResponse**](StreamCandlesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_order_book_balances**
> StreamOrderBookBalancesResponse stream_order_book_balances(order_book_id, since=since)

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
order_book_id = NULL # dict | 
since = NULL # dict |  (optional)

try:
    # Get a snapshot of base and quote balances for an order book and open a stream for real-time updates
    api_response = api_instance.stream_order_book_balances(order_book_id, since=since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->stream_order_book_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_book_id** | [**dict**](.md)|  | 
 **since** | [**dict**](.md)|  | [optional] 

### Return type

[**StreamOrderBookBalancesResponse**](StreamOrderBookBalancesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_orderbook_open_orders**
> LiveOrderbook stream_orderbook_open_orders(order_book_id, since=since)

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
order_book_id = NULL # dict | 
since = NULL # dict |  (optional)

try:
    # Get a snapshot of open orders in an order book and open a stream for real-time updates
    api_response = api_instance.stream_orderbook_open_orders(order_book_id, since=since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->stream_orderbook_open_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_book_id** | [**dict**](.md)|  | 
 **since** | [**dict**](.md)|  | [optional] 

### Return type

[**LiveOrderbook**](LiveOrderbook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_trades**
> StreamTradesResponse stream_trades(order_book_id, since=since)

Get a snapshot of trades executed on the given order book from a specific date and open a stream for real-time updates

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dora_client.DefaultApi()
order_book_id = NULL # dict | 
since = NULL # dict |  (optional)

try:
    # Get a snapshot of trades executed on the given order book from a specific date and open a stream for real-time updates
    api_response = api_instance.stream_trades(order_book_id, since=since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->stream_trades: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_book_id** | [**dict**](.md)|  | 
 **since** | [**dict**](.md)|  | [optional] 

### Return type

[**StreamTradesResponse**](StreamTradesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_available_balances**
> TransferBalancesResponse transfer_available_balances(body)

Transfer available balance between a user's accounts (e.g. global to isolated position)

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
body = dora_client.TransferBalancesRequest() # TransferBalancesRequest | 

try:
    # Transfer available balance between a user's accounts (e.g. global to isolated position)
    api_response = api_instance.transfer_available_balances(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->transfer_available_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransferBalancesRequest**](TransferBalancesRequest.md)|  | 

### Return type

[**TransferBalancesResponse**](TransferBalancesResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_config**
> UserUpdatedResponse update_user_config(body, user_id)

Update user configuration by ID

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
body = dora_client.UpdateUserConfigRequest() # UpdateUserConfigRequest | 
user_id = NULL # dict | 

try:
    # Update user configuration by ID
    api_response = api_instance.update_user_config(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_user_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateUserConfigRequest**](UpdateUserConfigRequest.md)|  | 
 **user_id** | [**dict**](.md)|  | 

### Return type

[**UserUpdatedResponse**](UserUpdatedResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_config_self**
> UserUpdatedResponse update_user_config_self(body)

Update user configuration for the authenticated user

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
body = dora_client.UpdateUserConfigRequest() # UpdateUserConfigRequest | 

try:
    # Update user configuration for the authenticated user
    api_response = api_instance.update_user_config_self(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_user_config_self: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateUserConfigRequest**](UpdateUserConfigRequest.md)|  | 

### Return type

[**UserUpdatedResponse**](UserUpdatedResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_submit_order**
> ValidateSubmitOrderResponse validate_submit_order(body)

Validate submit order request data

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
body = dora_client.ValidateSubmitOrderRequest() # ValidateSubmitOrderRequest | 

try:
    # Validate submit order request data
    api_response = api_instance.validate_submit_order(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->validate_submit_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ValidateSubmitOrderRequest**](ValidateSubmitOrderRequest.md)|  | 

### Return type

[**ValidateSubmitOrderResponse**](ValidateSubmitOrderResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_user**
> UserUpdatedResponse verify_user(user_id)

Verify a user by ID

### Example
```python
from __future__ import print_function
import time
import dora_client
from dora_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuthHeader
configuration = dora_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dora_client.DefaultApi(dora_client.ApiClient(configuration))
user_id = NULL # dict | 

try:
    # Verify a user by ID
    api_response = api_instance.verify_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->verify_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**dict**](.md)|  | 

### Return type

[**UserUpdatedResponse**](UserUpdatedResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

