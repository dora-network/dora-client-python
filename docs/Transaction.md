# Transaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_at** | **datetime** |  | 
**kind** | [**TransactionKind**](TransactionKind.md) |  | 
**asset0** | **str** |  | 
**quantity0** | **str** |  | 
**quantity1** | **str** |  | 
**asset1** | **str** |  | 
**user_id** | **str** |  | 
**admin_user_id** | **str** |  | 
**order_side** | [**Side**](Side.md) |  | 

## Example

```python
from dora_client.models.transaction import Transaction

# TODO update the JSON string below
json = "{}"
# create an instance of Transaction from a JSON string
transaction_instance = Transaction.from_json(json)
# print the JSON string representation of the object
print(Transaction.to_json())

# convert the object into a dict
transaction_dict = transaction_instance.to_dict()
# create an instance of Transaction from a dict
transaction_from_dict = Transaction.from_dict(transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


