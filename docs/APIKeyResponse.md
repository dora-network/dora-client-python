# APIKeyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**key_id** | **str** |  | 
**label** | **str** |  | 
**expires_at** | **datetime** |  | [optional] 
**is_active** | **bool** |  | 

## Example

```python
from dora_client.models.api_key_response import APIKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of APIKeyResponse from a JSON string
api_key_response_instance = APIKeyResponse.from_json(json)
# print the JSON string representation of the object
print(APIKeyResponse.to_json())

# convert the object into a dict
api_key_response_dict = api_key_response_instance.to_dict()
# create an instance of APIKeyResponse from a dict
api_key_response_from_dict = APIKeyResponse.from_dict(api_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


