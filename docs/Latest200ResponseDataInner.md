# Latest200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 
**attributes** | [**Latest200ResponseDataInnerAttributes**](Latest200ResponseDataInnerAttributes.md) |  | [optional] 

## Example

```python
from opensubtitles_client.models.latest200_response_data_inner import Latest200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of Latest200ResponseDataInner from a JSON string
latest200_response_data_inner_instance = Latest200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(Latest200ResponseDataInner.to_json())

# convert the object into a dict
latest200_response_data_inner_dict = latest200_response_data_inner_instance.to_dict()
# create an instance of Latest200ResponseDataInner from a dict
latest200_response_data_inner_from_dict = Latest200ResponseDataInner.from_dict(latest200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


