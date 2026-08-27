# Translation200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**pricing** | **str** |  | [optional] 
**reliability** | **str** |  | [optional] 
**price** | **float** |  | [optional] 
**languages_supported** | [**List[Translation200ResponseDataInnerLanguagesSupportedInner]**](Translation200ResponseDataInnerLanguagesSupportedInner.md) |  | [optional] 

## Example

```python
from opensubtitles_client.models.translation200_response_data_inner import Translation200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of Translation200ResponseDataInner from a JSON string
translation200_response_data_inner_instance = Translation200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(Translation200ResponseDataInner.to_json())

# convert the object into a dict
translation200_response_data_inner_dict = translation200_response_data_inner_instance.to_dict()
# create an instance of Translation200ResponseDataInner from a dict
translation200_response_data_inner_from_dict = Translation200ResponseDataInner.from_dict(translation200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


