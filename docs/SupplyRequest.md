# SupplyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position_id** | **str** |  | 
**asset_id** | **str** |  | 
**quantity** | **str** |  | 

## Example

```python
from dora_client.models.supply_request import SupplyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SupplyRequest from a JSON string
supply_request_instance = SupplyRequest.from_json(json)
# print the JSON string representation of the object
print(SupplyRequest.to_json())

# convert the object into a dict
supply_request_dict = supply_request_instance.to_dict()
# create an instance of SupplyRequest from a dict
supply_request_from_dict = SupplyRequest.from_dict(supply_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


