# AssignAffiliateReferralRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**referral_code** | **str** | Existing code, trimmed and matched case-insensitively. Required and nonempty. | 

## Example

```python
from dora_client.models.assign_affiliate_referral_request import AssignAffiliateReferralRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssignAffiliateReferralRequest from a JSON string
assign_affiliate_referral_request_instance = AssignAffiliateReferralRequest.from_json(json)
# print the JSON string representation of the object
print(AssignAffiliateReferralRequest.to_json())

# convert the object into a dict
assign_affiliate_referral_request_dict = assign_affiliate_referral_request_instance.to_dict()
# create an instance of AssignAffiliateReferralRequest from a dict
assign_affiliate_referral_request_from_dict = AssignAffiliateReferralRequest.from_dict(assign_affiliate_referral_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


