# IssuePromoLinkBatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**PromoSourceType**](PromoSourceType.md) |  | 
**source_id** | **str** |  | 
**source_name** | **str** |  | [optional] 
**allocation** | **int** | Cannot exceed the configured max_links_per_batch or remaining campaign capacity. | 
**note** | **str** |  | [optional] 
**expires_at** | **datetime** | Defaults to challenge end and must fall between challenge start and end in the future. | [optional] 

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


