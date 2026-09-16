# AffiliateCashFlowReportEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AffiliateCashFlowReport**](AffiliateCashFlowReport.md) |  | 
**metadata** | [**Metadata**](Metadata.md) |  | 

## Example

```python
from dora_client.models.affiliate_cash_flow_report_envelope import AffiliateCashFlowReportEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of AffiliateCashFlowReportEnvelope from a JSON string
affiliate_cash_flow_report_envelope_instance = AffiliateCashFlowReportEnvelope.from_json(json)
# print the JSON string representation of the object
print(AffiliateCashFlowReportEnvelope.to_json())

# convert the object into a dict
affiliate_cash_flow_report_envelope_dict = affiliate_cash_flow_report_envelope_instance.to_dict()
# create an instance of AffiliateCashFlowReportEnvelope from a dict
affiliate_cash_flow_report_envelope_from_dict = AffiliateCashFlowReportEnvelope.from_dict(affiliate_cash_flow_report_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


