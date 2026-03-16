# LeverageModuleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balances** | [**Dict[str, ModuleBalance]**](ModuleBalance.md) | A map of asset IDs to their module balances | 

## Example

```python
from dora_client.models.leverage_module_response import LeverageModuleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LeverageModuleResponse from a JSON string
leverage_module_response_instance = LeverageModuleResponse.from_json(json)
# print the JSON string representation of the object
print(LeverageModuleResponse.to_json())

# convert the object into a dict
leverage_module_response_dict = leverage_module_response_instance.to_dict()
# create an instance of LeverageModuleResponse from a dict
leverage_module_response_from_dict = LeverageModuleResponse.from_dict(leverage_module_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


