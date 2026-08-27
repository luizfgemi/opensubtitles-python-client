# BuyCredits200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**discount_percent** | **int** |  | [optional] 
**checkout_url** | **str** |  | [optional] 

## Example

```python
from opensubtitles_client.models.buy_credits200_response_data_inner import BuyCredits200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of BuyCredits200ResponseDataInner from a JSON string
buy_credits200_response_data_inner_instance = BuyCredits200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(BuyCredits200ResponseDataInner.to_json())

# convert the object into a dict
buy_credits200_response_data_inner_dict = buy_credits200_response_data_inner_instance.to_dict()
# create an instance of BuyCredits200ResponseDataInner from a dict
buy_credits200_response_data_inner_from_dict = BuyCredits200ResponseDataInner.from_dict(buy_credits200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


