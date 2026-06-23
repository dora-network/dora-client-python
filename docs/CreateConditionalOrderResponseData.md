# CreateConditionalOrderResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stop_loss_order_id** | **UUID** |  | [optional] 
**take_profit_order_id** | **UUID** |  | [optional] 

## Example

```python
from dora_client.models.create_conditional_order_response_data import CreateConditionalOrderResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConditionalOrderResponseData from a JSON string
create_conditional_order_response_data_instance = CreateConditionalOrderResponseData.from_json(json)
# print the JSON string representation of the object
print(CreateConditionalOrderResponseData.to_json())

# convert the object into a dict
create_conditional_order_response_data_dict = create_conditional_order_response_data_instance.to_dict()
# create an instance of CreateConditionalOrderResponseData from a dict
create_conditional_order_response_data_from_dict = CreateConditionalOrderResponseData.from_dict(create_conditional_order_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


