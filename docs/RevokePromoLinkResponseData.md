# RevokePromoLinkResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**status** | **str** |  | 
**repeated** | **bool** |  | 

## Example

```python
from dora_client.models.revoke_promo_link_response_data import RevokePromoLinkResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of RevokePromoLinkResponseData from a JSON string
revoke_promo_link_response_data_instance = RevokePromoLinkResponseData.from_json(json)
# print the JSON string representation of the object
print(RevokePromoLinkResponseData.to_json())

# convert the object into a dict
revoke_promo_link_response_data_dict = revoke_promo_link_response_data_instance.to_dict()
# create an instance of RevokePromoLinkResponseData from a dict
revoke_promo_link_response_data_from_dict = RevokePromoLinkResponseData.from_dict(revoke_promo_link_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


