# GetPnLRankingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PnLRankingResponse]**](PnLRankingResponse.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.get_pn_l_ranking_response import GetPnLRankingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPnLRankingResponse from a JSON string
get_pn_l_ranking_response_instance = GetPnLRankingResponse.from_json(json)
# print the JSON string representation of the object
print(GetPnLRankingResponse.to_json())

# convert the object into a dict
get_pn_l_ranking_response_dict = get_pn_l_ranking_response_instance.to_dict()
# create an instance of GetPnLRankingResponse from a dict
get_pn_l_ranking_response_from_dict = GetPnLRankingResponse.from_dict(get_pn_l_ranking_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


