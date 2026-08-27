# SubtitleAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subtitle_id** | **str** |  | 
**language** | **str** |  | 
**download_count** | **float** |  | 
**new_download_count** | **float** |  | 
**hearing_impaired** | **bool** |  | [optional] 
**hd** | **bool** |  | [optional] 
**fps** | **float** |  | [optional] 
**votes** | **float** |  | [optional] 
**points** | **float** |  | [optional] 
**ratings** | **float** |  | [optional] 
**from_trusted** | **bool** |  | 
**foreign_parts_only** | **bool** |  | 
**ai_translated** | **bool** |  | 
**machine_translated** | **bool** |  | 
**upload_date** | **str** |  | 
**release** | **str** |  | [optional] 
**comments** | **str** |  | [optional] 
**legacy_subtitle_id** | **float** |  | [optional] 
**uploader** | [**SubtitleAttributesUploader**](SubtitleAttributesUploader.md) |  | [optional] 
**feature_details** | [**SubtitleAttributesFeatureDetails**](SubtitleAttributesFeatureDetails.md) |  | 
**url** | **str** |  | 
**related_links** | **List[object]** |  | [optional] 
**files** | [**List[SubtitleAttributesFilesInner]**](SubtitleAttributesFilesInner.md) |  | 

## Example

```python
from opensubtitles_client.models.subtitle_attributes import SubtitleAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of SubtitleAttributes from a JSON string
subtitle_attributes_instance = SubtitleAttributes.from_json(json)
# print the JSON string representation of the object
print(SubtitleAttributes.to_json())

# convert the object into a dict
subtitle_attributes_dict = subtitle_attributes_instance.to_dict()
# create an instance of SubtitleAttributes from a dict
subtitle_attributes_from_dict = SubtitleAttributes.from_dict(subtitle_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


