# CreateBondReq

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | [**BondKind**](BondKind.md) |  | [optional] 
**coupon_start_at** | **datetime** | Date and time from which coupon payments are calculated. Should only be set if BondKind is COUPON-PAYING | [optional] 
**final_coupon_at** | **datetime** | Date and time at which coupon payments calculations stop. Should only be set if BondKind is COUPON-PAYING | [optional] 
**isin** | **str** |  | [optional] 
**issued_at** | **datetime** |  | [optional] 
**issuer** | **str** |  | [optional] 
**maturity_at** | **datetime** |  | [optional] 
**principal_value** | **str** |  | [optional] 
**payments_per_year** | **int** | Must be non-zero if coupon_start_at is not null. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

