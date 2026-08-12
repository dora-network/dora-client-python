# UpdateUserKYCRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed_kyc** | **bool** | If true, sets kyc_completed_at to now; if false, clears it. | 

## Example

```python
from dora_client.models.update_user_kyc_request import UpdateUserKYCRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserKYCRequest from a JSON string
update_user_kyc_request_instance = UpdateUserKYCRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateUserKYCRequest.to_json())

# convert the object into a dict
update_user_kyc_request_dict = update_user_kyc_request_instance.to_dict()
# create an instance of UpdateUserKYCRequest from a dict
update_user_kyc_request_from_dict = UpdateUserKYCRequest.from_dict(update_user_kyc_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


