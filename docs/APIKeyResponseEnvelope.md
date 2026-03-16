# APIKeyResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**APIKeys**](APIKeys.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.api_key_response_envelope import APIKeyResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of APIKeyResponseEnvelope from a JSON string
api_key_response_envelope_instance = APIKeyResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(APIKeyResponseEnvelope.to_json())

# convert the object into a dict
api_key_response_envelope_dict = api_key_response_envelope_instance.to_dict()
# create an instance of APIKeyResponseEnvelope from a dict
api_key_response_envelope_from_dict = APIKeyResponseEnvelope.from_dict(api_key_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


