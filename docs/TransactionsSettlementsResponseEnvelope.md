# TransactionsSettlementsResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TransactionsSettlementsResponse**](TransactionsSettlementsResponse.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.transactions_settlements_response_envelope import TransactionsSettlementsResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionsSettlementsResponseEnvelope from a JSON string
transactions_settlements_response_envelope_instance = TransactionsSettlementsResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(TransactionsSettlementsResponseEnvelope.to_json())

# convert the object into a dict
transactions_settlements_response_envelope_dict = transactions_settlements_response_envelope_instance.to_dict()
# create an instance of TransactionsSettlementsResponseEnvelope from a dict
transactions_settlements_response_envelope_from_dict = TransactionsSettlementsResponseEnvelope.from_dict(transactions_settlements_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


