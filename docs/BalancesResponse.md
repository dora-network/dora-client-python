# BalancesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balances** | [**List[Position]**](Position.md) |  | [optional] 

## Example

```python
from dora_client.models.balances_response import BalancesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BalancesResponse from a JSON string
balances_response_instance = BalancesResponse.from_json(json)
# print the JSON string representation of the object
print(BalancesResponse.to_json())

# convert the object into a dict
balances_response_dict = balances_response_instance.to_dict()
# create an instance of BalancesResponse from a dict
balances_response_from_dict = BalancesResponse.from_dict(balances_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


