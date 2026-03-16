# CouponPayment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**asset_id** | **str** |  | 
**var_yield** | **float** |  | 
**start_at** | **datetime** |  | 
**end_at** | **datetime** |  | 
**pay_at** | **datetime** |  | 
**available_to_pay** | **str** |  | 
**completed_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**process_every** | **int** | Number of nanoseconds to wait between coupon payment processing, must be at least 1000 (1 microsecond) | 
**last_processed_at** | **datetime** |  | 

## Example

```python
from dora_client.models.coupon_payment import CouponPayment

# TODO update the JSON string below
json = "{}"
# create an instance of CouponPayment from a JSON string
coupon_payment_instance = CouponPayment.from_json(json)
# print the JSON string representation of the object
print(CouponPayment.to_json())

# convert the object into a dict
coupon_payment_dict = coupon_payment_instance.to_dict()
# create an instance of CouponPayment from a dict
coupon_payment_from_dict = CouponPayment.from_dict(coupon_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


