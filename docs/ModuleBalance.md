# ModuleBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **UUID** |  | 
**seq** | **int** |  | 
**available** | **str** | The available balance in the module for this asset | 
**supplied** | **str** | The total amount supplied to the module for this asset | 
**virtual** | **str** | Assets minted by virtual-borrowing, but not yet repaid | 
**borrowed** | **str** | The total amount borrowed from the supplied but not yet repaid | 

## Example

```python
from dora_client.models.module_balance import ModuleBalance

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleBalance from a JSON string
module_balance_instance = ModuleBalance.from_json(json)
# print the JSON string representation of the object
print(ModuleBalance.to_json())

# convert the object into a dict
module_balance_dict = module_balance_instance.to_dict()
# create an instance of ModuleBalance from a dict
module_balance_from_dict = ModuleBalance.from_dict(module_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


