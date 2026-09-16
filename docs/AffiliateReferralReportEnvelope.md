# AffiliateReferralReportEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AffiliateReferralReport**](AffiliateReferralReport.md) |  | 
**metadata** | [**Metadata**](Metadata.md) |  | 

## Example

```python
from dora_client.models.affiliate_referral_report_envelope import AffiliateReferralReportEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of AffiliateReferralReportEnvelope from a JSON string
affiliate_referral_report_envelope_instance = AffiliateReferralReportEnvelope.from_json(json)
# print the JSON string representation of the object
print(AffiliateReferralReportEnvelope.to_json())

# convert the object into a dict
affiliate_referral_report_envelope_dict = affiliate_referral_report_envelope_instance.to_dict()
# create an instance of AffiliateReferralReportEnvelope from a dict
affiliate_referral_report_envelope_from_dict = AffiliateReferralReportEnvelope.from_dict(affiliate_referral_report_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


