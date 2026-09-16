# IssuePromoLinkBatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**IssuePromoLinkBatchResponseAllOfData**](IssuePromoLinkBatchResponseAllOfData.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.issue_promo_link_batch_response import IssuePromoLinkBatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IssuePromoLinkBatchResponse from a JSON string
issue_promo_link_batch_response_instance = IssuePromoLinkBatchResponse.from_json(json)
# print the JSON string representation of the object
print(IssuePromoLinkBatchResponse.to_json())

# convert the object into a dict
issue_promo_link_batch_response_dict = issue_promo_link_batch_response_instance.to_dict()
# create an instance of IssuePromoLinkBatchResponse from a dict
issue_promo_link_batch_response_from_dict = IssuePromoLinkBatchResponse.from_dict(issue_promo_link_batch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


