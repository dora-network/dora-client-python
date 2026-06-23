# CreateOrUpdateUserResponse

Response body for POST /user or PUT /user/{id}: contains the ID of the created or updated user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | The ID of the created or updated user. | 

## Example

```python
from dora_client.models.create_or_update_user_response import CreateOrUpdateUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrUpdateUserResponse from a JSON string
create_or_update_user_response_instance = CreateOrUpdateUserResponse.from_json(json)
# print the JSON string representation of the object
print(CreateOrUpdateUserResponse.to_json())

# convert the object into a dict
create_or_update_user_response_dict = create_or_update_user_response_instance.to_dict()
# create an instance of CreateOrUpdateUserResponse from a dict
create_or_update_user_response_from_dict = CreateOrUpdateUserResponse.from_dict(create_or_update_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


