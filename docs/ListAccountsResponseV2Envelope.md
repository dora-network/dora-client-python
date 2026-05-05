# ListAccountsResponseV2Envelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AccountSummaryV2]**](AccountSummaryV2.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.list_accounts_response_v2_envelope import ListAccountsResponseV2Envelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListAccountsResponseV2Envelope from a JSON string
list_accounts_response_v2_envelope_instance = ListAccountsResponseV2Envelope.from_json(json)
# print the JSON string representation of the object
print(ListAccountsResponseV2Envelope.to_json())

# convert the object into a dict
list_accounts_response_v2_envelope_dict = list_accounts_response_v2_envelope_instance.to_dict()
# create an instance of ListAccountsResponseV2Envelope from a dict
list_accounts_response_v2_envelope_from_dict = ListAccountsResponseV2Envelope.from_dict(list_accounts_response_v2_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


