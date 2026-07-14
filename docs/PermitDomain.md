# PermitDomain

The EIP-712 domain separator data for the USDC token on this chain.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | EIP-712 domain name of the USDC token, e.g. &#39;USD Coin&#39;. | 
**version** | **str** | EIP-712 domain version of the USDC token, e.g. &#39;2&#39;. | 
**chain_id** | **int** | EVM chain ID, as a JSON number. | 
**verifying_contract** | **str** | The USDC token contract address, as a 0x-prefixed hex string. | 

## Example

```python
from dora_client.models.permit_domain import PermitDomain

# TODO update the JSON string below
json = "{}"
# create an instance of PermitDomain from a JSON string
permit_domain_instance = PermitDomain.from_json(json)
# print the JSON string representation of the object
print(PermitDomain.to_json())

# convert the object into a dict
permit_domain_dict = permit_domain_instance.to_dict()
# create an instance of PermitDomain from a dict
permit_domain_from_dict = PermitDomain.from_dict(permit_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


