# PromoLinkListResponseAllOfData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**List[PromoLinkAdmin]**](PromoLinkAdmin.md) |  | 
**next_cursor** | **str** | Opaque unpadded base64url keyset cursor. | [optional] 

## Example

```python
from dora_client.models.promo_link_list_response_all_of_data import PromoLinkListResponseAllOfData

# TODO update the JSON string below
json = "{}"
# create an instance of PromoLinkListResponseAllOfData from a JSON string
promo_link_list_response_all_of_data_instance = PromoLinkListResponseAllOfData.from_json(json)
# print the JSON string representation of the object
print(PromoLinkListResponseAllOfData.to_json())

# convert the object into a dict
promo_link_list_response_all_of_data_dict = promo_link_list_response_all_of_data_instance.to_dict()
# create an instance of PromoLinkListResponseAllOfData from a dict
promo_link_list_response_all_of_data_from_dict = PromoLinkListResponseAllOfData.from_dict(promo_link_list_response_all_of_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


