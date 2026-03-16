# StreamCandlesEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**val** | [**Candle**](Candle.md) |  | 
**time** | **datetime** | The timestamp when the data was created | 

## Example

```python
from dora_client.models.stream_candles_entry import StreamCandlesEntry

# TODO update the JSON string below
json = "{}"
# create an instance of StreamCandlesEntry from a JSON string
stream_candles_entry_instance = StreamCandlesEntry.from_json(json)
# print the JSON string representation of the object
print(StreamCandlesEntry.to_json())

# convert the object into a dict
stream_candles_entry_dict = stream_candles_entry_instance.to_dict()
# create an instance of StreamCandlesEntry from a dict
stream_candles_entry_from_dict = StreamCandlesEntry.from_dict(stream_candles_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


