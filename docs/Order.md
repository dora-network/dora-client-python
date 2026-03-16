# Order


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** |  | 
**order_book_id** | **str** |  | 
**kind** | [**OrderKind**](OrderKind.md) |  | 
**original_price** | **str** | If Kind is LIMIT, this is the original limit price. If Kind is MARKET, this may be 0 or omitted. | 
**avg_fill_price** | **str** |  | 
**cancelled_quantity** | **str** | Quantity that was cancelled, if any. | 
**open_quantity** | **str** | Quantity that is still open, i.e., not filled or cancelled. | 
**original_quantity** | **str** | The original quantity of the order when it was created. | 
**filled_quantity** | **str** | Quantity that has been filled so far. | 
**filled_notional** | **str** | Quote quantity that has been filled so far. | 
**last_update_at** | **datetime** |  | [optional] 
**opened_at** | **datetime** |  | 
**inverse_leverage** | **str** |  | 
**side** | [**Side**](Side.md) |  | 
**status** | [**OrderStatus**](OrderStatus.md) |  | 
**user_id** | **str** |  | 
**order_modifiers** | [**List[OrderModifierKind]**](OrderModifierKind.md) |  | [optional] 
**position_id** | **str** |  | 
**order_info** | **str** |  | [optional] 
**good_till_date** | **datetime** |  | [optional] 
**trigger_price** | **str** |  | [optional] 
**trigger_type** | [**TriggerType**](TriggerType.md) |  | [optional] 
**client_order_id** | **str** | An optional client-provided identifier for the order. | [optional] 
**parent_order_id** | **str** |  | [optional] 

## Example

```python
from dora_client.models.order import Order

# TODO update the JSON string below
json = "{}"
# create an instance of Order from a JSON string
order_instance = Order.from_json(json)
# print the JSON string representation of the object
print(Order.to_json())

# convert the object into a dict
order_dict = order_instance.to_dict()
# create an instance of Order from a dict
order_from_dict = Order.from_dict(order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


