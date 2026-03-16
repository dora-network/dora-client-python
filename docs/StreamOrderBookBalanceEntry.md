# StreamOrderBookBalanceEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**val** | [**OrderBookBalance**](OrderBookBalance.md) |  | 
**time** | **datetime** | The timestamp when the data was created | 

## Example

```python
from dora_client.models.stream_order_book_balance_entry import StreamOrderBookBalanceEntry

# TODO update the JSON string below
json = "{}"
# create an instance of StreamOrderBookBalanceEntry from a JSON string
stream_order_book_balance_entry_instance = StreamOrderBookBalanceEntry.from_json(json)
# print the JSON string representation of the object
print(StreamOrderBookBalanceEntry.to_json())

# convert the object into a dict
stream_order_book_balance_entry_dict = stream_order_book_balance_entry_instance.to_dict()
# create an instance of StreamOrderBookBalanceEntry from a dict
stream_order_book_balance_entry_from_dict = StreamOrderBookBalanceEntry.from_dict(stream_order_book_balance_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


