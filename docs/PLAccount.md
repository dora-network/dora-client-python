# PLAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The ID of the account holding the position | 
**account_name** | **str** | The name of the account holding the position | 
**is_global** | **bool** | Whether the account is the global or an isolated account | 
**assets** | [**List[PLAsset]**](PLAsset.md) |  | 
**summary** | [**PLSummary**](PLSummary.md) |  | 

## Example

```python
from dora_client.models.pl_account import PLAccount

# TODO update the JSON string below
json = "{}"
# create an instance of PLAccount from a JSON string
pl_account_instance = PLAccount.from_json(json)
# print the JSON string representation of the object
print(PLAccount.to_json())

# convert the object into a dict
pl_account_dict = pl_account_instance.to_dict()
# create an instance of PLAccount from a dict
pl_account_from_dict = PLAccount.from_dict(pl_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


