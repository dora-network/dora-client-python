# RegisterAffiliateReferrerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **UUID** | Existing, nonzero DORA user ID in the program owning tenant. | 
**referral_code** | **str** | Optional custom code: 3 to 64 letters, digits, hyphens or underscores after trimming, starting with a letter or digit. Stored uppercase and unique across all programs and tenants. Omitted, null or empty generates a random code. | [optional] 

## Example

```python
from dora_client.models.register_affiliate_referrer_request import RegisterAffiliateReferrerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterAffiliateReferrerRequest from a JSON string
register_affiliate_referrer_request_instance = RegisterAffiliateReferrerRequest.from_json(json)
# print the JSON string representation of the object
print(RegisterAffiliateReferrerRequest.to_json())

# convert the object into a dict
register_affiliate_referrer_request_dict = register_affiliate_referrer_request_instance.to_dict()
# create an instance of RegisterAffiliateReferrerRequest from a dict
register_affiliate_referrer_request_from_dict = RegisterAffiliateReferrerRequest.from_dict(register_affiliate_referrer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


