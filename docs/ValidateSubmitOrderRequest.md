# ValidateSubmitOrderRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **str** |  | 
**tick** | **str** | Minimum tradable increment for the selected order book | 
**kind** | [**OrderKind**](OrderKind.md) |  | 
**side** | [**Side**](Side.md) |  | [optional] 
**price** | **str** | If kind is LIMIT, must be &gt; 0; if MARKET it must be 0 or omitted | 
**good_till_date** | **datetime** |  | [optional] 
**inverse_leverage** | **str** |  | 
**user_balance** | **str** | User balance used to ensure they can afford the requested quantity | 
**base_asset_id** | **str** | base asset of orderbook | [optional] 
**quote_asset_id** | **str** | quote asset of orderbook | [optional] 
**position_assets** | [**list[ValidateSubmitOrderRequestPositionAssets]**](ValidateSubmitOrderRequestPositionAssets.md) | Full list of assets in the position with their price and collateral weight, required when inverse_leverage &lt; 1 for leverage health checks | [optional] 
**assets_config** | [**list[ValidateSubmitOrderRequestAssetsConfig]**](ValidateSubmitOrderRequestAssetsConfig.md) | Configuration for the assets in the order | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

