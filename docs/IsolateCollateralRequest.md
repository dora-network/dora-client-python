# IsolateCollateralRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_position_id** | **UUID** |  | 
**asset_id** | **UUID** |  | 
**quantity** | **str** |  | 

## Example

```python
from dora_client.models.isolate_collateral_request import IsolateCollateralRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IsolateCollateralRequest from a JSON string
isolate_collateral_request_instance = IsolateCollateralRequest.from_json(json)
# print the JSON string representation of the object
print(IsolateCollateralRequest.to_json())

# convert the object into a dict
isolate_collateral_request_dict = isolate_collateral_request_instance.to_dict()
# create an instance of IsolateCollateralRequest from a dict
isolate_collateral_request_from_dict = IsolateCollateralRequest.from_dict(isolate_collateral_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


