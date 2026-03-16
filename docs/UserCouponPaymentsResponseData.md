# UserCouponPaymentsResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coupon_payments** | [**List[UserCouponPayment]**](UserCouponPayment.md) |  | [optional] 
**summary_by_asset** | [**List[UserCouponPaymentAssetSummary]**](UserCouponPaymentAssetSummary.md) |  | [optional] 

## Example

```python
from dora_client.models.user_coupon_payments_response_data import UserCouponPaymentsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of UserCouponPaymentsResponseData from a JSON string
user_coupon_payments_response_data_instance = UserCouponPaymentsResponseData.from_json(json)
# print the JSON string representation of the object
print(UserCouponPaymentsResponseData.to_json())

# convert the object into a dict
user_coupon_payments_response_data_dict = user_coupon_payments_response_data_instance.to_dict()
# create an instance of UserCouponPaymentsResponseData from a dict
user_coupon_payments_response_data_from_dict = UserCouponPaymentsResponseData.from_dict(user_coupon_payments_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


