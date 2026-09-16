# AffiliateReferralReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | 
**referrals** | [**List[AffiliateReferral]**](AffiliateReferral.md) |  | 
**has_more** | **bool** |  | 

## Example

```python
from dora_client.models.affiliate_referral_report import AffiliateReferralReport

# TODO update the JSON string below
json = "{}"
# create an instance of AffiliateReferralReport from a JSON string
affiliate_referral_report_instance = AffiliateReferralReport.from_json(json)
# print the JSON string representation of the object
print(AffiliateReferralReport.to_json())

# convert the object into a dict
affiliate_referral_report_dict = affiliate_referral_report_instance.to_dict()
# create an instance of AffiliateReferralReport from a dict
affiliate_referral_report_from_dict = AffiliateReferralReport.from_dict(affiliate_referral_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


