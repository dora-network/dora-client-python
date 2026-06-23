# ClosePositionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position_id** | **UUID** |  | 
**order_book_id** | **UUID** |  | 

## Example

```python
from dora_client.models.close_position_request import ClosePositionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClosePositionRequest from a JSON string
close_position_request_instance = ClosePositionRequest.from_json(json)
# print the JSON string representation of the object
print(ClosePositionRequest.to_json())

# convert the object into a dict
close_position_request_dict = close_position_request_instance.to_dict()
# create an instance of ClosePositionRequest from a dict
close_position_request_from_dict = ClosePositionRequest.from_dict(close_position_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


