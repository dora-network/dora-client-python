# RealizedPnlSettlements


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settlements** | [**List[RealizedPnlSettlement]**](RealizedPnlSettlement.md) | A list of realized PnL settlements matching the query parameters of the request | [optional] 
**user_totals** | **Dict[str, str]** | A map of user IDs to their total realized PnL in USD across all settlements included in the response | [optional] 
**tenant_totals** | **Dict[str, str]** | A map of tenant IDs to their total realized PnL in USD across all settlements included in the response | [optional] 
**user_totals_unsettled** | **Dict[str, str]** | A map of user IDs to their total realized PnL in USD across unsettled settlements (where settled_at is null) included in the response | [optional] 
**tenant_totals_unsettled** | **Dict[str, str]** | A map of tenant IDs to their total realized PnL in USD across unsettled settlements (where settled_at is null) included in the response | [optional] 

## Example

```python
from dora_client.models.realized_pnl_settlements import RealizedPnlSettlements

# TODO update the JSON string below
json = "{}"
# create an instance of RealizedPnlSettlements from a JSON string
realized_pnl_settlements_instance = RealizedPnlSettlements.from_json(json)
# print the JSON string representation of the object
print(RealizedPnlSettlements.to_json())

# convert the object into a dict
realized_pnl_settlements_dict = realized_pnl_settlements_instance.to_dict()
# create an instance of RealizedPnlSettlements from a dict
realized_pnl_settlements_from_dict = RealizedPnlSettlements.from_dict(realized_pnl_settlements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


