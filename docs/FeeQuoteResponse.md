# FeeQuoteResponse

The estimated network fee to withdraw USDC via web3, alongside a signed, TTL-bound quote token the client submits with a later withdrawal so the server can validate the fee it was quoted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** | The withdrawal destination address, echoed from the request. | 
**quantity** | **str** | Human-decimal USDC withdrawal quantity, echoed from the request. | 
**fee** | **str** | The estimated network fee, in human USDC. | 
**fee_base_units** | **str** | The estimated network fee, in micro-USDC base units. | 
**chain_id** | **str** | EVM chain ID the quote was computed for. | 
**quote_token** | **str** | Signed, TTL-bound quote token to submit with a later withdrawal so the server can validate the fee it was quoted. | 
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


