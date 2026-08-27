# FeatureTvshow



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 
**attributes** | [**FeatureTvshowAttributes**](FeatureTvshowAttributes.md) |  | 

## Example

```python
from opensubtitles_client.models.feature_tvshow import FeatureTvshow

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureTvshow from a JSON string
feature_tvshow_instance = FeatureTvshow.from_json(json)
# print the JSON string representation of the object
print(FeatureTvshow.to_json())

# convert the object into a dict
feature_tvshow_dict = feature_tvshow_instance.to_dict()
# create an instance of FeatureTvshow from a dict
feature_tvshow_from_dict = FeatureTvshow.from_dict(feature_tvshow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


