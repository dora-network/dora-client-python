# QRRewardPreviewEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**QRRewardPreview**](QRRewardPreview.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.qr_reward_preview_envelope import QRRewardPreviewEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of QRRewardPreviewEnvelope from a JSON string
qr_reward_preview_envelope_instance = QRRewardPreviewEnvelope.from_json(json)
# print the JSON string representation of the object
print(QRRewardPreviewEnvelope.to_json())

# convert the object into a dict
qr_reward_preview_envelope_dict = qr_reward_preview_envelope_instance.to_dict()
# create an instance of QRRewardPreviewEnvelope from a dict
qr_reward_preview_envelope_from_dict = QRRewardPreviewEnvelope.from_dict(qr_reward_preview_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


