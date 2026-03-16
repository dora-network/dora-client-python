# StreamOrdersEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**val** | [**Order**](Order.md) |  | 
**time** | **datetime** | The timestamp when the data was created | 

## Example

```python
from dora_client.models.stream_orders_entry import StreamOrdersEntry

# TODO update the JSON string below
json = "{}"
# create an instance of StreamOrdersEntry from a JSON string
stream_orders_entry_instance = StreamOrdersEntry.from_json(json)
# print the JSON string representation of the object
print(StreamOrdersEntry.to_json())

# convert the object into a dict
stream_orders_entry_dict = stream_orders_entry_instance.to_dict()
# create an instance of StreamOrdersEntry from a dict
stream_orders_entry_from_dict = StreamOrdersEntry.from_dict(stream_orders_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


