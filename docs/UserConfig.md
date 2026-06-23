# UserConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**photo_url** | **str** |  | [optional] 
**timezone** | **str** | User&#39;s timezone, e.g., &#39;America/New_York&#39;, or an offset. | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**show_tutorial_cards** | **bool** |  | 
**notifications_enabled** | **bool** |  | 
**allow_email_notifications** | **bool** |  | 
**allow_liquidations_notifications** | **bool** |  | 
**allow_deposit_withdrawal_notifications** | **bool** |  | 
**allow_orders_notifications** | **bool** |  | 
**allow_copy_trading** | **bool** |  | 

## Example

```python
from dora_client.models.user_config import UserConfig

# TODO update the JSON string below
json = "{}"
# create an instance of UserConfig from a JSON string
user_config_instance = UserConfig.from_json(json)
# print the JSON string representation of the object
print(UserConfig.to_json())

# convert the object into a dict
user_config_dict = user_config_instance.to_dict()
# create an instance of UserConfig from a dict
user_config_from_dict = UserConfig.from_dict(user_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


