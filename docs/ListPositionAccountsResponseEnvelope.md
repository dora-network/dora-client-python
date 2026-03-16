# ListPositionAccountsResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PositionAccount]**](PositionAccount.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.list_position_accounts_response_envelope import ListPositionAccountsResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListPositionAccountsResponseEnvelope from a JSON string
list_position_accounts_response_envelope_instance = ListPositionAccountsResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(ListPositionAccountsResponseEnvelope.to_json())

# convert the object into a dict
list_position_accounts_response_envelope_dict = list_position_accounts_response_envelope_instance.to_dict()
# create an instance of ListPositionAccountsResponseEnvelope from a dict
list_position_accounts_response_envelope_from_dict = ListPositionAccountsResponseEnvelope.from_dict(list_position_accounts_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


