# Trade


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** |  | 
**asset_0** | **str** |  | 
**created_at** | **datetime** |  | 
**order_book_id** | **str** |  | 
**order_id** | **str** |  | 
**order_seq** | **int** |  | 
**price** | **str** |  | 
**quantity_0** | **str** |  | 
**user_id** | **str** |  | 
**side** | [**Side**](Side.md) |  | 
**aggressor_indicator** | **bool** | If true, then this order is the aggressor (taker); otherwise it is the maker. | 

## Example

```python
from dora_client.models.trade import Trade

# TODO update the JSON string below
json = "{}"
# create an instance of Trade from a JSON string
trade_instance = Trade.from_json(json)
# print the JSON string representation of the object
print(Trade.to_json())

# convert the object into a dict
trade_dict = trade_instance.to_dict()
# create an instance of Trade from a dict
trade_from_dict = Trade.from_dict(trade_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


