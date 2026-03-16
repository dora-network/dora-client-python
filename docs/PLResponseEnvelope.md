# PLResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PLAccount]**](PLAccount.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.pl_response_envelope import PLResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of PLResponseEnvelope from a JSON string
pl_response_envelope_instance = PLResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(PLResponseEnvelope.to_json())

# convert the object into a dict
pl_response_envelope_dict = pl_response_envelope_instance.to_dict()
# create an instance of PLResponseEnvelope from a dict
pl_response_envelope_from_dict = PLResponseEnvelope.from_dict(pl_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


