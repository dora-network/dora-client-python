# TenantGuaranteeFundHistoryResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TenantGuaranteeFundHistory**](TenantGuaranteeFundHistory.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.tenant_guarantee_fund_history_response_envelope import TenantGuaranteeFundHistoryResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TenantGuaranteeFundHistoryResponseEnvelope from a JSON string
tenant_guarantee_fund_history_response_envelope_instance = TenantGuaranteeFundHistoryResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(TenantGuaranteeFundHistoryResponseEnvelope.to_json())

# convert the object into a dict
tenant_guarantee_fund_history_response_envelope_dict = tenant_guarantee_fund_history_response_envelope_instance.to_dict()
# create an instance of TenantGuaranteeFundHistoryResponseEnvelope from a dict
tenant_guarantee_fund_history_response_envelope_from_dict = TenantGuaranteeFundHistoryResponseEnvelope.from_dict(tenant_guarantee_fund_history_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


