# UpsertAutoRebalanceConfigsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configs** | [**List[AutoRebalanceConfigUpsert]**](AutoRebalanceConfigUpsert.md) |  | 

## Example

```python
from dora_client.models.upsert_auto_rebalance_configs_request import UpsertAutoRebalanceConfigsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertAutoRebalanceConfigsRequest from a JSON string
upsert_auto_rebalance_configs_request_instance = UpsertAutoRebalanceConfigsRequest.from_json(json)
# print the JSON string representation of the object
print(UpsertAutoRebalanceConfigsRequest.to_json())

# convert the object into a dict
upsert_auto_rebalance_configs_request_dict = upsert_auto_rebalance_configs_request_instance.to_dict()
# create an instance of UpsertAutoRebalanceConfigsRequest from a dict
upsert_auto_rebalance_configs_request_from_dict = UpsertAutoRebalanceConfigsRequest.from_dict(upsert_auto_rebalance_configs_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


