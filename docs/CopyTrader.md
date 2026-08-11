# CopyTrader


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **UUID** |  | 
**user_name** | **str** |  | 

## Example

```python
from dora_client.models.copy_trader import CopyTrader

# TODO update the JSON string below
json = "{}"
# create an instance of CopyTrader from a JSON string
copy_trader_instance = CopyTrader.from_json(json)
# print the JSON string representation of the object
print(CopyTrader.to_json())

# convert the object into a dict
copy_trader_dict = copy_trader_instance.to_dict()
# create an instance of CopyTrader from a dict
copy_trader_from_dict = CopyTrader.from_dict(copy_trader_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


