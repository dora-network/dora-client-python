# TerminateTradingChallengeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trading_challenge_id** | **UUID** |  | 
**user_id** | **UUID** |  | 
**status** | **str** |  | 

## Example

```python
from dora_client.models.terminate_trading_challenge_response import TerminateTradingChallengeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TerminateTradingChallengeResponse from a JSON string
terminate_trading_challenge_response_instance = TerminateTradingChallengeResponse.from_json(json)
# print the JSON string representation of the object
print(TerminateTradingChallengeResponse.to_json())

# convert the object into a dict
terminate_trading_challenge_response_dict = terminate_trading_challenge_response_instance.to_dict()
# create an instance of TerminateTradingChallengeResponse from a dict
terminate_trading_challenge_response_from_dict = TerminateTradingChallengeResponse.from_dict(terminate_trading_challenge_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


