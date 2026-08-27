# Latest200ResponseDataInnerAttributesFeatureDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_id** | **float** |  | 
**feature_type** | **str** |  | 
**year** | **float** |  | 
**title** | **str** |  | 
**movie_name** | **str** |  | 
**imdb_id** | **float** |  | 
**tmdb_id** | **object** |  | [optional] 

## Example

```python
from opensubtitles_client.models.latest200_response_data_inner_attributes_feature_details import Latest200ResponseDataInnerAttributesFeatureDetails

# TODO update the JSON string below
json = "{}"
# create an instance of Latest200ResponseDataInnerAttributesFeatureDetails from a JSON string
latest200_response_data_inner_attributes_feature_details_instance = Latest200ResponseDataInnerAttributesFeatureDetails.from_json(json)
# print the JSON string representation of the object
print(Latest200ResponseDataInnerAttributesFeatureDetails.to_json())

# convert the object into a dict
latest200_response_data_inner_attributes_feature_details_dict = latest200_response_data_inner_attributes_feature_details_instance.to_dict()
# create an instance of Latest200ResponseDataInnerAttributesFeatureDetails from a dict
latest200_response_data_inner_attributes_feature_details_from_dict = Latest200ResponseDataInnerAttributesFeatureDetails.from_dict(latest200_response_data_inner_attributes_feature_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


