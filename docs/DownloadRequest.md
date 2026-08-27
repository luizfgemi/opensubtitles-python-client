# DownloadRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **int** | file_id from /subtitles search results | 
**sub_format** | **str** | from /infos/formats | [optional] 
**file_name** | **str** | desired file name | [optional] 
**in_fps** | **float** | used for conversions, in_fps and out_fps must then be indicated | [optional] 
**out_fps** | **float** | used for conversions, in_fps and out_fps must then be indicated | [optional] 
**timeshift** | **float** | delay to add or remove to the subtitle, + or - value, in seconds, i.e. 2.5s or -1s  | [optional] 
**force_download** | **bool** | (1/0) set subtitle file headers to \&quot;application/force-download\&quot; | [optional] 

## Example

```python
from opensubtitles_client.models.download_request import DownloadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadRequest from a JSON string
download_request_instance = DownloadRequest.from_json(json)
# print the JSON string representation of the object
print(DownloadRequest.to_json())

# convert the object into a dict
download_request_dict = download_request_instance.to_dict()
# create an instance of DownloadRequest from a dict
download_request_from_dict = DownloadRequest.from_dict(download_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


