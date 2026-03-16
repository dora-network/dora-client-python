# PLAsset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | The symbol of the asset | 
**side** | **str** | The side of the position (LONG or SHORT) | 
**avg_entry_price** | **str** | The average entry price of the position | 
**mark_price** | **str** | The current mark price for the asset to calculate daily PL. This is usually the close price of the previous day | 
**liquidation_price** | **str** | The liquidation price of the position | 
**available** | **str** | The available quantity in units of the asset | 
**borrowed** | **str** | The borrowed quantity in units of the asset | 
**margin** | [**Margin**](Margin.md) |  | 
**unrealized_pl** | **str** | The unrealized profit or loss of the position | 
**leverage_limit** | **str** | The leverage limit for the position | 
**tp** | **str** | The take profit price set for the position, if any | [optional] 
**sl** | **str** | The stop loss price set for the position, if any | [optional] 
**initial_capital** | **str** | The initial capital of the position | 
**impending_borrows** | **str** | The impending borrows of the position | [optional] 
**locked** | **str** | The locked amount of the position | 
**unused_collateral** | **str** | The unused collateral of the position | 

## Example

```python
from dora_client.models.pl_asset import PLAsset

# TODO update the JSON string below
json = "{}"
# create an instance of PLAsset from a JSON string
pl_asset_instance = PLAsset.from_json(json)
# print the JSON string representation of the object
print(PLAsset.to_json())

# convert the object into a dict
pl_asset_dict = pl_asset_instance.to_dict()
# create an instance of PLAsset from a dict
pl_asset_from_dict = PLAsset.from_dict(pl_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


