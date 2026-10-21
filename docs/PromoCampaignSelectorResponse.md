# PromoCampaignSelectorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PromoCampaignSelectorResponseData**](PromoCampaignSelectorResponseData.md) |  | 

## Example

```python
from dora_client.models.promo_campaign_selector_response import PromoCampaignSelectorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PromoCampaignSelectorResponse from a JSON string
promo_campaign_selector_response_instance = PromoCampaignSelectorResponse.from_json(json)
# print the JSON string representation of the object
print(PromoCampaignSelectorResponse.to_json())

# convert the object into a dict
promo_campaign_selector_response_dict = promo_campaign_selector_response_instance.to_dict()
# create an instance of PromoCampaignSelectorResponse from a dict
promo_campaign_selector_response_from_dict = PromoCampaignSelectorResponse.from_dict(promo_campaign_selector_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


