# OrderBookBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_book_id** | **UUID** | The ID of the order book. | 
**base_quantity** | **float** | The quantity of the base asset. | 
**quote_quantity** | **float** | The quantity of the quote asset. | 
**shares_quantity** | **float** | The quantity of pool shares. | 

## Example

```python
from dora_client.models.order_book_balance import OrderBookBalance

# TODO update the JSON string below
json = "{}"
# create an instance of OrderBookBalance from a JSON string
order_book_balance_instance = OrderBookBalance.from_json(json)
# print the JSON string representation of the object
print(OrderBookBalance.to_json())

# convert the object into a dict
order_book_balance_dict = order_book_balance_instance.to_dict()
# create an instance of OrderBookBalance from a dict
order_book_balance_from_dict = OrderBookBalance.from_dict(order_book_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


