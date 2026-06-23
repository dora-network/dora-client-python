# TenantRestrictions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Tenant ID | 
**deposit_limit** | **str** | Maximum allowed deposit for the tenant. | 
**trade_limit** | **str** | Maximum allowed trade amount for the tenant. | 
**updated_at** | **datetime** | Last update timestamp for the restrictions. | 

## Example

```python
from dora_client.models.tenant_restrictions import TenantRestrictions

# TODO update the JSON string below
json = "{}"
# create an instance of TenantRestrictions from a JSON string
tenant_restrictions_instance = TenantRestrictions.from_json(json)
# print the JSON string representation of the object
print(TenantRestrictions.to_json())

# convert the object into a dict
tenant_restrictions_dict = tenant_restrictions_instance.to_dict()
# create an instance of TenantRestrictions from a dict
tenant_restrictions_from_dict = TenantRestrictions.from_dict(tenant_restrictions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


