# FeatureMovie



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 
**attributes** | [**FeatureMovieAttributes**](FeatureMovieAttributes.md) |  | 

## Example

```python
from opensubtitles_client.models.feature_movie import FeatureMovie

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureMovie from a JSON string
feature_movie_instance = FeatureMovie.from_json(json)
# print the JSON string representation of the object
print(FeatureMovie.to_json())

# convert the object into a dict
feature_movie_dict = feature_movie_instance.to_dict()
# create an instance of FeatureMovie from a dict
feature_movie_from_dict = FeatureMovie.from_dict(feature_movie_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


