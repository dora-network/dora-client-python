# LedgerAccountsResponseV2Envelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AccountPortfolioResponseV2**](AccountPortfolioResponseV2.md) |  | [optional] 
**error** | **str** | The error message. Present for error (non-2xx) responses. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Metadata about the response, including status code and trace information. | 

## Example

```python
from dora_client.models.ledger_accounts_response_v2_envelope import LedgerAccountsResponseV2Envelope

# TODO update the JSON string below
json = "{}"
# create an instance of LedgerAccountsResponseV2Envelope from a JSON string
ledger_accounts_response_v2_envelope_instance = LedgerAccountsResponseV2Envelope.from_json(json)
# print the JSON string representation of the object
print(LedgerAccountsResponseV2Envelope.to_json())

# convert the object into a dict
ledger_accounts_response_v2_envelope_dict = ledger_accounts_response_v2_envelope_instance.to_dict()
# create an instance of LedgerAccountsResponseV2Envelope from a dict
ledger_accounts_response_v2_envelope_from_dict = LedgerAccountsResponseV2Envelope.from_dict(ledger_accounts_response_v2_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


