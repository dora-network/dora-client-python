# TradingChallengeRegistrationRequest

A user's request to take part in a trading challenge, raised at sign-up and settled by an admin, the tenant's integrator or one of the challenge's managers. Approving it enrols the user; the row is kept after the decision as an audit trail.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**trading_challenge_id** | **UUID** |  | 
**trading_challenge_name** | **str** |  | [optional] 
**trading_challenge_type** | **str** |  | [optional] 
**trading_challenge_status** | **str** |  | [optional] 
**user_id** | **UUID** |  | 
**user_email** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 
**tenant_id** | **str** |  | 
**status** | **str** |  | 
**reviewed_by** | **UUID** | Who settled the request. Absent while it is PENDING. | [optional] 
**reviewed_at** | **datetime** | When it was settled. Absent while it is PENDING. | [optional] 
**review_reason** | **str** | Free-text note kept for the audit trail. Optional on both decisions. | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from dora_client.models.trading_challenge_registration_request import TradingChallengeRegistrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TradingChallengeRegistrationRequest from a JSON string
trading_challenge_registration_request_instance = TradingChallengeRegistrationRequest.from_json(json)
# print the JSON string representation of the object
print(TradingChallengeRegistrationRequest.to_json())

# convert the object into a dict
trading_challenge_registration_request_dict = trading_challenge_registration_request_instance.to_dict()
# create an instance of TradingChallengeRegistrationRequest from a dict
trading_challenge_registration_request_from_dict = TradingChallengeRegistrationRequest.from_dict(trading_challenge_registration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


