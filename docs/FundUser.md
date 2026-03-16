# FundUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**position_id** | **str** |  | 
**asset_id** | **str** |  | 
**final_quantity** | **str** |  | 
**amount** | **str** |  | 

## Example

```python
from dora_client.models.fund_user import FundUser

# TODO update the JSON string below
json = "{}"
# create an instance of FundUser from a JSON string
fund_user_instance = FundUser.from_json(json)
# print the JSON string representation of the object
print(FundUser.to_json())

# convert the object into a dict
fund_user_dict = fund_user_instance.to_dict()
# create an instance of FundUser from a dict
fund_user_from_dict = FundUser.from_dict(fund_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


