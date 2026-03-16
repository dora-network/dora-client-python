# StreamPositionsEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**val** | [**Position**](Position.md) |  | 
**time** | **datetime** | The timestamp when the data was created | 

## Example

```python
from dora_client.models.stream_positions_entry import StreamPositionsEntry

# TODO update the JSON string below
json = "{}"
# create an instance of StreamPositionsEntry from a JSON string
stream_positions_entry_instance = StreamPositionsEntry.from_json(json)
# print the JSON string representation of the object
print(StreamPositionsEntry.to_json())

# convert the object into a dict
stream_positions_entry_dict = stream_positions_entry_instance.to_dict()
# create an instance of StreamPositionsEntry from a dict
stream_positions_entry_from_dict = StreamPositionsEntry.from_dict(stream_positions_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


