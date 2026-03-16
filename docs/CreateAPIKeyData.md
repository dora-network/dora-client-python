# CreateAPIKeyData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** |  | 
**api_key** | **str** |  | 
**label** | **str** |  | 

## Example

```python
from dora_client.models.create_api_key_data import CreateAPIKeyData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAPIKeyData from a JSON string
create_api_key_data_instance = CreateAPIKeyData.from_json(json)
# print the JSON string representation of the object
print(CreateAPIKeyData.to_json())

# convert the object into a dict
create_api_key_data_dict = create_api_key_data_instance.to_dict()
# create an instance of CreateAPIKeyData from a dict
create_api_key_data_from_dict = CreateAPIKeyData.from_dict(create_api_key_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


