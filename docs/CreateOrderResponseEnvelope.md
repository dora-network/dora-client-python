# CreateOrderResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**OrderId**](OrderId.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.create_order_response_envelope import CreateOrderResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrderResponseEnvelope from a JSON string
create_order_response_envelope_instance = CreateOrderResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(CreateOrderResponseEnvelope.to_json())

# convert the object into a dict
create_order_response_envelope_dict = create_order_response_envelope_instance.to_dict()
# create an instance of CreateOrderResponseEnvelope from a dict
create_order_response_envelope_from_dict = CreateOrderResponseEnvelope.from_dict(create_order_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


