# CreateWithdrawalRequest

Request to create a USDC withdrawal. No fee quote is required: creating the request reserves the quantity only, and the withdrawal's fee is quoted and locked later, as part of approval.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**withdrawal_id** | **UUID** | Client-supplied idempotency key (also the on-chain correlation key). Repeating a request with the same withdrawal_id has no additional effect. | 
**to_address** | **str** | Destination wallet address as a 0x-prefixed hex string. Must not be the zero address. | 
**quantity** | **str** | Human-decimal USDC quantity to withdraw. Must be positive and no finer than USDC&#39;s 6 on-chain decimals. | 

## Example

```python
from dora_client.models.create_withdrawal_request import CreateWithdrawalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWithdrawalRequest from a JSON string
create_withdrawal_request_instance = CreateWithdrawalRequest.from_json(json)
# print the JSON string representation of the object
print(CreateWithdrawalRequest.to_json())

# convert the object into a dict
create_withdrawal_request_dict = create_withdrawal_request_instance.to_dict()
# create an instance of CreateWithdrawalRequest from a dict
create_withdrawal_request_from_dict = CreateWithdrawalRequest.from_dict(create_withdrawal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


