# SettleLeverageAccruedInterest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **UUID** |  | 
**asset_id** | **UUID** |  | 
**position_id** | **UUID** |  | 
**current_accrued_interest_usd** | **str** |  | 

## Example

```python
from dora_client.models.settle_leverage_accrued_interest import SettleLeverageAccruedInterest

# TODO update the JSON string below
json = "{}"
# create an instance of SettleLeverageAccruedInterest from a JSON string
settle_leverage_accrued_interest_instance = SettleLeverageAccruedInterest.from_json(json)
# print the JSON string representation of the object
print(SettleLeverageAccruedInterest.to_json())

# convert the object into a dict
settle_leverage_accrued_interest_dict = settle_leverage_accrued_interest_instance.to_dict()
# create an instance of SettleLeverageAccruedInterest from a dict
settle_leverage_accrued_interest_from_dict = SettleLeverageAccruedInterest.from_dict(settle_leverage_accrued_interest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


