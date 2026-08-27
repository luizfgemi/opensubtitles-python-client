# Userinfo200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Userinfo200ResponseData**](Userinfo200ResponseData.md) |  | 

## Example

```python
from opensubtitles_client.models.userinfo200_response import Userinfo200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Userinfo200Response from a JSON string
userinfo200_response_instance = Userinfo200Response.from_json(json)
# print the JSON string representation of the object
print(Userinfo200Response.to_json())

# convert the object into a dict
userinfo200_response_dict = userinfo200_response_instance.to_dict()
# create an instance of Userinfo200Response from a dict
userinfo200_response_from_dict = Userinfo200Response.from_dict(userinfo200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


