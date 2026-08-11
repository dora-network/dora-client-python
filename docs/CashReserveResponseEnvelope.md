# CashReserveResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CashReserveResponse**](CashReserveResponse.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.cash_reserve_response_envelope import CashReserveResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of CashReserveResponseEnvelope from a JSON string
cash_reserve_response_envelope_instance = CashReserveResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(CashReserveResponseEnvelope.to_json())

# convert the object into a dict
cash_reserve_response_envelope_dict = cash_reserve_response_envelope_instance.to_dict()
# create an instance of CashReserveResponseEnvelope from a dict
cash_reserve_response_envelope_from_dict = CashReserveResponseEnvelope.from_dict(cash_reserve_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


