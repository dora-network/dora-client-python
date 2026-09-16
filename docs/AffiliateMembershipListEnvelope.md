# AffiliateMembershipListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AffiliateMembership]**](AffiliateMembership.md) |  | 
**metadata** | [**Metadata**](Metadata.md) |  | 

## Example

```python
from dora_client.models.affiliate_membership_list_envelope import AffiliateMembershipListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of AffiliateMembershipListEnvelope from a JSON string
affiliate_membership_list_envelope_instance = AffiliateMembershipListEnvelope.from_json(json)
# print the JSON string representation of the object
print(AffiliateMembershipListEnvelope.to_json())

# convert the object into a dict
affiliate_membership_list_envelope_dict = affiliate_membership_list_envelope_instance.to_dict()
# create an instance of AffiliateMembershipListEnvelope from a dict
affiliate_membership_list_envelope_from_dict = AffiliateMembershipListEnvelope.from_dict(affiliate_membership_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


