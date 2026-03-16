# ResponseEnvelopeOfListAssets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Asset]**](Asset.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.response_envelope_of_list_assets import ResponseEnvelopeOfListAssets

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseEnvelopeOfListAssets from a JSON string
response_envelope_of_list_assets_instance = ResponseEnvelopeOfListAssets.from_json(json)
# print the JSON string representation of the object
print(ResponseEnvelopeOfListAssets.to_json())

# convert the object into a dict
response_envelope_of_list_assets_dict = response_envelope_of_list_assets_instance.to_dict()
# create an instance of ResponseEnvelopeOfListAssets from a dict
response_envelope_of_list_assets_from_dict = ResponseEnvelopeOfListAssets.from_dict(response_envelope_of_list_assets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


