# AssetYTM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** |  | 
**current_time** | **datetime** |  | 
**current_price** | **str** |  | 
**yield_to_maturity** | **str** |  | 

## Example

```python
from dora_client.models.asset_ytm import AssetYTM

# TODO update the JSON string below
json = "{}"
# create an instance of AssetYTM from a JSON string
asset_ytm_instance = AssetYTM.from_json(json)
# print the JSON string representation of the object
print(AssetYTM.to_json())

# convert the object into a dict
asset_ytm_dict = asset_ytm_instance.to_dict()
# create an instance of AssetYTM from a dict
asset_ytm_from_dict = AssetYTM.from_dict(asset_ytm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


