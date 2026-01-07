# ValidateSubmitOrderRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **dict** |  | 
**tick** | **dict** | Minimum tradable increment for the selected order book | 
**kind** | [**OrderKind**](OrderKind.md) | Must be LIMIT or MARKET | 
**side** | [**Side**](Side.md) | Must be BUY or SELL | [optional] 
**price** | **dict** | If kind is LIMIT, must be &gt; 0; if MARKET it must be 0 or omitted | 
**good_till_date** | **dict** |  | [optional] 
**inverse_leverage** | **dict** |  | 
**user_balance** | **dict** | User balance used to ensure they can afford the requested quantity | 
**base_asset_id** | **dict** | base asset of orderbook | [optional] 
**quote_asset_id** | **dict** | quote asset of orderbook | [optional] 
**position_assets** | **dict** | Full list of assets in the position with their price and collateral weight, required when inverse_leverage &lt; 1 for leverage health checks | [optional] 
**assets_config** | **dict** | Configuration for the assets in the order | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

