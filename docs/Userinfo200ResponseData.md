# Userinfo200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_downloads** | **float** |  | 
**level** | **str** |  | 
**user_id** | **float** |  | 
**vip** | **bool** |  | 
**downloads_count** | **float** |  | 
**remaining_downloads** | **float** |  | 

## Example

```python
from opensubtitles_client.models.userinfo200_response_data import Userinfo200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of Userinfo200ResponseData from a JSON string
userinfo200_response_data_instance = Userinfo200ResponseData.from_json(json)
# print the JSON string representation of the object
print(Userinfo200ResponseData.to_json())

# convert the object into a dict
userinfo200_response_data_dict = userinfo200_response_data_instance.to_dict()
# create an instance of Userinfo200ResponseData from a dict
userinfo200_response_data_from_dict = Userinfo200ResponseData.from_dict(userinfo200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


