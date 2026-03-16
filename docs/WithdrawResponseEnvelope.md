# WithdrawResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Withdraw**](Withdraw.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.withdraw_response_envelope import WithdrawResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of WithdrawResponseEnvelope from a JSON string
withdraw_response_envelope_instance = WithdrawResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(WithdrawResponseEnvelope.to_json())

# convert the object into a dict
withdraw_response_envelope_dict = withdraw_response_envelope_instance.to_dict()
# create an instance of WithdrawResponseEnvelope from a dict
withdraw_response_envelope_from_dict = WithdrawResponseEnvelope.from_dict(withdraw_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


