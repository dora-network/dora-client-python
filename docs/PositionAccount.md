# PositionAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position_id** | **UUID** | The ID of the position account | 
**position_name** | **str** | The name of the position account | 
**is_global** | **bool** | Whether the position account is the global or an isolated account | 

## Example

```python
from dora_client.models.position_account import PositionAccount

# TODO update the JSON string below
json = "{}"
# create an instance of PositionAccount from a JSON string
position_account_instance = PositionAccount.from_json(json)
# print the JSON string representation of the object
print(PositionAccount.to_json())

# convert the object into a dict
position_account_dict = position_account_instance.to_dict()
# create an instance of PositionAccount from a dict
position_account_from_dict = PositionAccount.from_dict(position_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


