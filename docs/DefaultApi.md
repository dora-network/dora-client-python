# dora_client.DefaultApi

All URIs are relative to *https://staging.dora.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_ledger_withdraw_request**](DefaultApi.md#approve_ledger_withdraw_request) | **POST** /v1/ledger/withdraw/requests/{withdrawal_id}/approve | Approve a pending withdrawal request
[**cancel_all_open_orders**](DefaultApi.md#cancel_all_open_orders) | **DELETE** /v1/orders | Cancel all open orders, if user passes orderbook on query param it will cancel all orders on specific orderbook, admin can cancel user&#39;s orders on specific orderbook
[**cancel_ledger_withdraw_request**](DefaultApi.md#cancel_ledger_withdraw_request) | **POST** /v1/ledger/withdraw/requests/{withdrawal_id}/cancel | Cancel a pending withdrawal request
[**cancel_order_by_id**](DefaultApi.md#cancel_order_by_id) | **DELETE** /v1/orders/{order_id} | Cancel an order by ID
[**check_user_email_exists**](DefaultApi.md#check_user_email_exists) | **GET** /v1/user/exists | Check whether a user email exists
[**claim_leverage_get_accrued_interest**](DefaultApi.md#claim_leverage_get_accrued_interest) | **POST** /v1/leverage/accrued_interest/claim | Claim current accrued leverage interest for a specific user
[**close_isolated_position**](DefaultApi.md#close_isolated_position) | **POST** /v1/positions/close | Close isolated positions, repaying the borrowed
[**create_api_key_for_user**](DefaultApi.md#create_api_key_for_user) | **POST** /v1/user/apikey | Create apikey for a user
[**create_api_key_for_user_id**](DefaultApi.md#create_api_key_for_user_id) | **POST** /v1/user/{user_id}/apikey | Create apikey for a user
[**create_conditional_order**](DefaultApi.md#create_conditional_order) | **POST** /v1/orders/conditional | Create a new conditional orders
[**create_order**](DefaultApi.md#create_order) | **POST** /v1/orders | Create a new order
[**create_user**](DefaultApi.md#create_user) | **POST** /v1/integrators/user | Create a new user
[**delete_user**](DefaultApi.md#delete_user) | **DELETE** /v1/user/{user_id} | Delete user by ID
[**get_all_asset_prices**](DefaultApi.md#get_all_asset_prices) | **GET** /v1/price | Get the current price of all assets
[**get_all_positions**](DefaultApi.md#get_all_positions) | **GET** /v1/ledger/positions | Get all users&#39; positions
[**get_all_withdrawal_requests**](DefaultApi.md#get_all_withdrawal_requests) | **GET** /v1/ledger/withdraw/requests | Get all withdrawal requests
[**get_api_keys_for_user_id**](DefaultApi.md#get_api_keys_for_user_id) | **GET** /v1/user/{user_id}/apikey | Get user&#39;s api keys: admin or integrator only
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
[**get_ledger_withdraw_requests_by_user_id**](DefaultApi.md#get_ledger_withdraw_requests_by_user_id) | **GET** /v1/ledger/withdraw/requests/{user_id} | Get all pending withdrawal requests for this user
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
[**get_realized_pnl_settlements**](DefaultApi.md#get_realized_pnl_settlements) | **GET** /v1/realized_pnl_settlements | Get realized P&amp;L settlements with filters
[**get_trade_by_id**](DefaultApi.md#get_trade_by_id) | **GET** /v1/trades/{trade_id} | Get a trade by ID
[**get_trades**](DefaultApi.md#get_trades) | **GET** /v1/trades | Get a filtered, paginated list of trades
[**get_transaction_by_id**](DefaultApi.md#get_transaction_by_id) | **GET** /v1/transactions/{transaction_id} | Get a transaction by ID
[**get_transactions**](DefaultApi.md#get_transactions) | **GET** /v1/transactions | Get a filtered, paginated list of transactions
[**get_transactions_settlements**](DefaultApi.md#get_transactions_settlements) | **GET** /v1/transactions/settlements | Get transactions settlements with filters
[**get_user_by_id**](DefaultApi.md#get_user_by_id) | **GET** /v1/user/{user_id} | Get user by ID (admin only)
[**get_user_coupon_payments_stream**](DefaultApi.md#get_user_coupon_payments_stream) | **GET** /v1/user/{user_id}/coupon_payments/stream | Stream user&#39;s coupon payment accruals in real time
[**get_user_ledger_stream**](DefaultApi.md#get_user_ledger_stream) | **GET** /v1/user/{user_id}/ledger/stream | Get a snapshot of user&#39;s ledger updates since a specific time, and opens a stream for further updates
[**get_user_order_updates_stream**](DefaultApi.md#get_user_order_updates_stream) | **GET** /v1/user/{user_id}/orders/{order_book_id}/updates/stream | Get a snapshot of user&#39;s order updates for the given order book since a specific time, and opens a stream for further updates
[**get_user_orders_updates_stream_all**](DefaultApi.md#get_user_orders_updates_stream_all) | **GET** /v1/user/{user_id}/orders/all/updates/stream | Get a snapshot of user&#39;s order updates across all order books since a specific time, and opens a stream for further updates
[**get_user_self**](DefaultApi.md#get_user_self) | **GET** /v1/user/self | Get user details for the authenticated user
[**get_user_transactions_stream**](DefaultApi.md#get_user_transactions_stream) | **GET** /v1/user/{user_id}/transactions/stream | Get a snapshot of user&#39;s executed transactions since a specific time, and opens a stream for further updates
[**get_users_api_keys**](DefaultApi.md#get_users_api_keys) | **GET** /v1/user/apikey | Get user&#39;s api keys
[**ledger_deposit**](DefaultApi.md#ledger_deposit) | **POST** /v1/ledger/deposit/{user_id} | Deposit assets into this user&#39;s account from the outside world
[**ledger_withdraw**](DefaultApi.md#ledger_withdraw) | **POST** /v1/ledger/withdraw/{user_id} | Withdraw assets from this user to the outside world
[**ledger_withdraw_request**](DefaultApi.md#ledger_withdraw_request) | **POST** /v1/ledger/withdraw/requests/{user_id} | Initiate a withdrawal request for this user to the outside world
[**ledger_withdraw_request_self**](DefaultApi.md#ledger_withdraw_request_self) | **POST** /v1/ledger/withdraw/requests/self | Initiate a withdrawal request for the logged in user to the outside world
[**leverage_get_accrued_interest_by_user**](DefaultApi.md#leverage_get_accrued_interest_by_user) | **GET** /v1/leverage/accrued_interest/self | Get current accrued leverage interest for the user
[**leverage_isolate_collateral**](DefaultApi.md#leverage_isolate_collateral) | **POST** /v1/leverage/isolate_collateral | Create an isolated position by transferring collateral to the position from the user&#39;s global collateral
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
[**reject_ledger_withdraw_request**](DefaultApi.md#reject_ledger_withdraw_request) | **POST** /v1/ledger/withdraw/requests/{withdrawal_id}/reject | Reject a pending withdrawal request
[**revoke_api_key_for_user**](DefaultApi.md#revoke_api_key_for_user) | **PUT** /v1/user/apikey/{key_id}/revoke | Revoke apikey for a user
[**revoke_api_key_for_user_id**](DefaultApi.md#revoke_api_key_for_user_id) | **PUT** /v1/user/{user_id}/apikey/{key_id}/revoke | Revoke apikey for a user: admin or integrator only
[**settle_leverage_accrued_interest**](DefaultApi.md#settle_leverage_accrued_interest) | **POST** /v1/leverage/accrued_interest/settle | Settle current accrued leverage interest for a specific user
[**settle_realized_pnl_record**](DefaultApi.md#settle_realized_pnl_record) | **PUT** /v1/realized_pnl_settlements/{settlement_id} | Mark a realized P&amp;L settlement as settled
[**settle_transactions_settlements**](DefaultApi.md#settle_transactions_settlements) | **PUT** /v1/transactions/settlements | Settle multiple transactions settlements in batch
[**stream_asset_prices**](DefaultApi.md#stream_asset_prices) | **GET** /v1/prices/stream | Stream real-time asset prices as map objects
[**stream_candle_data**](DefaultApi.md#stream_candle_data) | **GET** /v1/charts/{order_book_id}/candle/stream | Get a snapshot of candlestick data from date provided, and open a stream for real-time updates
[**stream_order_book_balances**](DefaultApi.md#stream_order_book_balances) | **GET** /v1/orderbooks/{order_book_id}/balances/stream | Get a snapshot of base and quote balances for an order book and open a stream for real-time updates
[**stream_orderbook_open_orders**](DefaultApi.md#stream_orderbook_open_orders) | **GET** /v1/orderbooks/{order_book_id}/open/stream | Get a snapshot of open orders in an order book and open a stream for real-time updates
[**stream_trades**](DefaultApi.md#stream_trades) | **GET** /v1/trades/{order_book_id}/stream | Get a snapshot of trades executed on the given order book from a specific date and open a stream for real-time updates
[**transfer_available_balances**](DefaultApi.md#transfer_available_balances) | **POST** /v1/positions/transfer_balances | Transfer available balance between a user&#39;s accounts (e.g. global to isolated position)
[**update_user_config**](DefaultApi.md#update_user_config) | **PUT** /v1/user/{user_id}/config | Update user configuration by ID
[**update_user_config_self**](DefaultApi.md#update_user_config_self) | **PUT** /v1/user/config/self | Update user configuration for the authenticated user
[**validate_submit_order**](DefaultApi.md#validate_submit_order) | **POST** /v1/orders/validate | Validate submit order request data
[**verify_user**](DefaultApi.md#verify_user) | **PUT** /v1/user/{user_id}/verify | Verify a user by ID


# **approve_ledger_withdraw_request**
> WithdrawalInitiationResponseEnvelope approve_ledger_withdraw_request(withdrawal_id, withdrawal_request_reason=withdrawal_request_reason)

Approve a pending withdrawal request

Approve a pending withdrawal request, allowing the transfer of assets to the outside world to proceed. Note that this does not interact with any external systems; it simply updates the status of the withdrawal request in the ledger. Actual transfer of assets must be handled separately.

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.withdrawal_initiation_response_envelope import WithdrawalInitiationResponseEnvelope
from dora_client.models.withdrawal_request_reason import WithdrawalRequestReason
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    withdrawal_id = 'withdrawal_id_example' # str | 
    withdrawal_request_reason = dora_client.WithdrawalRequestReason() # WithdrawalRequestReason |  (optional)

    try:
        # Approve a pending withdrawal request
        api_response = await api_instance.approve_ledger_withdraw_request(withdrawal_id, withdrawal_request_reason=withdrawal_request_reason)
        print("The response of DefaultApi->approve_ledger_withdraw_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->approve_ledger_withdraw_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **withdrawal_id** | **str**|  | 
 **withdrawal_request_reason** | [**WithdrawalRequestReason**](WithdrawalRequestReason.md)|  | [optional] 

### Return type

[**WithdrawalInitiationResponseEnvelope**](WithdrawalInitiationResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Withdrawal request approved successfully |  -  |
**400** | Bad request, e.g. invalid withdrawal ID format or request is not in a pending state |  -  |
**404** | Withdrawal request not found |  -  |
**403** | Forbidden, user does not have permission to approve this withdrawal request |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_all_open_orders**
> ListOrdersResponseEnvelope cancel_all_open_orders(order_book_id=order_book_id, user_id=user_id, order_kind=order_kind)

Cancel all open orders, if user passes orderbook on query param it will cancel all orders on specific orderbook, admin can cancel user's orders on specific orderbook

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.list_orders_response_envelope import ListOrdersResponseEnvelope
from dora_client.models.order_kind import OrderKind
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    order_book_id = 'order_book_id_example' # str |  (optional)
    user_id = 'user_id_example' # str |  (optional)
    order_kind = dora_client.OrderKind() # OrderKind |  (optional)

    try:
        # Cancel all open orders, if user passes orderbook on query param it will cancel all orders on specific orderbook, admin can cancel user's orders on specific orderbook
        api_response = await api_instance.cancel_all_open_orders(order_book_id=order_book_id, user_id=user_id, order_kind=order_kind)
        print("The response of DefaultApi->cancel_all_open_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->cancel_all_open_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_book_id** | **str**|  | [optional] 
 **user_id** | **str**|  | [optional] 
 **order_kind** | [**OrderKind**](.md)|  | [optional] 

### Return type

[**ListOrdersResponseEnvelope**](ListOrdersResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All open orders have been cancelled |  -  |
**401** | Unauthorized, user not logged in or does not have access to this orderbook |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_ledger_withdraw_request**
> WithdrawalInitiationResponseEnvelope cancel_ledger_withdraw_request(withdrawal_id, withdrawal_request_reason=withdrawal_request_reason)

Cancel a pending withdrawal request

Cancel a pending withdrawal request, providing an optional reason for the cancellation.

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.withdrawal_initiation_response_envelope import WithdrawalInitiationResponseEnvelope
from dora_client.models.withdrawal_request_reason import WithdrawalRequestReason
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    withdrawal_id = 'withdrawal_id_example' # str | 
    withdrawal_request_reason = dora_client.WithdrawalRequestReason() # WithdrawalRequestReason |  (optional)

    try:
        # Cancel a pending withdrawal request
        api_response = await api_instance.cancel_ledger_withdraw_request(withdrawal_id, withdrawal_request_reason=withdrawal_request_reason)
        print("The response of DefaultApi->cancel_ledger_withdraw_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->cancel_ledger_withdraw_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **withdrawal_id** | **str**|  | 
 **withdrawal_request_reason** | [**WithdrawalRequestReason**](WithdrawalRequestReason.md)|  | [optional] 

### Return type

[**WithdrawalInitiationResponseEnvelope**](WithdrawalInitiationResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Withdrawal request cancelled successfully |  -  |
**400** | Bad request, e.g. invalid withdrawal ID format or request is not in a pending state |  -  |
**404** | Withdrawal request not found |  -  |
**403** | Forbidden, user does not have permission to cancel this withdrawal request |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_order_by_id**
> CancelOrderResponseEnvelope cancel_order_by_id(order_id)

Cancel an order by ID

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.cancel_order_response_envelope import CancelOrderResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    order_id = 'order_id_example' # str | 

    try:
        # Cancel an order by ID
        api_response = await api_instance.cancel_order_by_id(order_id)
        print("The response of DefaultApi->cancel_order_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->cancel_order_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**|  | 

### Return type

[**CancelOrderResponseEnvelope**](CancelOrderResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order cancelled successfully |  -  |
**400** | Bad request, e.g. invalid order ID format |  -  |
**401** | Unauthorized, user not logged in or does not have access to this order |  -  |
**404** | Order not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_user_email_exists**
> EmailExistsResponseEnvelope check_user_email_exists(email)

Check whether a user email exists

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.email_exists_response_envelope import EmailExistsResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    email = 'email_example' # str | 

    try:
        # Check whether a user email exists
        api_response = await api_instance.check_user_email_exists(email)
        print("The response of DefaultApi->check_user_email_exists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->check_user_email_exists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

### Return type

[**EmailExistsResponseEnvelope**](EmailExistsResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | True if the email exists, false otherwise |  -  |
**400** | Bad request, e.g. invalid path parameters |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **claim_leverage_get_accrued_interest**
> ClaimLeverageAccruedInterestResponseEnvelope claim_leverage_get_accrued_interest(claim_leverage_accrued_interest_request)

Claim current accrued leverage interest for a specific user

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.claim_leverage_accrued_interest_request import ClaimLeverageAccruedInterestRequest
from dora_client.models.claim_leverage_accrued_interest_response_envelope import ClaimLeverageAccruedInterestResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    claim_leverage_accrued_interest_request = dora_client.ClaimLeverageAccruedInterestRequest() # ClaimLeverageAccruedInterestRequest | 

    try:
        # Claim current accrued leverage interest for a specific user
        api_response = await api_instance.claim_leverage_get_accrued_interest(claim_leverage_accrued_interest_request)
        print("The response of DefaultApi->claim_leverage_get_accrued_interest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->claim_leverage_get_accrued_interest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **claim_leverage_accrued_interest_request** | [**ClaimLeverageAccruedInterestRequest**](ClaimLeverageAccruedInterestRequest.md)|  | 

### Return type

[**ClaimLeverageAccruedInterestResponseEnvelope**](ClaimLeverageAccruedInterestResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current leverage accrued interest claimed successfully |  -  |
**400** | Bad request, e.g. invalid parameters |  -  |
**401** | Unauthorized, e.g. user not logged in or invalid credentials |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **close_isolated_position**
> ClosePositionResponseEnvelope close_isolated_position(close_position_request)

Close isolated positions, repaying the borrowed

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.close_position_request import ClosePositionRequest
from dora_client.models.close_position_response_envelope import ClosePositionResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    close_position_request = dora_client.ClosePositionRequest() # ClosePositionRequest | 

    try:
        # Close isolated positions, repaying the borrowed
        api_response = await api_instance.close_isolated_position(close_position_request)
        print("The response of DefaultApi->close_isolated_position:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->close_isolated_position: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **close_position_request** | [**ClosePositionRequest**](ClosePositionRequest.md)|  | 

### Return type

[**ClosePositionResponseEnvelope**](ClosePositionResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Isolated Position Closed |  -  |
**400** | Bad request, e.g. missing required fields |  -  |
**401** | Unauthorized, user not logged in or does not have access to this route |  -  |
**404** | Not found, e.g. order_book or position not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_api_key_for_user**
> CreateAPIKeyResponseEnvelope create_api_key_for_user(create_api_key_request)

Create apikey for a user

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.create_api_key_request import CreateAPIKeyRequest
from dora_client.models.create_api_key_response_envelope import CreateAPIKeyResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    create_api_key_request = dora_client.CreateAPIKeyRequest() # CreateAPIKeyRequest | 

    try:
        # Create apikey for a user
        api_response = await api_instance.create_api_key_for_user(create_api_key_request)
        print("The response of DefaultApi->create_api_key_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_api_key_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_api_key_request** | [**CreateAPIKeyRequest**](CreateAPIKeyRequest.md)|  | 

### Return type

[**CreateAPIKeyResponseEnvelope**](CreateAPIKeyResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | APIKey created |  -  |
**404** | User not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_api_key_for_user_id**
> CreateAPIKeyResponseEnvelope create_api_key_for_user_id(user_id, create_api_key_request)

Create apikey for a user

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.create_api_key_request import CreateAPIKeyRequest
from dora_client.models.create_api_key_response_envelope import CreateAPIKeyResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    user_id = 'user_id_example' # str | 
    create_api_key_request = dora_client.CreateAPIKeyRequest() # CreateAPIKeyRequest | 

    try:
        # Create apikey for a user
        api_response = await api_instance.create_api_key_for_user_id(user_id, create_api_key_request)
        print("The response of DefaultApi->create_api_key_for_user_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_api_key_for_user_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **create_api_key_request** | [**CreateAPIKeyRequest**](CreateAPIKeyRequest.md)|  | 

### Return type

[**CreateAPIKeyResponseEnvelope**](CreateAPIKeyResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | APIKey created |  -  |
**404** | User not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_conditional_order**
> CreateConditionalOrderResponseEnvelope create_conditional_order(create_conditional_order_request)

Create a new conditional orders

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.create_conditional_order_request import CreateConditionalOrderRequest
from dora_client.models.create_conditional_order_response_envelope import CreateConditionalOrderResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    create_conditional_order_request = dora_client.CreateConditionalOrderRequest() # CreateConditionalOrderRequest | 

    try:
        # Create a new conditional orders
        api_response = await api_instance.create_conditional_order(create_conditional_order_request)
        print("The response of DefaultApi->create_conditional_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_conditional_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_conditional_order_request** | [**CreateConditionalOrderRequest**](CreateConditionalOrderRequest.md)|  | 

### Return type

[**CreateConditionalOrderResponseEnvelope**](CreateConditionalOrderResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Conditional orders are created |  -  |
**400** | Bad request, e.g. missing required fields |  -  |
**401** | Unauthorized, user not logged in or does not have access to this orderbook |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_order**
> CreateOrderResponseEnvelope create_order(create_order_request)

Create a new order

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.create_order_request import CreateOrderRequest
from dora_client.models.create_order_response_envelope import CreateOrderResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    create_order_request = dora_client.CreateOrderRequest() # CreateOrderRequest | 

    try:
        # Create a new order
        api_response = await api_instance.create_order(create_order_request)
        print("The response of DefaultApi->create_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_order_request** | [**CreateOrderRequest**](CreateOrderRequest.md)|  | 

### Return type

[**CreateOrderResponseEnvelope**](CreateOrderResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Order created |  -  |
**400** | Bad request, e.g. missing required fields |  -  |
**401** | Unauthorized, user not logged in or does not have access to this orderbook |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> UserCreatedResponseEnvelope create_user(create_integrator_user_request)

Create a new user

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.create_integrator_user_request import CreateIntegratorUserRequest
from dora_client.models.user_created_response_envelope import UserCreatedResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    create_integrator_user_request = dora_client.CreateIntegratorUserRequest() # CreateIntegratorUserRequest | 

    try:
        # Create a new user
        api_response = await api_instance.create_user(create_integrator_user_request)
        print("The response of DefaultApi->create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_integrator_user_request** | [**CreateIntegratorUserRequest**](CreateIntegratorUserRequest.md)|  | 

### Return type

[**UserCreatedResponseEnvelope**](UserCreatedResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | User created |  -  |
**400** | Bad request, e.g. invalid query parameters |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> UserDeletedResponseEnvelope delete_user(user_id)

Delete user by ID

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.user_deleted_response_envelope import UserDeletedResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Delete user by ID
        api_response = await api_instance.delete_user(user_id)
        print("The response of DefaultApi->delete_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**UserDeletedResponseEnvelope**](UserDeletedResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User deleted |  -  |
**401** | Unauthorized, only admin can delete users |  -  |
**403** | Forbidden, only admin can delete users |  -  |
**404** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_asset_prices**
> ListAssetPriceResponseEnvelope get_all_asset_prices()

Get the current price of all assets

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.list_asset_price_response_envelope import ListAssetPriceResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)

    try:
        # Get the current price of all assets
        api_response = await api_instance.get_all_asset_prices()
        print("The response of DefaultApi->get_all_asset_prices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_asset_prices: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListAssetPriceResponseEnvelope**](ListAssetPriceResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current prices of all assets |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_positions**
> AllPositionsResponseEnvelope get_all_positions()

Get all users' positions

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.all_positions_response_envelope import AllPositionsResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)

    try:
        # Get all users' positions
        api_response = await api_instance.get_all_positions()
        print("The response of DefaultApi->get_all_positions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_positions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AllPositionsResponseEnvelope**](AllPositionsResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User positions |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_withdrawal_requests**
> AllWithdrawalInitiationsResponseEnvelope get_all_withdrawal_requests(status=status)

Get all withdrawal requests

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.all_withdrawal_initiations_response_envelope import AllWithdrawalInitiationsResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    status = 'status_example' # str |  (optional)

    try:
        # Get all withdrawal requests
        api_response = await api_instance.get_all_withdrawal_requests(status=status)
        print("The response of DefaultApi->get_all_withdrawal_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_withdrawal_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**|  | [optional] 

### Return type

[**AllWithdrawalInitiationsResponseEnvelope**](AllWithdrawalInitiationsResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of withdrawal requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_keys_for_user_id**
> APIKeyResponseEnvelope get_api_keys_for_user_id(user_id)

Get user's api keys: admin or integrator only

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.api_key_response_envelope import APIKeyResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Get user's api keys: admin or integrator only
        api_response = await api_instance.get_api_keys_for_user_id(user_id)
        print("The response of DefaultApi->get_api_keys_for_user_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_api_keys_for_user_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**APIKeyResponseEnvelope**](APIKeyResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of existing api-keys |  -  |
**400** | Bad request, e.g. invalid path parameters |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_by_id**
> GetAssetByIDResponseEnvelope get_asset_by_id(asset_id)

Get asset by ID

### Example


```python
import dora_client
from dora_client.models.get_asset_by_id_response_envelope import GetAssetByIDResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)


# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    asset_id = 'asset_id_example' # str | 

    try:
        # Get asset by ID
        api_response = await api_instance.get_asset_by_id(asset_id)
        print("The response of DefaultApi->get_asset_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_asset_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  | 

### Return type

[**GetAssetByIDResponseEnvelope**](GetAssetByIDResponseEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Asset details |  -  |
**400** | Bad request, e.g. invalid query parameters |  -  |
**404** | Asset not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_price**
> AssetPriceResponseEnvelope get_asset_price(asset_id)

Get the current price of an asset

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.asset_price_response_envelope import AssetPriceResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    asset_id = 'asset_id_example' # str | 

    try:
        # Get the current price of an asset
        api_response = await api_instance.get_asset_price(asset_id)
        print("The response of DefaultApi->get_asset_price:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_asset_price: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  | 

### Return type

[**AssetPriceResponseEnvelope**](AssetPriceResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current price of the asset |  -  |
**400** | Bad request, e.g. invalid ID format |  -  |
**404** | Asset not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_ytmby_id**
> GetAssetYTMByIDResponseEnvelope get_asset_ytmby_id(asset_id)

Get annualized yield to maturity for a bond asset

### Example


```python
import dora_client
from dora_client.models.get_asset_ytmby_id_response_envelope import GetAssetYTMByIDResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)


# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    asset_id = 'asset_id_example' # str | 

    try:
        # Get annualized yield to maturity for a bond asset
        api_response = await api_instance.get_asset_ytmby_id(asset_id)
        print("The response of DefaultApi->get_asset_ytmby_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_asset_ytmby_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  | 

### Return type

[**GetAssetYTMByIDResponseEnvelope**](GetAssetYTMByIDResponseEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Asset YTM details |  -  |
**400** | Bad request, e.g. invalid query parameters |  -  |
**404** | Asset not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assets_stream**
> StreamAssetsResponse get_assets_stream(since=since, until=until)

Get all inserts or updates for assets

### Example


```python
import dora_client
from dora_client.models.stream_assets_response import StreamAssetsResponse
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)


# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    since = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    until = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Get all inserts or updates for assets
        api_response = await api_instance.get_assets_stream(since=since, until=until)
        print("The response of DefaultApi->get_assets_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_assets_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **datetime**|  | [optional] 
 **until** | **datetime**|  | [optional] 

### Return type

[**StreamAssetsResponse**](StreamAssetsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Asset&#39;s stream |  -  |
**400** | Bad request, e.g. invalid query parameters |  -  |
**401** | Unauthorized, user not logged in or does not have access to this route |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_candle_data**
> ListCandlesResponseEnvelope get_candle_data(order_book_id, start, end, resolution=resolution)

Get candlestick data for an orderbook

### Example


```python
import dora_client
from dora_client.models.candle_resolution import CandleResolution
from dora_client.models.list_candles_response_envelope import ListCandlesResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)


# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    order_book_id = 'order_book_id_example' # str | 
    start = '2013-10-20T19:20:30+01:00' # datetime | 
    end = '2013-10-20T19:20:30+01:00' # datetime | 
    resolution = dora_client.CandleResolution() # CandleResolution |  (optional)

    try:
        # Get candlestick data for an orderbook
        api_response = await api_instance.get_candle_data(order_book_id, start, end, resolution=resolution)
        print("The response of DefaultApi->get_candle_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_candle_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_book_id** | **str**|  | 
 **start** | **datetime**|  | 
 **end** | **datetime**|  | 
 **resolution** | [**CandleResolution**](.md)|  | [optional] 

### Return type

[**ListCandlesResponseEnvelope**](ListCandlesResponseEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Candlestick data |  -  |
**400** | Bad request, e.g. invalid parameters |  -  |
**404** | Orderbook not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coupon_payments_by_asset_id**
> ListCouponPaymentsResponseEnvelope get_coupon_payments_by_asset_id(asset_id)

Get coupon payments for a bond asset

### Example


```python
import dora_client
from dora_client.models.list_coupon_payments_response_envelope import ListCouponPaymentsResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)


# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    asset_id = 'asset_id_example' # str | 

    try:
        # Get coupon payments for a bond asset
        api_response = await api_instance.get_coupon_payments_by_asset_id(asset_id)
        print("The response of DefaultApi->get_coupon_payments_by_asset_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_coupon_payments_by_asset_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  | 

### Return type

[**ListCouponPaymentsResponseEnvelope**](ListCouponPaymentsResponseEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of coupon payments |  -  |
**400** | Bad request, e.g. invalid query parameters |  -  |
**404** | Asset not found or no coupon payments available |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_l1_depth**
> GetTopOfBookResponseEnvelope get_l1_depth(order_book_id)

Get the top price levels for a specific orderbook (L1 market depth)

### Example


```python
import dora_client
from dora_client.models.get_top_of_book_response_envelope import GetTopOfBookResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)


# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    order_book_id = 'order_book_id_example' # str | 

    try:
        # Get the top price levels for a specific orderbook (L1 market depth)
        api_response = await api_instance.get_l1_depth(order_book_id)
        print("The response of DefaultApi->get_l1_depth:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_l1_depth: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_book_id** | **str**|  | 

### Return type

[**GetTopOfBookResponseEnvelope**](GetTopOfBookResponseEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Top price levels data |  -  |
**400** | Bad request, e.g. invalid query parameters |  -  |
**404** | Orderbook not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_l2_depth**
> ListOrderBookDepthResponseEnvelope get_l2_depth(order_book_id)

Get the aggregated price levels for a specific orderbook (L2 market depth)

### Example


```python
import dora_client
from dora_client.models.list_order_book_depth_response_envelope import ListOrderBookDepthResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)


# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    order_book_id = 'order_book_id_example' # str | 

    try:
        # Get the aggregated price levels for a specific orderbook (L2 market depth)
        api_response = await api_instance.get_l2_depth(order_book_id)
        print("The response of DefaultApi->get_l2_depth:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_l2_depth: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_book_id** | **str**|  | 

### Return type

[**ListOrderBookDepthResponseEnvelope**](ListOrderBookDepthResponseEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order book depth data |  -  |
**400** | Bad request, e.g. invalid query parameters |  -  |
**404** | Orderbook not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_l3_depth**
> ListOrdersResponseEnvelope get_l3_depth(order_book_id)

Get all open orders for a specific orderbook (L3 market depth)

### Example


```python
import dora_client
from dora_client.models.list_orders_response_envelope import ListOrdersResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)


# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    order_book_id = 'order_book_id_example' # str | 

    try:
        # Get all open orders for a specific orderbook (L3 market depth)
        api_response = await api_instance.get_l3_depth(order_book_id)
        print("The response of DefaultApi->get_l3_depth:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_l3_depth: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_book_id** | **str**|  | 

### Return type

[**ListOrdersResponseEnvelope**](ListOrdersResponseEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of orders for the orderbook |  -  |
**400** | Bad request, e.g. invalid query parameters |  -  |
**401** | Unauthorized, user not logged in or does not have access to this orderbook |  -  |
**404** | Orderbook not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ledger_balances_self**
> UserBalanceResponseEnvelope get_ledger_balances_self()

Get your own available, locked, and borrowed assets

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.user_balance_response_envelope import UserBalanceResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)

    try:
        # Get your own available, locked, and borrowed assets
        api_response = await api_instance.get_ledger_balances_self()
        print("The response of DefaultApi->get_ledger_balances_self:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_ledger_balances_self: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserBalanceResponseEnvelope**](UserBalanceResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User balances |  -  |
**400** | Bad request, e.g. invalid user ID format |  -  |
**404** | User not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ledger_interest_self**
> UserInterestResponseEnvelope get_ledger_interest_self()

Get your own interest

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.user_interest_response_envelope import UserInterestResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)

    try:
        # Get your own interest
        api_response = await api_instance.get_ledger_interest_self()
        print("The response of DefaultApi->get_ledger_interest_self:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_ledger_interest_self: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserInterestResponseEnvelope**](UserInterestResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User interest |  -  |
**400** | Bad request, e.g. invalid user ID format |  -  |
**404** | User not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ledger_module**
> LedgerModuleResponseEnvelope get_ledger_module()

Get the entire module object, including unborrowed leverage assets and total leverage trackers

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.ledger_module_response_envelope import LedgerModuleResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)

    try:
        # Get the entire module object, including unborrowed leverage assets and total leverage trackers
        api_response = await api_instance.get_ledger_module()
        print("The response of DefaultApi->get_ledger_module:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_ledger_module: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LedgerModuleResponseEnvelope**](LedgerModuleResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Leverage module object |  -  |
**404** | Module not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ledger_module_by_asset**
> LedgerModuleByAssetResponseEnvelope get_ledger_module_by_asset(asset_id)

Get the module object for a single asset ID

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.ledger_module_by_asset_response_envelope import LedgerModuleByAssetResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    asset_id = 'asset_id_example' # str | 

    try:
        # Get the module object for a single asset ID
        api_response = await api_instance.get_ledger_module_by_asset(asset_id)
        print("The response of DefaultApi->get_ledger_module_by_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_ledger_module_by_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  | 

### Return type

[**LedgerModuleByAssetResponseEnvelope**](LedgerModuleByAssetResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Leverage module balance for asset |  -  |
**400** | Bad request, e.g. invalid asset ID format |  -  |
**404** | Asset not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ledger_positions_self**
> UserPositionResponseEnvelope get_ledger_positions_self()

Get your own positions

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.user_position_response_envelope import UserPositionResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)

    try:
        # Get your own positions
        api_response = await api_instance.get_ledger_positions_self()
        print("The response of DefaultApi->get_ledger_positions_self:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_ledger_positions_self: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserPositionResponseEnvelope**](UserPositionResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User positions |  -  |
**400** | Bad request, e.g. invalid user ID format |  -  |
**404** | User not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ledger_value_self**
> UserValueResponseEnvelope get_ledger_value_self()

Get your own available, locked, and borrowed USD value; and realized and unrealized PnL

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.user_value_response_envelope import UserValueResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)

    try:
        # Get your own available, locked, and borrowed USD value; and realized and unrealized PnL
        api_response = await api_instance.get_ledger_value_self()
        print("The response of DefaultApi->get_ledger_value_self:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_ledger_value_self: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserValueResponseEnvelope**](UserValueResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User value |  -  |
**400** | Bad request, e.g. invalid user ID format |  -  |
**404** | User not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ledger_withdraw_requests_by_self**
> AllWithdrawalInitiationsResponseEnvelope get_ledger_withdraw_requests_by_self(status=status)

Get all pending withdrawal requests for the logged in user

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.all_withdrawal_initiations_response_envelope import AllWithdrawalInitiationsResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    status = 'status_example' # str |  (optional)

    try:
        # Get all pending withdrawal requests for the logged in user
        api_response = await api_instance.get_ledger_withdraw_requests_by_self(status=status)
        print("The response of DefaultApi->get_ledger_withdraw_requests_by_self:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_ledger_withdraw_requests_by_self: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**|  | [optional] 

### Return type

[**AllWithdrawalInitiationsResponseEnvelope**](AllWithdrawalInitiationsResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of pending withdrawal requests for the logged in user |  -  |
**400** | Bad request, e.g. invalid user ID format |  -  |
**404** | User not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ledger_withdraw_requests_by_user_id**
> AllWithdrawalInitiationsResponseEnvelope get_ledger_withdraw_requests_by_user_id(user_id, status=status)

Get all pending withdrawal requests for this user

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.all_withdrawal_initiations_response_envelope import AllWithdrawalInitiationsResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    user_id = 'user_id_example' # str | 
    status = 'status_example' # str |  (optional)

    try:
        # Get all pending withdrawal requests for this user
        api_response = await api_instance.get_ledger_withdraw_requests_by_user_id(user_id, status=status)
        print("The response of DefaultApi->get_ledger_withdraw_requests_by_user_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_ledger_withdraw_requests_by_user_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **status** | **str**|  | [optional] 

### Return type

[**AllWithdrawalInitiationsResponseEnvelope**](AllWithdrawalInitiationsResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of pending withdrawal requests for this user |  -  |
**400** | Bad request, e.g. invalid user ID format |  -  |
**404** | User not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_by_id**
> OrderResponseEnvelope get_order_by_id(order_id)

Get order by ID

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.order_response_envelope import OrderResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    order_id = 'order_id_example' # str | 

    try:
        # Get order by ID
        api_response = await api_instance.get_order_by_id(order_id)
        print("The response of DefaultApi->get_order_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_order_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**|  | 

### Return type

[**OrderResponseEnvelope**](OrderResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order details |  -  |
**400** | Bad request, e.g. invalid order ID format |  -  |
**401** | Unauthorized, user not logged in or does not have access to this order |  -  |
**404** | Order not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orderbook_by_id**
> OrderBookResponseEnvelope get_orderbook_by_id(order_book_id)

Get orderbook by ID

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.order_book_response_envelope import OrderBookResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    order_book_id = 'order_book_id_example' # str | 

    try:
        # Get orderbook by ID
        api_response = await api_instance.get_orderbook_by_id(order_book_id)
        print("The response of DefaultApi->get_orderbook_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_orderbook_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_book_id** | **str**|  | 

### Return type

[**OrderBookResponseEnvelope**](OrderBookResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Orderbook details |  -  |
**400** | Bad request, e.g. invalid query parameters |  -  |
**404** | Orderbook not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orderbook_depth**
> ListOrderBookDepthResponseEnvelope get_orderbook_depth(order_book_id)

Get the aggregated price levels for a specific orderbook (L2 market depth)

### Example


```python
import dora_client
from dora_client.models.list_order_book_depth_response_envelope import ListOrderBookDepthResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)


# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    order_book_id = 'order_book_id_example' # str | 

    try:
        # Get the aggregated price levels for a specific orderbook (L2 market depth)
        api_response = await api_instance.get_orderbook_depth(order_book_id)
        print("The response of DefaultApi->get_orderbook_depth:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_orderbook_depth: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_book_id** | **str**|  | 

### Return type

[**ListOrderBookDepthResponseEnvelope**](ListOrderBookDepthResponseEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order book depth data |  -  |
**400** | Bad request, e.g. invalid query parameters |  -  |
**404** | Orderbook not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orderbook_orders**
> ListOrdersResponseEnvelope get_orderbook_orders(order_book_id)

Get all open orders for a specific orderbook (L3 market depth)

### Example


```python
import dora_client
from dora_client.models.list_orders_response_envelope import ListOrdersResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)


# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    order_book_id = 'order_book_id_example' # str | 

    try:
        # Get all open orders for a specific orderbook (L3 market depth)
        api_response = await api_instance.get_orderbook_orders(order_book_id)
        print("The response of DefaultApi->get_orderbook_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_orderbook_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_book_id** | **str**|  | 

### Return type

[**ListOrdersResponseEnvelope**](ListOrdersResponseEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of orders for the orderbook |  -  |
**400** | Bad request, e.g. invalid query parameters |  -  |
**401** | Unauthorized, user not logged in or does not have access to this orderbook |  -  |
**404** | Orderbook not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orderbook_stats**
> OrderbookStatsResponseEnvelope get_orderbook_stats(order_book_id)

Get orderbook stats

### Example


```python
import dora_client
from dora_client.models.orderbook_stats_response_envelope import OrderbookStatsResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)


# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    order_book_id = 'order_book_id_example' # str | 

    try:
        # Get orderbook stats
        api_response = await api_instance.get_orderbook_stats(order_book_id)
        print("The response of DefaultApi->get_orderbook_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_orderbook_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_book_id** | **str**|  | 

### Return type

[**OrderbookStatsResponseEnvelope**](OrderbookStatsResponseEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Orderbook stats details |  -  |
**204** | No Content |  -  |
**400** | Bad request, e.g. invalid query parameters |  -  |
**404** | Orderbook not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orderbook_stats_stream**
> OrderbookStats get_orderbook_stats_stream(order_book_id)

Orderbook stats stream

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.orderbook_stats import OrderbookStats
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    order_book_id = 'order_book_id_example' # str | 

    try:
        # Orderbook stats stream
        api_response = await api_instance.get_orderbook_stats_stream(order_book_id)
        print("The response of DefaultApi->get_orderbook_stats_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_orderbook_stats_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_book_id** | **str**|  | 

### Return type

[**OrderbookStats**](OrderbookStats.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Orderbook stats stream |  -  |
**204** | No Content |  -  |
**400** | Bad request, e.g. invalid query parameters |  -  |
**404** | Orderbook not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orderbook_summary**
> OrderBookSummaryResponseEnvelope get_orderbook_summary(order_book_id)

Get summary of an orderbook

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.order_book_summary_response_envelope import OrderBookSummaryResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    order_book_id = 'order_book_id_example' # str | 

    try:
        # Get summary of an orderbook
        api_response = await api_instance.get_orderbook_summary(order_book_id)
        print("The response of DefaultApi->get_orderbook_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_orderbook_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_book_id** | **str**|  | 

### Return type

[**OrderBookSummaryResponseEnvelope**](OrderBookSummaryResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Orderbook summary data |  -  |
**400** | Bad request, e.g. invalid query parameters |  -  |
**404** | Orderbook not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orderbook_top**
> GetTopOfBookResponseEnvelope get_orderbook_top(order_book_id)

Get the top price levels for a specific orderbook (L1 market depth)

### Example


```python
import dora_client
from dora_client.models.get_top_of_book_response_envelope import GetTopOfBookResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)


# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    order_book_id = 'order_book_id_example' # str | 

    try:
        # Get the top price levels for a specific orderbook (L1 market depth)
        api_response = await api_instance.get_orderbook_top(order_book_id)
        print("The response of DefaultApi->get_orderbook_top:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_orderbook_top: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_book_id** | **str**|  | 

### Return type

[**GetTopOfBookResponseEnvelope**](GetTopOfBookResponseEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Top price levels data |  -  |
**400** | Bad request, e.g. invalid query parameters |  -  |
**404** | Orderbook not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pl_for_self_by_account**
> PLResponseEnvelope get_pl_for_self_by_account()

Get account-by-account PL breakdown for the logged in user

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.pl_response_envelope import PLResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)

    try:
        # Get account-by-account PL breakdown for the logged in user
        api_response = await api_instance.get_pl_for_self_by_account()
        print("The response of DefaultApi->get_pl_for_self_by_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_pl_for_self_by_account: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PLResponseEnvelope**](PLResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of user accounts with a PL breakdown by asset and summary |  -  |
**401** | Unauthorized, user is not logged in |  -  |
**404** | User not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pool_price**
> PoolPriceResponseEnvelope get_pool_price(pool_id)

Get the current price of a pool

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.pool_price_response_envelope import PoolPriceResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    pool_id = 'pool_id_example' # str | 

    try:
        # Get the current price of a pool
        api_response = await api_instance.get_pool_price(pool_id)
        print("The response of DefaultApi->get_pool_price:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_pool_price: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**|  | 

### Return type

[**PoolPriceResponseEnvelope**](PoolPriceResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current price of the pool |  -  |
**400** | Bad request, e.g. invalid ID format |  -  |
**404** | Pool not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_realized_pnl_settlements**
> GetRealizedPnlSettlementsResponseEnvelope get_realized_pnl_settlements(user_id=user_id, tenant_id=tenant_id, position_id=position_id, created_after=created_after, settled_before=settled_before, is_settled=is_settled)

Get realized P&L settlements with filters

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.get_realized_pnl_settlements_response_envelope import GetRealizedPnlSettlementsResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    user_id = 'user_id_example' # str |  (optional)
    tenant_id = 'tenant_id_example' # str |  (optional)
    position_id = 'position_id_example' # str |  (optional)
    created_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    settled_before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    is_settled = True # bool |  (optional)

    try:
        # Get realized P&L settlements with filters
        api_response = await api_instance.get_realized_pnl_settlements(user_id=user_id, tenant_id=tenant_id, position_id=position_id, created_after=created_after, settled_before=settled_before, is_settled=is_settled)
        print("The response of DefaultApi->get_realized_pnl_settlements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_realized_pnl_settlements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **position_id** | **str**|  | [optional] 
 **created_after** | **datetime**|  | [optional] 
 **settled_before** | **datetime**|  | [optional] 
 **is_settled** | **bool**|  | [optional] 

### Return type

[**GetRealizedPnlSettlementsResponseEnvelope**](GetRealizedPnlSettlementsResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of realized P&amp;L settlements with filters applied |  -  |
**401** | Unauthorized, user is not logged in |  -  |
**403** | Forbidden, user does not have access |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trade_by_id**
> TradeResponseEnvelope get_trade_by_id(trade_id)

Get a trade by ID

### Example


```python
import dora_client
from dora_client.models.trade_response_envelope import TradeResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)


# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    trade_id = 'trade_id_example' # str | 

    try:
        # Get a trade by ID
        api_response = await api_instance.get_trade_by_id(trade_id)
        print("The response of DefaultApi->get_trade_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_trade_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trade_id** | **str**|  | 

### Return type

[**TradeResponseEnvelope**](TradeResponseEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Trade details |  -  |
**400** | Bad request, e.g. invalid ID format |  -  |
**404** | Trade not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trades**
> ListTradeResponseEnvelope get_trades(order_book_ids=order_book_ids, user_ids=user_ids, start=start, end=end, page=page, limit=limit)

Get a filtered, paginated list of trades

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.list_trade_response_envelope import ListTradeResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    order_book_ids = ['order_book_ids_example'] # List[str] |  (optional)
    user_ids = ['user_ids_example'] # List[str] |  (optional)
    start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    page = 1 # int |  (optional) (default to 1)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Get a filtered, paginated list of trades
        api_response = await api_instance.get_trades(order_book_ids=order_book_ids, user_ids=user_ids, start=start, end=end, page=page, limit=limit)
        print("The response of DefaultApi->get_trades:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_trades: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_book_ids** | [**List[str]**](str.md)|  | [optional] 
 **user_ids** | [**List[str]**](str.md)|  | [optional] 
 **start** | **datetime**|  | [optional] 
 **end** | **datetime**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ListTradeResponseEnvelope**](ListTradeResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of trades |  -  |
**400** | Bad request, e.g. invalid parameters |  -  |
**404** | No trades found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_by_id**
> TransactionResponseEnvelope get_transaction_by_id(transaction_id)

Get a transaction by ID

### Example


```python
import dora_client
from dora_client.models.transaction_response_envelope import TransactionResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)


# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    transaction_id = 'transaction_id_example' # str | 

    try:
        # Get a transaction by ID
        api_response = await api_instance.get_transaction_by_id(transaction_id)
        print("The response of DefaultApi->get_transaction_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_transaction_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**|  | 

### Return type

[**TransactionResponseEnvelope**](TransactionResponseEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transaction details |  -  |
**400** | Bad request, e.g. invalid ID format |  -  |
**404** | Transaction not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions**
> ListTransactionsResponseEnvelope get_transactions(pools=pools, user_ids=user_ids, tx_kinds=tx_kinds, start=start, end=end, tenant_id=tenant_id, page=page, limit=limit)

Get a filtered, paginated list of transactions

### Example


```python
import dora_client
from dora_client.models.list_transactions_response_envelope import ListTransactionsResponseEnvelope
from dora_client.models.transaction_kind import TransactionKind
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)


# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    pools = ['pools_example'] # List[str] |  (optional)
    user_ids = ['user_ids_example'] # List[str] |  (optional)
    tx_kinds = [dora_client.TransactionKind()] # List[TransactionKind] |  (optional)
    start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    tenant_id = 'tenant_id_example' # str |  (optional)
    page = 1 # int |  (optional) (default to 1)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Get a filtered, paginated list of transactions
        api_response = await api_instance.get_transactions(pools=pools, user_ids=user_ids, tx_kinds=tx_kinds, start=start, end=end, tenant_id=tenant_id, page=page, limit=limit)
        print("The response of DefaultApi->get_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pools** | [**List[str]**](str.md)|  | [optional] 
 **user_ids** | [**List[str]**](str.md)|  | [optional] 
 **tx_kinds** | [**List[TransactionKind]**](TransactionKind.md)|  | [optional] 
 **start** | **datetime**|  | [optional] 
 **end** | **datetime**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ListTransactionsResponseEnvelope**](ListTransactionsResponseEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of transactions |  -  |
**400** | Bad request, e.g. insufficient funds or invalid parameters |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_settlements**
> TransactionsSettlementsResponseEnvelope get_transactions_settlements(tenant_id=tenant_id, user_id=user_id, position_id=position_id, tx_kind=tx_kind, created_after=created_after, settled_before=settled_before, is_settled=is_settled)

Get transactions settlements with filters

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.transactions_settlements_response_envelope import TransactionsSettlementsResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant ID to filter settlements (optional)
    user_id = 'user_id_example' # str | User ID to filter settlements (optional)
    position_id = 'position_id_example' # str | Position ID to filter settlements (optional)
    tx_kind = 'tx_kind_example' # str | Transaction kind to filter settlements (optional)
    created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter settlements created after this time (optional)
    settled_before = '2013-10-20T19:20:30+01:00' # datetime | Filter settlements settled before this time (optional)
    is_settled = True # bool | Filter settlements by settlement status (optional)

    try:
        # Get transactions settlements with filters
        api_response = await api_instance.get_transactions_settlements(tenant_id=tenant_id, user_id=user_id, position_id=position_id, tx_kind=tx_kind, created_after=created_after, settled_before=settled_before, is_settled=is_settled)
        print("The response of DefaultApi->get_transactions_settlements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_transactions_settlements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID to filter settlements | [optional] 
 **user_id** | **str**| User ID to filter settlements | [optional] 
 **position_id** | **str**| Position ID to filter settlements | [optional] 
 **tx_kind** | **str**| Transaction kind to filter settlements | [optional] 
 **created_after** | **datetime**| Filter settlements created after this time | [optional] 
 **settled_before** | **datetime**| Filter settlements settled before this time | [optional] 
 **is_settled** | **bool**| Filter settlements by settlement status | [optional] 

### Return type

[**TransactionsSettlementsResponseEnvelope**](TransactionsSettlementsResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of transaction settlements |  -  |
**400** | Bad request |  -  |
**404** | No settlements found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_id**
> UserEnvelope get_user_by_id(user_id)

Get user by ID (admin only)

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.user_envelope import UserEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Get user by ID (admin only)
        api_response = await api_instance.get_user_by_id(user_id)
        print("The response of DefaultApi->get_user_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_user_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**UserEnvelope**](UserEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User details |  -  |
**400** | Bad request, e.g. invalid query parameters |  -  |
**404** | User not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_coupon_payments_stream**
> StreamUserCouponPaymentsResponse get_user_coupon_payments_stream(user_id)

Stream user's coupon payment accruals in real time

### Example

* Api Key Authentication (apiKeyAuthQuery):

```python
import dora_client
from dora_client.models.stream_user_coupon_payments_response import StreamUserCouponPaymentsResponse
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthQuery
configuration.api_key['apiKeyAuthQuery'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthQuery'] = 'Bearer'

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Stream user's coupon payment accruals in real time
        api_response = await api_instance.get_user_coupon_payments_stream(user_id)
        print("The response of DefaultApi->get_user_coupon_payments_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_user_coupon_payments_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**StreamUserCouponPaymentsResponse**](StreamUserCouponPaymentsResponse.md)

### Authorization

[apiKeyAuthQuery](../README.md#apiKeyAuthQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User&#39;s coupon payments stream |  -  |
**400** | Bad request, e.g. invalid query parameters |  -  |
**401** | Unauthorized, user not logged in or does not have access to this data |  -  |
**404** | User not found or no coupon payments available |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_ledger_stream**
> StreamPositionsResponse get_user_ledger_stream(user_id)

Get a snapshot of user's ledger updates since a specific time, and opens a stream for further updates

### Example

* Api Key Authentication (apiKeyAuthQuery):

```python
import dora_client
from dora_client.models.stream_positions_response import StreamPositionsResponse
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthQuery
configuration.api_key['apiKeyAuthQuery'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthQuery'] = 'Bearer'

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Get a snapshot of user's ledger updates since a specific time, and opens a stream for further updates
        api_response = await api_instance.get_user_ledger_stream(user_id)
        print("The response of DefaultApi->get_user_ledger_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_user_ledger_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**StreamPositionsResponse**](StreamPositionsResponse.md)

### Authorization

[apiKeyAuthQuery](../README.md#apiKeyAuthQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User&#39;s ledger stream |  -  |
**400** | Bad request, e.g. invalid query parameters |  -  |
**401** | Unauthorized, user not logged in or does not have access to this ledger |  -  |
**404** | User not found or no ledger entries available |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_order_updates_stream**
> StreamOrderUpdatesResponse get_user_order_updates_stream(user_id, order_book_id, since=since)

Get a snapshot of user's order updates for the given order book since a specific time, and opens a stream for further updates

### Example

* Api Key Authentication (apiKeyAuthQuery):

```python
import dora_client
from dora_client.models.stream_order_updates_response import StreamOrderUpdatesResponse
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthQuery
configuration.api_key['apiKeyAuthQuery'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthQuery'] = 'Bearer'

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    user_id = 'user_id_example' # str | 
    order_book_id = 'order_book_id_example' # str | 
    since = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Get a snapshot of user's order updates for the given order book since a specific time, and opens a stream for further updates
        api_response = await api_instance.get_user_order_updates_stream(user_id, order_book_id, since=since)
        print("The response of DefaultApi->get_user_order_updates_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_user_order_updates_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **order_book_id** | **str**|  | 
 **since** | **datetime**|  | [optional] 

### Return type

[**StreamOrderUpdatesResponse**](StreamOrderUpdatesResponse.md)

### Authorization

[apiKeyAuthQuery](../README.md#apiKeyAuthQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User&#39;s orders stream |  -  |
**400** | Bad request, e.g. invalid query parameters |  -  |
**401** | Unauthorized, user not logged in or does not have access to this orderbook |  -  |
**404** | User not found or no orders available |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_orders_updates_stream_all**
> StreamOrderUpdatesResponse get_user_orders_updates_stream_all(user_id, since=since)

Get a snapshot of user's order updates across all order books since a specific time, and opens a stream for further updates

### Example

* Api Key Authentication (apiKeyAuthQuery):

```python
import dora_client
from dora_client.models.stream_order_updates_response import StreamOrderUpdatesResponse
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthQuery
configuration.api_key['apiKeyAuthQuery'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthQuery'] = 'Bearer'

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    user_id = 'user_id_example' # str | 
    since = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Get a snapshot of user's order updates across all order books since a specific time, and opens a stream for further updates
        api_response = await api_instance.get_user_orders_updates_stream_all(user_id, since=since)
        print("The response of DefaultApi->get_user_orders_updates_stream_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_user_orders_updates_stream_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **since** | **datetime**|  | [optional] 

### Return type

[**StreamOrderUpdatesResponse**](StreamOrderUpdatesResponse.md)

### Authorization

[apiKeyAuthQuery](../README.md#apiKeyAuthQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User&#39;s orders stream |  -  |
**400** | Bad request, e.g. invalid query parameters |  -  |
**401** | Unauthorized, user not logged in or does not have access to this orderbook |  -  |
**404** | User not found or no orders available |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_self**
> UserEnvelope get_user_self()

Get user details for the authenticated user

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.user_envelope import UserEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)

    try:
        # Get user details for the authenticated user
        api_response = await api_instance.get_user_self()
        print("The response of DefaultApi->get_user_self:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_user_self: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserEnvelope**](UserEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User details |  -  |
**400** | Bad request, e.g. invalid query parameters |  -  |
**404** | User not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_transactions_stream**
> StreamTransactionsResponse get_user_transactions_stream(user_id, since=since)

Get a snapshot of user's executed transactions since a specific time, and opens a stream for further updates

### Example

* Api Key Authentication (apiKeyAuthQuery):

```python
import dora_client
from dora_client.models.stream_transactions_response import StreamTransactionsResponse
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthQuery
configuration.api_key['apiKeyAuthQuery'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthQuery'] = 'Bearer'

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    user_id = 'user_id_example' # str | 
    since = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Get a snapshot of user's executed transactions since a specific time, and opens a stream for further updates
        api_response = await api_instance.get_user_transactions_stream(user_id, since=since)
        print("The response of DefaultApi->get_user_transactions_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_user_transactions_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **since** | **datetime**|  | [optional] 

### Return type

[**StreamTransactionsResponse**](StreamTransactionsResponse.md)

### Authorization

[apiKeyAuthQuery](../README.md#apiKeyAuthQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User&#39;s transactions stream |  -  |
**400** | Bad request, e.g. invalid query parameters |  -  |
**401** | Unauthorized, user not logged in or does not have access to this transactions |  -  |
**404** | User not found or no transactions available |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_api_keys**
> APIKeyResponseEnvelope get_users_api_keys()

Get user's api keys

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.api_key_response_envelope import APIKeyResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)

    try:
        # Get user's api keys
        api_response = await api_instance.get_users_api_keys()
        print("The response of DefaultApi->get_users_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_users_api_keys: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**APIKeyResponseEnvelope**](APIKeyResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of existing api-keys |  -  |
**400** | Bad request, e.g. invalid path parameters |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ledger_deposit**
> FundUserResponseEnvelope ledger_deposit(user_id, fund_user_request)

Deposit assets into this user's account from the outside world

Deposit assets into this user's account from the outside world. Note that this does not interact with any external systems; it simply adds the amount to the user's available balance in the ledger. Actual transfer of assets must be handled separately.

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.fund_user_request import FundUserRequest
from dora_client.models.fund_user_response_envelope import FundUserResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    user_id = 'user_id_example' # str | 
    fund_user_request = dora_client.FundUserRequest() # FundUserRequest | 

    try:
        # Deposit assets into this user's account from the outside world
        api_response = await api_instance.ledger_deposit(user_id, fund_user_request)
        print("The response of DefaultApi->ledger_deposit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->ledger_deposit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **fund_user_request** | [**FundUserRequest**](FundUserRequest.md)|  | 

### Return type

[**FundUserResponseEnvelope**](FundUserResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Deposit successful |  -  |
**400** | Bad request, e.g. invalid parameters or insufficient funds |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ledger_withdraw**
> FundUserResponseEnvelope ledger_withdraw(user_id, defund_user_request, status=status)

Withdraw assets from this user to the outside world

Withdraw assets from this user's account to the outside world. Note that this does not interact with any external systems; it simply deducts the amount from the user's available balance in the ledger. Actual transfer of assets must be handled separately.

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.defund_user_request import DefundUserRequest
from dora_client.models.fund_user_response_envelope import FundUserResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    user_id = 'user_id_example' # str | 
    defund_user_request = dora_client.DefundUserRequest() # DefundUserRequest | 
    status = 'status_example' # str |  (optional)

    try:
        # Withdraw assets from this user to the outside world
        api_response = await api_instance.ledger_withdraw(user_id, defund_user_request, status=status)
        print("The response of DefaultApi->ledger_withdraw:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->ledger_withdraw: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **defund_user_request** | [**DefundUserRequest**](DefundUserRequest.md)|  | 
 **status** | **str**|  | [optional] 

### Return type

[**FundUserResponseEnvelope**](FundUserResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Withdraw successful |  -  |
**400** | Bad request, e.g. invalid parameters or insufficient funds |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ledger_withdraw_request**
> WithdrawalInitiationResponseEnvelope ledger_withdraw_request(user_id, defund_user_request)

Initiate a withdrawal request for this user to the outside world

Withdraw assets from this user's account to the outside world. Note that this does not interact with any external systems; it simply deducts the amount from the user's available balance in the ledger. Actual transfer of assets must be handled separately.

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.defund_user_request import DefundUserRequest
from dora_client.models.withdrawal_initiation_response_envelope import WithdrawalInitiationResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    user_id = 'user_id_example' # str | 
    defund_user_request = dora_client.DefundUserRequest() # DefundUserRequest | 

    try:
        # Initiate a withdrawal request for this user to the outside world
        api_response = await api_instance.ledger_withdraw_request(user_id, defund_user_request)
        print("The response of DefaultApi->ledger_withdraw_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->ledger_withdraw_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **defund_user_request** | [**DefundUserRequest**](DefundUserRequest.md)|  | 

### Return type

[**WithdrawalInitiationResponseEnvelope**](WithdrawalInitiationResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Withdraw request initiation successful |  -  |
**400** | Bad request, e.g. invalid parameters or insufficient funds |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ledger_withdraw_request_self**
> WithdrawalInitiationResponseEnvelope ledger_withdraw_request_self(user_id, defund_user_request)

Initiate a withdrawal request for the logged in user to the outside world

Withdraw assets from the logged in user's account to the outside world. Note that this does not interact with any external systems; it simply deducts the amount from the user's available balance in the ledger. Actual transfer of assets must be handled separately.

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.defund_user_request import DefundUserRequest
from dora_client.models.withdrawal_initiation_response_envelope import WithdrawalInitiationResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    user_id = 'user_id_example' # str | 
    defund_user_request = dora_client.DefundUserRequest() # DefundUserRequest | 

    try:
        # Initiate a withdrawal request for the logged in user to the outside world
        api_response = await api_instance.ledger_withdraw_request_self(user_id, defund_user_request)
        print("The response of DefaultApi->ledger_withdraw_request_self:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->ledger_withdraw_request_self: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **defund_user_request** | [**DefundUserRequest**](DefundUserRequest.md)|  | 

### Return type

[**WithdrawalInitiationResponseEnvelope**](WithdrawalInitiationResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Withdraw request initiation successful |  -  |
**400** | Bad request, e.g. invalid parameters or insufficient funds |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leverage_get_accrued_interest_by_user**
> CurrentLeverageAccruedInterestResponseEnvelope leverage_get_accrued_interest_by_user(position_id=position_id, asset_id=asset_id)

Get current accrued leverage interest for the user

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.current_leverage_accrued_interest_response_envelope import CurrentLeverageAccruedInterestResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    position_id = 'position_id_example' # str |  (optional)
    asset_id = 'asset_id_example' # str |  (optional)

    try:
        # Get current accrued leverage interest for the user
        api_response = await api_instance.leverage_get_accrued_interest_by_user(position_id=position_id, asset_id=asset_id)
        print("The response of DefaultApi->leverage_get_accrued_interest_by_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->leverage_get_accrued_interest_by_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **position_id** | **str**|  | [optional] 
 **asset_id** | **str**|  | [optional] 

### Return type

[**CurrentLeverageAccruedInterestResponseEnvelope**](CurrentLeverageAccruedInterestResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current leverage accrued interest retrieved successfully |  -  |
**400** | Bad request, e.g. invalid parameters |  -  |
**401** | Unauthorized, e.g. user not logged in or invalid credentials |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leverage_isolate_collateral**
> IsolateCollateralResponse leverage_isolate_collateral(isolate_collateral_request)

Create an isolated position by transferring collateral to the position from the user's global collateral

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.isolate_collateral_request import IsolateCollateralRequest
from dora_client.models.isolate_collateral_response import IsolateCollateralResponse
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    isolate_collateral_request = dora_client.IsolateCollateralRequest() # IsolateCollateralRequest | 

    try:
        # Create an isolated position by transferring collateral to the position from the user's global collateral
        api_response = await api_instance.leverage_isolate_collateral(isolate_collateral_request)
        print("The response of DefaultApi->leverage_isolate_collateral:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->leverage_isolate_collateral: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **isolate_collateral_request** | [**IsolateCollateralRequest**](IsolateCollateralRequest.md)|  | 

### Return type

[**IsolateCollateralResponse**](IsolateCollateralResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Leverage position isolated |  -  |
**400** | Bad request, e.g. insufficient collateral or invalid parameters |  -  |
**401** | Unauthorized, e.g. user not logged in or invalid credentials |  -  |
**404** | Leverage position not found |  -  |
**409** | Conflict, e.g. the requested amount is not available to transfer |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leverage_supply**
> SupplyResponseEnvelope leverage_supply(supply_request)

Supply leverage for a specific asset

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.supply_request import SupplyRequest
from dora_client.models.supply_response_envelope import SupplyResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    supply_request = dora_client.SupplyRequest() # SupplyRequest | 

    try:
        # Supply leverage for a specific asset
        api_response = await api_instance.leverage_supply(supply_request)
        print("The response of DefaultApi->leverage_supply:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->leverage_supply: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supply_request** | [**SupplyRequest**](SupplyRequest.md)|  | 

### Return type

[**SupplyResponseEnvelope**](SupplyResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Supply successful |  -  |
**400** | Bad request, e.g. insufficient collateral or invalid parameters |  -  |
**401** | Unauthorized, e.g. user not logged in or invalid credentials |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leverage_unite**
> UnitePositionResponseEnvelope leverage_unite(unite_position_request)

Combines all isolated positions into a single global position

Combines all isolated positions into a single global position

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.unite_position_request import UnitePositionRequest
from dora_client.models.unite_position_response_envelope import UnitePositionResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    unite_position_request = dora_client.UnitePositionRequest() # UnitePositionRequest | 

    try:
        # Combines all isolated positions into a single global position
        api_response = await api_instance.leverage_unite(unite_position_request)
        print("The response of DefaultApi->leverage_unite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->leverage_unite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unite_position_request** | [**UnitePositionRequest**](UnitePositionRequest.md)|  | 

### Return type

[**UnitePositionResponseEnvelope**](UnitePositionResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Leverage position combined |  -  |
**400** | Bad request, e.g. insufficient collateral or invalid parameters |  -  |
**401** | Unauthorized, e.g. user not logged in or invalid credentials |  -  |
**404** | Leverage position not found |  -  |
**409** | Conflict, e.g. the requested amount is not available to transfer |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leverage_withdraw**
> WithdrawResponseEnvelope leverage_withdraw(withdraw_request)

Withdraw leverage for a specific asset

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.withdraw_request import WithdrawRequest
from dora_client.models.withdraw_response_envelope import WithdrawResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    withdraw_request = dora_client.WithdrawRequest() # WithdrawRequest | 

    try:
        # Withdraw leverage for a specific asset
        api_response = await api_instance.leverage_withdraw(withdraw_request)
        print("The response of DefaultApi->leverage_withdraw:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->leverage_withdraw: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **withdraw_request** | [**WithdrawRequest**](WithdrawRequest.md)|  | 

### Return type

[**WithdrawResponseEnvelope**](WithdrawResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Withdraw successful |  -  |
**400** | Bad request, e.g. insufficient collateral or invalid parameters |  -  |
**401** | Unauthorized, e.g. user not logged in or invalid credentials |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **liquidity_add**
> LiquidityResponseEnvelope liquidity_add(pool_id, liquidity_request)

Add liquidity to a pool

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.liquidity_request import LiquidityRequest
from dora_client.models.liquidity_response_envelope import LiquidityResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    pool_id = 'pool_id_example' # str | 
    liquidity_request = dora_client.LiquidityRequest() # LiquidityRequest | 

    try:
        # Add liquidity to a pool
        api_response = await api_instance.liquidity_add(pool_id, liquidity_request)
        print("The response of DefaultApi->liquidity_add:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->liquidity_add: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**|  | 
 **liquidity_request** | [**LiquidityRequest**](LiquidityRequest.md)|  | 

### Return type

[**LiquidityResponseEnvelope**](LiquidityResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Liquidity added |  -  |
**400** | Bad request, e.g. insufficient funds or invalid parameters |  -  |
**401** | Unauthorized, e.g. user not logged in or invalid credentials |  -  |
**404** | Pool not found |  -  |
**409** | Conflict, e.g. the requested amount is not available to transfer |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **liquidity_subtract**
> LiquidityResponseEnvelope liquidity_subtract(pool_id, liquidity_request)

Subtract liquidity from a pool

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.liquidity_request import LiquidityRequest
from dora_client.models.liquidity_response_envelope import LiquidityResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    pool_id = 'pool_id_example' # str | 
    liquidity_request = dora_client.LiquidityRequest() # LiquidityRequest | 

    try:
        # Subtract liquidity from a pool
        api_response = await api_instance.liquidity_subtract(pool_id, liquidity_request)
        print("The response of DefaultApi->liquidity_subtract:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->liquidity_subtract: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**|  | 
 **liquidity_request** | [**LiquidityRequest**](LiquidityRequest.md)|  | 

### Return type

[**LiquidityResponseEnvelope**](LiquidityResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Liquidity subtracted |  -  |
**400** | Bad request, e.g. insufficient funds or invalid parameters |  -  |
**401** | Unauthorized, e.g. user not logged in or invalid credentials |  -  |
**404** | Pool not found |  -  |
**409** | Conflict, e.g. the requested amount is not available to transfer |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_assets**
> ResponseEnvelopeOfListAssets list_assets(created_after=created_after, created_before=created_before, asset_kind=asset_kind, can_add_liquidity=can_add_liquidity, can_direct_borrow=can_direct_borrow, can_onboard=can_onboard, can_trade=can_trade, can_virtual_borrow=can_virtual_borrow, page=page, limit=limit)

List assets

### Example


```python
import dora_client
from dora_client.models.asset_kind import AssetKind
from dora_client.models.response_envelope_of_list_assets import ResponseEnvelopeOfListAssets
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)


# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    created_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    created_before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    asset_kind = dora_client.AssetKind() # AssetKind | Asset kind (BOND, CURRENCY, INTEREST, POOL_SHARE) (optional)
    can_add_liquidity = True # bool |  (optional)
    can_direct_borrow = True # bool |  (optional)
    can_onboard = True # bool |  (optional)
    can_trade = True # bool |  (optional)
    can_virtual_borrow = True # bool |  (optional)
    page = 1 # int |  (optional) (default to 1)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # List assets
        api_response = await api_instance.list_assets(created_after=created_after, created_before=created_before, asset_kind=asset_kind, can_add_liquidity=can_add_liquidity, can_direct_borrow=can_direct_borrow, can_onboard=can_onboard, can_trade=can_trade, can_virtual_borrow=can_virtual_borrow, page=page, limit=limit)
        print("The response of DefaultApi->list_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created_after** | **datetime**|  | [optional] 
 **created_before** | **datetime**|  | [optional] 
 **asset_kind** | [**AssetKind**](.md)| Asset kind (BOND, CURRENCY, INTEREST, POOL_SHARE) | [optional] 
 **can_add_liquidity** | **bool**|  | [optional] 
 **can_direct_borrow** | **bool**|  | [optional] 
 **can_onboard** | **bool**|  | [optional] 
 **can_trade** | **bool**|  | [optional] 
 **can_virtual_borrow** | **bool**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ResponseEnvelopeOfListAssets**](ResponseEnvelopeOfListAssets.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of assets |  -  |
**400** | Bad request, e.g. invalid query parameters |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_order_books**
> ListOrderbookResponseEnvelope list_order_books(status=status, base_asset_id=base_asset_id, quote_asset_id=quote_asset_id, page=page, limit=limit)

List order books

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.list_orderbook_response_envelope import ListOrderbookResponseEnvelope
from dora_client.models.order_book_status import OrderBookStatus
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    status = dora_client.OrderBookStatus() # OrderBookStatus |  (optional)
    base_asset_id = 'base_asset_id_example' # str |  (optional)
    quote_asset_id = 'quote_asset_id_example' # str |  (optional)
    page = 1 # int |  (optional) (default to 1)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # List order books
        api_response = await api_instance.list_order_books(status=status, base_asset_id=base_asset_id, quote_asset_id=quote_asset_id, page=page, limit=limit)
        print("The response of DefaultApi->list_order_books:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_order_books: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**OrderBookStatus**](.md)|  | [optional] 
 **base_asset_id** | **str**|  | [optional] 
 **quote_asset_id** | **str**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ListOrderbookResponseEnvelope**](ListOrderbookResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of orderbooks |  -  |
**400** | Bad request, e.g. invalid query parameters |  -  |
**404** | No orderbooks found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_orders**
> ListOrdersResponseEnvelope list_orders(order_book_id=order_book_id, kind=kind, status=status, side=side, var_from=var_from, to=to, page=page, limit=limit)

List all orders

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.list_orders_response_envelope import ListOrdersResponseEnvelope
from dora_client.models.order_kind import OrderKind
from dora_client.models.order_status import OrderStatus
from dora_client.models.side import Side
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    order_book_id = ['order_book_id_example'] # List[str] |  (optional)
    kind = [dora_client.OrderKind()] # List[OrderKind] |  (optional)
    status = [dora_client.OrderStatus()] # List[OrderStatus] |  (optional)
    side = dora_client.Side() # Side |  (optional)
    var_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    page = 1 # int |  (optional) (default to 1)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # List all orders
        api_response = await api_instance.list_orders(order_book_id=order_book_id, kind=kind, status=status, side=side, var_from=var_from, to=to, page=page, limit=limit)
        print("The response of DefaultApi->list_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_book_id** | [**List[str]**](str.md)|  | [optional] 
 **kind** | [**List[OrderKind]**](OrderKind.md)|  | [optional] 
 **status** | [**List[OrderStatus]**](OrderStatus.md)|  | [optional] 
 **side** | [**Side**](.md)|  | [optional] 
 **var_from** | **datetime**|  | [optional] 
 **to** | **datetime**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ListOrdersResponseEnvelope**](ListOrdersResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of orders |  -  |
**400** | Bad request, e.g. invalid query parameters |  -  |
**401** | Unauthorized, user not logged in or does not have access to this orderbook |  -  |
**404** | No orders found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_position_accounts_self**
> ListPositionAccountsResponseEnvelope list_position_accounts_self()

List all position accounts for the authenticated user

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.list_position_accounts_response_envelope import ListPositionAccountsResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)

    try:
        # List all position accounts for the authenticated user
        api_response = await api_instance.list_position_accounts_self()
        print("The response of DefaultApi->list_position_accounts_self:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_position_accounts_self: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListPositionAccountsResponseEnvelope**](ListPositionAccountsResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of position accounts including the position id, the position name, and global account indicator |  -  |
**400** | Bad request, e.g. invalid query parameters |  -  |
**404** | User not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_leverage_get_accrued_interest**
> PayLeverageAccruedInterestResponseEnvelope pay_leverage_get_accrued_interest(pay_leverage_accrued_interest_request)

Pay current accrued leverage interest for a specific user

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.pay_leverage_accrued_interest_request import PayLeverageAccruedInterestRequest
from dora_client.models.pay_leverage_accrued_interest_response_envelope import PayLeverageAccruedInterestResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    pay_leverage_accrued_interest_request = dora_client.PayLeverageAccruedInterestRequest() # PayLeverageAccruedInterestRequest | 

    try:
        # Pay current accrued leverage interest for a specific user
        api_response = await api_instance.pay_leverage_get_accrued_interest(pay_leverage_accrued_interest_request)
        print("The response of DefaultApi->pay_leverage_get_accrued_interest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->pay_leverage_get_accrued_interest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_leverage_accrued_interest_request** | [**PayLeverageAccruedInterestRequest**](PayLeverageAccruedInterestRequest.md)|  | 

### Return type

[**PayLeverageAccruedInterestResponseEnvelope**](PayLeverageAccruedInterestResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current leverage accrued interest paid successfully |  -  |
**400** | Bad request, e.g. invalid parameters |  -  |
**401** | Unauthorized, e.g. user not logged in or invalid credentials |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reject_ledger_withdraw_request**
> WithdrawalInitiationResponseEnvelope reject_ledger_withdraw_request(withdrawal_id, withdrawal_request_reason)

Reject a pending withdrawal request

Reject a pending withdrawal request, providing a reason for the rejection. Note that this does not interact with any external systems; it simply updates the status of the withdrawal request in the ledger. Actual transfer of assets must be handled separately.

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.withdrawal_initiation_response_envelope import WithdrawalInitiationResponseEnvelope
from dora_client.models.withdrawal_request_reason import WithdrawalRequestReason
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    withdrawal_id = 'withdrawal_id_example' # str | 
    withdrawal_request_reason = dora_client.WithdrawalRequestReason() # WithdrawalRequestReason | 

    try:
        # Reject a pending withdrawal request
        api_response = await api_instance.reject_ledger_withdraw_request(withdrawal_id, withdrawal_request_reason)
        print("The response of DefaultApi->reject_ledger_withdraw_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->reject_ledger_withdraw_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **withdrawal_id** | **str**|  | 
 **withdrawal_request_reason** | [**WithdrawalRequestReason**](WithdrawalRequestReason.md)|  | 

### Return type

[**WithdrawalInitiationResponseEnvelope**](WithdrawalInitiationResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Withdrawal request rejected successfully |  -  |
**400** | Bad request, e.g. invalid withdrawal ID format or request is not in a pending state |  -  |
**404** | Withdrawal request not found |  -  |
**403** | Forbidden, user does not have permission to reject this withdrawal request |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_api_key_for_user**
> RevokeAPIKeyResponseEnvelope revoke_api_key_for_user(key_id)

Revoke apikey for a user

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.revoke_api_key_response_envelope import RevokeAPIKeyResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    key_id = 'key_id_example' # str | 

    try:
        # Revoke apikey for a user
        api_response = await api_instance.revoke_api_key_for_user(key_id)
        print("The response of DefaultApi->revoke_api_key_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->revoke_api_key_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**|  | 

### Return type

[**RevokeAPIKeyResponseEnvelope**](RevokeAPIKeyResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | APIKey revoked |  -  |
**404** | User not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_api_key_for_user_id**
> RevokeAPIKeyResponseEnvelope revoke_api_key_for_user_id(user_id, key_id)

Revoke apikey for a user: admin or integrator only

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.revoke_api_key_response_envelope import RevokeAPIKeyResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    user_id = 'user_id_example' # str | 
    key_id = 'key_id_example' # str | 

    try:
        # Revoke apikey for a user: admin or integrator only
        api_response = await api_instance.revoke_api_key_for_user_id(user_id, key_id)
        print("The response of DefaultApi->revoke_api_key_for_user_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->revoke_api_key_for_user_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **key_id** | **str**|  | 

### Return type

[**RevokeAPIKeyResponseEnvelope**](RevokeAPIKeyResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | APIKey revoked |  -  |
**404** | User not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settle_leverage_accrued_interest**
> SettleLeverageAccruedInterestResponseEnvelope settle_leverage_accrued_interest(settle_leverage_accrued_interest_request)

Settle current accrued leverage interest for a specific user

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.settle_leverage_accrued_interest_request import SettleLeverageAccruedInterestRequest
from dora_client.models.settle_leverage_accrued_interest_response_envelope import SettleLeverageAccruedInterestResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    settle_leverage_accrued_interest_request = dora_client.SettleLeverageAccruedInterestRequest() # SettleLeverageAccruedInterestRequest | 

    try:
        # Settle current accrued leverage interest for a specific user
        api_response = await api_instance.settle_leverage_accrued_interest(settle_leverage_accrued_interest_request)
        print("The response of DefaultApi->settle_leverage_accrued_interest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->settle_leverage_accrued_interest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle_leverage_accrued_interest_request** | [**SettleLeverageAccruedInterestRequest**](SettleLeverageAccruedInterestRequest.md)|  | 

### Return type

[**SettleLeverageAccruedInterestResponseEnvelope**](SettleLeverageAccruedInterestResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current leverage accrued interest settled successfully |  -  |
**400** | Bad request, e.g. invalid parameters |  -  |
**401** | Unauthorized, e.g. user not logged in or invalid credentials |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settle_realized_pnl_record**
> SettleRealizedPnlRecordResponseEnvelope settle_realized_pnl_record(settlement_id)

Mark a realized P&L settlement as settled

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.settle_realized_pnl_record_response_envelope import SettleRealizedPnlRecordResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    settlement_id = 'settlement_id_example' # str | 

    try:
        # Mark a realized P&L settlement as settled
        api_response = await api_instance.settle_realized_pnl_record(settlement_id)
        print("The response of DefaultApi->settle_realized_pnl_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->settle_realized_pnl_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_id** | **str**|  | 

### Return type

[**SettleRealizedPnlRecordResponseEnvelope**](SettleRealizedPnlRecordResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The realized P&amp;L settlement record has been marked as settled |  -  |
**401** | Unauthorized, user is not logged in |  -  |
**403** | Forbidden, user does not have access |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settle_transactions_settlements**
> TransactionsSettlementsResponse settle_transactions_settlements(transactions_settlement_request)

Settle multiple transactions settlements in batch

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.transactions_settlement_request import TransactionsSettlementRequest
from dora_client.models.transactions_settlements_response import TransactionsSettlementsResponse
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    transactions_settlement_request = dora_client.TransactionsSettlementRequest() # TransactionsSettlementRequest | 

    try:
        # Settle multiple transactions settlements in batch
        api_response = await api_instance.settle_transactions_settlements(transactions_settlement_request)
        print("The response of DefaultApi->settle_transactions_settlements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->settle_transactions_settlements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transactions_settlement_request** | [**TransactionsSettlementRequest**](TransactionsSettlementRequest.md)|  | 

### Return type

[**TransactionsSettlementsResponse**](TransactionsSettlementsResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Settlements updated |  -  |
**400** | Bad request |  -  |
**404** | No transactions for settlement found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_asset_prices**
> StreamAssetPricesResponse stream_asset_prices(since=since, asset_id=asset_id)

Stream real-time asset prices as map objects

Opens a WebSocket stream for real-time asset price updates. First message contains all current prices, subsequent messages contain only changed prices. Data is sent as JSON objects keyed by asset ID.

### Example


```python
import dora_client
from dora_client.models.stream_asset_prices_response import StreamAssetPricesResponse
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)


# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    since = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    asset_id = 'asset_id_example' # str |  (optional)

    try:
        # Stream real-time asset prices as map objects
        api_response = await api_instance.stream_asset_prices(since=since, asset_id=asset_id)
        print("The response of DefaultApi->stream_asset_prices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->stream_asset_prices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **datetime**|  | [optional] 
 **asset_id** | **str**|  | [optional] 

### Return type

[**StreamAssetPricesResponse**](StreamAssetPricesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Real-time stream of asset prices. First message: all current prices. Subsequent messages: only changed prices. |  -  |
**400** | Bad request, e.g. invalid parameters |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_candle_data**
> StreamCandlesResponse stream_candle_data(order_book_id, since=since, resolution=resolution)

Get a snapshot of candlestick data from date provided, and open a stream for real-time updates

### Example


```python
import dora_client
from dora_client.models.candle_resolution import CandleResolution
from dora_client.models.stream_candles_response import StreamCandlesResponse
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)


# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    order_book_id = 'order_book_id_example' # str | 
    since = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    resolution = dora_client.CandleResolution() # CandleResolution |  (optional)

    try:
        # Get a snapshot of candlestick data from date provided, and open a stream for real-time updates
        api_response = await api_instance.stream_candle_data(order_book_id, since=since, resolution=resolution)
        print("The response of DefaultApi->stream_candle_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->stream_candle_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_book_id** | **str**|  | 
 **since** | **datetime**|  | [optional] 
 **resolution** | [**CandleResolution**](.md)|  | [optional] 

### Return type

[**StreamCandlesResponse**](StreamCandlesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stream opened successfully |  -  |
**400** | Bad request, e.g. invalid parameters |  -  |
**404** | Orderbook not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_order_book_balances**
> StreamOrderBookBalancesResponse stream_order_book_balances(order_book_id, since=since)

Get a snapshot of base and quote balances for an order book and open a stream for real-time updates

### Example


```python
import dora_client
from dora_client.models.stream_order_book_balances_response import StreamOrderBookBalancesResponse
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)


# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    order_book_id = 'order_book_id_example' # str | 
    since = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Get a snapshot of base and quote balances for an order book and open a stream for real-time updates
        api_response = await api_instance.stream_order_book_balances(order_book_id, since=since)
        print("The response of DefaultApi->stream_order_book_balances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->stream_order_book_balances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_book_id** | **str**|  | 
 **since** | **datetime**|  | [optional] 

### Return type

[**StreamOrderBookBalancesResponse**](StreamOrderBookBalancesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stream opened successfully |  -  |
**400** | Bad request, e.g. invalid order book ID format |  -  |
**404** | Orderbook not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_orderbook_open_orders**
> LiveOrderbook stream_orderbook_open_orders(order_book_id, since=since)

Get a snapshot of open orders in an order book and open a stream for real-time updates

### Example


```python
import dora_client
from dora_client.models.live_orderbook import LiveOrderbook
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)


# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    order_book_id = 'order_book_id_example' # str | 
    since = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Get a snapshot of open orders in an order book and open a stream for real-time updates
        api_response = await api_instance.stream_orderbook_open_orders(order_book_id, since=since)
        print("The response of DefaultApi->stream_orderbook_open_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->stream_orderbook_open_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_book_id** | **str**|  | 
 **since** | **datetime**|  | [optional] 

### Return type

[**LiveOrderbook**](LiveOrderbook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stream opened successfully |  -  |
**400** | Bad request, e.g. invalid order book ID format |  -  |
**404** | Orderbook not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_trades**
> StreamTradesResponse stream_trades(order_book_id, since=since)

Get a snapshot of trades executed on the given order book from a specific date and open a stream for real-time updates

### Example


```python
import dora_client
from dora_client.models.stream_trades_response import StreamTradesResponse
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)


# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    order_book_id = 'order_book_id_example' # str | 
    since = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Get a snapshot of trades executed on the given order book from a specific date and open a stream for real-time updates
        api_response = await api_instance.stream_trades(order_book_id, since=since)
        print("The response of DefaultApi->stream_trades:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->stream_trades: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_book_id** | **str**|  | 
 **since** | **datetime**|  | [optional] 

### Return type

[**StreamTradesResponse**](StreamTradesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Real-time trade updates |  -  |
**400** | Bad request, e.g. invalid parameters |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_available_balances**
> TransferBalancesResponseEnvelope transfer_available_balances(transfer_balances_request)

Transfer available balance between a user's accounts (e.g. global to isolated position)

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.transfer_balances_request import TransferBalancesRequest
from dora_client.models.transfer_balances_response_envelope import TransferBalancesResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    transfer_balances_request = dora_client.TransferBalancesRequest() # TransferBalancesRequest | 

    try:
        # Transfer available balance between a user's accounts (e.g. global to isolated position)
        api_response = await api_instance.transfer_available_balances(transfer_balances_request)
        print("The response of DefaultApi->transfer_available_balances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->transfer_available_balances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_balances_request** | [**TransferBalancesRequest**](TransferBalancesRequest.md)|  | 

### Return type

[**TransferBalancesResponseEnvelope**](TransferBalancesResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Isolated Position Created |  -  |
**400** | Bad request, e.g. missing required fields |  -  |
**401** | Unauthorized, user not logged in or does not have access to this orderbook |  -  |
**409** | Conflict, e.g. the requested amount is not available to transfer |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_config**
> UserUpdatedResponseEnvelope update_user_config(user_id, update_user_config_request)

Update user configuration by ID

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.update_user_config_request import UpdateUserConfigRequest
from dora_client.models.user_updated_response_envelope import UserUpdatedResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    user_id = 'user_id_example' # str | 
    update_user_config_request = dora_client.UpdateUserConfigRequest() # UpdateUserConfigRequest | 

    try:
        # Update user configuration by ID
        api_response = await api_instance.update_user_config(user_id, update_user_config_request)
        print("The response of DefaultApi->update_user_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_user_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **update_user_config_request** | [**UpdateUserConfigRequest**](UpdateUserConfigRequest.md)|  | 

### Return type

[**UserUpdatedResponseEnvelope**](UserUpdatedResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User configuration updated |  -  |
**400** | Bad request, e.g. invalid query parameters |  -  |
**404** | User not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_config_self**
> UserUpdatedResponseEnvelope update_user_config_self(update_user_config_request)

Update user configuration for the authenticated user

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.update_user_config_request import UpdateUserConfigRequest
from dora_client.models.user_updated_response_envelope import UserUpdatedResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    update_user_config_request = dora_client.UpdateUserConfigRequest() # UpdateUserConfigRequest | 

    try:
        # Update user configuration for the authenticated user
        api_response = await api_instance.update_user_config_self(update_user_config_request)
        print("The response of DefaultApi->update_user_config_self:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_user_config_self: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_user_config_request** | [**UpdateUserConfigRequest**](UpdateUserConfigRequest.md)|  | 

### Return type

[**UserUpdatedResponseEnvelope**](UserUpdatedResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User configuration updated |  -  |
**400** | Bad request, e.g. invalid query parameters |  -  |
**404** | User not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_submit_order**
> ValidateSubmitOrderResponse validate_submit_order(validate_submit_order_request)

Validate submit order request data

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.validate_submit_order_request import ValidateSubmitOrderRequest
from dora_client.models.validate_submit_order_response import ValidateSubmitOrderResponse
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    validate_submit_order_request = dora_client.ValidateSubmitOrderRequest() # ValidateSubmitOrderRequest | 

    try:
        # Validate submit order request data
        api_response = await api_instance.validate_submit_order(validate_submit_order_request)
        print("The response of DefaultApi->validate_submit_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->validate_submit_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate_submit_order_request** | [**ValidateSubmitOrderRequest**](ValidateSubmitOrderRequest.md)|  | 

### Return type

[**ValidateSubmitOrderResponse**](ValidateSubmitOrderResponse.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Validated submit order request |  -  |
**400** | Bad request, e.g. missing required fields |  -  |
**401** | Unauthorized, user not logged in or does not have access to this orderbook |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_user**
> UserUpdatedResponseEnvelope verify_user(user_id)

Verify a user by ID

### Example

* Api Key Authentication (apiKeyAuthHeader):
* Bearer (JWT) Authentication (bearerAuth):

```python
import dora_client
from dora_client.models.user_updated_response_envelope import UserUpdatedResponseEnvelope
from dora_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dora.co
# See configuration.py for a list of all supported configuration parameters.
configuration = dora_client.Configuration(
    host = "https://staging.dora.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuthHeader
configuration.api_key['apiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuthHeader'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = dora_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dora_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dora_client.DefaultApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Verify a user by ID
        api_response = await api_instance.verify_user(user_id)
        print("The response of DefaultApi->verify_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->verify_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**UserUpdatedResponseEnvelope**](UserUpdatedResponseEnvelope.md)

### Authorization

[apiKeyAuthHeader](../README.md#apiKeyAuthHeader), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User verified |  -  |
**400** | Bad request, e.g. invalid query parameters |  -  |
**404** | User not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

