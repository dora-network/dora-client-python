# AffiliateAttribution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**referred_user_id** | **UUID** |  | 
**program_id** | **UUID** |  | 
**referrer_id** | **UUID** |  | 
**referrer_user_id** | **UUID** |  | 
**tenant_id** | **str** |  | 
**signup_source** | **str** | Signup hostname when assigned at signup; empty for an assignment made later. | 
**created_at** | **datetime** | Immutable assignment time; activity begins counting from this timestamp. | 
**referral_code** | **str** |  | 

## Example

```python
from dora_client.models.affiliate_attribution import AffiliateAttribution

# TODO update the JSON string below
json = "{}"
# create an instance of AffiliateAttribution from a JSON string
affiliate_attribution_instance = AffiliateAttribution.from_json(json)
# print the JSON string representation of the object
print(AffiliateAttribution.to_json())

# convert the object into a dict
affiliate_attribution_dict = affiliate_attribution_instance.to_dict()
# create an instance of AffiliateAttribution from a dict
affiliate_attribution_from_dict = AffiliateAttribution.from_dict(affiliate_attribution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


