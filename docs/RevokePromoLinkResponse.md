# RevokePromoLinkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**RevokePromoLinkResponseAllOfData**](RevokePromoLinkResponseAllOfData.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.revoke_promo_link_response import RevokePromoLinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RevokePromoLinkResponse from a JSON string
revoke_promo_link_response_instance = RevokePromoLinkResponse.from_json(json)
# print the JSON string representation of the object
print(RevokePromoLinkResponse.to_json())

# convert the object into a dict
revoke_promo_link_response_dict = revoke_promo_link_response_instance.to_dict()
# create an instance of RevokePromoLinkResponse from a dict
revoke_promo_link_response_from_dict = RevokePromoLinkResponse.from_dict(revoke_promo_link_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


