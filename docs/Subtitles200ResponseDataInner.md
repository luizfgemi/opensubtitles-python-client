# Subtitles200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**Subtitles200ResponseDataInnerAttributes**](Subtitles200ResponseDataInnerAttributes.md) |  | [optional] 

## Example

```python
from opensubtitles_client.models.subtitles200_response_data_inner import Subtitles200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of Subtitles200ResponseDataInner from a JSON string
subtitles200_response_data_inner_instance = Subtitles200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(Subtitles200ResponseDataInner.to_json())

# convert the object into a dict
subtitles200_response_data_inner_dict = subtitles200_response_data_inner_instance.to_dict()
# create an instance of Subtitles200ResponseDataInner from a dict
subtitles200_response_data_inner_from_dict = Subtitles200ResponseDataInner.from_dict(subtitles200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


