# CreateOrderRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **dict** |  | 
**inverse_leverage** | **dict** |  | 
**price** | **dict** |  | [optional] 
**kind** | [**OrderKind**](OrderKind.md) |  | 
**side** | [**Side**](Side.md) | Required: Must be either &#x27;BUY&#x27; or &#x27;SELL&#x27; | 
**from_global_position** | **dict** | use global position for the order or isolated. required. | 
**order_book_id** | **dict** | Required: the order book to submit the order to | 
**order_modifiers** | **dict** |  | [optional] 
**good_till_date** | **dict** |  | [optional] 
**trigger_price** | **dict** |  | [optional] 
**trigger_type** | [**TriggerType**](TriggerType.md) |  | [optional] 
**client_order_id** | **dict** | An optional client-provided identifier for the order. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

