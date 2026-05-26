# ListAssetYieldResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AssetYield]**](AssetYield.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.list_asset_yield_response_envelope import ListAssetYieldResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListAssetYieldResponseEnvelope from a JSON string
list_asset_yield_response_envelope_instance = ListAssetYieldResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(ListAssetYieldResponseEnvelope.to_json())

# convert the object into a dict
list_asset_yield_response_envelope_dict = list_asset_yield_response_envelope_instance.to_dict()
# create an instance of ListAssetYieldResponseEnvelope from a dict
list_asset_yield_response_envelope_from_dict = ListAssetYieldResponseEnvelope.from_dict(list_asset_yield_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


