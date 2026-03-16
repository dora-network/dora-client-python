# FundUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** |  | 
**quantity** | **str** |  | 

## Example

```python
from dora_client.models.fund_user_request import FundUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FundUserRequest from a JSON string
fund_user_request_instance = FundUserRequest.from_json(json)
# print the JSON string representation of the object
print(FundUserRequest.to_json())

# convert the object into a dict
fund_user_request_dict = fund_user_request_instance.to_dict()
# create an instance of FundUserRequest from a dict
fund_user_request_from_dict = FundUserRequest.from_dict(fund_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


