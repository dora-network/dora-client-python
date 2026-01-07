# Order

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **dict** |  | [optional] 
**order_book_id** | **dict** |  | [optional] 
**kind** | [**OrderKind**](OrderKind.md) |  | [optional] 
**original_price** | **dict** | If Kind is LIMIT, this is the original limit price. If Kind is MARKET, this may be 0 or omitted. | [optional] 
**avg_fill_price** | **dict** |  | [optional] 
**cancelled_quantity** | **dict** | Quantity that was cancelled, if any. | [optional] 
**open_quantity** | **dict** | Quantity that is still open, i.e., not filled or cancelled. | [optional] 
**original_quantity** | **dict** | The original quantity of the order when it was created. | [optional] 
**filled_quantity** | **dict** | Quantity that has been filled so far. | [optional] 
**filled_notional** | **dict** | Quote quantity that has been filled so far. | [optional] 
**last_update_at** | **dict** |  | [optional] 
**opened_at** | **dict** |  | [optional] 
**inverse_leverage** | **dict** |  | [optional] 
**side** | [**Side**](Side.md) |  | [optional] 
**status** | [**OrderStatus**](OrderStatus.md) |  | [optional] 
**user_id** | **dict** |  | [optional] 
**order_modifiers** | **dict** |  | [optional] 
**position_id** | **dict** |  | [optional] 
**order_info** | **dict** |  | [optional] 
**good_till_date** | **dict** |  | [optional] 
**trigger_price** | **dict** |  | [optional] 
**trigger_type** | [**TriggerType**](TriggerType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

