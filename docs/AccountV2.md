# AccountV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the account. Used, for example, when creating an order from an account, or deciding collateral should be transferred from account A to account B. | 
**asset_id** | **str** |  | 
**seq** | **int** |  | 
**is_global** | **bool** |  | [optional] 
**available** | **str** | The available balance in the account for this asset that are not locked, supplied, or used as collateral | 
**locked** | **str** | The balance that has been reserved for a current order. If spent by the order, they are removed. If the order is cancelled, they are returned to the account&#39;s available balance. | 
**supplied** | **str** | The balance that user has supplied to the leverage module. The user remains entitled to these assets and can withdraw them into their available balance. | 
**borrowed** | **str** | The total amount of debt outstanding for this account. This account cannot be closed until all debt is fully repaid, i.e. borrowed &#x3D; 0. | 
**impending_borrows** | **str** | The equivalent of locked balances, but for leveraged orders. If a user has an active order that would borrow assets as part of its input, then their borrow limit must be reduced until the order is executed or cancelled. | 
**avg_entry_price** | **str** | average cost per unit quantity that was paid (long accounts) or received (short accounts) for this asset. | 
**borrow_limit** | **str** | The borrow limit | 
**liquidation_threshold** | **str** | The borrow limit | 
**created_at** | **datetime** |  | 
**pending_withdrawal** | **str** | The amount of asset that is pending withdrawal from the account. | 
**account_name** | **str** |  | 

## Example

```python
from dora_client.models.account_v2 import AccountV2

# TODO update the JSON string below
json = "{}"
# create an instance of AccountV2 from a JSON string
account_v2_instance = AccountV2.from_json(json)
# print the JSON string representation of the object
print(AccountV2.to_json())

# convert the object into a dict
account_v2_dict = account_v2_instance.to_dict()
# create an instance of AccountV2 from a dict
account_v2_from_dict = AccountV2.from_dict(account_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


