# UpdateUserKYCResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UpdateUserKYCResponse**](UpdateUserKYCResponse.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.update_user_kyc_response_envelope import UpdateUserKYCResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserKYCResponseEnvelope from a JSON string
update_user_kyc_response_envelope_instance = UpdateUserKYCResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(UpdateUserKYCResponseEnvelope.to_json())

# convert the object into a dict
update_user_kyc_response_envelope_dict = update_user_kyc_response_envelope_instance.to_dict()
# create an instance of UpdateUserKYCResponseEnvelope from a dict
update_user_kyc_response_envelope_from_dict = UpdateUserKYCResponseEnvelope.from_dict(update_user_kyc_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


