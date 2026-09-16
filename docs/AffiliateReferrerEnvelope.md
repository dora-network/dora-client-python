# AffiliateReferrerEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AffiliateReferrer**](AffiliateReferrer.md) |  | 
**metadata** | [**Metadata**](Metadata.md) |  | 

## Example

```python
from dora_client.models.affiliate_referrer_envelope import AffiliateReferrerEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of AffiliateReferrerEnvelope from a JSON string
affiliate_referrer_envelope_instance = AffiliateReferrerEnvelope.from_json(json)
# print the JSON string representation of the object
print(AffiliateReferrerEnvelope.to_json())

# convert the object into a dict
affiliate_referrer_envelope_dict = affiliate_referrer_envelope_instance.to_dict()
# create an instance of AffiliateReferrerEnvelope from a dict
affiliate_referrer_envelope_from_dict = AffiliateReferrerEnvelope.from_dict(affiliate_referrer_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


