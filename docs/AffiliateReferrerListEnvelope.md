# AffiliateReferrerListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AffiliateReferrer]**](AffiliateReferrer.md) |  | 
**metadata** | [**Metadata**](Metadata.md) |  | 

## Example

```python
from dora_client.models.affiliate_referrer_list_envelope import AffiliateReferrerListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of AffiliateReferrerListEnvelope from a JSON string
affiliate_referrer_list_envelope_instance = AffiliateReferrerListEnvelope.from_json(json)
# print the JSON string representation of the object
print(AffiliateReferrerListEnvelope.to_json())

# convert the object into a dict
affiliate_referrer_list_envelope_dict = affiliate_referrer_list_envelope_instance.to_dict()
# create an instance of AffiliateReferrerListEnvelope from a dict
affiliate_referrer_list_envelope_from_dict = AffiliateReferrerListEnvelope.from_dict(affiliate_referrer_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


