# WithdrawalInitiation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**withdrawal_id** | **UUID** |  | 
**user_id** | **UUID** |  | 
**position_id** | **UUID** |  | 
**asset_id** | **UUID** |  | 
**quantity** | **str** |  | 
**status** | [**WithdrawalStatus**](WithdrawalStatus.md) |  | 
**created_at** | **datetime** |  | 
**created_by** | **UUID** |  | 
**updated_at** | **datetime** |  | 
**updated_by** | **UUID** |  | 
**reason** | **str** |  | 

## Example

```python
from dora_client.models.withdrawal_initiation import WithdrawalInitiation

# TODO update the JSON string below
json = "{}"
# create an instance of WithdrawalInitiation from a JSON string
withdrawal_initiation_instance = WithdrawalInitiation.from_json(json)
# print the JSON string representation of the object
print(WithdrawalInitiation.to_json())

# convert the object into a dict
withdrawal_initiation_dict = withdrawal_initiation_instance.to_dict()
# create an instance of WithdrawalInitiation from a dict
withdrawal_initiation_from_dict = WithdrawalInitiation.from_dict(withdrawal_initiation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


