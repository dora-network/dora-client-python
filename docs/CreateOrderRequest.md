# CreateOrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **str** |  | 
**inverse_leverage** | **str** |  | 
**price** | **str** |  | [optional] 
**kind** | [**OrderKind**](OrderKind.md) |  | 
**side** | [**Side**](Side.md) | Required: Must be either &#39;BUY&#39; or &#39;SELL&#39; | 
**from_global_position** | **bool** | use global position for the order or isolated. required. | 
**order_book_id** | **UUID** | Required: the order book to submit the order to | 
**order_modifiers** | [**List[OrderModifierKind]**](OrderModifierKind.md) |  | [optional] 
**good_till_date** | **datetime** |  | [optional] 
**client_order_id** | **str** | An optional client-provided identifier for the order. | [optional] 
**stop_loss_price** | **str** | Stop loss price | [optional] 
**take_profit_price** | **str** | Take profit price | [optional] 

## Example

```python
from dora_client.models.create_order_request import CreateOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrderRequest from a JSON string
create_order_request_instance = CreateOrderRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOrderRequest.to_json())

# convert the object into a dict
create_order_request_dict = create_order_request_instance.to_dict()
# create an instance of CreateOrderRequest from a dict
create_order_request_from_dict = CreateOrderRequest.from_dict(create_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


