# CurrentLeverageAccruedInterest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **UUID** |  | 
**asset_id** | **UUID** |  | 
**position_id** | **UUID** |  | 
**current_accrued_interest_usd** | **str** |  | 
**asset_name** | **str** |  | [optional] 
**asset_symbol** | **str** |  | [optional] 

## Example

```python
from dora_client.models.current_leverage_accrued_interest import CurrentLeverageAccruedInterest

# TODO update the JSON string below
json = "{}"
# create an instance of CurrentLeverageAccruedInterest from a JSON string
current_leverage_accrued_interest_instance = CurrentLeverageAccruedInterest.from_json(json)
# print the JSON string representation of the object
print(CurrentLeverageAccruedInterest.to_json())

# convert the object into a dict
current_leverage_accrued_interest_dict = current_leverage_accrued_interest_instance.to_dict()
# create an instance of CurrentLeverageAccruedInterest from a dict
current_leverage_accrued_interest_from_dict = CurrentLeverageAccruedInterest.from_dict(current_leverage_accrued_interest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


