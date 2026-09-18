# TenantGuaranteeFundSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**totals_by_tx_kind** | **Dict[str, str]** | Summed balance movement amounts by tx_kind for the filtered result set. | 

## Example

```python
from dora_client.models.tenant_guarantee_fund_summary import TenantGuaranteeFundSummary

# TODO update the JSON string below
json = "{}"
# create an instance of TenantGuaranteeFundSummary from a JSON string
tenant_guarantee_fund_summary_instance = TenantGuaranteeFundSummary.from_json(json)
# print the JSON string representation of the object
print(TenantGuaranteeFundSummary.to_json())

# convert the object into a dict
tenant_guarantee_fund_summary_dict = tenant_guarantee_fund_summary_instance.to_dict()
# create an instance of TenantGuaranteeFundSummary from a dict
tenant_guarantee_fund_summary_from_dict = TenantGuaranteeFundSummary.from_dict(tenant_guarantee_fund_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


