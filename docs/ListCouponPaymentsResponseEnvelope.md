# ListCouponPaymentsResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CouponPayment]**](CouponPayment.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.list_coupon_payments_response_envelope import ListCouponPaymentsResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListCouponPaymentsResponseEnvelope from a JSON string
list_coupon_payments_response_envelope_instance = ListCouponPaymentsResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(ListCouponPaymentsResponseEnvelope.to_json())

# convert the object into a dict
list_coupon_payments_response_envelope_dict = list_coupon_payments_response_envelope_instance.to_dict()
# create an instance of ListCouponPaymentsResponseEnvelope from a dict
list_coupon_payments_response_envelope_from_dict = ListCouponPaymentsResponseEnvelope.from_dict(list_coupon_payments_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


