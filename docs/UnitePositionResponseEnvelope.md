# UnitePositionResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UnitedPosition**](UnitedPosition.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.unite_position_response_envelope import UnitePositionResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of UnitePositionResponseEnvelope from a JSON string
unite_position_response_envelope_instance = UnitePositionResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(UnitePositionResponseEnvelope.to_json())

# convert the object into a dict
unite_position_response_envelope_dict = unite_position_response_envelope_instance.to_dict()
# create an instance of UnitePositionResponseEnvelope from a dict
unite_position_response_envelope_from_dict = UnitePositionResponseEnvelope.from_dict(unite_position_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


