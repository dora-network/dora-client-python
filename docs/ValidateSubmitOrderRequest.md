# ValidateSubmitOrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **str** |  | 
**tick** | **str** | Minimum tradable increment for the selected order book | 
**kind** | [**OrderKind**](OrderKind.md) | Must be LIMIT or MARKET | 
**side** | [**Side**](Side.md) | Must be BUY or SELL | [optional] 
**price** | **str** | If kind is LIMIT, must be &gt; 0; if MARKET it must be 0 or omitted | 
**good_till_date** | **datetime** |  | [optional] 
**inverse_leverage** | **str** |  | 
**user_balance** | **str** | User balance used to ensure they can afford the requested quantity | 
**base_asset_id** | **UUID** | base asset of orderbook | [optional] 
**quote_asset_id** | **UUID** | quote asset of orderbook | [optional] 
**client_order_id** | **str** | An optional client-provided identifier for the order. | [optional] 
**position_assets** | [**List[PositionAsset]**](PositionAsset.md) | Full list of assets in the position with their price and collateral weight, required when inverse_leverage &lt; 1 for leverage health checks | [optional] 
**assets_config** | [**List[AssetConfig]**](AssetConfig.md) | Configuration for the assets in the order | [optional] 
**stop_loss_price** | **str** | Stop loss price | [optional] 
**take_profit_price** | **str** | Take profit price | [optional] 
**restrictions** | [**TenantRestrictions**](TenantRestrictions.md) |  | [optional] 
**initial_capital** | **str** | Initial capital value in USD only used to validate sells with leverage | [optional] 

## Example

```python
from dora_client.models.validate_submit_order_request import ValidateSubmitOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateSubmitOrderRequest from a JSON string
validate_submit_order_request_instance = ValidateSubmitOrderRequest.from_json(json)
# print the JSON string representation of the object
print(ValidateSubmitOrderRequest.to_json())

# convert the object into a dict
validate_submit_order_request_dict = validate_submit_order_request_instance.to_dict()
# create an instance of ValidateSubmitOrderRequest from a dict
validate_submit_order_request_from_dict = ValidateSubmitOrderRequest.from_dict(validate_submit_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


