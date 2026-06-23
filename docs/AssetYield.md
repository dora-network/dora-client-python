# AssetYield


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **UUID** |  | 
**timestamp** | **datetime** |  | 
**ytm** | **str** |  | 
**borrowing_yield_rate** | **str** |  | 
**lending_yield_rate** | **str** |  | 
**price** | **str** |  | 
**tvl** | **str** |  | 
**total_yield** | **str** |  | 

## Example

```python
from dora_client.models.asset_yield import AssetYield

# TODO update the JSON string below
json = "{}"
# create an instance of AssetYield from a JSON string
asset_yield_instance = AssetYield.from_json(json)
# print the JSON string representation of the object
print(AssetYield.to_json())

# convert the object into a dict
asset_yield_dict = asset_yield_instance.to_dict()
# create an instance of AssetYield from a dict
asset_yield_from_dict = AssetYield.from_dict(asset_yield_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


