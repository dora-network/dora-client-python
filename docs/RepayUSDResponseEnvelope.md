# RepayUSDResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**RepayUSDResult**](RepayUSDResult.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.repay_usd_response_envelope import RepayUSDResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of RepayUSDResponseEnvelope from a JSON string
repay_usd_response_envelope_instance = RepayUSDResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(RepayUSDResponseEnvelope.to_json())

# convert the object into a dict
repay_usd_response_envelope_dict = repay_usd_response_envelope_instance.to_dict()
# create an instance of RepayUSDResponseEnvelope from a dict
repay_usd_response_envelope_from_dict = RepayUSDResponseEnvelope.from_dict(repay_usd_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


