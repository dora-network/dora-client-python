# TransformedAssets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gained** | **Dict[str, str]** | Assets that have been gained by stablecoin equivalence transformations. They cannot be withdrawn from the platform until converted back to the original asset. | [optional] 
**lost** | **Dict[str, str]** | Assets that have been lost by stablecoin equivalence transformations. They can be recovered by converting back any assets gained by stablecoin equivalence transformations. | [optional] 

## Example

```python
from dora_client.models.transformed_assets import TransformedAssets

# TODO update the JSON string below
json = "{}"
# create an instance of TransformedAssets from a JSON string
transformed_assets_instance = TransformedAssets.from_json(json)
# print the JSON string representation of the object
print(TransformedAssets.to_json())

# convert the object into a dict
transformed_assets_dict = transformed_assets_instance.to_dict()
# create an instance of TransformedAssets from a dict
transformed_assets_from_dict = TransformedAssets.from_dict(transformed_assets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


