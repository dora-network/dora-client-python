# PoolPriceResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PoolPrice**](PoolPrice.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.pool_price_response_envelope import PoolPriceResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of PoolPriceResponseEnvelope from a JSON string
pool_price_response_envelope_instance = PoolPriceResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(PoolPriceResponseEnvelope.to_json())

# convert the object into a dict
pool_price_response_envelope_dict = pool_price_response_envelope_instance.to_dict()
# create an instance of PoolPriceResponseEnvelope from a dict
pool_price_response_envelope_from_dict = PoolPriceResponseEnvelope.from_dict(pool_price_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


