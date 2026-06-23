# IsolatedPosition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_position_id** | **UUID** |  | 
**isolated_position_id** | **UUID** |  | 
**transaction_id** | **UUID** |  | 

## Example

```python
from dora_client.models.isolated_position import IsolatedPosition

# TODO update the JSON string below
json = "{}"
# create an instance of IsolatedPosition from a JSON string
isolated_position_instance = IsolatedPosition.from_json(json)
# print the JSON string representation of the object
print(IsolatedPosition.to_json())

# convert the object into a dict
isolated_position_dict = isolated_position_instance.to_dict()
# create an instance of IsolatedPosition from a dict
isolated_position_from_dict = IsolatedPosition.from_dict(isolated_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


