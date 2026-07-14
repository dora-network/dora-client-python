# DepositInstructionsResponse

Per-chain instructions for depositing USDC into the Dora vault via EIP-2612 permit.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **UUID** | The authenticated user the instructions are issued for. | 
**owner_address** | **str** | The wallet address the instructions were issued for, echoed from the request. | 
**quantity** | **str** | Human-decimal USDC deposit quantity, echoed from the request. | 
**chains** | [**List[DepositInstructionForChain]**](DepositInstructionForChain.md) |  | 

## Example

```python
from dora_client.models.deposit_instructions_response import DepositInstructionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DepositInstructionsResponse from a JSON string
deposit_instructions_response_instance = DepositInstructionsResponse.from_json(json)
# print the JSON string representation of the object
print(DepositInstructionsResponse.to_json())

# convert the object into a dict
deposit_instructions_response_dict = deposit_instructions_response_instance.to_dict()
# create an instance of DepositInstructionsResponse from a dict
deposit_instructions_response_from_dict = DepositInstructionsResponse.from_dict(deposit_instructions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


