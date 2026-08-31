# TerminateTradingChallengeResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TerminateTradingChallengeResponse**](TerminateTradingChallengeResponse.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.terminate_trading_challenge_response_envelope import TerminateTradingChallengeResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TerminateTradingChallengeResponseEnvelope from a JSON string
terminate_trading_challenge_response_envelope_instance = TerminateTradingChallengeResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(TerminateTradingChallengeResponseEnvelope.to_json())

# convert the object into a dict
terminate_trading_challenge_response_envelope_dict = terminate_trading_challenge_response_envelope_instance.to_dict()
# create an instance of TerminateTradingChallengeResponseEnvelope from a dict
terminate_trading_challenge_response_envelope_from_dict = TerminateTradingChallengeResponseEnvelope.from_dict(terminate_trading_challenge_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


