# UpdateFieldString

A generic struct to handle optional updates for string fields in user requests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update** | **bool** | Whether to update the field. | 
**value** | **str** | The new value to set for the field. | [optional] 

## Example

```python
from dora_client.models.update_field_string import UpdateFieldString

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFieldString from a JSON string
update_field_string_instance = UpdateFieldString.from_json(json)
# print the JSON string representation of the object
print(UpdateFieldString.to_json())

# convert the object into a dict
update_field_string_dict = update_field_string_instance.to_dict()
# create an instance of UpdateFieldString from a dict
update_field_string_from_dict = UpdateFieldString.from_dict(update_field_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


