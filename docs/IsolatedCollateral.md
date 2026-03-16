# IsolatedCollateral


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_position_id** | **str** |  | 
**isolated_position_id** | **str** |  | 
**transaction_id** | **str** |  | 
**asset_id** | **str** |  | 
**quantity** | **str** |  | 

## Example

```python
from dora_client.models.isolated_collateral import IsolatedCollateral

# TODO update the JSON string below
json = "{}"
# create an instance of IsolatedCollateral from a JSON string
isolated_collateral_instance = IsolatedCollateral.from_json(json)
# print the JSON string representation of the object
print(IsolatedCollateral.to_json())

# convert the object into a dict
isolated_collateral_dict = isolated_collateral_instance.to_dict()
# create an instance of IsolatedCollateral from a dict
isolated_collateral_from_dict = IsolatedCollateral.from_dict(isolated_collateral_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


