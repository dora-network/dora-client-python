# CreateTradingChallengeQRRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_reward_amount** | **str** | Must be greater than zero and greater than initial_user_balance. | 
**max_reward_amount** | **str** | Must be greater than or equal to min_reward_amount. | 
**reward_claim_grace_days** | **int** |  | [optional] [default to 14]

## Example

```python
from dora_client.models.create_trading_challenge_qr_request import CreateTradingChallengeQRRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTradingChallengeQRRequest from a JSON string
create_trading_challenge_qr_request_instance = CreateTradingChallengeQRRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTradingChallengeQRRequest.to_json())

# convert the object into a dict
create_trading_challenge_qr_request_dict = create_trading_challenge_qr_request_instance.to_dict()
# create an instance of CreateTradingChallengeQRRequest from a dict
create_trading_challenge_qr_request_from_dict = CreateTradingChallengeQRRequest.from_dict(create_trading_challenge_qr_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


