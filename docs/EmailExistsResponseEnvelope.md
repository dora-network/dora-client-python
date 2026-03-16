# EmailExistsResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserExistsResponse**](UserExistsResponse.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.email_exists_response_envelope import EmailExistsResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of EmailExistsResponseEnvelope from a JSON string
email_exists_response_envelope_instance = EmailExistsResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(EmailExistsResponseEnvelope.to_json())

# convert the object into a dict
email_exists_response_envelope_dict = email_exists_response_envelope_instance.to_dict()
# create an instance of EmailExistsResponseEnvelope from a dict
email_exists_response_envelope_from_dict = EmailExistsResponseEnvelope.from_dict(email_exists_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


