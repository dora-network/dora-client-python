# RemoveTradingChallengeUsersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trading_challenge_id** | **UUID** |  | 
**users** | **List[UUID]** |  | 

## Example

```python
from dora_client.models.remove_trading_challenge_users_request import RemoveTradingChallengeUsersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveTradingChallengeUsersRequest from a JSON string
remove_trading_challenge_users_request_instance = RemoveTradingChallengeUsersRequest.from_json(json)
# print the JSON string representation of the object
print(RemoveTradingChallengeUsersRequest.to_json())

# convert the object into a dict
remove_trading_challenge_users_request_dict = remove_trading_challenge_users_request_instance.to_dict()
# create an instance of RemoveTradingChallengeUsersRequest from a dict
remove_trading_challenge_users_request_from_dict = RemoveTradingChallengeUsersRequest.from_dict(remove_trading_challenge_users_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


