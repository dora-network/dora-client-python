# RealizedPnlSettlement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | The ID of the realized PnL settlement | 
**user_id** | **UUID** | The ID of the user associated with the realized PnL settlement | 
**tenant_id** | **str** | The ID of the tenant associated with the realized PnL settlement | 
**position_id** | **UUID** | The ID of the position associated with the realized PnL settlement | 
**order_id** | **UUID** | The ID of the position-closing order associated with the realized PnL settlement | 
**realized_usd** | **str** | The amount of realized PnL in USD | 
**settled_at** | **datetime** | The timestamp when the realized PnL settlement was settled | [optional] 
**created_at** | **datetime** | The timestamp when the realized PnL settlement was created | 

## Example

```python
from dora_client.models.realized_pnl_settlement import RealizedPnlSettlement

# TODO update the JSON string below
json = "{}"
# create an instance of RealizedPnlSettlement from a JSON string
realized_pnl_settlement_instance = RealizedPnlSettlement.from_json(json)
# print the JSON string representation of the object
print(RealizedPnlSettlement.to_json())

# convert the object into a dict
realized_pnl_settlement_dict = realized_pnl_settlement_instance.to_dict()
# create an instance of RealizedPnlSettlement from a dict
realized_pnl_settlement_from_dict = RealizedPnlSettlement.from_dict(realized_pnl_settlement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


