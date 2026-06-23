# OrderBookTop


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_book_id** | **UUID** |  | 
**best_bid** | **str** |  | 
**best_ask** | **str** |  | 
**timestamp** | **datetime** |  | 

## Example

```python
from dora_client.models.order_book_top import OrderBookTop

# TODO update the JSON string below
json = "{}"
# create an instance of OrderBookTop from a JSON string
order_book_top_instance = OrderBookTop.from_json(json)
# print the JSON string representation of the object
print(OrderBookTop.to_json())

# convert the object into a dict
order_book_top_dict = order_book_top_instance.to_dict()
# create an instance of OrderBookTop from a dict
order_book_top_from_dict = OrderBookTop.from_dict(order_book_top_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


