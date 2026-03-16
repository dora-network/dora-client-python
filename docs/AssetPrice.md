# AssetPrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** |  | 
**price** | **str** |  | 
**ytm** | **str** |  | [optional] 
**time** | **datetime** |  | 

## Example

```python
from dora_client.models.asset_price import AssetPrice

# TODO update the JSON string below
json = "{}"
# create an instance of AssetPrice from a JSON string
asset_price_instance = AssetPrice.from_json(json)
# print the JSON string representation of the object
print(AssetPrice.to_json())

# convert the object into a dict
asset_price_dict = asset_price_instance.to_dict()
# create an instance of AssetPrice from a dict
asset_price_from_dict = AssetPrice.from_dict(asset_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


