# Restriction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deposit_limit** | **str** | Maximum deposit allowed (decimal as string) | [optional] 

## Example

```python
from dora_client.models.restriction import Restriction

# TODO update the JSON string below
json = "{}"
# create an instance of Restriction from a JSON string
restriction_instance = Restriction.from_json(json)
# print the JSON string representation of the object
print(Restriction.to_json())

# convert the object into a dict
restriction_dict = restriction_instance.to_dict()
# create an instance of Restriction from a dict
restriction_from_dict = Restriction.from_dict(restriction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


