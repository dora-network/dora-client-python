# TransferAccountBalancesResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AccountBalanceTransfer**](AccountBalanceTransfer.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.transfer_account_balances_response_envelope import TransferAccountBalancesResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TransferAccountBalancesResponseEnvelope from a JSON string
transfer_account_balances_response_envelope_instance = TransferAccountBalancesResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(TransferAccountBalancesResponseEnvelope.to_json())

# convert the object into a dict
transfer_account_balances_response_envelope_dict = transfer_account_balances_response_envelope_instance.to_dict()
# create an instance of TransferAccountBalancesResponseEnvelope from a dict
transfer_account_balances_response_envelope_from_dict = TransferAccountBalancesResponseEnvelope.from_dict(transfer_account_balances_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


