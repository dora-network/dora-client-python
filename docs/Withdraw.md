# Withdraw


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position_id** | **str** |  | 
**transaction_id** | **str** |  | 
**asset_id** | **str** |  | 
**quantity** | **str** |  | 

## Example

```python
from dora_client.models.withdraw import Withdraw

# TODO update the JSON string below
json = "{}"
# create an instance of Withdraw from a JSON string
withdraw_instance = Withdraw.from_json(json)
# print the JSON string representation of the object
print(Withdraw.to_json())

# convert the object into a dict
withdraw_dict = withdraw_instance.to_dict()
# create an instance of Withdraw from a dict
withdraw_from_dict = Withdraw.from_dict(withdraw_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


