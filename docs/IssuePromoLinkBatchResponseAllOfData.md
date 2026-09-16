# IssuePromoLinkBatchResponseAllOfData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_id** | **UUID** |  | 
**source_id** | **str** |  | 
**allocation** | **int** |  | 
**links** | [**List[IssuedPromoLink]**](IssuedPromoLink.md) |  | 

## Example

```python
from dora_client.models.issue_promo_link_batch_response_all_of_data import IssuePromoLinkBatchResponseAllOfData

# TODO update the JSON string below
json = "{}"
# create an instance of IssuePromoLinkBatchResponseAllOfData from a JSON string
issue_promo_link_batch_response_all_of_data_instance = IssuePromoLinkBatchResponseAllOfData.from_json(json)
# print the JSON string representation of the object
print(IssuePromoLinkBatchResponseAllOfData.to_json())

# convert the object into a dict
issue_promo_link_batch_response_all_of_data_dict = issue_promo_link_batch_response_all_of_data_instance.to_dict()
# create an instance of IssuePromoLinkBatchResponseAllOfData from a dict
issue_promo_link_batch_response_all_of_data_from_dict = IssuePromoLinkBatchResponseAllOfData.from_dict(issue_promo_link_batch_response_all_of_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


