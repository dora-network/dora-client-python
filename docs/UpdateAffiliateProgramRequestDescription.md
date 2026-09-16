# UpdateAffiliateProgramRequestDescription

Updated descriptions must not exceed 2048 characters or contain NUL. Omitted, null, or update=false leaves the field unchanged.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update** | **bool** | Whether to update the field. | 
**value** | **str** | The new value to set for the field. | [optional] 

## Example

```python
from dora_client.models.update_affiliate_program_request_description import UpdateAffiliateProgramRequestDescription

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAffiliateProgramRequestDescription from a JSON string
update_affiliate_program_request_description_instance = UpdateAffiliateProgramRequestDescription.from_json(json)
# print the JSON string representation of the object
print(UpdateAffiliateProgramRequestDescription.to_json())

# convert the object into a dict
update_affiliate_program_request_description_dict = update_affiliate_program_request_description_instance.to_dict()
# create an instance of UpdateAffiliateProgramRequestDescription from a dict
update_affiliate_program_request_description_from_dict = UpdateAffiliateProgramRequestDescription.from_dict(update_affiliate_program_request_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


