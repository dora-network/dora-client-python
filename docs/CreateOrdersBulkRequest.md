# CreateOrdersBulkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orders** | [**List[CreateOrderRequest]**](CreateOrderRequest.md) | Orders to submit, all with the same &#x60;order_book_id&#x60;. The maximum is configurable (matching.bulk_order_max_orders, default 20). | 
**atomic** | **bool** | Not currently supported: must be omitted or false, and &#x60;true&#x60; is rejected with 400. Orders are processed independently and partial creation is allowed. | [optional] [default to False]

## Example

```python
from dora_client.models.create_orders_bulk_request import CreateOrdersBulkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrdersBulkRequest from a JSON string
create_orders_bulk_request_instance = CreateOrdersBulkRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOrdersBulkRequest.to_json())

# convert the object into a dict
create_orders_bulk_request_dict = create_orders_bulk_request_instance.to_dict()
# create an instance of CreateOrdersBulkRequest from a dict
create_orders_bulk_request_from_dict = CreateOrdersBulkRequest.from_dict(create_orders_bulk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


