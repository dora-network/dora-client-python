# BulkOrderResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Position of the order in the request | 
**client_order_id** | **str** |  | [optional] 
**order_id** | **UUID** | Present when the order was created | [optional] 
**status** | **int** | HTTP status the order would have received from POST /v1/orders: 201 when created | 
**error** | **str** | Present when the order was rejected | [optional] 

## Example

```python
from dora_client.models.bulk_order_result import BulkOrderResult

# TODO update the JSON string below
json = "{}"
# create an instance of BulkOrderResult from a JSON string
bulk_order_result_instance = BulkOrderResult.from_json(json)
# print the JSON string representation of the object
print(BulkOrderResult.to_json())

# convert the object into a dict
bulk_order_result_dict = bulk_order_result_instance.to_dict()
# create an instance of BulkOrderResult from a dict
bulk_order_result_from_dict = BulkOrderResult.from_dict(bulk_order_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


