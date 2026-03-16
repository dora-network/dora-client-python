# ClosePositionResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** |  | [optional] 

## Example

```python
from dora_client.models.close_position_resp import ClosePositionResp

# TODO update the JSON string below
json = "{}"
# create an instance of ClosePositionResp from a JSON string
close_position_resp_instance = ClosePositionResp.from_json(json)
# print the JSON string representation of the object
print(ClosePositionResp.to_json())

# convert the object into a dict
close_position_resp_dict = close_position_resp_instance.to_dict()
# create an instance of ClosePositionResp from a dict
close_position_resp_from_dict = ClosePositionResp.from_dict(close_position_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


