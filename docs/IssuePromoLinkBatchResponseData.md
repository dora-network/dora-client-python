# IssuePromoLinkBatchResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_id** | **UUID** |  | 
**source_id** | **str** |  | 
**allocation** | **int** |  | [optional] 
**links** | [**List[IssuedPromoLink]**](IssuedPromoLink.md) |  | 
**link_type** | **str** | Defaults to SINGLE_USE for existing clients. REUSABLE creates one tracked link without a quantity. | [optional] 
**affiliate_program_id** | **UUID** |  | [optional] 
**affiliate_member_id** | **UUID** | Existing affiliate referrer/member ID, not user ID. | [optional] 
**referral_code** | **str** | An existing code belonging to the selected member. Required with both IDs for reusable links; bound on the server and revalidated at claim time. | [optional] 

## Example

```python
from dora_client.models.issue_promo_link_batch_response_data import IssuePromoLinkBatchResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of IssuePromoLinkBatchResponseData from a JSON string
issue_promo_link_batch_response_data_instance = IssuePromoLinkBatchResponseData.from_json(json)
# print the JSON string representation of the object
print(IssuePromoLinkBatchResponseData.to_json())

# convert the object into a dict
issue_promo_link_batch_response_data_dict = issue_promo_link_batch_response_data_instance.to_dict()
# create an instance of IssuePromoLinkBatchResponseData from a dict
issue_promo_link_batch_response_data_from_dict = IssuePromoLinkBatchResponseData.from_dict(issue_promo_link_batch_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


