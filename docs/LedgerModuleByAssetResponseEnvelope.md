# LedgerModuleByAssetResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ModuleBalance**](ModuleBalance.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.ledger_module_by_asset_response_envelope import LedgerModuleByAssetResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of LedgerModuleByAssetResponseEnvelope from a JSON string
ledger_module_by_asset_response_envelope_instance = LedgerModuleByAssetResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(LedgerModuleByAssetResponseEnvelope.to_json())

# convert the object into a dict
ledger_module_by_asset_response_envelope_dict = ledger_module_by_asset_response_envelope_instance.to_dict()
# create an instance of LedgerModuleByAssetResponseEnvelope from a dict
ledger_module_by_asset_response_envelope_from_dict = LedgerModuleByAssetResponseEnvelope.from_dict(ledger_module_by_asset_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


