# PLAsset

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **dict** | The symbol of the asset | [optional] 
**side** | **dict** | The side of the position (LONG or SHORT) | [optional] 
**avg_entry_price** | **dict** | The average entry price of the position | [optional] 
**mark_price** | **dict** | The current mark price for the asset to calculate daily PL. This is usually the close price of the previous day | [optional] 
**liquidation_price** | **dict** | The liquidation price of the position | [optional] 
**available** | **dict** | The available quantity in units of the asset | [optional] 
**borrowed** | **dict** | The borrowed quantity in units of the asset | [optional] 
**margin** | [**Margin**](Margin.md) |  | [optional] 
**unrealized_pl** | **dict** | The unrealized profit or loss of the position | [optional] 
**leverage_limit** | **dict** | The leverage limit for the position | [optional] 
**tp** | **dict** | The take profit price set for the position, if any | [optional] 
**sl** | **dict** | The stop loss price set for the position, if any | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

