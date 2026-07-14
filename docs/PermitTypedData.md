# PermitTypedData

An EIP-712 typed-data message in the exact shape expected by eth_signTypedData_v4. The user signs it to authorize the vault as a USDC spender via EIP-2612 permit.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**types** | **Dict[str, List[TypedDataField]]** | EIP-712 type definitions, keyed by type name (&#39;EIP712Domain&#39; and &#39;Permit&#39;). | 
**primary_type** | **str** | Always &#39;Permit&#39;. | 
**domain** | [**PermitDomain**](PermitDomain.md) |  | 
**message** | [**PermitMessage**](PermitMessage.md) |  | 

## Example

```python
from dora_client.models.permit_typed_data import PermitTypedData

# TODO update the JSON string below
json = "{}"
# create an instance of PermitTypedData from a JSON string
permit_typed_data_instance = PermitTypedData.from_json(json)
# print the JSON string representation of the object
print(PermitTypedData.to_json())

# convert the object into a dict
permit_typed_data_dict = permit_typed_data_instance.to_dict()
# create an instance of PermitTypedData from a dict
permit_typed_data_from_dict = PermitTypedData.from_dict(permit_typed_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


