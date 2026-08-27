# Download200Response



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | 
**file_name** | **str** |  | 
**requests** | **float** |  | 
**remaining** | **float** |  | 
**message** | **str** |  | 
**reset_time** | **str** |  | 
**reset_time_utc** | **str** |  | 

## Example

```python
from opensubtitles_client.models.download200_response import Download200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Download200Response from a JSON string
download200_response_instance = Download200Response.from_json(json)
# print the JSON string representation of the object
print(Download200Response.to_json())

# convert the object into a dict
download200_response_dict = download200_response_instance.to_dict()
# create an instance of Download200Response from a dict
download200_response_from_dict = Download200Response.from_dict(download200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


