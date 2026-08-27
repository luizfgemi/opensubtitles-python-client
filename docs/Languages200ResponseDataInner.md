# Languages200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language_code** | **str** |  | 
**language_name** | **str** |  | 

## Example

```python
from opensubtitles_client.models.languages200_response_data_inner import Languages200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of Languages200ResponseDataInner from a JSON string
languages200_response_data_inner_instance = Languages200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(Languages200ResponseDataInner.to_json())

# convert the object into a dict
languages200_response_data_inner_dict = languages200_response_data_inner_instance.to_dict()
# create an instance of Languages200ResponseDataInner from a dict
languages200_response_data_inner_from_dict = Languages200ResponseDataInner.from_dict(languages200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


