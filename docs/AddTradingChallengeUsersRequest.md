# AddTradingChallengeUsersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trading_challenge_id** | **UUID** |  | 
**users** | **List[UUID]** |  | 

## Example

```python
from dora_client.models.add_trading_challenge_users_request import AddTradingChallengeUsersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddTradingChallengeUsersRequest from a JSON string
add_trading_challenge_users_request_instance = AddTradingChallengeUsersRequest.from_json(json)
# print the JSON string representation of the object
print(AddTradingChallengeUsersRequest.to_json())

# convert the object into a dict
add_trading_challenge_users_request_dict = add_trading_challenge_users_request_instance.to_dict()
# create an instance of AddTradingChallengeUsersRequest from a dict
add_trading_challenge_users_request_from_dict = AddTradingChallengeUsersRequest.from_dict(add_trading_challenge_users_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


