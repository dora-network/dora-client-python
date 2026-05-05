# NewIsolatedAccountResponseV2Envelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AccountV2**](AccountV2.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.new_isolated_account_response_v2_envelope import NewIsolatedAccountResponseV2Envelope

# TODO update the JSON string below
json = "{}"
# create an instance of NewIsolatedAccountResponseV2Envelope from a JSON string
new_isolated_account_response_v2_envelope_instance = NewIsolatedAccountResponseV2Envelope.from_json(json)
# print the JSON string representation of the object
print(NewIsolatedAccountResponseV2Envelope.to_json())

# convert the object into a dict
new_isolated_account_response_v2_envelope_dict = new_isolated_account_response_v2_envelope_instance.to_dict()
# create an instance of NewIsolatedAccountResponseV2Envelope from a dict
new_isolated_account_response_v2_envelope_from_dict = NewIsolatedAccountResponseV2Envelope.from_dict(new_isolated_account_response_v2_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


