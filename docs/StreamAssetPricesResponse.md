# StreamAssetPricesResponse

Map of asset prices keyed by asset ID. Format: {\"asset_id\": {\"asset_id\": \"uuid\", \"price\": \"decimal\", \"time\": \"date-time\"}}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from dora_client.models.stream_asset_prices_response import StreamAssetPricesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StreamAssetPricesResponse from a JSON string
stream_asset_prices_response_instance = StreamAssetPricesResponse.from_json(json)
# print the JSON string representation of the object
print(StreamAssetPricesResponse.to_json())

# convert the object into a dict
stream_asset_prices_response_dict = stream_asset_prices_response_instance.to_dict()
# create an instance of StreamAssetPricesResponse from a dict
stream_asset_prices_response_from_dict = StreamAssetPricesResponse.from_dict(stream_asset_prices_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


