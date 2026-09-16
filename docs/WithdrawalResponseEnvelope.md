# WithdrawalResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**WithdrawalResponse**](WithdrawalResponse.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.withdrawal_response_envelope import WithdrawalResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of WithdrawalResponseEnvelope from a JSON string
withdrawal_response_envelope_instance = WithdrawalResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(WithdrawalResponseEnvelope.to_json())

# convert the object into a dict
withdrawal_response_envelope_dict = withdrawal_response_envelope_instance.to_dict()
# create an instance of WithdrawalResponseEnvelope from a dict
withdrawal_response_envelope_from_dict = WithdrawalResponseEnvelope.from_dict(withdrawal_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


