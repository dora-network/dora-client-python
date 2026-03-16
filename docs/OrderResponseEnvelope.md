# OrderResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Order**](Order.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.order_response_envelope import OrderResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of OrderResponseEnvelope from a JSON string
order_response_envelope_instance = OrderResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(OrderResponseEnvelope.to_json())

# convert the object into a dict
order_response_envelope_dict = order_response_envelope_instance.to_dict()
# create an instance of OrderResponseEnvelope from a dict
order_response_envelope_from_dict = OrderResponseEnvelope.from_dict(order_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


