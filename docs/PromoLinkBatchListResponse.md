# PromoLinkBatchListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PromoLinkBatchListResponseAllOfData**](PromoLinkBatchListResponseAllOfData.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.promo_link_batch_list_response import PromoLinkBatchListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PromoLinkBatchListResponse from a JSON string
promo_link_batch_list_response_instance = PromoLinkBatchListResponse.from_json(json)
# print the JSON string representation of the object
print(PromoLinkBatchListResponse.to_json())

# convert the object into a dict
promo_link_batch_list_response_dict = promo_link_batch_list_response_instance.to_dict()
# create an instance of PromoLinkBatchListResponse from a dict
promo_link_batch_list_response_from_dict = PromoLinkBatchListResponse.from_dict(promo_link_batch_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


