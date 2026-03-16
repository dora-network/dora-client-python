# TransactionResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Transaction**](Transaction.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.transaction_response_envelope import TransactionResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionResponseEnvelope from a JSON string
transaction_response_envelope_instance = TransactionResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(TransactionResponseEnvelope.to_json())

# convert the object into a dict
transaction_response_envelope_dict = transaction_response_envelope_instance.to_dict()
# create an instance of TransactionResponseEnvelope from a dict
transaction_response_envelope_from_dict = TransactionResponseEnvelope.from_dict(transaction_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


