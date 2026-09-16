# PromoAttributionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PromoAttributionResponseAllOfData**](PromoAttributionResponseAllOfData.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.promo_attribution_response import PromoAttributionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PromoAttributionResponse from a JSON string
promo_attribution_response_instance = PromoAttributionResponse.from_json(json)
# print the JSON string representation of the object
print(PromoAttributionResponse.to_json())

# convert the object into a dict
promo_attribution_response_dict = promo_attribution_response_instance.to_dict()
# create an instance of PromoAttributionResponse from a dict
promo_attribution_response_from_dict = PromoAttributionResponse.from_dict(promo_attribution_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


