# UserCouponPaymentAssetSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** |  | 
**pending** | **str** |  | 
**completed** | **str** |  | 

## Example

```python
from dora_client.models.user_coupon_payment_asset_summary import UserCouponPaymentAssetSummary

# TODO update the JSON string below
json = "{}"
# create an instance of UserCouponPaymentAssetSummary from a JSON string
user_coupon_payment_asset_summary_instance = UserCouponPaymentAssetSummary.from_json(json)
# print the JSON string representation of the object
print(UserCouponPaymentAssetSummary.to_json())

# convert the object into a dict
user_coupon_payment_asset_summary_dict = user_coupon_payment_asset_summary_instance.to_dict()
# create an instance of UserCouponPaymentAssetSummary from a dict
user_coupon_payment_asset_summary_from_dict = UserCouponPaymentAssetSummary.from_dict(user_coupon_payment_asset_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


