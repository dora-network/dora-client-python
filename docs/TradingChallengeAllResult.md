# TradingChallengeAllResult


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
**pnl_pct** | **str** |  | [optional] 

## Example

```python
from dora_client.models.trading_challenge_all_result import TradingChallengeAllResult

# TODO update the JSON string below
json = "{}"
# create an instance of TradingChallengeAllResult from a JSON string
trading_challenge_all_result_instance = TradingChallengeAllResult.from_json(json)
# print the JSON string representation of the object
print(TradingChallengeAllResult.to_json())

# convert the object into a dict
trading_challenge_all_result_dict = trading_challenge_all_result_instance.to_dict()
# create an instance of TradingChallengeAllResult from a dict
trading_challenge_all_result_from_dict = TradingChallengeAllResult.from_dict(trading_challenge_all_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


