# opensubtitles_client.AITranscribeApi

All URIs are relative to *https://api.opensubtitles.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transcribe**](AITranscribeApi.md#transcribe) | **POST** /ai/transcribe | AI Transcribe
[**transcribe_status**](AITranscribeApi.md#transcribe_status) | **GET** /ai/transcribe/{correlation_id} | AI Transcribe status


# **transcribe**
> object transcribe(api, file, language)

AI Transcribe

**Transcribe** media (audio, video) file using AI into subtitles. Max size of file: 100 MB 

Credits on user account are needed. [Buy Credits](../open_api.json/paths/~1ai~1credits~1buy/get)

Check following method: [Get AI Transcribe status](../open_api.json/paths/~1ai~1transcribe~1{correlation_id}/get)

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
    api_instance = opensubtitles_client.AITranscribeApi(api_client)
    api = 'api_example' # str | transcribe API
    file = 'file_example' # str | media file
    language = 'language_example' # str | language of media file

    try:
        # AI Transcribe
        api_response = api_instance.transcribe(api, file, language)
        print("The response of AITranscribeApi->transcribe:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AITranscribeApi->transcribe: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| transcribe API | 
 **file** | **str**| media file | 
 **language** | **str**| language of media file | 

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

# **transcribe_status**
> transcribe_status(correlation_id)

AI Transcribe status

Get status of **[transcribe](../open_api.json/paths/~1ai~1transcribe)** job using `correlation_id`

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
    api_instance = opensubtitles_client.AITranscribeApi(api_client)
    correlation_id = 'correlation_id_example' # str | correlation_id

    try:
        # AI Transcribe status
        api_instance.transcribe_status(correlation_id)
    except Exception as e:
        print("Exception when calling AITranscribeApi->transcribe_status: %s\n" % e)
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

