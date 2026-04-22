# UserCouponPayment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**position_id** | **str** |  | 
**asset_id** | **str** |  | 
**coupon_payment_id** | **str** |  | 
**seq** | **int** |  | 
**pending** | **str** |  | 
**completed** | **str** |  | 
**started_at** | **datetime** |  | 
**ended_at** | **datetime** |  | 
**transaction_id** | **str** |  | [optional] 

## Example

```python
from dora_client.models.user_coupon_payment import UserCouponPayment

# TODO update the JSON string below
json = "{}"
# create an instance of UserCouponPayment from a JSON string
user_coupon_payment_instance = UserCouponPayment.from_json(json)
# print the JSON string representation of the object
print(UserCouponPayment.to_json())

# convert the object into a dict
user_coupon_payment_dict = user_coupon_payment_instance.to_dict()
# create an instance of UserCouponPayment from a dict
user_coupon_payment_from_dict = UserCouponPayment.from_dict(user_coupon_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


