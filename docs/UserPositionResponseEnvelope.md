# UserPositionResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PositionResponse**](PositionResponse.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.user_position_response_envelope import UserPositionResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of UserPositionResponseEnvelope from a JSON string
user_position_response_envelope_instance = UserPositionResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(UserPositionResponseEnvelope.to_json())

# convert the object into a dict
user_position_response_envelope_dict = user_position_response_envelope_instance.to_dict()
# create an instance of UserPositionResponseEnvelope from a dict
user_position_response_envelope_from_dict = UserPositionResponseEnvelope.from_dict(user_position_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


