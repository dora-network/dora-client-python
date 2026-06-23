# HistoricalLeverageInterestRates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **UUID** |  | 
**start_time** | **datetime** |  | 
**end_time** | **datetime** |  | 
**rates** | [**List[HistoricalLeverageInterestRate]**](HistoricalLeverageInterestRate.md) |  | 

## Example

```python
from dora_client.models.historical_leverage_interest_rates import HistoricalLeverageInterestRates

# TODO update the JSON string below
json = "{}"
# create an instance of HistoricalLeverageInterestRates from a JSON string
historical_leverage_interest_rates_instance = HistoricalLeverageInterestRates.from_json(json)
# print the JSON string representation of the object
print(HistoricalLeverageInterestRates.to_json())

# convert the object into a dict
historical_leverage_interest_rates_dict = historical_leverage_interest_rates_instance.to_dict()
# create an instance of HistoricalLeverageInterestRates from a dict
historical_leverage_interest_rates_from_dict = HistoricalLeverageInterestRates.from_dict(historical_leverage_interest_rates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


