# TradingChallengeQR


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_reward_amount** | **str** |  | 
**max_reward_amount** | **str** |  | 
**reward_claim_grace_days** | **int** |  | 
**claimed_links_count** | **int** |  | 
**issued_links_count** | **int** |  | 

## Example

```python
from dora_client.models.trading_challenge_qr import TradingChallengeQR

# TODO update the JSON string below
json = "{}"
# create an instance of TradingChallengeQR from a JSON string
trading_challenge_qr_instance = TradingChallengeQR.from_json(json)
# print the JSON string representation of the object
print(TradingChallengeQR.to_json())

# convert the object into a dict
trading_challenge_qr_dict = trading_challenge_qr_instance.to_dict()
# create an instance of TradingChallengeQR from a dict
trading_challenge_qr_from_dict = TradingChallengeQR.from_dict(trading_challenge_qr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


