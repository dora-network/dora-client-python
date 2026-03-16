# StreamTradesEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**val** | [**Trade**](Trade.md) |  | 
**time** | **datetime** | The timestamp when the data was created | 

## Example

```python
from dora_client.models.stream_trades_entry import StreamTradesEntry

# TODO update the JSON string below
json = "{}"
# create an instance of StreamTradesEntry from a JSON string
stream_trades_entry_instance = StreamTradesEntry.from_json(json)
# print the JSON string representation of the object
print(StreamTradesEntry.to_json())

# convert the object into a dict
stream_trades_entry_dict = stream_trades_entry_instance.to_dict()
# create an instance of StreamTradesEntry from a dict
stream_trades_entry_from_dict = StreamTradesEntry.from_dict(stream_trades_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


