# PositionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolio** | [**Portfolio**](Portfolio.md) |  | [optional] 

## Example

```python
from dora_client.models.position_response import PositionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PositionResponse from a JSON string
position_response_instance = PositionResponse.from_json(json)
# print the JSON string representation of the object
print(PositionResponse.to_json())

# convert the object into a dict
position_response_dict = position_response_instance.to_dict()
# create an instance of PositionResponse from a dict
position_response_from_dict = PositionResponse.from_dict(position_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


