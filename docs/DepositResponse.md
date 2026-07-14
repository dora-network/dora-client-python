# DepositResponse

A single USDC deposit observed on-chain.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_chain_id** | **int** | Internal numeric identifier of the chain. | 
**network_name** | **str** | Human-readable network name. | 
**chain_id** | **str** | EVM chain ID. | 
**tx_hash** | **str** | Transaction hash as a 0x-prefixed hex string. | 
**log_index** | **int** | Index of the log within the transaction. | 
**block_number** | **int** |  | 
**block_time** | **datetime** |  | 
**contract_address** | **str** | Vault contract address as a 0x-prefixed hex string. | 
**depositor_address** | **str** | Address that made the deposit, as a 0x-prefixed hex string. | 
**user_id** | **UUID** |  | 
**quantity** | **str** | Human-decimal USDC value (base units divided by 10^6). | 
**client_reference_id** | **str** | Optional client-supplied reference, as a 0x-prefixed hex string. | [optional] 
**status** | [**Web3EventStatus**](Web3EventStatus.md) |  | 
**transaction_id** | **UUID** | Internal transaction ID, present once the deposit has been credited. | [optional] 
**observed_at** | **datetime** |  | 

## Example

```python
from dora_client.models.deposit_response import DepositResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DepositResponse from a JSON string
deposit_response_instance = DepositResponse.from_json(json)
# print the JSON string representation of the object
print(DepositResponse.to_json())

# convert the object into a dict
deposit_response_dict = deposit_response_instance.to_dict()
# create an instance of DepositResponse from a dict
deposit_response_from_dict = DepositResponse.from_dict(deposit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


