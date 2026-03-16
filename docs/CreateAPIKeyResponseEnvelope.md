# CreateAPIKeyResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateAPIKeyData**](CreateAPIKeyData.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.create_api_key_response_envelope import CreateAPIKeyResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAPIKeyResponseEnvelope from a JSON string
create_api_key_response_envelope_instance = CreateAPIKeyResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(CreateAPIKeyResponseEnvelope.to_json())

# convert the object into a dict
create_api_key_response_envelope_dict = create_api_key_response_envelope_instance.to_dict()
# create an instance of CreateAPIKeyResponseEnvelope from a dict
create_api_key_response_envelope_from_dict = CreateAPIKeyResponseEnvelope.from_dict(create_api_key_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


