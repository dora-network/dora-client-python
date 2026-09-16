# AffiliateCashFlow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**kind** | **str** |  | 
**created_at** | **datetime** |  | 
**asset_id** | **UUID** |  | 
**asset_symbol** | **str** |  | 
**amount** | **str** | Decimal value, without binary floating-point rounding. | 

## Example

```python
from dora_client.models.affiliate_cash_flow import AffiliateCashFlow

# TODO update the JSON string below
json = "{}"
# create an instance of AffiliateCashFlow from a JSON string
affiliate_cash_flow_instance = AffiliateCashFlow.from_json(json)
# print the JSON string representation of the object
print(AffiliateCashFlow.to_json())

# convert the object into a dict
affiliate_cash_flow_dict = affiliate_cash_flow_instance.to_dict()
# create an instance of AffiliateCashFlow from a dict
affiliate_cash_flow_from_dict = AffiliateCashFlow.from_dict(affiliate_cash_flow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


