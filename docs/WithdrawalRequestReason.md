# WithdrawalRequestReason


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | 

## Example

```python
from dora_client.models.withdrawal_request_reason import WithdrawalRequestReason

# TODO update the JSON string below
json = "{}"
# create an instance of WithdrawalRequestReason from a JSON string
withdrawal_request_reason_instance = WithdrawalRequestReason.from_json(json)
# print the JSON string representation of the object
print(WithdrawalRequestReason.to_json())

# convert the object into a dict
withdrawal_request_reason_dict = withdrawal_request_reason_instance.to_dict()
# create an instance of WithdrawalRequestReason from a dict
withdrawal_request_reason_from_dict = WithdrawalRequestReason.from_dict(withdrawal_request_reason_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


