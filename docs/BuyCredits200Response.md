# BuyCredits200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BuyCredits200ResponseDataInner]**](BuyCredits200ResponseDataInner.md) |  | [optional] 

## Example

```python
from opensubtitles_client.models.buy_credits200_response import BuyCredits200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BuyCredits200Response from a JSON string
buy_credits200_response_instance = BuyCredits200Response.from_json(json)
# print the JSON string representation of the object
print(BuyCredits200Response.to_json())

# convert the object into a dict
buy_credits200_response_dict = buy_credits200_response_instance.to_dict()
# create an instance of BuyCredits200Response from a dict
buy_credits200_response_from_dict = BuyCredits200Response.from_dict(buy_credits200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


