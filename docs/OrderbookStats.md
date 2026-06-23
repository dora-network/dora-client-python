# OrderbookStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_book_id** | **UUID** |  | 
**open_price** | **str** | Open price of the orderbook | 
**last_price** | **str** | Price of the most recent executed trade. | 
**high_24h** | **str** | Highest price of the orderbook in the last 24 hours. | 
**low_24h** | **str** | Lowest price of the orderbook in the last 24 hours. | 
**change_24h** | **str** | Change in price of the orderbook in the last 24 hours. | 
**change_pct_24h** | **str** | Change percentage in price of the orderbook in the last 24 hours. | 
**volume_24h_base** | **str** | Total volume of the orderbook in the last 24 hours. | 
**volume_24h_usd** | **str** | Total volume of the orderbook in the last 24 hours in USD. | 

## Example

```python
from dora_client.models.orderbook_stats import OrderbookStats

# TODO update the JSON string below
json = "{}"
# create an instance of OrderbookStats from a JSON string
orderbook_stats_instance = OrderbookStats.from_json(json)
# print the JSON string representation of the object
print(OrderbookStats.to_json())

# convert the object into a dict
orderbook_stats_dict = orderbook_stats_instance.to_dict()
# create an instance of OrderbookStats from a dict
orderbook_stats_from_dict = OrderbookStats.from_dict(orderbook_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


