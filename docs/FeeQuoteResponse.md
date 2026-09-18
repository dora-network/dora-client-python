# FeeQuoteResponse

The estimated network fee for one approved USDC withdrawal, alongside a signed, TTL-bound quote token bound to that withdrawal. Submit the token to PUT /v1/web3/withdrawals/{withdrawal_id} to reserve the quoted fee.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**withdrawal_id** | **UUID** | The withdrawal this quote was issued for. The quote token is bound to it and cannot be redeemed against any other withdrawal. | 
**to** | **str** | The withdrawal destination address, read from the withdrawal row. | 
**quantity** | **str** | Human-decimal USDC withdrawal quantity, read from the withdrawal row. | 
**fee** | **str** | The estimated network fee, in human USDC. | 
**fee_base_units** | **str** | The estimated network fee, in micro-USDC base units. | 
**chain_id** | **str** | EVM chain ID the quote was computed for. | 
**quote_token** | **str** | Signed, TTL-bound quote token to submit to PUT /v1/web3/withdrawals/{withdrawal_id} so the server can validate the fee it quoted. It names the withdrawal it was issued for. | 
**expires_at** | **datetime** | When the quote token expires. | 

## Example

```python
from dora_client.models.fee_quote_response import FeeQuoteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FeeQuoteResponse from a JSON string
fee_quote_response_instance = FeeQuoteResponse.from_json(json)
# print the JSON string representation of the object
print(FeeQuoteResponse.to_json())

# convert the object into a dict
fee_quote_response_dict = fee_quote_response_instance.to_dict()
# create an instance of FeeQuoteResponse from a dict
fee_quote_response_from_dict = FeeQuoteResponse.from_dict(fee_quote_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


