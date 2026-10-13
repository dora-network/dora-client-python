# CustomizeAffiliateReferrerCodeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**referral_code** | **str** | New unique code. Trimmed and stored uppercase; 3 to 64 letters, digits, hyphens or underscores, starting with a letter or digit. | 

## Example

```python
from dora_client.models.customize_affiliate_referrer_code_request import CustomizeAffiliateReferrerCodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizeAffiliateReferrerCodeRequest from a JSON string
customize_affiliate_referrer_code_request_instance = CustomizeAffiliateReferrerCodeRequest.from_json(json)
# print the JSON string representation of the object
print(CustomizeAffiliateReferrerCodeRequest.to_json())

# convert the object into a dict
customize_affiliate_referrer_code_request_dict = customize_affiliate_referrer_code_request_instance.to_dict()
# create an instance of CustomizeAffiliateReferrerCodeRequest from a dict
customize_affiliate_referrer_code_request_from_dict = CustomizeAffiliateReferrerCodeRequest.from_dict(customize_affiliate_referrer_code_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


