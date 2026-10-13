# CloseAllPositionsResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CloseAllPositionsItem]**](CloseAllPositionsItem.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.close_all_positions_response_envelope import CloseAllPositionsResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of CloseAllPositionsResponseEnvelope from a JSON string
close_all_positions_response_envelope_instance = CloseAllPositionsResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(CloseAllPositionsResponseEnvelope.to_json())

# convert the object into a dict
close_all_positions_response_envelope_dict = close_all_positions_response_envelope_instance.to_dict()
# create an instance of CloseAllPositionsResponseEnvelope from a dict
close_all_positions_response_envelope_from_dict = CloseAllPositionsResponseEnvelope.from_dict(close_all_positions_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


