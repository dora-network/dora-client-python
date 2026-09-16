# CreateAffiliateProgramRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Owning tenant for administration. This does not define a referral destination. | 
**name** | **str** | No surrounding whitespace or control characters. | 
**description** | **str** | Omitted or null defaults to an empty description. | [optional] [default to '']
**is_active** | **bool** | Inactive programs retain registrations, but cannot issue or resolve codes. Set true to create an active program. | [optional] [default to False]

## Example

```python
from dora_client.models.create_affiliate_program_request import CreateAffiliateProgramRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAffiliateProgramRequest from a JSON string
create_affiliate_program_request_instance = CreateAffiliateProgramRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAffiliateProgramRequest.to_json())

# convert the object into a dict
create_affiliate_program_request_dict = create_affiliate_program_request_instance.to_dict()
# create an instance of CreateAffiliateProgramRequest from a dict
create_affiliate_program_request_from_dict = CreateAffiliateProgramRequest.from_dict(create_affiliate_program_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


