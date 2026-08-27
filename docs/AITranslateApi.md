# opensubtitles_client.AITranslateApi

All URIs are relative to *https://api.opensubtitles.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**translate**](AITranslateApi.md#translate) | **POST** /ai/translate | AI Translate
[**translate_status**](AITranslateApi.md#translate_status) | **GET** /ai/translate/{correlation_id} | AI Translate status


# **translate**
> object translate(api, file, translate_to, translate_from=translate_from, file_id=file_id)

AI Translate

**Translate** subtitles using AI from one language to another language. 

Credits on user account are needed. [Buy Credits](../open_api.json/paths/~1ai~1credits~1buy/get)

Check following method: [Get AI Translate status](../open_api.json/paths/~1ai~1translate~1{correlation_id}/get)

Method is returning 
```
{
  "status": "CREATED",
  "correlation_id": "67eda18f52e11"
}
```
Status possible values: 
```
CREATED     -> Initial state`
PENDING     -> procedure is still running
COMPLETED   -> remote procedure call is completed and has a result
ERROR       -> procedure resulted in an error and is not running anymore
TIMEOUT     -> No matching procedure call found before timeout
```
Using `correlation_id` can check status of job using GET


### Example

* Api Key Authentication (Api-Key):
* Bearer (JWT) Authentication (Bearer):

```python
import opensubtitles_client
from opensubtitles_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.opensubtitles.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = opensubtitles_client.Configuration(
    host = "https://api.opensubtitles.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Api-Key
configuration.api_key['Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Api-Key'] = 'Bearer'

# Configure Bearer authorization (JWT): Bearer
configuration = opensubtitles_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with opensubtitles_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opensubtitles_client.AITranslateApi(api_client)
    api = 'api_example' # str | translation_apis
    file = 'file_example' # str | file contents to translate
    translate_to = 'translate_to_example' # str | language ISO639 translate_from
    translate_from = 'auto' # str | language ISO639 translate_from (auto is default) (optional) (default to 'auto')
    file_id = 56 # int | file_id from /subtitles endpoint (optional)

    try:
        # AI Translate
        api_response = api_instance.translate(api, file, translate_to, translate_from=translate_from, file_id=file_id)
        print("The response of AITranslateApi->translate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AITranslateApi->translate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| translation_apis | 
 **file** | **str**| file contents to translate | 
 **translate_to** | **str**| language ISO639 translate_from | 
 **translate_from** | **str**| language ISO639 translate_from (auto is default) | [optional] [default to &#39;auto&#39;]
 **file_id** | **int**| file_id from /subtitles endpoint | [optional] 

### Return type

**object**

### Authorization

[Api-Key](../README.md#Api-Key), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: multipart/form-data

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translate_status**
> translate_status(correlation_id)

AI Translate status

Get status of **[translate](..open_api.json/paths/~1ai~1translate/post)** job using `correlation_id`


### Example

* Api Key Authentication (Api-Key):
* Bearer (JWT) Authentication (Bearer):

```python
import opensubtitles_client
from opensubtitles_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.opensubtitles.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = opensubtitles_client.Configuration(
    host = "https://api.opensubtitles.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Api-Key
configuration.api_key['Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Api-Key'] = 'Bearer'

# Configure Bearer authorization (JWT): Bearer
configuration = opensubtitles_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with opensubtitles_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opensubtitles_client.AITranslateApi(api_client)
    correlation_id = 'correlation_id_example' # str | correlation_id

    try:
        # AI Translate status
        api_instance.translate_status(correlation_id)
    except Exception as e:
        print("Exception when calling AITranslateApi->translate_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **correlation_id** | **str**| correlation_id | 

### Return type

void (empty response body)

### Authorization

[Api-Key](../README.md#Api-Key), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

