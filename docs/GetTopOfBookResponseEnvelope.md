# GetTopOfBookResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**OrderBookTop**](OrderBookTop.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.get_top_of_book_response_envelope import GetTopOfBookResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of GetTopOfBookResponseEnvelope from a JSON string
get_top_of_book_response_envelope_instance = GetTopOfBookResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(GetTopOfBookResponseEnvelope.to_json())

# convert the object into a dict
get_top_of_book_response_envelope_dict = get_top_of_book_response_envelope_instance.to_dict()
# create an instance of GetTopOfBookResponseEnvelope from a dict
get_top_of_book_response_envelope_from_dict = GetTopOfBookResponseEnvelope.from_dict(get_top_of_book_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


