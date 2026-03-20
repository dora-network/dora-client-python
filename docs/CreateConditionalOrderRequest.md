# CreateConditionalOrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **decimal.Decimal** |  | 
**order_book_id** | **str** | Required: the order book to submit the order to | 
**position_id** | **str** | Required: the position to submit the order to | 
**asset_id** | **str** | Required: the asset to submit the order to | 
**stop_loss_price** | **decimal.Decimal** | Stop loss price | [optional] 
**take_profit_price** | **decimal.Decimal** | Take profit price | [optional] 

## Example

```python
from dora_client.models.create_conditional_order_request import CreateConditionalOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConditionalOrderRequest from a JSON string
create_conditional_order_request_instance = CreateConditionalOrderRequest.from_json(json)
# print the JSON string representation of the object
print(CreateConditionalOrderRequest.to_json())

# convert the object into a dict
create_conditional_order_request_dict = create_conditional_order_request_instance.to_dict()
# create an instance of CreateConditionalOrderRequest from a dict
create_conditional_order_request_from_dict = CreateConditionalOrderRequest.from_dict(create_conditional_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


