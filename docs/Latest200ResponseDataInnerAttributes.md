# Latest200ResponseDataInnerAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subtitle_id** | **str** |  | 
**language** | **str** |  | 
**download_count** | **float** |  | 
**new_download_count** | **float** |  | 
**hearing_impaired** | **bool** |  | 
**hd** | **bool** |  | 
**format** | **object** |  | [optional] 
**fps** | **float** |  | 
**votes** | **float** |  | 
**points** | **float** |  | 
**ratings** | **float** |  | 
**from_trusted** | **bool** |  | 
**foreign_parts_only** | **bool** |  | 
**ai_translated** | **bool** |  | 
**machine_translated** | **object** |  | [optional] 
**upload_date** | **str** |  | 
**release** | **str** |  | 
**comments** | **str** |  | 
**legacy_subtitle_id** | **float** |  | 
**uploader** | [**Latest200ResponseDataInnerAttributesUploader**](Latest200ResponseDataInnerAttributesUploader.md) |  | 
**feature_details** | [**Latest200ResponseDataInnerAttributesFeatureDetails**](Latest200ResponseDataInnerAttributesFeatureDetails.md) |  | 
**url** | **str** |  | 
**related_links** | [**Latest200ResponseDataInnerAttributesRelatedLinks**](Latest200ResponseDataInnerAttributesRelatedLinks.md) |  | 
**files** | [**List[Latest200ResponseDataInnerAttributesFilesInner]**](Latest200ResponseDataInnerAttributesFilesInner.md) |  | 

## Example

```python
from opensubtitles_client.models.latest200_response_data_inner_attributes import Latest200ResponseDataInnerAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of Latest200ResponseDataInnerAttributes from a JSON string
latest200_response_data_inner_attributes_instance = Latest200ResponseDataInnerAttributes.from_json(json)
# print the JSON string representation of the object
print(Latest200ResponseDataInnerAttributes.to_json())

# convert the object into a dict
latest200_response_data_inner_attributes_dict = latest200_response_data_inner_attributes_instance.to_dict()
# create an instance of Latest200ResponseDataInnerAttributes from a dict
latest200_response_data_inner_attributes_from_dict = Latest200ResponseDataInnerAttributes.from_dict(latest200_response_data_inner_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


