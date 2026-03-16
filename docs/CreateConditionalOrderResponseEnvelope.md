# CreateConditionalOrderResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateConditionalOrderResponseEnvelopeAllOfData**](CreateConditionalOrderResponseEnvelopeAllOfData.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.create_conditional_order_response_envelope import CreateConditionalOrderResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConditionalOrderResponseEnvelope from a JSON string
create_conditional_order_response_envelope_instance = CreateConditionalOrderResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(CreateConditionalOrderResponseEnvelope.to_json())

# convert the object into a dict
create_conditional_order_response_envelope_dict = create_conditional_order_response_envelope_instance.to_dict()
# create an instance of CreateConditionalOrderResponseEnvelope from a dict
create_conditional_order_response_envelope_from_dict = CreateConditionalOrderResponseEnvelope.from_dict(create_conditional_order_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


