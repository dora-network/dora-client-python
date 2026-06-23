# User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**closed_at** | **datetime** |  | [optional] 
**disabled_at** | **datetime** |  | [optional] 
**email** | **str** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**country_of_domicile** | [**CountryCode**](CountryCode.md) |  | 
**native_asset_id** | **UUID** |  | 
**photo_url** | **str** |  | [optional] 
**provider** | **str** |  | [optional] 
**provider_id** | **UUID** |  | [optional] 
**roles** | [**List[UserRole]**](UserRole.md) |  | 
**timezone** | **str** | User&#39;s timezone, e.g., &#39;America/New_York&#39;, or an offset. | [optional] 
**timezone_offset** | **int** | timezone offset in seconds | [optional] 
**verified_at** | **datetime** |  | [optional] 
**show_tutorial_cards** | **bool** |  | 
**notifications_enabled** | **bool** |  | 
**tenant_id** | **str** |  | 
**allow_email_notifications** | **bool** |  | 
**allow_liquidations_notifications** | **bool** |  | 
**allow_deposit_withdrawal_notifications** | **bool** |  | 
**allow_orders_notifications** | **bool** |  | 
**allow_copy_trading** | **bool** |  | 

## Example

```python
from dora_client.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


