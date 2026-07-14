# PermitMessage

The EIP-2612 Permit struct the user signs. The uint256 fields are decimal strings to avoid JSON number precision loss.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner** | **str** | The user&#39;s wallet address (permit owner), as a 0x-prefixed hex string. | 
**spender** | **str** | The vault contract address granted the allowance, as a 0x-prefixed hex string. | 
**value** | **str** | Approved quantity in USDC base units (10^-6 USDC), as a decimal string. | 
**nonce** | **str** | The owner&#39;s current USDC permit nonce on this chain, as a decimal string. | 
**deadline** | **str** | Unix timestamp (seconds) at which the permit expires, as a decimal string. One hour from issuance. | 

## Example

```python
from dora_client.models.permit_message import PermitMessage

# TODO update the JSON string below
json = "{}"
# create an instance of PermitMessage from a JSON string
permit_message_instance = PermitMessage.from_json(json)
# print the JSON string representation of the object
print(PermitMessage.to_json())

# convert the object into a dict
permit_message_dict = permit_message_instance.to_dict()
# create an instance of PermitMessage from a dict
permit_message_from_dict = PermitMessage.from_dict(permit_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


