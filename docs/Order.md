# Order

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** |  | [optional] 
**order_book_id** | **str** |  | [optional] 
**kind** | [**OrderKind**](OrderKind.md) |  | [optional] 
**original_price** | **str** | If Kind is LIMIT, this is the original limit price. If Kind is MARKET, this may be 0 or omitted. | [optional] 
**avg_fill_price** | **str** |  | [optional] 
**cancelled_quantity** | **str** | Quantity that was cancelled, if any. | [optional] 
**open_quantity** | **str** | Quantity that is still open, i.e., not filled or cancelled. | [optional] 
**original_quantity** | **str** | The original quantity of the order when it was created. | [optional] 
**filled_quantity** | **str** | Quantity that has been filled so far. | [optional] 
**filled_notional** | **str** | Quote quantity that has been filled so far. | [optional] 
**last_update_at** | **datetime** |  | [optional] 
**opened_at** | **datetime** |  | [optional] 
**inverse_leverage** | **str** |  | [optional] 
**side** | [**Side**](Side.md) |  | [optional] 
**status** | [**OrderStatus**](OrderStatus.md) |  | [optional] 
**user_id** | **str** |  | [optional] 
**order_modifiers** | [**list[OrderModifierKind]**](OrderModifierKind.md) |  | [optional] 
**position_id** | **str** |  | [optional] 
**order_info** | **str** |  | [optional] 
**good_till_date** | **datetime** |  | [optional] 
**trigger_price** | **str** |  | [optional] 
**trigger_type** | [**TriggerType**](TriggerType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

