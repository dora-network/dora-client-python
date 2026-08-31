# UserDeactivationListResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UserDeactivation]**](UserDeactivation.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.user_deactivation_list_response_envelope import UserDeactivationListResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of UserDeactivationListResponseEnvelope from a JSON string
user_deactivation_list_response_envelope_instance = UserDeactivationListResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(UserDeactivationListResponseEnvelope.to_json())

# convert the object into a dict
user_deactivation_list_response_envelope_dict = user_deactivation_list_response_envelope_instance.to_dict()
# create an instance of UserDeactivationListResponseEnvelope from a dict
user_deactivation_list_response_envelope_from_dict = UserDeactivationListResponseEnvelope.from_dict(user_deactivation_list_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


