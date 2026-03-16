# Collateral


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position_id** | **str** |  | 
**transaction_id** | **str** |  | 
**asset_id** | **str** |  | 
**quantity** | **str** |  | 

## Example

```python
from dora_client.models.collateral import Collateral

# TODO update the JSON string below
json = "{}"
# create an instance of Collateral from a JSON string
collateral_instance = Collateral.from_json(json)
# print the JSON string representation of the object
print(Collateral.to_json())

# convert the object into a dict
collateral_dict = collateral_instance.to_dict()
# create an instance of Collateral from a dict
collateral_from_dict = Collateral.from_dict(collateral_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


