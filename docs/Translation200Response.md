# Translation200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Translation200ResponseDataInner]**](Translation200ResponseDataInner.md) |  | [optional] 

## Example

```python
from opensubtitles_client.models.translation200_response import Translation200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Translation200Response from a JSON string
translation200_response_instance = Translation200Response.from_json(json)
# print the JSON string representation of the object
print(Translation200Response.to_json())

# convert the object into a dict
translation200_response_dict = translation200_response_instance.to_dict()
# create an instance of Translation200Response from a dict
translation200_response_from_dict = Translation200Response.from_dict(translation200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


