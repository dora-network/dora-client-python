# PnLRankingSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_users_daily_trading_volume** | **str** | Sum of daily_trading_volume across all users matching ranking filters before pagination. | 
**all_users_total_trading_volume** | **str** | Sum of total_trading_volume across all users matching ranking filters before pagination. | 
**all_users_avg_daily_trading_volume** | **str** | all_users_total_trading_volume divided by the number of distinct UTC days on which any matching user had an executed fill. 0 if there are none. | 
**all_users_avg_daily_trading_volume_on_n_days** | **str** | Executed trading volume within [start, end) across all users matching ranking filters, divided by the number of requested days elapsed so far (end clamped to now, partial days rounded up). 0 if start is in the future. | 

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


