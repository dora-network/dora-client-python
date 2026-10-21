# PromoLinkListResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**List[PromoLinkAdmin]**](PromoLinkAdmin.md) |  | 
**next_cursor** | **str** | Opaque unpadded base64url keyset cursor. | [optional] 

## Example

```python
from dora_client.models.promo_link_list_response_data import PromoLinkListResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PromoLinkListResponseData from a JSON string
promo_link_list_response_data_instance = PromoLinkListResponseData.from_json(json)
# print the JSON string representation of the object
print(PromoLinkListResponseData.to_json())

# convert the object into a dict
promo_link_list_response_data_dict = promo_link_list_response_data_instance.to_dict()
# create an instance of PromoLinkListResponseData from a dict
promo_link_list_response_data_from_dict = PromoLinkListResponseData.from_dict(promo_link_list_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


