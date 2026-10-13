# AutoRebalanceConfigUpsert


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **UUID** |  | 
**enabled** | **bool** |  | 
**min_utilization** | **str** | Lower utilization threshold, greater than 0 and less than max_utilization. | 
**max_utilization** | **str** | Upper utilization threshold, greater than min_utilization and less than or equal to 1. | 

## Example

```python
from dora_client.models.auto_rebalance_config_upsert import AutoRebalanceConfigUpsert

# TODO update the JSON string below
json = "{}"
# create an instance of AutoRebalanceConfigUpsert from a JSON string
auto_rebalance_config_upsert_instance = AutoRebalanceConfigUpsert.from_json(json)
# print the JSON string representation of the object
print(AutoRebalanceConfigUpsert.to_json())

# convert the object into a dict
auto_rebalance_config_upsert_dict = auto_rebalance_config_upsert_instance.to_dict()
# create an instance of AutoRebalanceConfigUpsert from a dict
auto_rebalance_config_upsert_from_dict = AutoRebalanceConfigUpsert.from_dict(auto_rebalance_config_upsert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


