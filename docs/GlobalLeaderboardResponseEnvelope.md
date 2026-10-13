# GlobalLeaderboardResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GlobalLeaderboardResult]**](GlobalLeaderboardResult.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.global_leaderboard_response_envelope import GlobalLeaderboardResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalLeaderboardResponseEnvelope from a JSON string
global_leaderboard_response_envelope_instance = GlobalLeaderboardResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(GlobalLeaderboardResponseEnvelope.to_json())

# convert the object into a dict
global_leaderboard_response_envelope_dict = global_leaderboard_response_envelope_instance.to_dict()
# create an instance of GlobalLeaderboardResponseEnvelope from a dict
global_leaderboard_response_envelope_from_dict = GlobalLeaderboardResponseEnvelope.from_dict(global_leaderboard_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


