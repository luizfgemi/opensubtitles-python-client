# MostDownloaded200Response



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_pages** | **float** |  | 
**total_count** | **float** |  | 
**page** | **float** |  | 
**data** | [**List[Subtitle]**](Subtitle.md) |  | 

## Example

```python
from opensubtitles_client.models.most_downloaded200_response import MostDownloaded200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MostDownloaded200Response from a JSON string
most_downloaded200_response_instance = MostDownloaded200Response.from_json(json)
# print the JSON string representation of the object
print(MostDownloaded200Response.to_json())

# convert the object into a dict
most_downloaded200_response_dict = most_downloaded200_response_instance.to_dict()
# create an instance of MostDownloaded200Response from a dict
most_downloaded200_response_from_dict = MostDownloaded200Response.from_dict(most_downloaded200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


