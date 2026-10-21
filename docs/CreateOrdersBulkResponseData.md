# CreateOrdersBulkResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **int** |  | [optional] 
**rejected** | **int** |  | [optional] 
**results** | [**List[BulkOrderResult]**](BulkOrderResult.md) |  | [optional] 

## Example

```python
from dora_client.models.create_orders_bulk_response_data import CreateOrdersBulkResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrdersBulkResponseData from a JSON string
create_orders_bulk_response_data_instance = CreateOrdersBulkResponseData.from_json(json)
# print the JSON string representation of the object
print(CreateOrdersBulkResponseData.to_json())

# convert the object into a dict
create_orders_bulk_response_data_dict = create_orders_bulk_response_data_instance.to_dict()
# create an instance of CreateOrdersBulkResponseData from a dict
create_orders_bulk_response_data_from_dict = CreateOrdersBulkResponseData.from_dict(create_orders_bulk_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


