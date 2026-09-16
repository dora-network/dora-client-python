# WithdrawalResponse

A single USDC withdrawal request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**withdrawal_id** | **UUID** |  | [optional] 
**network_chain_id** | **int** | Internal numeric identifier of the chain. | [optional] 
**network_name** | **str** | Human-readable network name. | [optional] 
**chain_id** | **str** | EVM chain ID. | [optional] 
**user_id** | **UUID** |  | [optional] 
**account_id** | **UUID** |  | [optional] 
**to_address** | **str** | Destination wallet address as a 0x-prefixed hex string. | [optional] 
**quantity** | **str** | Human-decimal USDC quantity to withdraw (base units divided by 10^6). | [optional] 
**fee** | **str** | Human-decimal USDC network fee (base units divided by 10^6). 0 until the requester locks a quoted fee as part of approval. | [optional] 
**status** | [**Web3WithdrawalStatus**](Web3WithdrawalStatus.md) |  | [optional] 
**tx_hash** | **str** | Broadcast withdraw() transaction hash as a 0x-prefixed hex string. Present from &#x60;BROADCAST&#x60; onward. | [optional] 
**failure_reason** | **str** | Reason the withdrawal was rejected or failed. Present for REJECTED/FAILED. | [optional] 
**approved_by** | **UUID** | Admin who approved the withdrawal. Present once approved. | [optional] 
**approved_at** | **datetime** | When the withdrawal was approved. Present once approved. | [optional] 
**settlement_transaction_id** | **UUID** | Ledger settlement transaction. Present once confirmed. | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from dora_client.models.withdrawal_response import WithdrawalResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WithdrawalResponse from a JSON string
withdrawal_response_instance = WithdrawalResponse.from_json(json)
# print the JSON string representation of the object
print(WithdrawalResponse.to_json())

# convert the object into a dict
withdrawal_response_dict = withdrawal_response_instance.to_dict()
# create an instance of WithdrawalResponse from a dict
withdrawal_response_from_dict = WithdrawalResponse.from_dict(withdrawal_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


