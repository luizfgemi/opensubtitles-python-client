# SubtitleAttributesUploader


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uploader_id** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**rank** | **str** |  | [optional] 

## Example

```python
from opensubtitles_client.models.subtitle_attributes_uploader import SubtitleAttributesUploader

# TODO update the JSON string below
json = "{}"
# create an instance of SubtitleAttributesUploader from a JSON string
subtitle_attributes_uploader_instance = SubtitleAttributesUploader.from_json(json)
# print the JSON string representation of the object
print(SubtitleAttributesUploader.to_json())

# convert the object into a dict
subtitle_attributes_uploader_dict = subtitle_attributes_uploader_instance.to_dict()
# create an instance of SubtitleAttributesUploader from a dict
subtitle_attributes_uploader_from_dict = SubtitleAttributesUploader.from_dict(subtitle_attributes_uploader_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


