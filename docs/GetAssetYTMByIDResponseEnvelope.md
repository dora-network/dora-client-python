# GetAssetYTMByIDResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AssetYTM**](AssetYTM.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.get_asset_ytmby_id_response_envelope import GetAssetYTMByIDResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of GetAssetYTMByIDResponseEnvelope from a JSON string
get_asset_ytmby_id_response_envelope_instance = GetAssetYTMByIDResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(GetAssetYTMByIDResponseEnvelope.to_json())

# convert the object into a dict
get_asset_ytmby_id_response_envelope_dict = get_asset_ytmby_id_response_envelope_instance.to_dict()
# create an instance of GetAssetYTMByIDResponseEnvelope from a dict
get_asset_ytmby_id_response_envelope_from_dict = GetAssetYTMByIDResponseEnvelope.from_dict(get_asset_ytmby_id_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


