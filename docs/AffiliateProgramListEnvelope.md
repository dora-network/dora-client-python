# AffiliateProgramListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AffiliateProgram]**](AffiliateProgram.md) |  | 
**metadata** | [**Metadata**](Metadata.md) |  | 

## Example

```python
from dora_client.models.affiliate_program_list_envelope import AffiliateProgramListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of AffiliateProgramListEnvelope from a JSON string
affiliate_program_list_envelope_instance = AffiliateProgramListEnvelope.from_json(json)
# print the JSON string representation of the object
print(AffiliateProgramListEnvelope.to_json())

# convert the object into a dict
affiliate_program_list_envelope_dict = affiliate_program_list_envelope_instance.to_dict()
# create an instance of AffiliateProgramListEnvelope from a dict
affiliate_program_list_envelope_from_dict = AffiliateProgramListEnvelope.from_dict(affiliate_program_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


