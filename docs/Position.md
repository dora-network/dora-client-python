# Position


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the position. Used, for example, when creating an order from a position, or deciding collateral should be transferred from position A to position B. | 
**asset_id** | **str** |  | 
**seq** | **int** |  | 
**is_global** | **bool** |  | [optional] 
**available** | **str** | The available balance in the position for this asset that are not locked, supplied, or used as collateral | 
**locked** | **str** | The balance that has been reserved for a current order. If spent by the order, they are removed. If the order is cancelled, they are returned to the position&#39;s available balance. | 
**supplied** | **str** | The balance that user has supplied to the leverage module. The user remains entitled to these assets and can withdraw them into their available balance. | 
**borrowed** | **str** | The total amount of debt outstanding for this position. This position cannot be closed until all debt is fully repaid, i.e. borrowed &#x3D; 0. | 
**impending_borrows** | **str** | The equivalent of locked balances, but for leveraged orders. If a user has an active order that would borrow assets as part of its input, then their borrow limit must be reduced until the order is executed or cancelled. | 
**avg_entry_price** | **str** | average cost per unit quantity that was paid (long positions) or received (short positions) for this asset. | 
**borrow_limit** | **str** | The borrow limit | 
**liquidation_threshold** | **str** | The borrow limit | 
**created_at** | **datetime** |  | 
**position_name** | **str** |  | 
**pending_withdrawal** | **str** | The amount of asset that is pending withdrawal from the position. | 

## Example

```python
from dora_client.models.position import Position

# TODO update the JSON string below
json = "{}"
# create an instance of Position from a JSON string
position_instance = Position.from_json(json)
# print the JSON string representation of the object
print(Position.to_json())

# convert the object into a dict
position_dict = position_instance.to_dict()
# create an instance of Position from a dict
position_from_dict = Position.from_dict(position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


