# PayLeverageAccruedInterestResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PayLeverageAccruedInterest**](PayLeverageAccruedInterest.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.pay_leverage_accrued_interest_response_envelope import PayLeverageAccruedInterestResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of PayLeverageAccruedInterestResponseEnvelope from a JSON string
pay_leverage_accrued_interest_response_envelope_instance = PayLeverageAccruedInterestResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(PayLeverageAccruedInterestResponseEnvelope.to_json())

# convert the object into a dict
pay_leverage_accrued_interest_response_envelope_dict = pay_leverage_accrued_interest_response_envelope_instance.to_dict()
# create an instance of PayLeverageAccruedInterestResponseEnvelope from a dict
pay_leverage_accrued_interest_response_envelope_from_dict = PayLeverageAccruedInterestResponseEnvelope.from_dict(pay_leverage_accrued_interest_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


