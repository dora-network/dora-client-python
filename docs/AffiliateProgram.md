# AffiliateProgram


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**tenant_id** | **str** | Owning tenant for administration. This does not define a referral destination. | 
**name** | **str** | No surrounding whitespace or control characters. | 
**description** | **str** | Must not contain NUL characters. | 
**is_active** | **bool** | Inactive programs retain registrations, but cannot issue or resolve codes. | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from dora_client.models.affiliate_program import AffiliateProgram

# TODO update the JSON string below
json = "{}"
# create an instance of AffiliateProgram from a JSON string
affiliate_program_instance = AffiliateProgram.from_json(json)
# print the JSON string representation of the object
print(AffiliateProgram.to_json())

# convert the object into a dict
affiliate_program_dict = affiliate_program_instance.to_dict()
# create an instance of AffiliateProgram from a dict
affiliate_program_from_dict = AffiliateProgram.from_dict(affiliate_program_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


