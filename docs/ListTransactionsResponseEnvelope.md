# ListTransactionsResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Transaction]**](Transaction.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.list_transactions_response_envelope import ListTransactionsResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListTransactionsResponseEnvelope from a JSON string
list_transactions_response_envelope_instance = ListTransactionsResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(ListTransactionsResponseEnvelope.to_json())

# convert the object into a dict
list_transactions_response_envelope_dict = list_transactions_response_envelope_instance.to_dict()
# create an instance of ListTransactionsResponseEnvelope from a dict
list_transactions_response_envelope_from_dict = ListTransactionsResponseEnvelope.from_dict(list_transactions_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


