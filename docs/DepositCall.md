# DepositCall

Descriptor of the vault deposit() transaction the client builds after signing the permit. The client splits the permit signature into v/r/s and ABI-encodes function_signature with args plus (v, r, s) to produce the calldata sent to 'to'.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** | The vault contract address, as a 0x-prefixed hex string. | 
**chain_id** | **int** | EVM chain ID, as a JSON number. | 
**value** | **str** | Native currency value to send with the transaction. Always &#39;0&#39;. | 
**function_signature** | **str** | Canonical Solidity signature of the vault&#39;s permit-aware deposit function: deposit(uint256,bytes16,bytes32,uint256,uint8,bytes32,bytes32). | 
**selector** | **str** | The 4-byte ABI call selector of function_signature, as a 0x-prefixed hex string. | 
**args** | [**DepositArgs**](DepositArgs.md) |  | 

## Example

```python
from dora_client.models.deposit_call import DepositCall

# TODO update the JSON string below
json = "{}"
# create an instance of DepositCall from a JSON string
deposit_call_instance = DepositCall.from_json(json)
# print the JSON string representation of the object
print(DepositCall.to_json())

# convert the object into a dict
deposit_call_dict = deposit_call_instance.to_dict()
# create an instance of DepositCall from a dict
deposit_call_from_dict = DepositCall.from_dict(deposit_call_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


