# PoolRequestError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **dict** | The response data. Present for successful (2xx) responses. | [optional] 
**error** | **str** |  | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.pool_request_error import PoolRequestError

# TODO update the JSON string below
json = "{}"
# create an instance of PoolRequestError from a JSON string
pool_request_error_instance = PoolRequestError.from_json(json)
# print the JSON string representation of the object
print(PoolRequestError.to_json())

# convert the object into a dict
pool_request_error_dict = pool_request_error_instance.to_dict()
# create an instance of PoolRequestError from a dict
pool_request_error_from_dict = PoolRequestError.from_dict(pool_request_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


