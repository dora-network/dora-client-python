# UpdateAffiliateProgramRequestName

Updated names must contain 1 to 128 characters, without surrounding whitespace or control characters. Omitted, null, or update=false leaves the field unchanged.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update** | **bool** | Whether to update the field. | 
**value** | **str** | The new value to set for the field. | [optional] 

## Example

```python
from dora_client.models.update_affiliate_program_request_name import UpdateAffiliateProgramRequestName

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAffiliateProgramRequestName from a JSON string
update_affiliate_program_request_name_instance = UpdateAffiliateProgramRequestName.from_json(json)
# print the JSON string representation of the object
print(UpdateAffiliateProgramRequestName.to_json())

# convert the object into a dict
update_affiliate_program_request_name_dict = update_affiliate_program_request_name_instance.to_dict()
# create an instance of UpdateAffiliateProgramRequestName from a dict
update_affiliate_program_request_name_from_dict = UpdateAffiliateProgramRequestName.from_dict(update_affiliate_program_request_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


