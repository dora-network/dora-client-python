# StreamAssetsEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**val** | [**Asset**](Asset.md) |  | 
**time** | **datetime** | The timestamp when the data was created | 

## Example

```python
from dora_client.models.stream_assets_entry import StreamAssetsEntry

# TODO update the JSON string below
json = "{}"
# create an instance of StreamAssetsEntry from a JSON string
stream_assets_entry_instance = StreamAssetsEntry.from_json(json)
# print the JSON string representation of the object
print(StreamAssetsEntry.to_json())

# convert the object into a dict
stream_assets_entry_dict = stream_assets_entry_instance.to_dict()
# create an instance of StreamAssetsEntry from a dict
stream_assets_entry_from_dict = StreamAssetsEntry.from_dict(stream_assets_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


