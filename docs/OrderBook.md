# OrderBook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_book_id** | **str** |  | 
**order_book_seq** | **int** |  | [optional] 
**base_quantity** | **float** |  | 
**base_asset_id** | **str** |  | 
**created_at** | **datetime** |  | 
**display_name** | **str** |  | 
**base_asset_fractionalized_units** | **int** |  | 
**quote_asset_fractionalized_units** | **int** |  | 
**fee_factor** | **float** |  | 
**initial_assets_ratio** | **float** |  | 
**maturity_at** | **datetime** |  | 
**quote_quantity** | **float** |  | 
**quote_asset_id** | **str** |  | 
**shares_quantity** | **float** |  | 
**status** | [**OrderBookStatus**](OrderBookStatus.md) |  | 
**tick_size** | **float** |  | 
**updated_at** | **datetime** |  | 
**halted_at** | **datetime** |  | [optional] 
**terminated_at** | **datetime** |  | [optional] 
**pool_updated_at** | **datetime** |  | [optional] 
**shares_asset_id** | **str** |  | 

## Example

```python
from dora_client.models.order_book import OrderBook

# TODO update the JSON string below
json = "{}"
# create an instance of OrderBook from a JSON string
order_book_instance = OrderBook.from_json(json)
# print the JSON string representation of the object
print(OrderBook.to_json())

# convert the object into a dict
order_book_dict = order_book_instance.to_dict()
# create an instance of OrderBook from a dict
order_book_from_dict = OrderBook.from_dict(order_book_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


