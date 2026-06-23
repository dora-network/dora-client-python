# PayLeverageAccruedInterestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **UUID** |  | 
**position_id** | **UUID** |  | 

## Example

```python
from dora_client.models.pay_leverage_accrued_interest_request import PayLeverageAccruedInterestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PayLeverageAccruedInterestRequest from a JSON string
pay_leverage_accrued_interest_request_instance = PayLeverageAccruedInterestRequest.from_json(json)
# print the JSON string representation of the object
print(PayLeverageAccruedInterestRequest.to_json())

# convert the object into a dict
pay_leverage_accrued_interest_request_dict = pay_leverage_accrued_interest_request_instance.to_dict()
# create an instance of PayLeverageAccruedInterestRequest from a dict
pay_leverage_accrued_interest_request_from_dict = PayLeverageAccruedInterestRequest.from_dict(pay_leverage_accrued_interest_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


