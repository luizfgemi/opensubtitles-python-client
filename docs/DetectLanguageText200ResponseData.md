# DetectLanguageText200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**language** | [**DetectLanguageText200ResponseDataLanguage**](DetectLanguageText200ResponseDataLanguage.md) |  | [optional] 

## Example

```python
from opensubtitles_client.models.detect_language_text200_response_data import DetectLanguageText200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of DetectLanguageText200ResponseData from a JSON string
detect_language_text200_response_data_instance = DetectLanguageText200ResponseData.from_json(json)
# print the JSON string representation of the object
print(DetectLanguageText200ResponseData.to_json())

# convert the object into a dict
detect_language_text200_response_data_dict = detect_language_text200_response_data_instance.to_dict()
# create an instance of DetectLanguageText200ResponseData from a dict
detect_language_text200_response_data_from_dict = DetectLanguageText200ResponseData.from_dict(detect_language_text200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


