# CreateIntegratorUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**referral_code** | **str** | Optional affiliate code, normalized to uppercase. Accepted only when creating a new account in the program owning tenant. One immutable attribution per user account; a later signup/linking call cannot add or replace it. Invalid or inactive codes fail signup atomically. Independent of QR acquisition attribution. Existing unassigned users can instead use POST /v1/affiliate_referrals/self; earlier activity is excluded. | [optional] 
**signup_source** | **str** | Optional client-reported HTTP(S) signup site URL, used only with referral_code. When omitted, a valid HTTP(S) Origin header is used; other origins are ignored. Only the hostname is stored, without path, query, credentials or fragment. Unknown if neither supplies a usable hostname. Ignored when referral_code is empty. It does not select or authenticate the tenant. | [optional] 
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


