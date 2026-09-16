# PnLRankingSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_users_daily_trading_volume** | **str** | Sum of daily_trading_volume across all users matching ranking filters before pagination. | 
**all_users_total_trading_volume** | **str** | Sum of total_trading_volume across all users matching ranking filters before pagination. | 

## Example

```python
from dora_client.models.pn_l_ranking_summary import PnLRankingSummary

# TODO update the JSON string below
json = "{}"
# create an instance of PnLRankingSummary from a JSON string
pn_l_ranking_summary_instance = PnLRankingSummary.from_json(json)
# print the JSON string representation of the object
print(PnLRankingSummary.to_json())

# convert the object into a dict
pn_l_ranking_summary_dict = pn_l_ranking_summary_instance.to_dict()
# create an instance of PnLRankingSummary from a dict
pn_l_ranking_summary_from_dict = PnLRankingSummary.from_dict(pn_l_ranking_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


