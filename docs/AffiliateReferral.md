# AffiliateReferral

User profile and affiliate activity. Trade metrics, realized PnL and cash-flow counts/dates include only events at or after attributed_at. Signup and KYC fields describe the user profile.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **UUID** |  | 
**program_id** | **UUID** |  | 
**referrer_id** | **UUID** |  | 
**referrer_user_id** | **UUID** |  | 
**signup_source** | **str** | Client-reported signup hostname. Empty means unknown. | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**email** | **str** |  | 
**signed_up_at** | **datetime** |  | 
**kyc_completed** | **bool** |  | 
**kyc_completed_at** | **datetime** |  | 
**discord_status** | **str** | No Discord membership integration is currently available. Unknown must not be interpreted as not joined. | 
**deposit_count** | **int** |  | 
**withdrawal_count** | **int** |  | 
**has_traded** | **bool** |  | 
**first_deposit_at** | **datetime** |  | 
**last_deposit_at** | **datetime** |  | 
**first_withdrawal_at** | **datetime** |  | 
**last_withdrawal_at** | **datetime** |  | 
**daily_volume_usd** | **str** | Sum of absolute executed FILL quantity1 on USD-quoted trades during the selected UTC day. Both buy and sell executions count, once per user-side fill. | 
**monthly_volume_usd** | **str** | Same executed USD quote-notional definition for the calendar month containing date. | 
**daily_realized_pnl_usd** | **str** | Sum of realized_pnl_settlements.realized_usd created during the selected UTC day, matching the existing PnL ranking convention. Excludes unrealized PnL; this is not total account equity change. | 
**attributed_at** | **datetime** | Immutable referral assignment time. Earlier activity is excluded from affiliate metrics and cash flows. | 
**monthly_realized_pnl_usd** | **str** | Realized PnL for the UTC calendar month containing date, including only settlements at or after attributed_at. | 

## Example

```python
from dora_client.models.affiliate_referral import AffiliateReferral

# TODO update the JSON string below
json = "{}"
# create an instance of AffiliateReferral from a JSON string
affiliate_referral_instance = AffiliateReferral.from_json(json)
# print the JSON string representation of the object
print(AffiliateReferral.to_json())

# convert the object into a dict
affiliate_referral_dict = affiliate_referral_instance.to_dict()
# create an instance of AffiliateReferral from a dict
affiliate_referral_from_dict = AffiliateReferral.from_dict(affiliate_referral_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


