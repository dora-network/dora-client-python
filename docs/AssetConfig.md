# AssetConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** |  | 
**price** | **str** | if an asset is a CURRENCY, set 1 USD price,If an asset is a BOND and the price isn&#39;t found, set to 0 USD   You can find price details on /price/asset/{asset_id} route | 

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


