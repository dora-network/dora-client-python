# PLAsset

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **dict** | The symbol of the asset | 
**side** | **dict** | The side of the position (LONG or SHORT) | 
**avg_entry_price** | **dict** | The average entry price of the position | 
**mark_price** | **dict** | The current mark price for the asset to calculate daily PL. This is usually the close price of the previous day | 
**liquidation_price** | **dict** | The liquidation price of the position | 
**available** | **dict** | The available quantity in units of the asset | 
**borrowed** | **dict** | The borrowed quantity in units of the asset | 
**margin** | [**Margin**](Margin.md) |  | 
**unrealized_pl** | **dict** | The unrealized profit or loss of the position | 
**leverage_limit** | **dict** | The leverage limit for the position | 
**tp** | **dict** | The take profit price set for the position, if any | [optional] 
**sl** | **dict** | The stop loss price set for the position, if any | [optional] 
**initial_capital** | **dict** | The initial capital of the position | 
**impending_borrows** | **dict** | The impending borrows of the position | [optional] 
**locked** | **dict** | The locked amount of the position | 
**unused_collateral** | **dict** | The unused collateral of the position | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

