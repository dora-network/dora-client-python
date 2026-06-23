# PoolPrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool_id** | **UUID** |  | 
**price** | **str** |  | 
**timestamp** | **datetime** |  | 

## Example

```python
from dora_client.models.pool_price import PoolPrice

# TODO update the JSON string below
json = "{}"
# create an instance of PoolPrice from a JSON string
pool_price_instance = PoolPrice.from_json(json)
# print the JSON string representation of the object
print(PoolPrice.to_json())

# convert the object into a dict
pool_price_dict = pool_price_instance.to_dict()
# create an instance of PoolPrice from a dict
pool_price_from_dict = PoolPrice.from_dict(pool_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


