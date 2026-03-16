# LeverageRequestError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **dict** | The response data. Present for successful (2xx) responses. | [optional] 
**error** | **str** |  | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.leverage_request_error import LeverageRequestError

# TODO update the JSON string below
json = "{}"
# create an instance of LeverageRequestError from a JSON string
leverage_request_error_instance = LeverageRequestError.from_json(json)
# print the JSON string representation of the object
print(LeverageRequestError.to_json())

# convert the object into a dict
leverage_request_error_dict = leverage_request_error_instance.to_dict()
# create an instance of LeverageRequestError from a dict
leverage_request_error_from_dict = LeverageRequestError.from_dict(leverage_request_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


