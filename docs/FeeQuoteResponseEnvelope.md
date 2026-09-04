# FeeQuoteResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**FeeQuoteResponse**](FeeQuoteResponse.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.fee_quote_response_envelope import FeeQuoteResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of FeeQuoteResponseEnvelope from a JSON string
fee_quote_response_envelope_instance = FeeQuoteResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(FeeQuoteResponseEnvelope.to_json())

# convert the object into a dict
fee_quote_response_envelope_dict = fee_quote_response_envelope_instance.to_dict()
# create an instance of FeeQuoteResponseEnvelope from a dict
fee_quote_response_envelope_from_dict = FeeQuoteResponseEnvelope.from_dict(fee_quote_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


