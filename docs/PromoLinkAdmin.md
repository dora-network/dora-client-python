# PromoLinkAdmin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**token_prefix** | **str** |  | 
**url** | **str** | Only present when reveal&#x3D;true. Private; do not log or cache. | [optional] 
**status** | [**PromoLinkStatus**](PromoLinkStatus.md) |  | 
**expires_at** | **datetime** |  | 
**claimed_at** | **datetime** |  | [optional] 
**claimed_email** | **str** | Masked as the first character, three asterisks, and domain. | [optional] 
**user_id** | **UUID** |  | [optional] 

## Example

```python
from dora_client.models.promo_link_admin import PromoLinkAdmin

# TODO update the JSON string below
json = "{}"
# create an instance of PromoLinkAdmin from a JSON string
promo_link_admin_instance = PromoLinkAdmin.from_json(json)
# print the JSON string representation of the object
print(PromoLinkAdmin.to_json())

# convert the object into a dict
promo_link_admin_dict = promo_link_admin_instance.to_dict()
# create an instance of PromoLinkAdmin from a dict
promo_link_admin_from_dict = PromoLinkAdmin.from_dict(promo_link_admin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


