# ClaimLeverageAccruedInterestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** |  | 
**position_id** | **str** |  | 

## Example

```python
from dora_client.models.claim_leverage_accrued_interest_request import ClaimLeverageAccruedInterestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClaimLeverageAccruedInterestRequest from a JSON string
claim_leverage_accrued_interest_request_instance = ClaimLeverageAccruedInterestRequest.from_json(json)
# print the JSON string representation of the object
print(ClaimLeverageAccruedInterestRequest.to_json())

# convert the object into a dict
claim_leverage_accrued_interest_request_dict = claim_leverage_accrued_interest_request_instance.to_dict()
# create an instance of ClaimLeverageAccruedInterestRequest from a dict
claim_leverage_accrued_interest_request_from_dict = ClaimLeverageAccruedInterestRequest.from_dict(claim_leverage_accrued_interest_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


