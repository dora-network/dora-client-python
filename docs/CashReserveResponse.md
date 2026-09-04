# CashReserveResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enforced** | **bool** | Whether the minimum cash reserve guard is active in this environment. | 
**available_usd** | **str** | The user&#39;s currently available USD balance in their Global Account. | 
**committed_usd** | **str** | USD still counted in available_usd but already claimed by the user&#39;s open market buy orders on the Global Account, which reserve no funds at submission time. The reserve is evaluated against available_usd minus committed_usd. | 
**required_usd** | **str** | The user&#39;s minimum USD cash reserve requirement. | 
**satisfied** | **bool** | Whether available_usd minus committed_usd is at least required_usd. | 
**max_volume_usd** | **str** | How much more traded USD notional the user can add to the current settlement period before the reserve stops being covered, for an order that borrows nothing. Null means the fee leg does not constrain the user, because the guard is disabled or the trading fee volume cap is zero. | 
**max_borrow_usd** | **str** | How much more the user can borrow before the reserve stops being covered, for an order that adds no traded volume. Null means the borrow leg does not constrain the user, because the guard is disabled or the borrowed fraction is zero. The two caps are single axis: a leveraged order consumes both at once and is admissible when notional/max_volume_usd + borrowed/max_borrow_usd &lt;&#x3D; 1. | 
**breakdown** | [**CashReserveBreakdown**](CashReserveBreakdown.md) |  | 

## Example

```python
from dora_client.models.cash_reserve_response import CashReserveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CashReserveResponse from a JSON string
cash_reserve_response_instance = CashReserveResponse.from_json(json)
# print the JSON string representation of the object
print(CashReserveResponse.to_json())

# convert the object into a dict
cash_reserve_response_dict = cash_reserve_response_instance.to_dict()
# create an instance of CashReserveResponse from a dict
cash_reserve_response_from_dict = CashReserveResponse.from_dict(cash_reserve_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


