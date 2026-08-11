# TradingChallengeResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trading_challenge_id** | **UUID** |  | [optional] 
**user_id** | **UUID** |  | [optional] 
**user_name** | **str** |  | [optional] 
**cum_volume** | **str** |  | [optional] 
**cum_pnl** | **str** |  | [optional] 
**pnl_pct** | **str** |  | [optional] 
**calendar_days_since_start** | **int** |  | [optional] 
**active_days** | **int** |  | [optional] 
**compliant_days** | **int** |  | [optional] 
**crown_eligible** | **bool** |  | [optional] 
**claim_eligible** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 
**crown** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**current_day_daily_volume** | **str** |  | [optional] 
**current_day_daily_pnl** | **str** |  | [optional] 
**current_day_trading_date** | **date** |  | [optional] 
**cum_trades** | **int** |  | [optional] 

## Example

```python
from dora_client.models.trading_challenge_result import TradingChallengeResult

# TODO update the JSON string below
json = "{}"
# create an instance of TradingChallengeResult from a JSON string
trading_challenge_result_instance = TradingChallengeResult.from_json(json)
# print the JSON string representation of the object
print(TradingChallengeResult.to_json())

# convert the object into a dict
trading_challenge_result_dict = trading_challenge_result_instance.to_dict()
# create an instance of TradingChallengeResult from a dict
trading_challenge_result_from_dict = TradingChallengeResult.from_dict(trading_challenge_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


