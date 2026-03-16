# LeverageBalanceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leverage_balance** | **dict** |  | [optional] 

## Example

```python
from dora_client.models.leverage_balance_response import LeverageBalanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LeverageBalanceResponse from a JSON string
leverage_balance_response_instance = LeverageBalanceResponse.from_json(json)
# print the JSON string representation of the object
print(LeverageBalanceResponse.to_json())

# convert the object into a dict
leverage_balance_response_dict = leverage_balance_response_instance.to_dict()
# create an instance of LeverageBalanceResponse from a dict
leverage_balance_response_from_dict = LeverageBalanceResponse.from_dict(leverage_balance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


