# AffiliateAttributionEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AffiliateAttribution**](AffiliateAttribution.md) |  | 
**metadata** | [**Metadata**](Metadata.md) |  | 

## Example

```python
from dora_client.models.affiliate_attribution_envelope import AffiliateAttributionEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of AffiliateAttributionEnvelope from a JSON string
affiliate_attribution_envelope_instance = AffiliateAttributionEnvelope.from_json(json)
# print the JSON string representation of the object
print(AffiliateAttributionEnvelope.to_json())

# convert the object into a dict
affiliate_attribution_envelope_dict = affiliate_attribution_envelope_instance.to_dict()
# create an instance of AffiliateAttributionEnvelope from a dict
affiliate_attribution_envelope_from_dict = AffiliateAttributionEnvelope.from_dict(affiliate_attribution_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


