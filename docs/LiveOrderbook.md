# LiveOrderbook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bids** | [**List[PriceLevel]**](PriceLevel.md) | sorted in desc order by price | 
**asks** | [**List[PriceLevel]**](PriceLevel.md) | sorted in asc order by price | 

## Example

```python
from dora_client.models.live_orderbook import LiveOrderbook

# TODO update the JSON string below
json = "{}"
# create an instance of LiveOrderbook from a JSON string
live_orderbook_instance = LiveOrderbook.from_json(json)
# print the JSON string representation of the object
print(LiveOrderbook.to_json())

# convert the object into a dict
live_orderbook_dict = live_orderbook_instance.to_dict()
# create an instance of LiveOrderbook from a dict
live_orderbook_from_dict = LiveOrderbook.from_dict(live_orderbook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


