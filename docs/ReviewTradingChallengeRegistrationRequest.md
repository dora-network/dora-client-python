# ReviewTradingChallengeRegistrationRequest

Body of approve and reject. Optional: an empty body is accepted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Free-text note kept for the audit trail. | [optional] 

## Example

```python
from dora_client.models.review_trading_challenge_registration_request import ReviewTradingChallengeRegistrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewTradingChallengeRegistrationRequest from a JSON string
review_trading_challenge_registration_request_instance = ReviewTradingChallengeRegistrationRequest.from_json(json)
# print the JSON string representation of the object
print(ReviewTradingChallengeRegistrationRequest.to_json())

# convert the object into a dict
review_trading_challenge_registration_request_dict = review_trading_challenge_registration_request_instance.to_dict()
# create an instance of ReviewTradingChallengeRegistrationRequest from a dict
review_trading_challenge_registration_request_from_dict = ReviewTradingChallengeRegistrationRequest.from_dict(review_trading_challenge_registration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


