# TradingChallenge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**name** | **str** | Trading challenge name | [optional] 
**tenant_id** | **str** |  | 
**type** | [**TradingChallengeType**](TradingChallengeType.md) |  | 
**status** | [**TradingChallengeStatus**](TradingChallengeStatus.md) |  | 
**max_users** | **int** |  | 
**start_at** | **datetime** |  | 
**end_at** | **datetime** |  | 
**initial_user_balance** | **str** |  | 
**gold_prize_quantity** | **str** |  | 
**silver_prize_quantity** | **str** |  | 
**bronze_prize_quantity** | **str** |  | 
**pnl_condition** | **str** |  | 
**total_volume_condition** | **str** |  | 
**avg_daily_volume_condition** | **str** |  | 
**minimum_equity_percentage_condition** | **int** |  | 
**created_at** | **datetime** |  | 
**last_processed_at** | **datetime** |  | [optional] 
**users** | **List[UUID]** |  | [optional] 
**users_count** | **int** |  | 

## Example

```python
from dora_client.models.trading_challenge import TradingChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of TradingChallenge from a JSON string
trading_challenge_instance = TradingChallenge.from_json(json)
# print the JSON string representation of the object
print(TradingChallenge.to_json())

# convert the object into a dict
trading_challenge_dict = trading_challenge_instance.to_dict()
# create an instance of TradingChallenge from a dict
trading_challenge_from_dict = TradingChallenge.from_dict(trading_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


