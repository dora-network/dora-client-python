# UserExistsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_exists** | **bool** |  | 
**firebase_set** | **bool** |  | 
**should_create_user** | **bool** |  | 

## Example

```python
from dora_client.models.user_exists_response import UserExistsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserExistsResponse from a JSON string
user_exists_response_instance = UserExistsResponse.from_json(json)
# print the JSON string representation of the object
print(UserExistsResponse.to_json())

# convert the object into a dict
user_exists_response_dict = user_exists_response_instance.to_dict()
# create an instance of UserExistsResponse from a dict
user_exists_response_from_dict = UserExistsResponse.from_dict(user_exists_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


