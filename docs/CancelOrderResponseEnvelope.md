# CancelOrderResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Order**](Order.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.cancel_order_response_envelope import CancelOrderResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of CancelOrderResponseEnvelope from a JSON string
cancel_order_response_envelope_instance = CancelOrderResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(CancelOrderResponseEnvelope.to_json())

# convert the object into a dict
cancel_order_response_envelope_dict = cancel_order_response_envelope_instance.to_dict()
# create an instance of CancelOrderResponseEnvelope from a dict
cancel_order_response_envelope_from_dict = CancelOrderResponseEnvelope.from_dict(cancel_order_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


