# PLSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leverage** | **str** | The leverage used to obtain the position on the isolated account | 
**account_equity** | **str** |  | 
**available** | **str** |  | 
**health** | **str** |  | 
**ltv** | **str** |  | 

## Example

```python
from dora_client.models.pl_summary import PLSummary

# TODO update the JSON string below
json = "{}"
# create an instance of PLSummary from a JSON string
pl_summary_instance = PLSummary.from_json(json)
# print the JSON string representation of the object
print(PLSummary.to_json())

# convert the object into a dict
pl_summary_dict = pl_summary_instance.to_dict()
# create an instance of PLSummary from a dict
pl_summary_from_dict = PLSummary.from_dict(pl_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


