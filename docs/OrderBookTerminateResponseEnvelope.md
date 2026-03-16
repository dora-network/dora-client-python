# OrderBookTerminateResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **bool** |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.order_book_terminate_response_envelope import OrderBookTerminateResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of OrderBookTerminateResponseEnvelope from a JSON string
order_book_terminate_response_envelope_instance = OrderBookTerminateResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(OrderBookTerminateResponseEnvelope.to_json())

# convert the object into a dict
order_book_terminate_response_envelope_dict = order_book_terminate_response_envelope_instance.to_dict()
# create an instance of OrderBookTerminateResponseEnvelope from a dict
order_book_terminate_response_envelope_from_dict = OrderBookTerminateResponseEnvelope.from_dict(order_book_terminate_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


