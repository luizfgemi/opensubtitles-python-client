# Subtitles200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_pages** | **int** |  | [optional] 
**total_count** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**page** | **int** |  | [optional] 
**data** | [**List[Subtitles200ResponseDataInner]**](Subtitles200ResponseDataInner.md) |  | [optional] 

## Example

```python
from opensubtitles_client.models.subtitles200_response import Subtitles200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Subtitles200Response from a JSON string
subtitles200_response_instance = Subtitles200Response.from_json(json)
# print the JSON string representation of the object
print(Subtitles200Response.to_json())

# convert the object into a dict
subtitles200_response_dict = subtitles200_response_instance.to_dict()
# create an instance of Subtitles200Response from a dict
subtitles200_response_from_dict = Subtitles200Response.from_dict(subtitles200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


