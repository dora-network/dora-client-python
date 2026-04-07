# TransactionsSettlement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx_id** | **str** |  | 
**user_id** | **str** |  | 
**tenant_id** | **str** |  | 
**position_id** | **str** |  | 
**tx_kind** | **str** |  | 
**quantity_usd** | **decimal.Decimal** |  | 
**created_at** | **datetime** |  | 
**settled_at** | **datetime** |  | [optional] 
**settled_by** | **str** |  | [optional] 

## Example

```python
from dora_client.models.transactions_settlement import TransactionsSettlement

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionsSettlement from a JSON string
transactions_settlement_instance = TransactionsSettlement.from_json(json)
# print the JSON string representation of the object
print(TransactionsSettlement.to_json())

# convert the object into a dict
transactions_settlement_dict = transactions_settlement_instance.to_dict()
# create an instance of TransactionsSettlement from a dict
transactions_settlement_from_dict = TransactionsSettlement.from_dict(transactions_settlement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


