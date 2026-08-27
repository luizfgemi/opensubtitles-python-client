# FeatureEpisodeAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**original_title** | **object** |  | [optional] 
**year** | **str** |  | 
**parent_imdb_id** | **object** |  | [optional] 
**parent_title** | **str** |  | 
**season_number** | **float** |  | 
**episode_number** | **float** |  | 
**imdb_id** | **float** |  | 
**tmdb_id** | **float** |  | 
**title_aka** | **List[object]** |  | 
**feature_id** | **str** |  | 
**url** | **str** |  | 
**img_url** | **str** |  | 
**subtitles_counts** | [**FeatureEpisodeAttributesSubtitlesCounts**](FeatureEpisodeAttributesSubtitlesCounts.md) |  | 
**subtitles_count** | **float** |  | 

## Example

```python
from opensubtitles_client.models.feature_episode_attributes import FeatureEpisodeAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureEpisodeAttributes from a JSON string
feature_episode_attributes_instance = FeatureEpisodeAttributes.from_json(json)
# print the JSON string representation of the object
print(FeatureEpisodeAttributes.to_json())

# convert the object into a dict
feature_episode_attributes_dict = feature_episode_attributes_instance.to_dict()
# create an instance of FeatureEpisodeAttributes from a dict
feature_episode_attributes_from_dict = FeatureEpisodeAttributes.from_dict(feature_episode_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


