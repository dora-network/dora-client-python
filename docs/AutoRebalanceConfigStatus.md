# AutoRebalanceConfigStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **UUID** |  | 
**enabled** | **bool** |  | 
**min_utilization** | **str** |  | 
**max_utilization** | **str** |  | 
**available_usd** | **str** |  | [optional] 
**borrowed_value** | **str** |  | [optional] 
**borrow_limit** | **str** |  | [optional] 
**current_utilization** | **str** |  | [optional] 
**above_max** | **bool** | True when current_utilization is greater than max_utilization. | [optional] 
**in_active_liquidation** | **bool** |  | [optional] 
**last_rebalance_outcome** | **str** | Most recent persisted auto-rebalance attempt status for this account, when available. | [optional] 

## Example

```python
from dora_client.models.auto_rebalance_config_status import AutoRebalanceConfigStatus

# TODO update the JSON string below
json = "{}"
# create an instance of AutoRebalanceConfigStatus from a JSON string
auto_rebalance_config_status_instance = AutoRebalanceConfigStatus.from_json(json)
# print the JSON string representation of the object
print(AutoRebalanceConfigStatus.to_json())

# convert the object into a dict
auto_rebalance_config_status_dict = auto_rebalance_config_status_instance.to_dict()
# create an instance of AutoRebalanceConfigStatus from a dict
auto_rebalance_config_status_from_dict = AutoRebalanceConfigStatus.from_dict(auto_rebalance_config_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


