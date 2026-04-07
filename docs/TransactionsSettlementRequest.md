# TransactionsSettlementRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx_ids** | **List[str]** |  | [optional] 

## Example

```python
from dora_client.models.transactions_settlement_request import TransactionsSettlementRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionsSettlementRequest from a JSON string
transactions_settlement_request_instance = TransactionsSettlementRequest.from_json(json)
# print the JSON string representation of the object
print(TransactionsSettlementRequest.to_json())

# convert the object into a dict
transactions_settlement_request_dict = transactions_settlement_request_instance.to_dict()
# create an instance of TransactionsSettlementRequest from a dict
transactions_settlement_request_from_dict = TransactionsSettlementRequest.from_dict(transactions_settlement_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


