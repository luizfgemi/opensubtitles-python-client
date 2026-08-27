# SubtitleAttributesFeatureDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_id** | **float** |  | 
**feature_type** | **str** |  | 
**year** | **float** |  | [optional] 
**title** | **str** |  | 
**movie_name** | **str** |  | 
**imdb_id** | **float** |  | 
**tmdb_id** | **float** |  | [optional] 

## Example

```python
from opensubtitles_client.models.subtitle_attributes_feature_details import SubtitleAttributesFeatureDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SubtitleAttributesFeatureDetails from a JSON string
subtitle_attributes_feature_details_instance = SubtitleAttributesFeatureDetails.from_json(json)
# print the JSON string representation of the object
print(SubtitleAttributesFeatureDetails.to_json())

# convert the object into a dict
subtitle_attributes_feature_details_dict = subtitle_attributes_feature_details_instance.to_dict()
# create an instance of SubtitleAttributesFeatureDetails from a dict
subtitle_attributes_feature_details_from_dict = SubtitleAttributesFeatureDetails.from_dict(subtitle_attributes_feature_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


