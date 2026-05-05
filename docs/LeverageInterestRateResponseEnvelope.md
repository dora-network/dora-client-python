# LeverageInterestRateResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**LeverageInterestRate**](LeverageInterestRate.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.leverage_interest_rate_response_envelope import LeverageInterestRateResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of LeverageInterestRateResponseEnvelope from a JSON string
leverage_interest_rate_response_envelope_instance = LeverageInterestRateResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(LeverageInterestRateResponseEnvelope.to_json())

# convert the object into a dict
leverage_interest_rate_response_envelope_dict = leverage_interest_rate_response_envelope_instance.to_dict()
# create an instance of LeverageInterestRateResponseEnvelope from a dict
leverage_interest_rate_response_envelope_from_dict = LeverageInterestRateResponseEnvelope.from_dict(leverage_interest_rate_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


