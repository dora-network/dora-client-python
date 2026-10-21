# IssuePromoLinkBatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**PromoSourceType**](PromoSourceType.md) |  | 
**source_id** | **str** |  | 
**source_name** | **str** |  | [optional] 
**allocation** | **int** | Required for SINGLE_USE; omit for REUSABLE. Bounded by max_links_per_batch. Minting reserves no campaign place. | [optional] 
**note** | **str** |  | [optional] 
**expires_at** | **datetime** | Defaults to challenge end and must fall between challenge start and end in the future. | [optional] 
**link_type** | **str** | Defaults to SINGLE_USE for existing clients. REUSABLE creates one tracked link without a quantity. | [optional] 
**affiliate_program_id** | **UUID** |  | [optional] 
**affiliate_member_id** | **UUID** | Existing affiliate referrer/member ID, not user ID. | [optional] 
**referral_code** | **str** | An existing code belonging to the selected member. Required with both IDs for reusable links; bound on the server and revalidated at claim time. | [optional] 

## Example

```python
from dora_client.models.issue_promo_link_batch_request import IssuePromoLinkBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IssuePromoLinkBatchRequest from a JSON string
issue_promo_link_batch_request_instance = IssuePromoLinkBatchRequest.from_json(json)
# print the JSON string representation of the object
print(IssuePromoLinkBatchRequest.to_json())

# convert the object into a dict
issue_promo_link_batch_request_dict = issue_promo_link_batch_request_instance.to_dict()
# create an instance of IssuePromoLinkBatchRequest from a dict
issue_promo_link_batch_request_from_dict = IssuePromoLinkBatchRequest.from_dict(issue_promo_link_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


