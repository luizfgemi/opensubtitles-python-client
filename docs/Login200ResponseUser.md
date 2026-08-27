# Login200ResponseUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_translations** | **float** |  | 
**allowed_downloads** | **float** |  | 
**level** | **str** |  | 
**user_id** | **float** |  | 
**ext_installed** | **bool** |  | 
**vip** | **bool** |  | 

## Example

```python
from opensubtitles_client.models.login200_response_user import Login200ResponseUser

# TODO update the JSON string below
json = "{}"
# create an instance of Login200ResponseUser from a JSON string
login200_response_user_instance = Login200ResponseUser.from_json(json)
# print the JSON string representation of the object
print(Login200ResponseUser.to_json())

# convert the object into a dict
login200_response_user_dict = login200_response_user_instance.to_dict()
# create an instance of Login200ResponseUser from a dict
login200_response_user_from_dict = Login200ResponseUser.from_dict(login200_response_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


