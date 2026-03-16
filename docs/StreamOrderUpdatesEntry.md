# StreamOrderUpdatesEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**val** | [**Order**](Order.md) |  | 
**time** | **datetime** | The timestamp when the data was created | 

## Example

```python
from dora_client.models.stream_order_updates_entry import StreamOrderUpdatesEntry

# TODO update the JSON string below
json = "{}"
# create an instance of StreamOrderUpdatesEntry from a JSON string
stream_order_updates_entry_instance = StreamOrderUpdatesEntry.from_json(json)
# print the JSON string representation of the object
print(StreamOrderUpdatesEntry.to_json())

# convert the object into a dict
stream_order_updates_entry_dict = stream_order_updates_entry_instance.to_dict()
# create an instance of StreamOrderUpdatesEntry from a dict
stream_order_updates_entry_from_dict = StreamOrderUpdatesEntry.from_dict(stream_order_updates_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


