# UpdateAffiliateProgramRequestIsActive

Inactive programs retain registrations, but cannot issue or resolve codes. Omitted, null, or update=false leaves the field unchanged.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update** | **bool** | Whether to update the field. | 
**value** | **bool** | The new value to set for the field. | [optional] 

## Example

```python
from dora_client.models.update_affiliate_program_request_is_active import UpdateAffiliateProgramRequestIsActive

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAffiliateProgramRequestIsActive from a JSON string
update_affiliate_program_request_is_active_instance = UpdateAffiliateProgramRequestIsActive.from_json(json)
# print the JSON string representation of the object
print(UpdateAffiliateProgramRequestIsActive.to_json())

# convert the object into a dict
update_affiliate_program_request_is_active_dict = update_affiliate_program_request_is_active_instance.to_dict()
# create an instance of UpdateAffiliateProgramRequestIsActive from a dict
update_affiliate_program_request_is_active_from_dict = UpdateAffiliateProgramRequestIsActive.from_dict(update_affiliate_program_request_is_active_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


