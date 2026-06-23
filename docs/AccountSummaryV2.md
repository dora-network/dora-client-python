# AccountSummaryV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **UUID** | The ID of the account | 
**account_name** | **str** | The name of the account | 
**is_global** | **bool** | Whether the account is the global or an isolated account | 

## Example

```python
from dora_client.models.account_summary_v2 import AccountSummaryV2

# TODO update the JSON string below
json = "{}"
# create an instance of AccountSummaryV2 from a JSON string
account_summary_v2_instance = AccountSummaryV2.from_json(json)
# print the JSON string representation of the object
print(AccountSummaryV2.to_json())

# convert the object into a dict
account_summary_v2_dict = account_summary_v2_instance.to_dict()
# create an instance of AccountSummaryV2 from a dict
account_summary_v2_from_dict = AccountSummaryV2.from_dict(account_summary_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


