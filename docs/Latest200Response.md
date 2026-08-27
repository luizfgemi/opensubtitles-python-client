# Latest200Response



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_pages** | **float** |  | 
**total_count** | **float** |  | 
**page** | **float** |  | 
**data** | [**List[Latest200ResponseDataInner]**](Latest200ResponseDataInner.md) |  | 

## Example

```python
from opensubtitles_client.models.latest200_response import Latest200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Latest200Response from a JSON string
latest200_response_instance = Latest200Response.from_json(json)
# print the JSON string representation of the object
print(Latest200Response.to_json())

# convert the object into a dict
latest200_response_dict = latest200_response_instance.to_dict()
# create an instance of Latest200Response from a dict
latest200_response_from_dict = Latest200Response.from_dict(latest200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


