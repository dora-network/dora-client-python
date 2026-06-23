# SettleLeverageAccruedInterestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **UUID** |  | [optional] 
**position_id** | **UUID** |  | [optional] 

## Example

```python
from dora_client.models.settle_leverage_accrued_interest_request import SettleLeverageAccruedInterestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SettleLeverageAccruedInterestRequest from a JSON string
settle_leverage_accrued_interest_request_instance = SettleLeverageAccruedInterestRequest.from_json(json)
# print the JSON string representation of the object
print(SettleLeverageAccruedInterestRequest.to_json())

# convert the object into a dict
settle_leverage_accrued_interest_request_dict = settle_leverage_accrued_interest_request_instance.to_dict()
# create an instance of SettleLeverageAccruedInterestRequest from a dict
settle_leverage_accrued_interest_request_from_dict = SettleLeverageAccruedInterestRequest.from_dict(settle_leverage_accrued_interest_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


