# StreamUserCouponPaymentsEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**val** | [**UserCouponPayment**](UserCouponPayment.md) |  | 
**time** | **datetime** | The timestamp when the data was created | 

## Example

```python
from dora_client.models.stream_user_coupon_payments_entry import StreamUserCouponPaymentsEntry

# TODO update the JSON string below
json = "{}"
# create an instance of StreamUserCouponPaymentsEntry from a JSON string
stream_user_coupon_payments_entry_instance = StreamUserCouponPaymentsEntry.from_json(json)
# print the JSON string representation of the object
print(StreamUserCouponPaymentsEntry.to_json())

# convert the object into a dict
stream_user_coupon_payments_entry_dict = stream_user_coupon_payments_entry_instance.to_dict()
# create an instance of StreamUserCouponPaymentsEntry from a dict
stream_user_coupon_payments_entry_from_dict = StreamUserCouponPaymentsEntry.from_dict(stream_user_coupon_payments_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


