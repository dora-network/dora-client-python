# IssuedPromoLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**token_prefix** | **str** |  | 
**url** | **str** | Private claim URL. Do not log or cache. | 
**qr_url** | **str** |  | 
**expires_at** | **datetime** |  | 

## Example

```python
from dora_client.models.issued_promo_link import IssuedPromoLink

# TODO update the JSON string below
json = "{}"
# create an instance of IssuedPromoLink from a JSON string
issued_promo_link_instance = IssuedPromoLink.from_json(json)
# print the JSON string representation of the object
print(IssuedPromoLink.to_json())

# convert the object into a dict
issued_promo_link_dict = issued_promo_link_instance.to_dict()
# create an instance of IssuedPromoLink from a dict
issued_promo_link_from_dict = IssuedPromoLink.from_dict(issued_promo_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


