# FeatureTvshowAttributesSeasonsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season_number** | **float** |  | 
**episodes** | [**List[FeatureTvshowAttributesSeasonsInnerEpisodesInner]**](FeatureTvshowAttributesSeasonsInnerEpisodesInner.md) |  | [optional] 

## Example

```python
from opensubtitles_client.models.feature_tvshow_attributes_seasons_inner import FeatureTvshowAttributesSeasonsInner

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureTvshowAttributesSeasonsInner from a JSON string
feature_tvshow_attributes_seasons_inner_instance = FeatureTvshowAttributesSeasonsInner.from_json(json)
# print the JSON string representation of the object
print(FeatureTvshowAttributesSeasonsInner.to_json())

# convert the object into a dict
feature_tvshow_attributes_seasons_inner_dict = feature_tvshow_attributes_seasons_inner_instance.to_dict()
# create an instance of FeatureTvshowAttributesSeasonsInner from a dict
feature_tvshow_attributes_seasons_inner_from_dict = FeatureTvshowAttributesSeasonsInner.from_dict(feature_tvshow_attributes_seasons_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


