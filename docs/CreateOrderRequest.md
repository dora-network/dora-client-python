# CreateOrderRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **str** |  | 
**inverse_leverage** | **str** |  | 
**price** | **str** |  | [optional] 
**kind** | [**OrderKind**](OrderKind.md) |  | 
**side** | [**Side**](Side.md) |  | 
**position_id** | **str** | position ID to use for the order. required. | 
**order_book_id** | **str** | Required: the order book to submit the order to | 
**order_info** | **str** | Optional: User-defined text for the order, e.g., &#x27;buying dips&#x27; | [optional] 
**order_modifiers** | [**list[OrderModifierKind]**](OrderModifierKind.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

