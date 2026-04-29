# StreamCurrentLeverageAccruedInterestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_leverage_accrued_interest** | [**List[CurrentLeverageAccruedInterest]**](CurrentLeverageAccruedInterest.md) |  | [optional] 

## Example

```python
from dora_client.models.stream_current_leverage_accrued_interest_response import StreamCurrentLeverageAccruedInterestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StreamCurrentLeverageAccruedInterestResponse from a JSON string
stream_current_leverage_accrued_interest_response_instance = StreamCurrentLeverageAccruedInterestResponse.from_json(json)
# print the JSON string representation of the object
print(StreamCurrentLeverageAccruedInterestResponse.to_json())

# convert the object into a dict
stream_current_leverage_accrued_interest_response_dict = stream_current_leverage_accrued_interest_response_instance.to_dict()
# create an instance of StreamCurrentLeverageAccruedInterestResponse from a dict
stream_current_leverage_accrued_interest_response_from_dict = StreamCurrentLeverageAccruedInterestResponse.from_dict(stream_current_leverage_accrued_interest_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


