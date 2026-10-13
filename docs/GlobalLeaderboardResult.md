# GlobalLeaderboardResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **UUID** |  | [optional] 
**user_name** | **str** |  | [optional] 
**cum_volume** | **str** |  | [optional] 
**cum_pnl** | **str** |  | [optional] 
**active_days** | **int** |  | [optional] 
**cum_trades** | **int** |  | [optional] 
**account_value** | **str** |  | [optional] 
**pnl_pct** | **str** | Cumulative pnl as a percentage of total TRADING_CHALLENGE_DEPOSIT and EXTERNAL_DEPOSIT quantities. | [optional] 

## Example

```python
from dora_client.models.global_leaderboard_result import GlobalLeaderboardResult

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalLeaderboardResult from a JSON string
global_leaderboard_result_instance = GlobalLeaderboardResult.from_json(json)
# print the JSON string representation of the object
print(GlobalLeaderboardResult.to_json())

# convert the object into a dict
global_leaderboard_result_dict = global_leaderboard_result_instance.to_dict()
# create an instance of GlobalLeaderboardResult from a dict
global_leaderboard_result_from_dict = GlobalLeaderboardResult.from_dict(global_leaderboard_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


