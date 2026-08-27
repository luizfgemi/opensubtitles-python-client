# Subtitles200ResponseDataInnerAttributesFeatureDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_id** | **int** |  | [optional] 
**feature_type** | **str** |  | [optional] 
**year** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**movie_name** | **str** |  | [optional] 
**imdb_id** | **int** |  | [optional] 
**tmdb_id** | **int** |  | [optional] 
**season_number** | **int** |  | [optional] 
**episode_number** | **int** |  | [optional] 
**parent_imdb_id** | **int** |  | [optional] 
**parent_title** | **str** |  | [optional] 
**parent_tmdb_id** | **int** |  | [optional] 
**parent_feature_id** | **int** |  | [optional] 

## Example

```python
from opensubtitles_client.models.subtitles200_response_data_inner_attributes_feature_details import Subtitles200ResponseDataInnerAttributesFeatureDetails

# TODO update the JSON string below
json = "{}"
# create an instance of Subtitles200ResponseDataInnerAttributesFeatureDetails from a JSON string
subtitles200_response_data_inner_attributes_feature_details_instance = Subtitles200ResponseDataInnerAttributesFeatureDetails.from_json(json)
# print the JSON string representation of the object
print(Subtitles200ResponseDataInnerAttributesFeatureDetails.to_json())

# convert the object into a dict
subtitles200_response_data_inner_attributes_feature_details_dict = subtitles200_response_data_inner_attributes_feature_details_instance.to_dict()
# create an instance of Subtitles200ResponseDataInnerAttributesFeatureDetails from a dict
subtitles200_response_data_inner_attributes_feature_details_from_dict = Subtitles200ResponseDataInnerAttributesFeatureDetails.from_dict(subtitles200_response_data_inner_attributes_feature_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


