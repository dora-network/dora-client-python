# DepositArgs

The non-signature arguments to the vault deposit() call. The remaining (v, r, s) arguments come from the permit signature the client obtains by signing the approval.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **str** | Deposit quantity in USDC base units (10^-6 USDC), as a decimal string. Matches the permit&#39;s value. | 
**user_id** | **str** | The caller&#39;s user ID as 16 bytes, 0x-prefixed hex. Stored on-chain with the deposit and mapped back to the user by the indexer. | 
**client_reference_id** | **str** | The bytes32 client reference as a 0x-prefixed hex string. All zero bytes when not supplied. | 
**deadline** | **str** | Unix timestamp (seconds), as a decimal string. Matches the permit&#39;s deadline exactly. | 

## Example

```python
from dora_client.models.deposit_args import DepositArgs

# TODO update the JSON string below
json = "{}"
# create an instance of DepositArgs from a JSON string
deposit_args_instance = DepositArgs.from_json(json)
# print the JSON string representation of the object
print(DepositArgs.to_json())

# convert the object into a dict
deposit_args_dict = deposit_args_instance.to_dict()
# create an instance of DepositArgs from a dict
deposit_args_from_dict = DepositArgs.from_dict(deposit_args_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


