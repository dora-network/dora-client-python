# AssetRequestError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **dict** | The response data. Present for successful (2xx) responses. | [optional] 
**error** | **str** |  | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.asset_request_error import AssetRequestError

# TODO update the JSON string below
json = "{}"
# create an instance of AssetRequestError from a JSON string
asset_request_error_instance = AssetRequestError.from_json(json)
# print the JSON string representation of the object
print(AssetRequestError.to_json())

# convert the object into a dict
asset_request_error_dict = asset_request_error_instance.to_dict()
# create an instance of AssetRequestError from a dict
asset_request_error_from_dict = AssetRequestError.from_dict(asset_request_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


