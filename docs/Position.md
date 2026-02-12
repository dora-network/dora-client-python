# Position

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **dict** | The unique identifier for the position. Used, for example, when creating an order from a position, or deciding collateral should be transferred from position A to position B. | 
**asset_id** | **dict** |  | 
**seq** | **dict** |  | 
**is_global** | **dict** |  | [optional] 
**available** | **dict** | The available balance in the position for this asset that are not locked, supplied, or used as collateral | 
**locked** | **dict** | The balance that has been reserved for a current order. If spent by the order, they are removed. If the order is cancelled, they are returned to the position&#x27;s available balance. | 
**supplied** | **dict** | The balance that user has supplied to the leverage module. The user remains entitled to these assets and can withdraw them into their available balance. | 
**borrowed** | **dict** | The total amount of debt outstanding for this position. This position cannot be closed until all debt is fully repaid, i.e. borrowed &#x3D; 0. | 
**impending_borrows** | **dict** | The equivalent of locked balances, but for leveraged orders. If a user has an active order that would borrow assets as part of its input, then their borrow limit must be reduced until the order is executed or cancelled. | 
**avg_entry_price** | **dict** | average cost per unit quantity that was paid (long positions) or received (short positions) for this asset. | 
**borrow_limit** | **dict** | The borrow limit | 
**liquidation_threshold** | **dict** | The borrow limit | 
**created_at** | **dict** |  | 
**position_name** | **dict** |  | 
**pending_withdrawal** | **dict** | The amount of asset that is pending withdrawal from the position. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

