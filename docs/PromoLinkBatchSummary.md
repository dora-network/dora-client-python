# PromoLinkBatchSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**source_type** | [**PromoSourceType**](PromoSourceType.md) |  | 
**source_id** | **str** |  | 
**source_name** | **str** |  | 
**allocation** | **int** |  | [optional] 
**issued** | **int** |  | [optional] 
**claimed** | **int** |  | [optional] 
**revoked** | **int** |  | [optional] 
**created_at** | **datetime** |  | 
**link_type** | **str** | Defaults to SINGLE_USE for existing clients. REUSABLE creates one tracked link without a quantity. | [optional] 
**affiliate_program_id** | **UUID** |  | [optional] 
**affiliate_member_id** | **UUID** | Existing affiliate referrer/member ID, not user ID. | [optional] 
**referral_code** | **str** | An existing code belonging to the selected member. Required with both IDs for reusable links; bound on the server and revalidated at claim time. | [optional] 
**campaign_id** | **UUID** |  | [optional] 
**signups** | **int** | Successful signups; reusable links omit allocation/issued/claimed/revoked counts. | [optional] 

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


