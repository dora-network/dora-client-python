# AssetPriceResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AssetPrice**](AssetPrice.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.asset_price_response_envelope import AssetPriceResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of AssetPriceResponseEnvelope from a JSON string
asset_price_response_envelope_instance = AssetPriceResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(AssetPriceResponseEnvelope.to_json())

# convert the object into a dict
asset_price_response_envelope_dict = asset_price_response_envelope_instance.to_dict()
# create an instance of AssetPriceResponseEnvelope from a dict
asset_price_response_envelope_from_dict = AssetPriceResponseEnvelope.from_dict(asset_price_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


