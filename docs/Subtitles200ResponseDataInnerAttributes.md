# Subtitles200ResponseDataInnerAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subtitle_id** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**download_count** | **int** |  | [optional] 
**new_download_count** | **int** |  | [optional] 
**hearing_impaired** | **bool** |  | [optional] 
**hd** | **bool** |  | [optional] 
**fps** | **float** |  | [optional] 
**votes** | **int** |  | [optional] 
**ratings** | **int** |  | [optional] 
**from_trusted** | **bool** |  | [optional] 
**foreign_parts_only** | **bool** |  | [optional] 
**upload_date** | **str** |  | [optional] 
**ai_translated** | **bool** |  | [optional] 
**nb_cd** | **int** |  | [optional] 
**slug** | **str** |  | [optional] 
**machine_translated** | **bool** |  | [optional] 
**release** | **str** |  | [optional] 
**comments** | **str** |  | [optional] 
**legacy_subtitle_id** | **int** |  | [optional] 
**legacy_uploader_id** | **int** |  | [optional] 
**uploader** | [**Subtitles200ResponseDataInnerAttributesUploader**](Subtitles200ResponseDataInnerAttributesUploader.md) |  | [optional] 
**feature_details** | [**Subtitles200ResponseDataInnerAttributesFeatureDetails**](Subtitles200ResponseDataInnerAttributesFeatureDetails.md) |  | [optional] 
**url** | **str** |  | [optional] 
**related_links** | [**List[Subtitles200ResponseDataInnerAttributesRelatedLinksInner]**](Subtitles200ResponseDataInnerAttributesRelatedLinksInner.md) |  | [optional] 
**files** | [**List[Subtitles200ResponseDataInnerAttributesFilesInner]**](Subtitles200ResponseDataInnerAttributesFilesInner.md) |  | [optional] 

## Example

```python
from opensubtitles_client.models.subtitles200_response_data_inner_attributes import Subtitles200ResponseDataInnerAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of Subtitles200ResponseDataInnerAttributes from a JSON string
subtitles200_response_data_inner_attributes_instance = Subtitles200ResponseDataInnerAttributes.from_json(json)
# print the JSON string representation of the object
print(Subtitles200ResponseDataInnerAttributes.to_json())

# convert the object into a dict
subtitles200_response_data_inner_attributes_dict = subtitles200_response_data_inner_attributes_instance.to_dict()
# create an instance of Subtitles200ResponseDataInnerAttributes from a dict
subtitles200_response_data_inner_attributes_from_dict = Subtitles200ResponseDataInnerAttributes.from_dict(subtitles200_response_data_inner_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


