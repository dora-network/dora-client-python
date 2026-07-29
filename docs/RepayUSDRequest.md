# RepayUSDRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position_id** | **UUID** |  | 

## Example

```python
from dora_client.models.repay_usd_request import RepayUSDRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RepayUSDRequest from a JSON string
repay_usd_request_instance = RepayUSDRequest.from_json(json)
# print the JSON string representation of the object
print(RepayUSDRequest.to_json())

# convert the object into a dict
repay_usd_request_dict = repay_usd_request_instance.to_dict()
# create an instance of RepayUSDRequest from a dict
repay_usd_request_from_dict = RepayUSDRequest.from_dict(repay_usd_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


