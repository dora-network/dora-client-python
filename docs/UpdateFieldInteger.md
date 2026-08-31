# UpdateFieldInteger

A generic struct to handle optional updates for integer fields in user requests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update** | **bool** | Whether to update the field. | 
**value** | **int** | The new value to set for the field. | [optional] 

## Example

```python
from dora_client.models.update_field_integer import UpdateFieldInteger

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFieldInteger from a JSON string
update_field_integer_instance = UpdateFieldInteger.from_json(json)
# print the JSON string representation of the object
print(UpdateFieldInteger.to_json())

# convert the object into a dict
update_field_integer_dict = update_field_integer_instance.to_dict()
# create an instance of UpdateFieldInteger from a dict
update_field_integer_from_dict = UpdateFieldInteger.from_dict(update_field_integer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


