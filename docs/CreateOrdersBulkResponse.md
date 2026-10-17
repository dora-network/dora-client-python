# CreateOrdersBulkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateOrdersBulkResponseAllOfData**](CreateOrdersBulkResponseAllOfData.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.create_orders_bulk_response import CreateOrdersBulkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrdersBulkResponse from a JSON string
create_orders_bulk_response_instance = CreateOrdersBulkResponse.from_json(json)
# print the JSON string representation of the object
print(CreateOrdersBulkResponse.to_json())

# convert the object into a dict
create_orders_bulk_response_dict = create_orders_bulk_response_instance.to_dict()
# create an instance of CreateOrdersBulkResponse from a dict
create_orders_bulk_response_from_dict = CreateOrdersBulkResponse.from_dict(create_orders_bulk_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


