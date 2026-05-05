# HistoricalLeverageInterestRate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** |  | 
**updated_at** | **datetime** |  | 
**utilization** | **decimal.Decimal** |  | 
**maximum_utilization** | **decimal.Decimal** |  | 
**minimum_rate** | **decimal.Decimal** |  | 
**kink_rate** | **decimal.Decimal** |  | 
**maximum_rate** | **decimal.Decimal** |  | 
**kink_utilization** | **decimal.Decimal** |  | 
**interest_rate** | **decimal.Decimal** |  | 

## Example

```python
from dora_client.models.historical_leverage_interest_rate import HistoricalLeverageInterestRate

# TODO update the JSON string below
json = "{}"
# create an instance of HistoricalLeverageInterestRate from a JSON string
historical_leverage_interest_rate_instance = HistoricalLeverageInterestRate.from_json(json)
# print the JSON string representation of the object
print(HistoricalLeverageInterestRate.to_json())

# convert the object into a dict
historical_leverage_interest_rate_dict = historical_leverage_interest_rate_instance.to_dict()
# create an instance of HistoricalLeverageInterestRate from a dict
historical_leverage_interest_rate_from_dict = HistoricalLeverageInterestRate.from_dict(historical_leverage_interest_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


