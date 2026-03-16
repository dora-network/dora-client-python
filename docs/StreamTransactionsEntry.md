# StreamTransactionsEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**val** | [**Transaction**](Transaction.md) |  | 
**time** | **datetime** | The timestamp when the data was created | 

## Example

```python
from dora_client.models.stream_transactions_entry import StreamTransactionsEntry

# TODO update the JSON string below
json = "{}"
# create an instance of StreamTransactionsEntry from a JSON string
stream_transactions_entry_instance = StreamTransactionsEntry.from_json(json)
# print the JSON string representation of the object
print(StreamTransactionsEntry.to_json())

# convert the object into a dict
stream_transactions_entry_dict = stream_transactions_entry_instance.to_dict()
# create an instance of StreamTransactionsEntry from a dict
stream_transactions_entry_from_dict = StreamTransactionsEntry.from_dict(stream_transactions_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


