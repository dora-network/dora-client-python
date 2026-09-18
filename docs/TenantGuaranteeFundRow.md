# TenantGuaranteeFundRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**tenant_id** | **str** |  | 
**seq** | **int** |  | 
**available** | **str** |  | 
**tx_kind** | **str** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from dora_client.models.tenant_guarantee_fund_row import TenantGuaranteeFundRow

# TODO update the JSON string below
json = "{}"
# create an instance of TenantGuaranteeFundRow from a JSON string
tenant_guarantee_fund_row_instance = TenantGuaranteeFundRow.from_json(json)
# print the JSON string representation of the object
print(TenantGuaranteeFundRow.to_json())

# convert the object into a dict
tenant_guarantee_fund_row_dict = tenant_guarantee_fund_row_instance.to_dict()
# create an instance of TenantGuaranteeFundRow from a dict
tenant_guarantee_fund_row_from_dict = TenantGuaranteeFundRow.from_dict(tenant_guarantee_fund_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


