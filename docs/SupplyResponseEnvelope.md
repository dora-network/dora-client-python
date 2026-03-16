# SupplyResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Supply**](Supply.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.supply_response_envelope import SupplyResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SupplyResponseEnvelope from a JSON string
supply_response_envelope_instance = SupplyResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(SupplyResponseEnvelope.to_json())

# convert the object into a dict
supply_response_envelope_dict = supply_response_envelope_instance.to_dict()
# create an instance of SupplyResponseEnvelope from a dict
supply_response_envelope_from_dict = SupplyResponseEnvelope.from_dict(supply_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


