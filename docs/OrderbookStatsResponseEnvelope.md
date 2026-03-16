# OrderbookStatsResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**OrderbookStats**](OrderbookStats.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.orderbook_stats_response_envelope import OrderbookStatsResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of OrderbookStatsResponseEnvelope from a JSON string
orderbook_stats_response_envelope_instance = OrderbookStatsResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(OrderbookStatsResponseEnvelope.to_json())

# convert the object into a dict
orderbook_stats_response_envelope_dict = orderbook_stats_response_envelope_instance.to_dict()
# create an instance of OrderbookStatsResponseEnvelope from a dict
orderbook_stats_response_envelope_from_dict = OrderbookStatsResponseEnvelope.from_dict(orderbook_stats_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


