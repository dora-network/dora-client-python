# UpdateTradingChallengeRequest

Request body for PUT /v1/trading_challenges/{trading_challenge_id}: partially update a trading challenge. A field that is omitted, or sent as null, is left unchanged. Each field accepts either the {update, value} object or the bare value on its own. PENDING CASH and TOURNAMENT challenges accept every field; ACTIVE CASH and TOURNAMENT challenges accept only name, max_users, end and the prize quantities; QR_PROMO challenges accept only name, max_users and end while PENDING or ACTIVE; COMPLETED challenges accept none. tenant_id and status are never updatable, and the participant list is managed by add_users and remove_users.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**UpdateFieldString**](UpdateFieldString.md) | Trading challenge name. | [optional] 
**type** | [**UpdateFieldString**](UpdateFieldString.md) | CASH or TOURNAMENT. Only updatable while the challenge is PENDING. | [optional] 
**max_users** | [**UpdateFieldInteger**](UpdateFieldInteger.md) | Must be &gt; 0 and cannot be lowered below the number of users already registered. | [optional] 
**start** | [**UpdateFieldDateTime**](UpdateFieldDateTime.md) | Only updatable while the challenge is PENDING. | [optional] 
**end** | [**UpdateFieldDateTime**](UpdateFieldDateTime.md) | Must be after start and in the future. | [optional] 
**initial_user_balance** | [**UpdateFieldDecimal**](UpdateFieldDecimal.md) | Must be &gt; 0. Only updatable while the challenge is PENDING. | [optional] 
**gold_prize_quantity** | [**UpdateFieldDecimal**](UpdateFieldDecimal.md) | Must be &gt; 0 for a TOURNAMENT challenge. | [optional] 
**silver_prize_quantity** | [**UpdateFieldDecimal**](UpdateFieldDecimal.md) | Must be &gt;&#x3D; 0. | [optional] 
**bronze_prize_quantity** | [**UpdateFieldDecimal**](UpdateFieldDecimal.md) | Must be &gt;&#x3D; 0. | [optional] 
**pnl_condition** | [**UpdateFieldDecimal**](UpdateFieldDecimal.md) | Must be &gt;&#x3D; 0. Only updatable while the challenge is PENDING. | [optional] 
**total_volume_condition** | [**UpdateFieldDecimal**](UpdateFieldDecimal.md) | Must be &gt;&#x3D; 0. Only updatable while the challenge is PENDING. | [optional] 
**avg_daily_volume_condition** | [**UpdateFieldDecimal**](UpdateFieldDecimal.md) | Must be &gt;&#x3D; 0. Only updatable while the challenge is PENDING. | [optional] 
**minimum_equity_percentage_condition** | [**UpdateFieldInteger**](UpdateFieldInteger.md) | In the range [0,100). Only updatable while the challenge is PENDING. | [optional] 

## Example

```python
from dora_client.models.update_trading_challenge_request import UpdateTradingChallengeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTradingChallengeRequest from a JSON string
update_trading_challenge_request_instance = UpdateTradingChallengeRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateTradingChallengeRequest.to_json())

# convert the object into a dict
update_trading_challenge_request_dict = update_trading_challenge_request_instance.to_dict()
# create an instance of UpdateTradingChallengeRequest from a dict
update_trading_challenge_request_from_dict = UpdateTradingChallengeRequest.from_dict(update_trading_challenge_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


