# Guessit200Response



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**year** | **float** |  | 
**language** | **str** |  | 
**subtitle_language** | **str** |  | 
**screen_size** | **str** |  | 
**streaming_service** | **str** |  | 
**source** | **str** |  | 
**other** | **str** |  | 
**audio_codec** | **str** |  | 
**audio_channels** | **str** |  | 
**video_codec** | **str** |  | 
**release_group** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from opensubtitles_client.models.guessit200_response import Guessit200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Guessit200Response from a JSON string
guessit200_response_instance = Guessit200Response.from_json(json)
# print the JSON string representation of the object
print(Guessit200Response.to_json())

# convert the object into a dict
guessit200_response_dict = guessit200_response_instance.to_dict()
# create an instance of Guessit200Response from a dict
guessit200_response_from_dict = Guessit200Response.from_dict(guessit200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


