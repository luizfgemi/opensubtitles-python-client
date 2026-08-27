# FeatureTvshowAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**original_title** | **str** |  | 
**year** | **str** |  | 
**imdb_id** | **float** |  | 
**tmdb_id** | **float** |  | 
**title_aka** | **List[object]** |  | 
**feature_id** | **str** |  | 
**url** | **str** |  | 
**img_url** | **str** |  | 
**subtitles_counts** | [**FeatureTvshowAttributesSubtitlesCounts**](FeatureTvshowAttributesSubtitlesCounts.md) |  | 
**subtitles_count** | **float** |  | 
**seasons** | [**List[FeatureTvshowAttributesSeasonsInner]**](FeatureTvshowAttributesSeasonsInner.md) |  | 

## Example

```python
from opensubtitles_client.models.feature_tvshow_attributes import FeatureTvshowAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureTvshowAttributes from a JSON string
feature_tvshow_attributes_instance = FeatureTvshowAttributes.from_json(json)
# print the JSON string representation of the object
print(FeatureTvshowAttributes.to_json())

# convert the object into a dict
feature_tvshow_attributes_dict = feature_tvshow_attributes_instance.to_dict()
# create an instance of FeatureTvshowAttributes from a dict
feature_tvshow_attributes_from_dict = FeatureTvshowAttributes.from_dict(feature_tvshow_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


