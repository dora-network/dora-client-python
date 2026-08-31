# UserDeactivation

An admin-requested account deactivation. A non-REACTIVATED request blocks the user's trading, funding, and transfers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deactivation_id** | **UUID** |  | 
**user_id** | **UUID** |  | 
**requested_by** | **UUID** | Admin that requested the deactivation. | 
**reason** | **str** |  | 
**status** | **str** | PENDING: wind-down in progress. FAILED: wind-down gave up; admin can re-trigger. COMPLETED: account deactivated. REACTIVATED: blocks lifted. | 
**attempts** | **int** | Wind-down attempts performed so far. | 
**result** | **str** | Latest wind-down outcome or error summary. | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**completed_at** | **datetime** |  | [optional] 
**reactivated_by** | **UUID** |  | [optional] 
**reactivated_at** | **datetime** |  | [optional] 

## Example

```python
from dora_client.models.user_deactivation import UserDeactivation

# TODO update the JSON string below
json = "{}"
# create an instance of UserDeactivation from a JSON string
user_deactivation_instance = UserDeactivation.from_json(json)
# print the JSON string representation of the object
print(UserDeactivation.to_json())

# convert the object into a dict
user_deactivation_dict = user_deactivation_instance.to_dict()
# create an instance of UserDeactivation from a dict
user_deactivation_from_dict = UserDeactivation.from_dict(user_deactivation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


