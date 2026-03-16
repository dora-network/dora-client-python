# UserInterest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **Dict[str, int]** |  | 
**value** | **Dict[str, str]** |  | 

## Example

```python
from dora_client.models.user_interest import UserInterest

# TODO update the JSON string below
json = "{}"
# create an instance of UserInterest from a JSON string
user_interest_instance = UserInterest.from_json(json)
# print the JSON string representation of the object
print(UserInterest.to_json())

# convert the object into a dict
user_interest_dict = user_interest_instance.to_dict()
# create an instance of UserInterest from a dict
user_interest_from_dict = UserInterest.from_dict(user_interest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


