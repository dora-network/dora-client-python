# PositionAsset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** |  | 
**kind** | [**AssetKind**](AssetKind.md) |  | 
**borrowed** | **str** |  | 
**impending_borrows** | **str** |  | 
**available** | **str** |  | 
**locked** | **str** |  | 

## Example

```python
from dora_client.models.position_asset import PositionAsset

# TODO update the JSON string below
json = "{}"
# create an instance of PositionAsset from a JSON string
position_asset_instance = PositionAsset.from_json(json)
# print the JSON string representation of the object
print(PositionAsset.to_json())

# convert the object into a dict
position_asset_dict = position_asset_instance.to_dict()
# create an instance of PositionAsset from a dict
position_asset_from_dict = PositionAsset.from_dict(position_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


