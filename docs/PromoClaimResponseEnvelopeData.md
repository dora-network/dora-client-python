# PromoClaimResponseEnvelopeData


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
**link_type** | **str** | Defaults to SINGLE_USE for existing clients. REUSABLE creates one tracked link without a quantity. | [optional] 
**affiliate_program_id** | **UUID** |  | [optional] 
**affiliate_member_id** | **UUID** | Existing affiliate referrer/member ID, not user ID. | [optional] 
**referral_code** | **str** | An existing code belonging to the selected member. Required with both IDs for reusable links; bound on the server and revalidated at claim time. | [optional] 
**campaign_id** | **UUID** |  | [optional] 
**link_id** | **UUID** |  | [optional] 
**source_id** | **str** |  | [optional] 

## Example

```python
from dora_client.models.promo_claim_response_envelope_data import PromoClaimResponseEnvelopeData

# TODO update the JSON string below
json = "{}"
# create an instance of PromoClaimResponseEnvelopeData from a JSON string
promo_claim_response_envelope_data_instance = PromoClaimResponseEnvelopeData.from_json(json)
# print the JSON string representation of the object
print(PromoClaimResponseEnvelopeData.to_json())

# convert the object into a dict
promo_claim_response_envelope_data_dict = promo_claim_response_envelope_data_instance.to_dict()
# create an instance of PromoClaimResponseEnvelopeData from a dict
promo_claim_response_envelope_data_from_dict = PromoClaimResponseEnvelopeData.from_dict(promo_claim_response_envelope_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


