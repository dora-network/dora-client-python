# TypedDataField

A single field in an EIP-712 type definition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | **str** | Solidity type, e.g. &#39;address&#39; or &#39;uint256&#39;. | 

## Example

```python
from dora_client.models.typed_data_field import TypedDataField

# TODO update the JSON string below
json = "{}"
# create an instance of TypedDataField from a JSON string
typed_data_field_instance = TypedDataField.from_json(json)
# print the JSON string representation of the object
print(TypedDataField.to_json())

# convert the object into a dict
typed_data_field_dict = typed_data_field_instance.to_dict()
# create an instance of TypedDataField from a dict
typed_data_field_from_dict = TypedDataField.from_dict(typed_data_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


