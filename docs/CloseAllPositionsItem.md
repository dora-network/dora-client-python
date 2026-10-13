# CloseAllPositionsItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **UUID** |  | 
**order_id** | **UUID** |  | 

## Example

```python
from dora_client.models.close_all_positions_item import CloseAllPositionsItem

# TODO update the JSON string below
json = "{}"
# create an instance of CloseAllPositionsItem from a JSON string
close_all_positions_item_instance = CloseAllPositionsItem.from_json(json)
# print the JSON string representation of the object
print(CloseAllPositionsItem.to_json())

# convert the object into a dict
close_all_positions_item_dict = close_all_positions_item_instance.to_dict()
# create an instance of CloseAllPositionsItem from a dict
close_all_positions_item_from_dict = CloseAllPositionsItem.from_dict(close_all_positions_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


