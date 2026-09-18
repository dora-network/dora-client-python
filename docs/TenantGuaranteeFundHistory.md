# TenantGuaranteeFundHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[TenantGuaranteeFundRow]**](TenantGuaranteeFundRow.md) |  | 
**summary** | [**TenantGuaranteeFundSummary**](TenantGuaranteeFundSummary.md) |  | 

## Example

```python
from dora_client.models.tenant_guarantee_fund_history import TenantGuaranteeFundHistory

# TODO update the JSON string below
json = "{}"
# create an instance of TenantGuaranteeFundHistory from a JSON string
tenant_guarantee_fund_history_instance = TenantGuaranteeFundHistory.from_json(json)
# print the JSON string representation of the object
print(TenantGuaranteeFundHistory.to_json())

# convert the object into a dict
tenant_guarantee_fund_history_dict = tenant_guarantee_fund_history_instance.to_dict()
# create an instance of TenantGuaranteeFundHistory from a dict
tenant_guarantee_fund_history_from_dict = TenantGuaranteeFundHistory.from_dict(tenant_guarantee_fund_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


