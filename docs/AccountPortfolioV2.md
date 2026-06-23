# AccountPortfolioV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **UUID** |  | 
**accounts** | **Dict[str, Dict[str, AccountV2]]** |  | 
**net_stablecoin_equivalence** | [**TransformedAssets**](TransformedAssets.md) |  | 

## Example

```python
from dora_client.models.account_portfolio_v2 import AccountPortfolioV2

# TODO update the JSON string below
json = "{}"
# create an instance of AccountPortfolioV2 from a JSON string
account_portfolio_v2_instance = AccountPortfolioV2.from_json(json)
# print the JSON string representation of the object
print(AccountPortfolioV2.to_json())

# convert the object into a dict
account_portfolio_v2_dict = account_portfolio_v2_instance.to_dict()
# create an instance of AccountPortfolioV2 from a dict
account_portfolio_v2_from_dict = AccountPortfolioV2.from_dict(account_portfolio_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


