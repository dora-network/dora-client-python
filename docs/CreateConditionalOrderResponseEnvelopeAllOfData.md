# CreateConditionalOrderResponseEnvelopeAllOfData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stop_loss_order_id** | **str** |  | [optional] 
**take_profit_order_id** | **str** |  | [optional] 

## Example

```python
from dora_client.models.create_conditional_order_response_envelope_all_of_data import CreateConditionalOrderResponseEnvelopeAllOfData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConditionalOrderResponseEnvelopeAllOfData from a JSON string
create_conditional_order_response_envelope_all_of_data_instance = CreateConditionalOrderResponseEnvelopeAllOfData.from_json(json)
# print the JSON string representation of the object
print(CreateConditionalOrderResponseEnvelopeAllOfData.to_json())

# convert the object into a dict
create_conditional_order_response_envelope_all_of_data_dict = create_conditional_order_response_envelope_all_of_data_instance.to_dict()
# create an instance of CreateConditionalOrderResponseEnvelopeAllOfData from a dict
create_conditional_order_response_envelope_all_of_data_from_dict = CreateConditionalOrderResponseEnvelopeAllOfData.from_dict(create_conditional_order_response_envelope_all_of_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


