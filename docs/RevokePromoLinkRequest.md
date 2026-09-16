# RevokePromoLinkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | 

## Example

```python
from dora_client.models.revoke_promo_link_request import RevokePromoLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RevokePromoLinkRequest from a JSON string
revoke_promo_link_request_instance = RevokePromoLinkRequest.from_json(json)
# print the JSON string representation of the object
print(RevokePromoLinkRequest.to_json())

# convert the object into a dict
revoke_promo_link_request_dict = revoke_promo_link_request_instance.to_dict()
# create an instance of RevokePromoLinkRequest from a dict
revoke_promo_link_request_from_dict = RevokePromoLinkRequest.from_dict(revoke_promo_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


