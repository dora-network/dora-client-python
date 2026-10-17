# CreateOrdersBulkResponseAllOfData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **int** |  | [optional] 
**rejected** | **int** |  | [optional] 
**results** | [**List[BulkOrderResult]**](BulkOrderResult.md) |  | [optional] 

## Example

```python
from dora_client.models.create_orders_bulk_response_all_of_data import CreateOrdersBulkResponseAllOfData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrdersBulkResponseAllOfData from a JSON string
create_orders_bulk_response_all_of_data_instance = CreateOrdersBulkResponseAllOfData.from_json(json)
# print the JSON string representation of the object
print(CreateOrdersBulkResponseAllOfData.to_json())

# convert the object into a dict
create_orders_bulk_response_all_of_data_dict = create_orders_bulk_response_all_of_data_instance.to_dict()
# create an instance of CreateOrdersBulkResponseAllOfData from a dict
create_orders_bulk_response_all_of_data_from_dict = CreateOrdersBulkResponseAllOfData.from_dict(create_orders_bulk_response_all_of_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


