# Order

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **dict** |  | 
**order_book_id** | **dict** |  | 
**kind** | [**OrderKind**](OrderKind.md) |  | 
**original_price** | **dict** | If Kind is LIMIT, this is the original limit price. If Kind is MARKET, this may be 0 or omitted. | 
**avg_fill_price** | **dict** |  | 
**cancelled_quantity** | **dict** | Quantity that was cancelled, if any. | 
**open_quantity** | **dict** | Quantity that is still open, i.e., not filled or cancelled. | 
**original_quantity** | **dict** | The original quantity of the order when it was created. | 
**filled_quantity** | **dict** | Quantity that has been filled so far. | 
**filled_notional** | **dict** | Quote quantity that has been filled so far. | 
**last_update_at** | **dict** |  | [optional] 
**opened_at** | **dict** |  | 
**inverse_leverage** | **dict** |  | 
**side** | [**Side**](Side.md) |  | 
**status** | [**OrderStatus**](OrderStatus.md) |  | 
**user_id** | **dict** |  | 
**order_modifiers** | **dict** |  | [optional] 
**position_id** | **dict** |  | 
**order_info** | **dict** |  | [optional] 
**good_till_date** | **dict** |  | [optional] 
**trigger_price** | **dict** |  | [optional] 
**trigger_type** | [**TriggerType**](TriggerType.md) |  | [optional] 
**client_order_id** | **dict** | An optional client-provided identifier for the order. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

