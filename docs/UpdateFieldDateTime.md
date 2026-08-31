# UpdateFieldDateTime

A generic struct to handle optional updates for date-time fields in user requests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update** | **bool** | Whether to update the field. | 
**value** | **datetime** | The new value to set for the field. | [optional] 

## Example

```python
from dora_client.models.update_field_date_time import UpdateFieldDateTime

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFieldDateTime from a JSON string
update_field_date_time_instance = UpdateFieldDateTime.from_json(json)
# print the JSON string representation of the object
print(UpdateFieldDateTime.to_json())

# convert the object into a dict
update_field_date_time_dict = update_field_date_time_instance.to_dict()
# create an instance of UpdateFieldDateTime from a dict
update_field_date_time_from_dict = UpdateFieldDateTime.from_dict(update_field_date_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


