# UserValueResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserValue**](UserValue.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.user_value_response_envelope import UserValueResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of UserValueResponseEnvelope from a JSON string
user_value_response_envelope_instance = UserValueResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(UserValueResponseEnvelope.to_json())

# convert the object into a dict
user_value_response_envelope_dict = user_value_response_envelope_instance.to_dict()
# create an instance of UserValueResponseEnvelope from a dict
user_value_response_envelope_from_dict = UserValueResponseEnvelope.from_dict(user_value_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


