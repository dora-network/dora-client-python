# APIKeys


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_keys** | [**List[APIKeyResponse]**](APIKeyResponse.md) |  | [optional] 

## Example

```python
from dora_client.models.api_keys import APIKeys

# TODO update the JSON string below
json = "{}"
# create an instance of APIKeys from a JSON string
api_keys_instance = APIKeys.from_json(json)
# print the JSON string representation of the object
print(APIKeys.to_json())

# convert the object into a dict
api_keys_dict = api_keys_instance.to_dict()
# create an instance of APIKeys from a dict
api_keys_from_dict = APIKeys.from_dict(api_keys_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


