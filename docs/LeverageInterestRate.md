# LeverageInterestRate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** |  | 
**utilization** | **decimal.Decimal** |  | 
**avg_utilization** | **decimal.Decimal** |  | 
**avg_interest_rate** | **decimal.Decimal** |  | 
**interest_rate** | **decimal.Decimal** |  | 
**start_time** | **datetime** |  | 
**end_time** | **datetime** |  | 

## Example

```python
from dora_client.models.leverage_interest_rate import LeverageInterestRate

# TODO update the JSON string below
json = "{}"
# create an instance of LeverageInterestRate from a JSON string
leverage_interest_rate_instance = LeverageInterestRate.from_json(json)
# print the JSON string representation of the object
print(LeverageInterestRate.to_json())

# convert the object into a dict
leverage_interest_rate_dict = leverage_interest_rate_instance.to_dict()
# create an instance of LeverageInterestRate from a dict
leverage_interest_rate_from_dict = LeverageInterestRate.from_dict(leverage_interest_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


