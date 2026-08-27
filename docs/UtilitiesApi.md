# opensubtitles_client.UtilitiesApi

All URIs are relative to *https://api.opensubtitles.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**detect_language_audio**](UtilitiesApi.md#detect_language_audio) | **POST** /ai/detect_language_audio | Detect Language Audio
[**detect_language_audio_status**](UtilitiesApi.md#detect_language_audio_status) | **GET** /ai/detect_language_audio/{correlation_id} | Detect Language Audio Status
[**detect_language_text**](UtilitiesApi.md#detect_language_text) | **POST** /ai/detect_language_text | Detect Language Text
[**guessit**](UtilitiesApi.md#guessit) | **GET** /utilities/guessit | Guessit


# **detect_language_audio**
> object detect_language_audio(api, file, language)

Detect Language Audio

**Detect language**  of media audio file. Max size of file: 100 MB 

At least 1 credits on user account is needed. [Buy Credits](../open_api.json/paths/~1ai~1credits~1buy/get)

Check following method: [Get Detect Language Audio status](../open_api.json/paths/~1ai~1detect_language_audio~1{correlation_id}/get)

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
    api_instance = opensubtitles_client.UtilitiesApi(api_client)
    api = 'api_example' # str | transcribe API
    file = 'file_example' # str | media file
    language = 'language_example' # str | language of media file

    try:
        # Detect Language Audio
        api_response = api_instance.detect_language_audio(api, file, language)
        print("The response of UtilitiesApi->detect_language_audio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilitiesApi->detect_language_audio: %s\n" % e)
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

# **detect_language_audio_status**
> detect_language_audio_status(correlation_id)

Detect Language Audio Status

Get status of **[Detect Language Audio](../open_api.json/paths/~1ai~1detect_language_audio/post)** job using `correlation_id`


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
    api_instance = opensubtitles_client.UtilitiesApi(api_client)
    correlation_id = 'correlation_id_example' # str | correlation_id

    try:
        # Detect Language Audio Status
        api_instance.detect_language_audio_status(correlation_id)
    except Exception as e:
        print("Exception when calling UtilitiesApi->detect_language_audio_status: %s\n" % e)
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

# **detect_language_text**
> DetectLanguageText200Response detect_language_text(file)

Detect Language Text

**Detect language** of subtitle file.

At least 1 credits on user account is needed. [Buy Credits](../open_api.json/paths/~1ai~1credits~1buy/get)

Method is returning 
```
{
  "data": {
    "format": "SubRip",
    "type": "text",
    "language": {
      "W3C": "en",
      "name": "english",
      "native": "english",
      "ISO_639_1": "en",
      "ISO_639_2b": "eng"
    }
  }
}
```

### Example

* Api Key Authentication (Api-Key):
* Bearer (JWT) Authentication (Bearer):

```python
import opensubtitles_client
from opensubtitles_client.models.detect_language_text200_response import DetectLanguageText200Response
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
    api_instance = opensubtitles_client.UtilitiesApi(api_client)
    file = 'file_example' # str | subtitle file

    try:
        # Detect Language Text
        api_response = api_instance.detect_language_text(file)
        print("The response of UtilitiesApi->detect_language_text:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilitiesApi->detect_language_text: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**| subtitle file | 

### Return type

[**DetectLanguageText200Response**](DetectLanguageText200Response.md)

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

# **guessit**
> Guessit200Response guessit(filename=filename, user_agent=user_agent)

Guessit

Extracts as much information as possible from a video filename.

It has a very powerful matcher that allows to guess properties from a video using its filename only. This matcher works with both movies and tv shows episodes.

This is a simple implementation of the python guessit library.
https://guessit-io.github.io/guessit/

Find examples of the returned data.
https://guessit-io.github.io/guessit/properties/

### Example

* Api Key Authentication (Api-Key):

```python
import opensubtitles_client
from opensubtitles_client.models.guessit200_response import Guessit200Response
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

# Enter a context with an instance of the API client
with opensubtitles_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opensubtitles_client.UtilitiesApi(api_client)
    filename = 'filename_example' # str | File name (optional)
    user_agent = 'user_agent_example' # str | <<{{APP_NAME}} v{{APP_VERSION}}>> (optional)

    try:
        # Guessit
        api_response = api_instance.guessit(filename=filename, user_agent=user_agent)
        print("The response of UtilitiesApi->guessit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilitiesApi->guessit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**| File name | [optional] 
 **user_agent** | **str**| &lt;&lt;{{APP_NAME}} v{{APP_VERSION}}&gt;&gt; | [optional] 

### Return type

[**Guessit200Response**](Guessit200Response.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

