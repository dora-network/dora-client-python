# UserConfigResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserConfig**](UserConfig.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.user_config_response_envelope import UserConfigResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of UserConfigResponseEnvelope from a JSON string
user_config_response_envelope_instance = UserConfigResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(UserConfigResponseEnvelope.to_json())

# convert the object into a dict
user_config_response_envelope_dict = user_config_response_envelope_instance.to_dict()
# create an instance of UserConfigResponseEnvelope from a dict
user_config_response_envelope_from_dict = UserConfigResponseEnvelope.from_dict(user_config_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


