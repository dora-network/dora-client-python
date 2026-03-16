# CurrentLeverageAccruedInterestResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CurrentLeverageAccruedInterest**](CurrentLeverageAccruedInterest.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.current_leverage_accrued_interest_response_envelope import CurrentLeverageAccruedInterestResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of CurrentLeverageAccruedInterestResponseEnvelope from a JSON string
current_leverage_accrued_interest_response_envelope_instance = CurrentLeverageAccruedInterestResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(CurrentLeverageAccruedInterestResponseEnvelope.to_json())

# convert the object into a dict
current_leverage_accrued_interest_response_envelope_dict = current_leverage_accrued_interest_response_envelope_instance.to_dict()
# create an instance of CurrentLeverageAccruedInterestResponseEnvelope from a dict
current_leverage_accrued_interest_response_envelope_from_dict = CurrentLeverageAccruedInterestResponseEnvelope.from_dict(current_leverage_accrued_interest_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


