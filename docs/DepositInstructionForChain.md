# DepositInstructionForChain

Everything the caller needs to deposit USDC into the Dora vault on a single chain with one signature and one transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_name** | **str** | Human-readable network name, e.g. &#39;Ethereum Mainnet&#39;. | 
**chain_id** | **str** | EVM chain ID. | 
**contract_address** | **str** | The DoraUSDCVault contract address for this chain, as a 0x-prefixed hex string. | 
**usdc_address** | **str** | The ERC-20 USDC token contract on this chain, as a 0x-prefixed hex string. It is the verifying contract of the permit; the spender granted by the permit is contract_address (the vault). | 
**approval** | [**PermitTypedData**](PermitTypedData.md) |  | 
**deposit** | [**DepositCall**](DepositCall.md) |  | 

## Example

```python
from dora_client.models.deposit_instruction_for_chain import DepositInstructionForChain

# TODO update the JSON string below
json = "{}"
# create an instance of DepositInstructionForChain from a JSON string
deposit_instruction_for_chain_instance = DepositInstructionForChain.from_json(json)
# print the JSON string representation of the object
print(DepositInstructionForChain.to_json())

# convert the object into a dict
deposit_instruction_for_chain_dict = deposit_instruction_for_chain_instance.to_dict()
# create an instance of DepositInstructionForChain from a dict
deposit_instruction_for_chain_from_dict = DepositInstructionForChain.from_dict(deposit_instruction_for_chain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


