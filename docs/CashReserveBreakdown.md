# CashReserveBreakdown

Breakdown of the minimum USD cash reserve requirement.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed_pac** | **str** | Completed PAC (partially accrued coupon) obligations the user owes, in USD. | 
**outstanding_lai** | **str** | Outstanding LAI (leverage accrued interest) the user owes, in USD. | 
**estimated_fees** | **str** | Estimated trading fees for the current settlement period, capped at a configured fraction (1% by default) of the user&#39;s traded USD volume since 00:00:00 UTC. | 
**borrowed_portion** | **str** | Configured fraction (10% by default) of the user&#39;s total outstanding borrowed value, in USD. | 
**floor** | **str** | Configured absolute minimum requirement, in USD. | 
**total** | **str** | The amount of USD the user must keep available in their Global Account. | 

## Example

```python
from dora_client.models.cash_reserve_breakdown import CashReserveBreakdown

# TODO update the JSON string below
json = "{}"
# create an instance of CashReserveBreakdown from a JSON string
cash_reserve_breakdown_instance = CashReserveBreakdown.from_json(json)
# print the JSON string representation of the object
print(CashReserveBreakdown.to_json())

# convert the object into a dict
cash_reserve_breakdown_dict = cash_reserve_breakdown_instance.to_dict()
# create an instance of CashReserveBreakdown from a dict
cash_reserve_breakdown_from_dict = CashReserveBreakdown.from_dict(cash_reserve_breakdown_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


