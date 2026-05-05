# TransferAccountBalancesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_account_id** | **str** |  | 
**to_account_id** | **str** |  | 
**asset_id** | **str** |  | 
**quantity** | **decimal.Decimal** |  | 

## Example

```python
from dora_client.models.transfer_account_balances_request import TransferAccountBalancesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransferAccountBalancesRequest from a JSON string
transfer_account_balances_request_instance = TransferAccountBalancesRequest.from_json(json)
# print the JSON string representation of the object
print(TransferAccountBalancesRequest.to_json())

# convert the object into a dict
transfer_account_balances_request_dict = transfer_account_balances_request_instance.to_dict()
# create an instance of TransferAccountBalancesRequest from a dict
transfer_account_balances_request_from_dict = TransferAccountBalancesRequest.from_dict(transfer_account_balances_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


