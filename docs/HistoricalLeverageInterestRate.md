# HistoricalLeverageInterestRate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **UUID** |  | 
**updated_at** | **datetime** |  | 
**utilization** | **str** |  | 
**maximum_utilization** | **str** |  | 
**minimum_rate** | **str** |  | 
**kink_rate** | **str** |  | 
**maximum_rate** | **str** |  | 
**kink_utilization** | **str** |  | 
**borrowing_yield_rate** | **str** |  | 
**lending_yield_rate** | **str** |  | 
**yield_to_maturity** | **str** |  | 

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


