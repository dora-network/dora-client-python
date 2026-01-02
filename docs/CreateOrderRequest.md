# CreateOrderRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **str** |  | 
**inverse_leverage** | **str** |  | 
**price** | **str** |  | [optional] 
**kind** | [**OrderKind**](OrderKind.md) |  | 
**side** | [**Side**](Side.md) |  | 
**from_global_position** | **bool** | use global position for the order or isolated. required. | 
**order_book_id** | **str** | Required: the order book to submit the order to | 
**order_modifiers** | [**list[OrderModifierKind]**](OrderModifierKind.md) |  | [optional] 
**good_till_date** | **datetime** |  | [optional] 
**trigger_price** | **str** |  | [optional] 
**trigger_type** | [**TriggerType**](TriggerType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

