# UpdateFieldBoolean

A generic struct to handle optional updates for boolean fields in user requests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update** | **bool** | Whether to update the field. | 
**value** | **bool** | The new value to set for the field. | [optional] 

## Example

```python
from dora_client.models.update_field_boolean import UpdateFieldBoolean

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFieldBoolean from a JSON string
update_field_boolean_instance = UpdateFieldBoolean.from_json(json)
# print the JSON string representation of the object
print(UpdateFieldBoolean.to_json())

# convert the object into a dict
update_field_boolean_dict = update_field_boolean_instance.to_dict()
# create an instance of UpdateFieldBoolean from a dict
update_field_boolean_from_dict = UpdateFieldBoolean.from_dict(update_field_boolean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


