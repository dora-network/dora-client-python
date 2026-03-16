# ClaimLeverageAccruedInterestResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClaimLeverageAccruedInterest**](ClaimLeverageAccruedInterest.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.claim_leverage_accrued_interest_response_envelope import ClaimLeverageAccruedInterestResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ClaimLeverageAccruedInterestResponseEnvelope from a JSON string
claim_leverage_accrued_interest_response_envelope_instance = ClaimLeverageAccruedInterestResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(ClaimLeverageAccruedInterestResponseEnvelope.to_json())

# convert the object into a dict
claim_leverage_accrued_interest_response_envelope_dict = claim_leverage_accrued_interest_response_envelope_instance.to_dict()
# create an instance of ClaimLeverageAccruedInterestResponseEnvelope from a dict
claim_leverage_accrued_interest_response_envelope_from_dict = ClaimLeverageAccruedInterestResponseEnvelope.from_dict(claim_leverage_accrued_interest_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


