# CreateIntegratorUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**country_of_domicile** | [**CountryCode**](CountryCode.md) |  | [optional] 
**native_asset_id** | **UUID** |  | [optional] 
**photo_url** | **str** |  | [optional] 
**provider** | **str** |  | [optional] 
**provider_id** | **UUID** |  | [optional] 
**timezone** | **str** |  | [optional] 

## Example

```python
from dora_client.models.create_integrator_user_request import CreateIntegratorUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateIntegratorUserRequest from a JSON string
create_integrator_user_request_instance = CreateIntegratorUserRequest.from_json(json)
# print the JSON string representation of the object
print(CreateIntegratorUserRequest.to_json())

# convert the object into a dict
create_integrator_user_request_dict = create_integrator_user_request_instance.to_dict()
# create an instance of CreateIntegratorUserRequest from a dict
create_integrator_user_request_from_dict = CreateIntegratorUserRequest.from_dict(create_integrator_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


