# PromoLinkBatchSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**source_type** | [**PromoSourceType**](PromoSourceType.md) |  | 
**source_id** | **str** |  | 
**source_name** | **str** |  | 
**allocation** | **int** |  | 
**issued** | **int** |  | 
**claimed** | **int** |  | 
**revoked** | **int** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from dora_client.models.promo_link_batch_summary import PromoLinkBatchSummary

# TODO update the JSON string below
json = "{}"
# create an instance of PromoLinkBatchSummary from a JSON string
promo_link_batch_summary_instance = PromoLinkBatchSummary.from_json(json)
# print the JSON string representation of the object
print(PromoLinkBatchSummary.to_json())

# convert the object into a dict
promo_link_batch_summary_dict = promo_link_batch_summary_instance.to_dict()
# create an instance of PromoLinkBatchSummary from a dict
promo_link_batch_summary_from_dict = PromoLinkBatchSummary.from_dict(promo_link_batch_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


