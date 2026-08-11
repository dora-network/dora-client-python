# TradingChallengeDailySnapshotsResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TradingChallengeDailySnapshot]**](TradingChallengeDailySnapshot.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.trading_challenge_daily_snapshots_response_envelope import TradingChallengeDailySnapshotsResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TradingChallengeDailySnapshotsResponseEnvelope from a JSON string
trading_challenge_daily_snapshots_response_envelope_instance = TradingChallengeDailySnapshotsResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(TradingChallengeDailySnapshotsResponseEnvelope.to_json())

# convert the object into a dict
trading_challenge_daily_snapshots_response_envelope_dict = trading_challenge_daily_snapshots_response_envelope_instance.to_dict()
# create an instance of TradingChallengeDailySnapshotsResponseEnvelope from a dict
trading_challenge_daily_snapshots_response_envelope_from_dict = TradingChallengeDailySnapshotsResponseEnvelope.from_dict(trading_challenge_daily_snapshots_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


