# StreamUserCouponPaymentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[StreamUserCouponPaymentsEntry]**](StreamUserCouponPaymentsEntry.md) |  | [optional] 
**summary_by_asset** | [**List[UserCouponPaymentAssetSummary]**](UserCouponPaymentAssetSummary.md) |  | [optional] 

## Example

```python
from dora_client.models.stream_user_coupon_payments_response import StreamUserCouponPaymentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StreamUserCouponPaymentsResponse from a JSON string
stream_user_coupon_payments_response_instance = StreamUserCouponPaymentsResponse.from_json(json)
# print the JSON string representation of the object
print(StreamUserCouponPaymentsResponse.to_json())

# convert the object into a dict
stream_user_coupon_payments_response_dict = stream_user_coupon_payments_response_instance.to_dict()
# create an instance of StreamUserCouponPaymentsResponse from a dict
stream_user_coupon_payments_response_from_dict = StreamUserCouponPaymentsResponse.from_dict(stream_user_coupon_payments_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


