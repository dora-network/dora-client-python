# Liquidity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_book_id** | **UUID** |  | 
**position_id** | **UUID** |  | 
**transaction_id** | **UUID** |  | 
**base_quantity** | **str** |  | 
**quote_quantity** | **str** |  | 
**shares_quantity** | **str** |  | 

## Example

```python
from dora_client.models.liquidity import Liquidity

# TODO update the JSON string below
json = "{}"
# create an instance of Liquidity from a JSON string
liquidity_instance = Liquidity.from_json(json)
# print the JSON string representation of the object
print(Liquidity.to_json())

# convert the object into a dict
liquidity_dict = liquidity_instance.to_dict()
# create an instance of Liquidity from a dict
liquidity_from_dict = Liquidity.from_dict(liquidity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


