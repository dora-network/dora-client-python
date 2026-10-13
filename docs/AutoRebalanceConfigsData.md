# AutoRebalanceConfigsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configs** | [**List[AutoRebalanceConfigStatus]**](AutoRebalanceConfigStatus.md) |  | 

## Example

```python
from dora_client.models.auto_rebalance_configs_data import AutoRebalanceConfigsData

# TODO update the JSON string below
json = "{}"
# create an instance of AutoRebalanceConfigsData from a JSON string
auto_rebalance_configs_data_instance = AutoRebalanceConfigsData.from_json(json)
# print the JSON string representation of the object
print(AutoRebalanceConfigsData.to_json())

# convert the object into a dict
auto_rebalance_configs_data_dict = auto_rebalance_configs_data_instance.to_dict()
# create an instance of AutoRebalanceConfigsData from a dict
auto_rebalance_configs_data_from_dict = AutoRebalanceConfigsData.from_dict(auto_rebalance_configs_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


