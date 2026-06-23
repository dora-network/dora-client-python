# NewIsolatedAccountRequestV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_account_id** | **UUID** |  | 
**asset_id** | **UUID** |  | 
**quantity** | **str** |  | 
**account_name** | **str** |  | [optional] 

## Example

```python
from dora_client.models.new_isolated_account_request_v2 import NewIsolatedAccountRequestV2

# TODO update the JSON string below
json = "{}"
# create an instance of NewIsolatedAccountRequestV2 from a JSON string
new_isolated_account_request_v2_instance = NewIsolatedAccountRequestV2.from_json(json)
# print the JSON string representation of the object
print(NewIsolatedAccountRequestV2.to_json())

# convert the object into a dict
new_isolated_account_request_v2_dict = new_isolated_account_request_v2_instance.to_dict()
# create an instance of NewIsolatedAccountRequestV2 from a dict
new_isolated_account_request_v2_from_dict = NewIsolatedAccountRequestV2.from_dict(new_isolated_account_request_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


