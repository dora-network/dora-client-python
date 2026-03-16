# IsolateCollateralResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**IsolatedCollateral**](IsolatedCollateral.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.isolate_collateral_response import IsolateCollateralResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IsolateCollateralResponse from a JSON string
isolate_collateral_response_instance = IsolateCollateralResponse.from_json(json)
# print the JSON string representation of the object
print(IsolateCollateralResponse.to_json())

# convert the object into a dict
isolate_collateral_response_dict = isolate_collateral_response_instance.to_dict()
# create an instance of IsolateCollateralResponse from a dict
isolate_collateral_response_from_dict = IsolateCollateralResponse.from_dict(isolate_collateral_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


