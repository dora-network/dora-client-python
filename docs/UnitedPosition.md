# UnitedPosition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_position_id** | **str** |  | 
**transaction_ids** | **List[str]** |  | [optional] 

## Example

```python
from dora_client.models.united_position import UnitedPosition

# TODO update the JSON string below
json = "{}"
# create an instance of UnitedPosition from a JSON string
united_position_instance = UnitedPosition.from_json(json)
# print the JSON string representation of the object
print(UnitedPosition.to_json())

# convert the object into a dict
united_position_dict = united_position_instance.to_dict()
# create an instance of UnitedPosition from a dict
united_position_from_dict = UnitedPosition.from_dict(united_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


