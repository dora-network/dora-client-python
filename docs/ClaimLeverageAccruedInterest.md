# ClaimLeverageAccruedInterest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **UUID** |  | 
**asset_id** | **UUID** |  | 
**position_id** | **UUID** |  | 
**current_accrued_interest_usd** | **str** |  | 

## Example

```python
from dora_client.models.claim_leverage_accrued_interest import ClaimLeverageAccruedInterest

# TODO update the JSON string below
json = "{}"
# create an instance of ClaimLeverageAccruedInterest from a JSON string
claim_leverage_accrued_interest_instance = ClaimLeverageAccruedInterest.from_json(json)
# print the JSON string representation of the object
print(ClaimLeverageAccruedInterest.to_json())

# convert the object into a dict
claim_leverage_accrued_interest_dict = claim_leverage_accrued_interest_instance.to_dict()
# create an instance of ClaimLeverageAccruedInterest from a dict
claim_leverage_accrued_interest_from_dict = ClaimLeverageAccruedInterest.from_dict(claim_leverage_accrued_interest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


