# QRRewardPreview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trading_challenge_id** | **UUID** |  | 
**state** | **str** |  | 
**current_equity** | **str** |  | [optional] 
**promo_credit** | **str** |  | 
**eligible_profit** | **str** |  | [optional] 
**projected_reward** | **str** |  | [optional] 
**reward_amount** | **str** |  | [optional] 
**min_reward_amount** | **str** |  | 
**max_reward_amount** | **str** |  | 
**reward_deadline_at** | **datetime** |  | 
**kyc_completed** | **bool** |  | 
**kyc_url** | **str** |  | [optional] 
**blockers** | **List[str]** |  | 

## Example

```python
from dora_client.models.qr_reward_preview import QRRewardPreview

# TODO update the JSON string below
json = "{}"
# create an instance of QRRewardPreview from a JSON string
qr_reward_preview_instance = QRRewardPreview.from_json(json)
# print the JSON string representation of the object
print(QRRewardPreview.to_json())

# convert the object into a dict
qr_reward_preview_dict = qr_reward_preview_instance.to_dict()
# create an instance of QRRewardPreview from a dict
qr_reward_preview_from_dict = QRRewardPreview.from_dict(qr_reward_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


