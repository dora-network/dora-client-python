# Asset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**collateral_weight** | **float** |  | 
**created_at** | **datetime** |  | 
**decimals** | **int** |  | 
**fractionalized_units** | **int** |  | 
**description** | **str** |  | 
**liquidation_weight** | **float** |  | 
**max_supply** | **int** |  | 
**max_utilization** | **int** |  | 
**name** | **str** |  | 
**symbol** | **str** |  | 
**kind** | [**AssetKind**](AssetKind.md) |  | 
**var_yield** | **float** |  | [optional] 
**can_add_liquidity** | **bool** |  | 
**can_direct_borrow** | **bool** |  | 
**can_onboard** | **bool** |  | 
**can_trade** | **bool** |  | 
**can_virtual_borrow** | **bool** |  | 
**max_leverage** | **float** |  | 
**leverage_interest_rate** | **float** |  | [optional] [default to 0]
**bond** | [**Bond**](Bond.md) |  | [optional] 

## Example

```python
from dora_client.models.asset import Asset

# TODO update the JSON string below
json = "{}"
# create an instance of Asset from a JSON string
asset_instance = Asset.from_json(json)
# print the JSON string representation of the object
print(Asset.to_json())

# convert the object into a dict
asset_dict = asset_instance.to_dict()
# create an instance of Asset from a dict
asset_from_dict = Asset.from_dict(asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


