# BalanceTransfer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_position_id** | **UUID** |  | 
**to_position_id** | **UUID** |  | 
**transaction_id** | **UUID** |  | 

## Example

```python
from dora_client.models.balance_transfer import BalanceTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceTransfer from a JSON string
balance_transfer_instance = BalanceTransfer.from_json(json)
# print the JSON string representation of the object
print(BalanceTransfer.to_json())

# convert the object into a dict
balance_transfer_dict = balance_transfer_instance.to_dict()
# create an instance of BalanceTransfer from a dict
balance_transfer_from_dict = BalanceTransfer.from_dict(balance_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


