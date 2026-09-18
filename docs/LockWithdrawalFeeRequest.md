# LockWithdrawalFeeRequest

Request to lock the network fee for an approved USDC withdrawal. The withdrawal is named by the path, and the fee itself is not part of the body: it is read from the signed quote token, so a client cannot choose what its own withdrawal costs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_token** | **str** | The signed quote token returned by GET /v1/web3/withdrawals/fee-quote. It must still be within its TTL and must have been issued for this withdrawal&#39;s destination, quantity, and chain. | 

## Example

```python
from dora_client.models.lock_withdrawal_fee_request import LockWithdrawalFeeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LockWithdrawalFeeRequest from a JSON string
lock_withdrawal_fee_request_instance = LockWithdrawalFeeRequest.from_json(json)
# print the JSON string representation of the object
print(LockWithdrawalFeeRequest.to_json())

# convert the object into a dict
lock_withdrawal_fee_request_dict = lock_withdrawal_fee_request_instance.to_dict()
# create an instance of LockWithdrawalFeeRequest from a dict
lock_withdrawal_fee_request_from_dict = LockWithdrawalFeeRequest.from_dict(lock_withdrawal_fee_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


