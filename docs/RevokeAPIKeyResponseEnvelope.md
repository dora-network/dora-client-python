# RevokeAPIKeyResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**RevokeAPIKeyData**](RevokeAPIKeyData.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.revoke_api_key_response_envelope import RevokeAPIKeyResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of RevokeAPIKeyResponseEnvelope from a JSON string
revoke_api_key_response_envelope_instance = RevokeAPIKeyResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(RevokeAPIKeyResponseEnvelope.to_json())

# convert the object into a dict
revoke_api_key_response_envelope_dict = revoke_api_key_response_envelope_instance.to_dict()
# create an instance of RevokeAPIKeyResponseEnvelope from a dict
revoke_api_key_response_envelope_from_dict = RevokeAPIKeyResponseEnvelope.from_dict(revoke_api_key_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


