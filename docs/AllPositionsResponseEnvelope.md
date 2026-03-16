# AllPositionsResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AllPositions**](AllPositions.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.all_positions_response_envelope import AllPositionsResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of AllPositionsResponseEnvelope from a JSON string
all_positions_response_envelope_instance = AllPositionsResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(AllPositionsResponseEnvelope.to_json())

# convert the object into a dict
all_positions_response_envelope_dict = all_positions_response_envelope_instance.to_dict()
# create an instance of AllPositionsResponseEnvelope from a dict
all_positions_response_envelope_from_dict = AllPositionsResponseEnvelope.from_dict(all_positions_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


