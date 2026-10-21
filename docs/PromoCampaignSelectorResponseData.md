# PromoCampaignSelectorResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaigns** | [**List[PromoCampaignSelectorResponseDataCampaigns]**](PromoCampaignSelectorResponseDataCampaigns.md) |  | 

## Example

```python
from dora_client.models.promo_campaign_selector_response_data import PromoCampaignSelectorResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PromoCampaignSelectorResponseData from a JSON string
promo_campaign_selector_response_data_instance = PromoCampaignSelectorResponseData.from_json(json)
# print the JSON string representation of the object
print(PromoCampaignSelectorResponseData.to_json())

# convert the object into a dict
promo_campaign_selector_response_data_dict = promo_campaign_selector_response_data_instance.to_dict()
# create an instance of PromoCampaignSelectorResponseData from a dict
promo_campaign_selector_response_data_from_dict = PromoCampaignSelectorResponseData.from_dict(promo_campaign_selector_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


