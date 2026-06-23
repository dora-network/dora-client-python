# LiquidityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position_id** | **UUID** |  | 
**quantity** | **str** |  | 

## Example

```python
from dora_client.models.liquidity_request import LiquidityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LiquidityRequest from a JSON string
liquidity_request_instance = LiquidityRequest.from_json(json)
# print the JSON string representation of the object
print(LiquidityRequest.to_json())

# convert the object into a dict
liquidity_request_dict = liquidity_request_instance.to_dict()
# create an instance of LiquidityRequest from a dict
liquidity_request_from_dict = LiquidityRequest.from_dict(liquidity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


