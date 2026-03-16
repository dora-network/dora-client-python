# SettleLeverageAccruedInterestResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SettleLeverageAccruedInterest]**](SettleLeverageAccruedInterest.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.settle_leverage_accrued_interest_response_envelope import SettleLeverageAccruedInterestResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SettleLeverageAccruedInterestResponseEnvelope from a JSON string
settle_leverage_accrued_interest_response_envelope_instance = SettleLeverageAccruedInterestResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(SettleLeverageAccruedInterestResponseEnvelope.to_json())

# convert the object into a dict
settle_leverage_accrued_interest_response_envelope_dict = settle_leverage_accrued_interest_response_envelope_instance.to_dict()
# create an instance of SettleLeverageAccruedInterestResponseEnvelope from a dict
settle_leverage_accrued_interest_response_envelope_from_dict = SettleLeverageAccruedInterestResponseEnvelope.from_dict(settle_leverage_accrued_interest_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


