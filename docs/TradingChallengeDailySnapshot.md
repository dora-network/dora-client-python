# TradingChallengeDailySnapshot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trading_challenge_id** | **UUID** |  | [optional] 
**user_id** | **UUID** |  | [optional] 
**user_name** | **str** |  | [optional] 
**trading_date** | **date** |  | [optional] 
**daily_volume** | **str** |  | [optional] 
**daily_pnl** | **str** |  | [optional] 
**daily_trades** | **int** |  | [optional] 
**volume_compliant** | **bool** |  | [optional] 
**eod_equity** | **str** |  | [optional] 
**active_day** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from dora_client.models.trading_challenge_daily_snapshot import TradingChallengeDailySnapshot

# TODO update the JSON string below
json = "{}"
# create an instance of TradingChallengeDailySnapshot from a JSON string
trading_challenge_daily_snapshot_instance = TradingChallengeDailySnapshot.from_json(json)
# print the JSON string representation of the object
print(TradingChallengeDailySnapshot.to_json())

# convert the object into a dict
trading_challenge_daily_snapshot_dict = trading_challenge_daily_snapshot_instance.to_dict()
# create an instance of TradingChallengeDailySnapshot from a dict
trading_challenge_daily_snapshot_from_dict = TradingChallengeDailySnapshot.from_dict(trading_challenge_daily_snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


