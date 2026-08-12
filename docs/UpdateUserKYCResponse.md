# UpdateUserKYCResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **UUID** |  | 
**kyc_completed** | **bool** |  | 

## Example

```python
from dora_client.models.update_user_kyc_response import UpdateUserKYCResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserKYCResponse from a JSON string
update_user_kyc_response_instance = UpdateUserKYCResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateUserKYCResponse.to_json())

# convert the object into a dict
update_user_kyc_response_dict = update_user_kyc_response_instance.to_dict()
# create an instance of UpdateUserKYCResponse from a dict
update_user_kyc_response_from_dict = UpdateUserKYCResponse.from_dict(update_user_kyc_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


