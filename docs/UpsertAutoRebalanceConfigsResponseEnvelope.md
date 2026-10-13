# UpsertAutoRebalanceConfigsResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AutoRebalanceConfigsData**](AutoRebalanceConfigsData.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.upsert_auto_rebalance_configs_response_envelope import UpsertAutoRebalanceConfigsResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertAutoRebalanceConfigsResponseEnvelope from a JSON string
upsert_auto_rebalance_configs_response_envelope_instance = UpsertAutoRebalanceConfigsResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(UpsertAutoRebalanceConfigsResponseEnvelope.to_json())

# convert the object into a dict
upsert_auto_rebalance_configs_response_envelope_dict = upsert_auto_rebalance_configs_response_envelope_instance.to_dict()
# create an instance of UpsertAutoRebalanceConfigsResponseEnvelope from a dict
upsert_auto_rebalance_configs_response_envelope_from_dict = UpsertAutoRebalanceConfigsResponseEnvelope.from_dict(upsert_auto_rebalance_configs_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


