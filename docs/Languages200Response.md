# Languages200Response



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Languages200ResponseDataInner]**](Languages200ResponseDataInner.md) |  | 

## Example

```python
from opensubtitles_client.models.languages200_response import Languages200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Languages200Response from a JSON string
languages200_response_instance = Languages200Response.from_json(json)
# print the JSON string representation of the object
print(Languages200Response.to_json())

# convert the object into a dict
languages200_response_dict = languages200_response_instance.to_dict()
# create an instance of Languages200Response from a dict
languages200_response_from_dict = Languages200Response.from_dict(languages200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


