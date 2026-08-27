# SubtitleAttributesFilesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **float** |  | 
**cd_number** | **float** |  | [optional] 
**file_name** | **str** |  | 
**** | **str** |  | [optional] 

## Example

```python
from opensubtitles_client.models.subtitle_attributes_files_inner import SubtitleAttributesFilesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SubtitleAttributesFilesInner from a JSON string
subtitle_attributes_files_inner_instance = SubtitleAttributesFilesInner.from_json(json)
# print the JSON string representation of the object
print(SubtitleAttributesFilesInner.to_json())

# convert the object into a dict
subtitle_attributes_files_inner_dict = subtitle_attributes_files_inner_instance.to_dict()
# create an instance of SubtitleAttributesFilesInner from a dict
subtitle_attributes_files_inner_from_dict = SubtitleAttributesFilesInner.from_dict(subtitle_attributes_files_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


