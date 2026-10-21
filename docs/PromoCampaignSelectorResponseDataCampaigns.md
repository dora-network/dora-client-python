# PromoCampaignSelectorResponseDataCampaigns


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**name** | **str** |  | 
**tenant_id** | **str** |  | 
**status** | **str** |  | 
**start** | **datetime** |  | 
**end** | **datetime** |  | 
**max_users** | **int** |  | 

## Example

```python
from dora_client.models.promo_campaign_selector_response_data_campaigns import PromoCampaignSelectorResponseDataCampaigns

# TODO update the JSON string below
json = "{}"
# create an instance of PromoCampaignSelectorResponseDataCampaigns from a JSON string
promo_campaign_selector_response_data_campaigns_instance = PromoCampaignSelectorResponseDataCampaigns.from_json(json)
# print the JSON string representation of the object
print(PromoCampaignSelectorResponseDataCampaigns.to_json())

# convert the object into a dict
promo_campaign_selector_response_data_campaigns_dict = promo_campaign_selector_response_data_campaigns_instance.to_dict()
# create an instance of PromoCampaignSelectorResponseDataCampaigns from a dict
promo_campaign_selector_response_data_campaigns_from_dict = PromoCampaignSelectorResponseDataCampaigns.from_dict(promo_campaign_selector_response_data_campaigns_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


