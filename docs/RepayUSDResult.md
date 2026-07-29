# RepayUSDResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position_id** | **UUID** |  | 
**asset_id** | **UUID** |  | 
**repaid** | **str** |  | 
**transaction_id** | **UUID** |  | 

## Example

```python
from dora_client.models.repay_usd_result import RepayUSDResult

# TODO update the JSON string below
json = "{}"
# create an instance of RepayUSDResult from a JSON string
repay_usd_result_instance = RepayUSDResult.from_json(json)
# print the JSON string representation of the object
print(RepayUSDResult.to_json())

# convert the object into a dict
repay_usd_result_dict = repay_usd_result_instance.to_dict()
# create an instance of RepayUSDResult from a dict
repay_usd_result_from_dict = RepayUSDResult.from_dict(repay_usd_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


