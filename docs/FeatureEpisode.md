# FeatureEpisode



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 
**attributes** | [**FeatureEpisodeAttributes**](FeatureEpisodeAttributes.md) |  | 

## Example

```python
from opensubtitles_client.models.feature_episode import FeatureEpisode

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureEpisode from a JSON string
feature_episode_instance = FeatureEpisode.from_json(json)
# print the JSON string representation of the object
print(FeatureEpisode.to_json())

# convert the object into a dict
feature_episode_dict = feature_episode_instance.to_dict()
# create an instance of FeatureEpisode from a dict
feature_episode_from_dict = FeatureEpisode.from_dict(feature_episode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


