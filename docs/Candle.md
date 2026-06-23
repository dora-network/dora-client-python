# Candle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_book_id** | **UUID** |  | 
**start_timestamp** | **datetime** |  | 
**open** | **str** |  | 
**high** | **str** |  | 
**low** | **str** |  | 
**close** | **str** |  | 
**ytm** | **str** | DEPRECATED: Use close_ytm instead. | [optional] 
**open_ytm** | **str** |  | 
**close_ytm** | **str** |  | 
**high_ytm** | **str** |  | 
**low_ytm** | **str** |  | 
**volume** | **str** |  | 

## Example

```python
from dora_client.models.candle import Candle

# TODO update the JSON string below
json = "{}"
# create an instance of Candle from a JSON string
candle_instance = Candle.from_json(json)
# print the JSON string representation of the object
print(Candle.to_json())

# convert the object into a dict
candle_dict = candle_instance.to_dict()
# create an instance of Candle from a dict
candle_from_dict = Candle.from_dict(candle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


