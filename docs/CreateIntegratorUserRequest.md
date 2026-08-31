# CreateIntegratorUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 
**country_of_domicile** | [**CountryCode**](CountryCode.md) |  | [optional] 
**native_asset_id** | **UUID** | Optional: the user&#39;s native asset ID. Must be a CURRENCY asset; defaults to USD. The USDC asset is never allowed for integrator-created users. | [optional] 
**photo_url** | **str** |  | [optional] 
**provider** | **str** |  | [optional] 
**provider_id** | **UUID** |  | [optional] 
**timezone** | **str** |  | [optional] 
**challenge_id** | **UUID** | Optional: sign the new user up for this trading challenge. This creates a PENDING registration request that an admin, the tenant&#39;s integrator or one of the challenge&#39;s managers must approve before the user is actually enrolled. The challenge must belong to the new user&#39;s tenant and still be open for entries, otherwise the whole sign-up fails. | [optional] 

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


