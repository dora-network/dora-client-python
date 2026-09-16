# ClaimPromoLinkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 

## Example

```python
from dora_client.models.claim_promo_link_request import ClaimPromoLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClaimPromoLinkRequest from a JSON string
claim_promo_link_request_instance = ClaimPromoLinkRequest.from_json(json)
# print the JSON string representation of the object
print(ClaimPromoLinkRequest.to_json())

# convert the object into a dict
claim_promo_link_request_dict = claim_promo_link_request_instance.to_dict()
# create an instance of ClaimPromoLinkRequest from a dict
claim_promo_link_request_from_dict = ClaimPromoLinkRequest.from_dict(claim_promo_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


