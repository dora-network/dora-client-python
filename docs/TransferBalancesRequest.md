# TransferBalancesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_position_id** | **UUID** |  | 
**to_position_id** | **UUID** |  | 
**asset_id** | **UUID** |  | 
**quantity** | **str** |  | 

## Example

```python
from dora_client.models.transfer_balances_request import TransferBalancesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransferBalancesRequest from a JSON string
transfer_balances_request_instance = TransferBalancesRequest.from_json(json)
# print the JSON string representation of the object
print(TransferBalancesRequest.to_json())

# convert the object into a dict
transfer_balances_request_dict = transfer_balances_request_instance.to_dict()
# create an instance of TransferBalancesRequest from a dict
transfer_balances_request_from_dict = TransferBalancesRequest.from_dict(transfer_balances_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


