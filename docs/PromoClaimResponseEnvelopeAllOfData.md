# PromoClaimResponseEnvelopeAllOfData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | [**PromoClaimState**](PromoClaimState.md) |  | 
**email** | **str** |  | [optional] 
**campaign_name** | **str** |  | [optional] 
**promo_credit** | **str** |  | [optional] 
**min_reward_amount** | **str** |  | [optional] 
**max_reward_amount** | **str** |  | [optional] 
**target_equity** | **str** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**source_name** | **str** |  | [optional] 

## Example

```python
from dora_client.models.promo_claim_response_envelope_all_of_data import PromoClaimResponseEnvelopeAllOfData

# TODO update the JSON string below
json = "{}"
# create an instance of PromoClaimResponseEnvelopeAllOfData from a JSON string
promo_claim_response_envelope_all_of_data_instance = PromoClaimResponseEnvelopeAllOfData.from_json(json)
# print the JSON string representation of the object
print(PromoClaimResponseEnvelopeAllOfData.to_json())

# convert the object into a dict
promo_claim_response_envelope_all_of_data_dict = promo_claim_response_envelope_all_of_data_instance.to_dict()
# create an instance of PromoClaimResponseEnvelopeAllOfData from a dict
promo_claim_response_envelope_all_of_data_from_dict = PromoClaimResponseEnvelopeAllOfData.from_dict(promo_claim_response_envelope_all_of_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


