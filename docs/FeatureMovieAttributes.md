# FeatureMovieAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**original_title** | **str** |  | 
**year** | **str** |  | 
**subtitles_counts** | [**FeatureMovieAttributesSubtitlesCounts**](FeatureMovieAttributesSubtitlesCounts.md) |  | 
**subtitles_count** | **float** |  | 
**seasons_count** | **float** |  | 
**parent_title** | **str** |  | 
**season_number** | **float** |  | 
**episode_number** | **object** |  | [optional] 
**imdb_id** | **float** |  | 
**tmdb_id** | **float** |  | 
**parent_imdb_id** | **object** |  | [optional] 
**feature_id** | **str** |  | 
**title_aka** | **List[object]** |  | 
**feature_type** | **str** |  | 
**url** | **str** |  | 
**img_url** | **str** |  | 

## Example

```python
from opensubtitles_client.models.feature_movie_attributes import FeatureMovieAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureMovieAttributes from a JSON string
feature_movie_attributes_instance = FeatureMovieAttributes.from_json(json)
# print the JSON string representation of the object
print(FeatureMovieAttributes.to_json())

# convert the object into a dict
feature_movie_attributes_dict = feature_movie_attributes_instance.to_dict()
# create an instance of FeatureMovieAttributes from a dict
feature_movie_attributes_from_dict = FeatureMovieAttributes.from_dict(feature_movie_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


