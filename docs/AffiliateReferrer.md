# AffiliateReferrer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**program_id** | **UUID** |  | 
**tenant_id** | **str** | Owning tenant for administration. This does not define a referral destination. | 
**user_id** | **UUID** |  | 
**referral_code** | **str** | Reusable referral code, stored uppercase. Letters, digits, hyphens and underscores are accepted; the first character must be a letter or digit. Matching is case-insensitive. Separate from QR claim tokens. | 
**created_at** | **datetime** |  | 

## Example

```python
from dora_client.models.affiliate_referrer import AffiliateReferrer

# TODO update the JSON string below
json = "{}"
# create an instance of AffiliateReferrer from a JSON string
affiliate_referrer_instance = AffiliateReferrer.from_json(json)
# print the JSON string representation of the object
print(AffiliateReferrer.to_json())

# convert the object into a dict
affiliate_referrer_dict = affiliate_referrer_instance.to_dict()
# create an instance of AffiliateReferrer from a dict
affiliate_referrer_from_dict = AffiliateReferrer.from_dict(affiliate_referrer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


