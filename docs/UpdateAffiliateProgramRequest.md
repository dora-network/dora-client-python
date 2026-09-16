# UpdateAffiliateProgramRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**UpdateAffiliateProgramRequestName**](UpdateAffiliateProgramRequestName.md) |  | [optional] 
**description** | [**UpdateAffiliateProgramRequestDescription**](UpdateAffiliateProgramRequestDescription.md) |  | [optional] 
**is_active** | [**UpdateAffiliateProgramRequestIsActive**](UpdateAffiliateProgramRequestIsActive.md) |  | [optional] 

## Example

```python
from dora_client.models.update_affiliate_program_request import UpdateAffiliateProgramRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAffiliateProgramRequest from a JSON string
update_affiliate_program_request_instance = UpdateAffiliateProgramRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAffiliateProgramRequest.to_json())

# convert the object into a dict
update_affiliate_program_request_dict = update_affiliate_program_request_instance.to_dict()
# create an instance of UpdateAffiliateProgramRequest from a dict
update_affiliate_program_request_from_dict = UpdateAffiliateProgramRequest.from_dict(update_affiliate_program_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


