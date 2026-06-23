# UpdateUserConfigRequest

Request body for PUT /user/{id}/config: update a user changeable details only. Other properties can only be changed by an admin following a manual request by the user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**photo_url** | [**UpdateFieldString**](UpdateFieldString.md) | Optional: URL of the user&#39;s profile photo, optional. | [optional] 
**timezone** | [**UpdateFieldString**](UpdateFieldString.md) | User&#39;s timezone, e.g., &#39;America/New_York&#39;, or an offset. | 
**show_tutorial_cards** | [**UpdateFieldBoolean**](UpdateFieldBoolean.md) | Optional: Whether to show the tutorial. | [optional] 
**notifications_enabled** | [**UpdateFieldBoolean**](UpdateFieldBoolean.md) | Optional: Whether to show the notifications. | [optional] 
**allow_email_notifications** | [**UpdateFieldBoolean**](UpdateFieldBoolean.md) | Optional: Whether to allow email notifications. | [optional] 
**allow_liquidations_notifications** | [**UpdateFieldBoolean**](UpdateFieldBoolean.md) | Optional: Whether to allow liquidations notifications. | [optional] 
**allow_deposit_withdrawal_notifications** | [**UpdateFieldBoolean**](UpdateFieldBoolean.md) | Optional: Whether to allow deposit/withdrawal notifications. | [optional] 
**allow_orders_notifications** | [**UpdateFieldBoolean**](UpdateFieldBoolean.md) | Optional: Whether to allow orders notifications. | [optional] 
**allow_copy_trading** | [**UpdateFieldBoolean**](UpdateFieldBoolean.md) | Optional: Whether to allow copy trading. | [optional] 

## Example

```python
from dora_client.models.update_user_config_request import UpdateUserConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserConfigRequest from a JSON string
update_user_config_request_instance = UpdateUserConfigRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateUserConfigRequest.to_json())

# convert the object into a dict
update_user_config_request_dict = update_user_config_request_instance.to_dict()
# create an instance of UpdateUserConfigRequest from a dict
update_user_config_request_from_dict = UpdateUserConfigRequest.from_dict(update_user_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


