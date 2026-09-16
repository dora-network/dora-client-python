# PnLRankingResponses


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | [**PnLRankingSummary**](PnLRankingSummary.md) |  | 
**rankings** | [**List[PnLRankingResponse]**](PnLRankingResponse.md) |  | 

## Example

```python
from dora_client.models.pn_l_ranking_responses import PnLRankingResponses

# TODO update the JSON string below
json = "{}"
# create an instance of PnLRankingResponses from a JSON string
pn_l_ranking_responses_instance = PnLRankingResponses.from_json(json)
# print the JSON string representation of the object
print(PnLRankingResponses.to_json())

# convert the object into a dict
pn_l_ranking_responses_dict = pn_l_ranking_responses_instance.to_dict()
# create an instance of PnLRankingResponses from a dict
pn_l_ranking_responses_from_dict = PnLRankingResponses.from_dict(pn_l_ranking_responses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


