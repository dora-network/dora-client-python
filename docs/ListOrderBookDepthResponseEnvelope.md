# ListOrderBookDepthResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**OrderBookDepth**](OrderBookDepth.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.list_order_book_depth_response_envelope import ListOrderBookDepthResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListOrderBookDepthResponseEnvelope from a JSON string
list_order_book_depth_response_envelope_instance = ListOrderBookDepthResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(ListOrderBookDepthResponseEnvelope.to_json())

# convert the object into a dict
list_order_book_depth_response_envelope_dict = list_order_book_depth_response_envelope_instance.to_dict()
# create an instance of ListOrderBookDepthResponseEnvelope from a dict
list_order_book_depth_response_envelope_from_dict = ListOrderBookDepthResponseEnvelope.from_dict(list_order_book_depth_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


