# AffiliateMembership


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**program_id** | **UUID** |  | 
**tenant_id** | **str** | Owning tenant for administration. This does not define a referral destination. | 
**user_id** | **UUID** |  | 
**referral_code** | **str** | Current code to share; previously issued codes remain valid. | 
**created_at** | **datetime** |  | 
**program_name** | **str** |  | 
**is_active** | **bool** |  | 
**customized_at** | **datetime** |  | 
**can_customize** | **bool** | True when this membership has not used its one-time code change, including while the program is inactive. | 

## Example

```python
from dora_client.models.affiliate_membership import AffiliateMembership

# TODO update the JSON string below
json = "{}"
# create an instance of AffiliateMembership from a JSON string
affiliate_membership_instance = AffiliateMembership.from_json(json)
# print the JSON string representation of the object
print(AffiliateMembership.to_json())

# convert the object into a dict
affiliate_membership_dict = affiliate_membership_instance.to_dict()
# create an instance of AffiliateMembership from a dict
affiliate_membership_from_dict = AffiliateMembership.from_dict(affiliate_membership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


