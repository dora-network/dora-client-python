# TransactionsSettlementsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settlements** | [**List[TransactionsSettlement]**](TransactionsSettlement.md) |  | [optional] 
**user_totals** | **Dict[str, decimal.Decimal]** |  | [optional] 
**tenant_totals** | **Dict[str, decimal.Decimal]** |  | [optional] 

## Example

```python
from dora_client.models.transactions_settlements_response import TransactionsSettlementsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionsSettlementsResponse from a JSON string
transactions_settlements_response_instance = TransactionsSettlementsResponse.from_json(json)
# print the JSON string representation of the object
print(TransactionsSettlementsResponse.to_json())

# convert the object into a dict
transactions_settlements_response_dict = transactions_settlements_response_instance.to_dict()
# create an instance of TransactionsSettlementsResponse from a dict
transactions_settlements_response_from_dict = TransactionsSettlementsResponse.from_dict(transactions_settlements_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


