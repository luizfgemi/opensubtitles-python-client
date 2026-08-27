# Features200Response



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**movie** | [**FeatureMovie**](FeatureMovie.md) |  | [optional] 
**episode** | [**FeatureEpisode**](FeatureEpisode.md) |  | [optional] 
**tv** | [**FeatureTvshow**](FeatureTvshow.md) |  | [optional] 

## Example

```python
from opensubtitles_client.models.features200_response import Features200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Features200Response from a JSON string
features200_response_instance = Features200Response.from_json(json)
# print the JSON string representation of the object
print(Features200Response.to_json())

# convert the object into a dict
features200_response_dict = features200_response_instance.to_dict()
# create an instance of Features200Response from a dict
features200_response_from_dict = Features200Response.from_dict(features200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


