# CreateTradingChallengeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**name** | **str** | Trading challenge name | 
**type** | [**TradingChallengeType**](TradingChallengeType.md) |  | 
**max_users** | **int** |  | 
**start** | **datetime** |  | 
**end** | **datetime** |  | 
**initial_user_balance** | **str** |  | 
**gold_prize_quantity** | **str** |  | [optional] 
**silver_prize_quantity** | **str** |  | [optional] 
**bronze_prize_quantity** | **str** |  | [optional] 
**pnl_condition** | **str** |  | [optional] 
**total_volume_condition** | **str** |  | [optional] 
**avg_daily_volume_condition** | **str** |  | [optional] 
**minimum_equity_percentage_condition** | **int** |  | [optional] 
**users** | **List[UUID]** |  | [optional] 

## Example

```python
from dora_client.models.create_trading_challenge_request import CreateTradingChallengeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTradingChallengeRequest from a JSON string
create_trading_challenge_request_instance = CreateTradingChallengeRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTradingChallengeRequest.to_json())

# convert the object into a dict
create_trading_challenge_request_dict = create_trading_challenge_request_instance.to_dict()
# create an instance of CreateTradingChallengeRequest from a dict
create_trading_challenge_request_from_dict = CreateTradingChallengeRequest.from_dict(create_trading_challenge_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


