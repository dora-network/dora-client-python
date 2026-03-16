# OrderBookSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_book_id** | **str** |  | 
**mid_price** | **str** |  | 
**spread** | **str** |  | 
**best_bid** | **str** |  | 
**best_ask** | **str** |  | 

## Example

```python
from dora_client.models.order_book_summary import OrderBookSummary

# TODO update the JSON string below
json = "{}"
# create an instance of OrderBookSummary from a JSON string
order_book_summary_instance = OrderBookSummary.from_json(json)
# print the JSON string representation of the object
print(OrderBookSummary.to_json())

# convert the object into a dict
order_book_summary_dict = order_book_summary_instance.to_dict()
# create an instance of OrderBookSummary from a dict
order_book_summary_from_dict = OrderBookSummary.from_dict(order_book_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


