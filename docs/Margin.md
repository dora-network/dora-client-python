# Margin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **str** | The total margin available from this position. | 
**used** | **str** | The amount of margin used from this position. | 
**remaining** | **str** | The margin remaining available from this position. | 

## Example

```python
from dora_client.models.margin import Margin

# TODO update the JSON string below
json = "{}"
# create an instance of Margin from a JSON string
margin_instance = Margin.from_json(json)
# print the JSON string representation of the object
print(Margin.to_json())

# convert the object into a dict
margin_dict = margin_instance.to_dict()
# create an instance of Margin from a dict
margin_from_dict = Margin.from_dict(margin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


