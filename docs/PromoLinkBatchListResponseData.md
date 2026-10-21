# PromoLinkBatchListResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batches** | [**List[PromoLinkBatchSummary]**](PromoLinkBatchSummary.md) |  | 

## Example

```python
from dora_client.models.promo_link_batch_list_response_data import PromoLinkBatchListResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PromoLinkBatchListResponseData from a JSON string
promo_link_batch_list_response_data_instance = PromoLinkBatchListResponseData.from_json(json)
# print the JSON string representation of the object
print(PromoLinkBatchListResponseData.to_json())

# convert the object into a dict
promo_link_batch_list_response_data_dict = promo_link_batch_list_response_data_instance.to_dict()
# create an instance of PromoLinkBatchListResponseData from a dict
promo_link_batch_list_response_data_from_dict = PromoLinkBatchListResponseData.from_dict(promo_link_batch_list_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


