# AccountPortfolioResponseV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolio** | [**AccountPortfolioV2**](AccountPortfolioV2.md) |  | [optional] 

## Example

```python
from dora_client.models.account_portfolio_response_v2 import AccountPortfolioResponseV2

# TODO update the JSON string below
json = "{}"
# create an instance of AccountPortfolioResponseV2 from a JSON string
account_portfolio_response_v2_instance = AccountPortfolioResponseV2.from_json(json)
# print the JSON string representation of the object
print(AccountPortfolioResponseV2.to_json())

# convert the object into a dict
account_portfolio_response_v2_dict = account_portfolio_response_v2_instance.to_dict()
# create an instance of AccountPortfolioResponseV2 from a dict
account_portfolio_response_v2_from_dict = AccountPortfolioResponseV2.from_dict(account_portfolio_response_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


