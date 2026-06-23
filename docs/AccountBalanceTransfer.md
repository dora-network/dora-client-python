# AccountBalanceTransfer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_account_id** | **UUID** |  | 
**to_account_id** | **UUID** |  | 
**transaction_id** | **UUID** |  | 

## Example

```python
from dora_client.models.account_balance_transfer import AccountBalanceTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of AccountBalanceTransfer from a JSON string
account_balance_transfer_instance = AccountBalanceTransfer.from_json(json)
# print the JSON string representation of the object
print(AccountBalanceTransfer.to_json())

# convert the object into a dict
account_balance_transfer_dict = account_balance_transfer_instance.to_dict()
# create an instance of AccountBalanceTransfer from a dict
account_balance_transfer_from_dict = AccountBalanceTransfer.from_dict(account_balance_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


