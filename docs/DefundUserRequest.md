# DefundUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **UUID** |  | 
**quantity** | **str** |  | 

## Example

```python
from dora_client.models.defund_user_request import DefundUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DefundUserRequest from a JSON string
defund_user_request_instance = DefundUserRequest.from_json(json)
# print the JSON string representation of the object
print(DefundUserRequest.to_json())

# convert the object into a dict
defund_user_request_dict = defund_user_request_instance.to_dict()
# create an instance of DefundUserRequest from a dict
defund_user_request_from_dict = DefundUserRequest.from_dict(defund_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


