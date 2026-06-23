# LiquidationTargetsResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[UUID]** |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.liquidation_targets_response_envelope import LiquidationTargetsResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of LiquidationTargetsResponseEnvelope from a JSON string
liquidation_targets_response_envelope_instance = LiquidationTargetsResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(LiquidationTargetsResponseEnvelope.to_json())

# convert the object into a dict
liquidation_targets_response_envelope_dict = liquidation_targets_response_envelope_instance.to_dict()
# create an instance of LiquidationTargetsResponseEnvelope from a dict
liquidation_targets_response_envelope_from_dict = LiquidationTargetsResponseEnvelope.from_dict(liquidation_targets_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


