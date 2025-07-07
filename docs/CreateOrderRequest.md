# CreateOrderRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **str** |  | [optional] 
**inverse_leverage** | **float** | Required: Inverse leverage for the order, must be between 0 and 1 (inclusive) | [optional] 
**price** | **str** |  | [optional] 
**kind** | **str** |  | [optional] 
**side** | **str** | Required: Must be either &#x27;BUY&#x27; or &#x27;SELL&#x27; | [optional] 
**order_book_id** | **str** | Required: the order book to submit the order to | [optional] 
**user_text** | **str** | Optional: User-defined text for the order, e.g., &#x27;buying dips&#x27; | [optional] 
**order_modifiers** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

