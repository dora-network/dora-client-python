# ClaimTradingChallengeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trading_challenge_id** | **UUID** |  | 
**user_id** | **UUID** |  | 
**status** | **str** |  | 

## Example

```python
from dora_client.models.claim_trading_challenge_response import ClaimTradingChallengeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClaimTradingChallengeResponse from a JSON string
claim_trading_challenge_response_instance = ClaimTradingChallengeResponse.from_json(json)
# print the JSON string representation of the object
print(ClaimTradingChallengeResponse.to_json())

# convert the object into a dict
claim_trading_challenge_response_dict = claim_trading_challenge_response_instance.to_dict()
# create an instance of ClaimTradingChallengeResponse from a dict
claim_trading_challenge_response_from_dict = ClaimTradingChallengeResponse.from_dict(claim_trading_challenge_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


