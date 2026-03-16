# PayLeverageAccruedInterest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** |  | 
**asset_id** | **str** |  | 
**position_id** | **str** |  | 
**current_accrued_interest_usd** | **str** |  | 

## Example

```python
from dora_client.models.pay_leverage_accrued_interest import PayLeverageAccruedInterest

# TODO update the JSON string below
json = "{}"
# create an instance of PayLeverageAccruedInterest from a JSON string
pay_leverage_accrued_interest_instance = PayLeverageAccruedInterest.from_json(json)
# print the JSON string representation of the object
print(PayLeverageAccruedInterest.to_json())

# convert the object into a dict
pay_leverage_accrued_interest_dict = pay_leverage_accrued_interest_instance.to_dict()
# create an instance of PayLeverageAccruedInterest from a dict
pay_leverage_accrued_interest_from_dict = PayLeverageAccruedInterest.from_dict(pay_leverage_accrued_interest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


