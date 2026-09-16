# AffiliateError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | 
**metadata** | [**Metadata**](Metadata.md) |  | 

## Example

```python
from dora_client.models.affiliate_error import AffiliateError

# TODO update the JSON string below
json = "{}"
# create an instance of AffiliateError from a JSON string
affiliate_error_instance = AffiliateError.from_json(json)
# print the JSON string representation of the object
print(AffiliateError.to_json())

# convert the object into a dict
affiliate_error_dict = affiliate_error_instance.to_dict()
# create an instance of AffiliateError from a dict
affiliate_error_from_dict = AffiliateError.from_dict(affiliate_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


