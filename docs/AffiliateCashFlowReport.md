# AffiliateCashFlowReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cash_flows** | [**List[AffiliateCashFlow]**](AffiliateCashFlow.md) |  | 
**has_more** | **bool** |  | 

## Example

```python
from dora_client.models.affiliate_cash_flow_report import AffiliateCashFlowReport

# TODO update the JSON string below
json = "{}"
# create an instance of AffiliateCashFlowReport from a JSON string
affiliate_cash_flow_report_instance = AffiliateCashFlowReport.from_json(json)
# print the JSON string representation of the object
print(AffiliateCashFlowReport.to_json())

# convert the object into a dict
affiliate_cash_flow_report_dict = affiliate_cash_flow_report_instance.to_dict()
# create an instance of AffiliateCashFlowReport from a dict
affiliate_cash_flow_report_from_dict = AffiliateCashFlowReport.from_dict(affiliate_cash_flow_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


