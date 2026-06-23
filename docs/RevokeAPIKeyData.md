# RevokeAPIKeyData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **UUID** |  | 
**key_id** | **str** |  | 
**label** | **str** |  | 
**is_active** | **bool** |  | 

## Example

```python
from dora_client.models.revoke_api_key_data import RevokeAPIKeyData

# TODO update the JSON string below
json = "{}"
# create an instance of RevokeAPIKeyData from a JSON string
revoke_api_key_data_instance = RevokeAPIKeyData.from_json(json)
# print the JSON string representation of the object
print(RevokeAPIKeyData.to_json())

# convert the object into a dict
revoke_api_key_data_dict = revoke_api_key_data_instance.to_dict()
# create an instance of RevokeAPIKeyData from a dict
revoke_api_key_data_from_dict = RevokeAPIKeyData.from_dict(revoke_api_key_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


