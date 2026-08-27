# Transcription200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Translation200ResponseDataInner]**](Translation200ResponseDataInner.md) |  | [optional] 

## Example

```python
from opensubtitles_client.models.transcription200_response import Transcription200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Transcription200Response from a JSON string
transcription200_response_instance = Transcription200Response.from_json(json)
# print the JSON string representation of the object
print(Transcription200Response.to_json())

# convert the object into a dict
transcription200_response_dict = transcription200_response_instance.to_dict()
# create an instance of Transcription200Response from a dict
transcription200_response_from_dict = Transcription200Response.from_dict(transcription200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


