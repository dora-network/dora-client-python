# AffiliateProgramEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AffiliateProgram**](AffiliateProgram.md) |  | 
**metadata** | [**Metadata**](Metadata.md) |  | 

## Example

```python
from dora_client.models.affiliate_program_envelope import AffiliateProgramEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of AffiliateProgramEnvelope from a JSON string
affiliate_program_envelope_instance = AffiliateProgramEnvelope.from_json(json)
# print the JSON string representation of the object
print(AffiliateProgramEnvelope.to_json())

# convert the object into a dict
affiliate_program_envelope_dict = affiliate_program_envelope_instance.to_dict()
# create an instance of AffiliateProgramEnvelope from a dict
affiliate_program_envelope_from_dict = AffiliateProgramEnvelope.from_dict(affiliate_program_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


