# GetCopyTradersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CopyTrader]**](CopyTrader.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.get_copy_traders_response import GetCopyTradersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCopyTradersResponse from a JSON string
get_copy_traders_response_instance = GetCopyTradersResponse.from_json(json)
# print the JSON string representation of the object
print(GetCopyTradersResponse.to_json())

# convert the object into a dict
get_copy_traders_response_dict = get_copy_traders_response_instance.to_dict()
# create an instance of GetCopyTradersResponse from a dict
get_copy_traders_response_from_dict = GetCopyTradersResponse.from_dict(get_copy_traders_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


