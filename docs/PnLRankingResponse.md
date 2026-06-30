# PnLRankingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **UUID** |  | 
**first_name** | **str** |  | 
**total_pnl** | **str** |  | 
**total_trades** | **int** |  | 
**winning_trades** | **int** |  | 
**losing_trades** | **int** |  | 
**win_rate** | **str** |  | 

## Example

```python
from dora_client.models.pn_l_ranking_response import PnLRankingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PnLRankingResponse from a JSON string
pn_l_ranking_response_instance = PnLRankingResponse.from_json(json)
# print the JSON string representation of the object
print(PnLRankingResponse.to_json())

# convert the object into a dict
pn_l_ranking_response_dict = pn_l_ranking_response_instance.to_dict()
# create an instance of PnLRankingResponse from a dict
pn_l_ranking_response_from_dict = PnLRankingResponse.from_dict(pn_l_ranking_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


