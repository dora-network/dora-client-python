# AllWithdrawalInitiationsResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[WithdrawalInitiation]**](WithdrawalInitiation.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.all_withdrawal_initiations_response_envelope import AllWithdrawalInitiationsResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of AllWithdrawalInitiationsResponseEnvelope from a JSON string
all_withdrawal_initiations_response_envelope_instance = AllWithdrawalInitiationsResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(AllWithdrawalInitiationsResponseEnvelope.to_json())

# convert the object into a dict
all_withdrawal_initiations_response_envelope_dict = all_withdrawal_initiations_response_envelope_instance.to_dict()
# create an instance of AllWithdrawalInitiationsResponseEnvelope from a dict
all_withdrawal_initiations_response_envelope_from_dict = AllWithdrawalInitiationsResponseEnvelope.from_dict(all_withdrawal_initiations_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


