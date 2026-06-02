# TransactionInternalTransfer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_account_id** | **str** |  | 
**to_account_id** | **str** |  | 
**asset_id** | **str** |  | 
**quantity** | **str** |  | 

## Example

```python
from dora_client.models.transaction_internal_transfer import TransactionInternalTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionInternalTransfer from a JSON string
transaction_internal_transfer_instance = TransactionInternalTransfer.from_json(json)
# print the JSON string representation of the object
print(TransactionInternalTransfer.to_json())

# convert the object into a dict
transaction_internal_transfer_dict = transaction_internal_transfer_instance.to_dict()
# create an instance of TransactionInternalTransfer from a dict
transaction_internal_transfer_from_dict = TransactionInternalTransfer.from_dict(transaction_internal_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


