# UpdateRolesString

A generic struct to handle optional updates for roles fields in user requests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update** | **bool** | Whether to update the field. | 
**value** | [**UserRole**](UserRole.md) | The new value to set for the field. | [optional] 

## Example

```python
from dora_client.models.update_roles_string import UpdateRolesString

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRolesString from a JSON string
update_roles_string_instance = UpdateRolesString.from_json(json)
# print the JSON string representation of the object
print(UpdateRolesString.to_json())

# convert the object into a dict
update_roles_string_dict = update_roles_string_instance.to_dict()
# create an instance of UpdateRolesString from a dict
update_roles_string_from_dict = UpdateRolesString.from_dict(update_roles_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


