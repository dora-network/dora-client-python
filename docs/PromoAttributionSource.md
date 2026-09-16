# PromoAttributionSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**PromoSourceType**](PromoSourceType.md) |  | 
**source_id** | **str** |  | 
**source_name** | **str** |  | 
**links_issued** | **int** |  | 
**links_claimed** | **int** |  | 
**users_funded** | **int** |  | 
**users_traded** | **int** |  | 
**users_busted** | **int** |  | 
**users_reward_eligible** | **int** |  | 
**users_rewarded** | **int** |  | 
**total_volume** | **str** |  | 
**total_pnl** | **str** |  | 
**promo_credit_issued** | **str** |  | 
**rewards_paid** | **str** |  | 

## Example

```python
from dora_client.models.promo_attribution_source import PromoAttributionSource

# TODO update the JSON string below
json = "{}"
# create an instance of PromoAttributionSource from a JSON string
promo_attribution_source_instance = PromoAttributionSource.from_json(json)
# print the JSON string representation of the object
print(PromoAttributionSource.to_json())

# convert the object into a dict
promo_attribution_source_dict = promo_attribution_source_instance.to_dict()
# create an instance of PromoAttributionSource from a dict
promo_attribution_source_from_dict = PromoAttributionSource.from_dict(promo_attribution_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


