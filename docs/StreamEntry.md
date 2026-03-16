# StreamEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**val** | **dict** | The data being streamed | 
**time** | **datetime** | The timestamp when the data was created | 

## Example

```python
from dora_client.models.stream_entry import StreamEntry

# TODO update the JSON string below
json = "{}"
# create an instance of StreamEntry from a JSON string
stream_entry_instance = StreamEntry.from_json(json)
# print the JSON string representation of the object
print(StreamEntry.to_json())

# convert the object into a dict
stream_entry_dict = stream_entry_instance.to_dict()
# create an instance of StreamEntry from a dict
stream_entry_from_dict = StreamEntry.from_dict(stream_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


