# AssetConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **UUID** |  | 
**price** | **str** | if an asset is a CURRENCY, set 1 USD price,If an asset is a BOND and the price isn&#39;t found, set to 0 USD   You can find price details on /price/asset/{asset_id} route | 
**module_available** | **str** | Optional leverage module available balance for this asset, from /v1/ledger/module/{asset_id}. If provided, validation rejects orders that need to borrow more than the module can supply. | [optional] 
**module_supplied** | **str** | Optional leverage module total supplied balance for this asset, from /v1/ledger/module/{asset_id}. Required with module_available when the asset has max_utilization. | [optional] 
**module_borrowed** | **str** | Optional leverage module borrowed balance for this asset, from /v1/ledger/module/{asset_id}. Required with module_available when the asset has max_utilization. | [optional] 

## Example

```python
from dora_client.models.asset_config import AssetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AssetConfig from a JSON string
asset_config_instance = AssetConfig.from_json(json)
# print the JSON string representation of the object
print(AssetConfig.to_json())

# convert the object into a dict
asset_config_dict = asset_config_instance.to_dict()
# create an instance of AssetConfig from a dict
asset_config_from_dict = AssetConfig.from_dict(asset_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


