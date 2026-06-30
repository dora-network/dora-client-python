# Bond


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**kind** | [**CouponKind**](CouponKind.md) |  | 
**coupon_kind** | [**CouponKind**](CouponKind.md) |  | [optional] 
**bond_kind** | [**BondKind**](BondKind.md) |  | [optional] 
**coupon_start_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | 
**final_coupon_at** | **datetime** |  | [optional] 
**isin** | **str** |  | 
**issued_at** | **datetime** |  | 
**issuer** | **str** |  | 
**maturity_at** | **datetime** |  | 
**principal_value** | **str** |  | 
**payments_per_year** | **int** |  | 
**payments_every** | **int** | Coupon payment frequency in nanoseconds (minimum 1000 i.e. 1 microsecond) | [optional] 
**next_coupon_payment** | **datetime** |  | [optional] 

## Example

```python
from dora_client.models.bond import Bond

# TODO update the JSON string below
json = "{}"
# create an instance of Bond from a JSON string
bond_instance = Bond.from_json(json)
# print the JSON string representation of the object
print(Bond.to_json())

# convert the object into a dict
bond_dict = bond_instance.to_dict()
# create an instance of Bond from a dict
bond_from_dict = Bond.from_dict(bond_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


