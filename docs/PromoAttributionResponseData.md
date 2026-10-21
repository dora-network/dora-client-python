# PromoAttributionResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sources** | [**List[PromoAttributionSource]**](PromoAttributionSource.md) |  | 

## Example

```python
from dora_client.models.promo_attribution_response_data import PromoAttributionResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PromoAttributionResponseData from a JSON string
promo_attribution_response_data_instance = PromoAttributionResponseData.from_json(json)
# print the JSON string representation of the object
print(PromoAttributionResponseData.to_json())

# convert the object into a dict
promo_attribution_response_data_dict = promo_attribution_response_data_instance.to_dict()
# create an instance of PromoAttributionResponseData from a dict
promo_attribution_response_data_from_dict = PromoAttributionResponseData.from_dict(promo_attribution_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


