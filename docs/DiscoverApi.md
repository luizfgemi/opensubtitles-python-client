# opensubtitles_client.DiscoverApi

All URIs are relative to *https://api.opensubtitles.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**latest**](DiscoverApi.md#latest) | **GET** /discover/latest | Latest subtitles
[**most_downloaded**](DiscoverApi.md#most_downloaded) | **GET** /discover/most_downloaded | Most downloaded subtitles
[**popular**](DiscoverApi.md#popular) | **GET** /discover/popular | Popular features


# **latest**
> Latest200Response latest(language=language, type=type, user_agent=user_agent)

Latest subtitles

Lists 60 latest uploaded subtitles

### Example

* Api Key Authentication (Api-Key):

```python
import opensubtitles_client
from opensubtitles_client.models.latest200_response import Latest200Response
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
    api_instance = opensubtitles_client.DiscoverApi(api_client)
    language = 'language_example' # str | Language code, 1 language per query, or \"all\" (optional)
    type = 'type_example' # str | Type (movie or tvshow) (optional)
    user_agent = 'user_agent_example' # str | <<{{APP_NAME}} v{{APP_VERSION}}>> (optional)

    try:
        # Latest subtitles
        api_response = api_instance.latest(language=language, type=type, user_agent=user_agent)
        print("The response of DiscoverApi->latest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscoverApi->latest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| Language code, 1 language per query, or \&quot;all\&quot; | [optional] 
 **type** | **str**| Type (movie or tvshow) | [optional] 
 **user_agent** | **str**| &lt;&lt;{{APP_NAME}} v{{APP_VERSION}}&gt;&gt; | [optional] 

### Return type

[**Latest200Response**](Latest200Response.md)

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

# **most_downloaded**
> MostDownloaded200Response most_downloaded(language=language, type=type, user_agent=user_agent)

Most downloaded subtitles

Discover popular subtitles, according to last 30 days downloads on opensubtitles.com. This list can be filtered by language code or feature type (movie, episode)

### Example

* Api Key Authentication (Api-Key):

```python
import opensubtitles_client
from opensubtitles_client.models.most_downloaded200_response import MostDownloaded200Response
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
    api_instance = opensubtitles_client.DiscoverApi(api_client)
    language = 'language_example' # str | Language code, 1 language per query, or \"all\" (optional)
    type = 'type_example' # str | Type (movie or tvshow) (optional)
    user_agent = 'user_agent_example' # str | <<{{APP_NAME}} v{{APP_VERSION}}>> (optional)

    try:
        # Most downloaded subtitles
        api_response = api_instance.most_downloaded(language=language, type=type, user_agent=user_agent)
        print("The response of DiscoverApi->most_downloaded:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscoverApi->most_downloaded: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| Language code, 1 language per query, or \&quot;all\&quot; | [optional] 
 **type** | **str**| Type (movie or tvshow) | [optional] 
 **user_agent** | **str**| &lt;&lt;{{APP_NAME}} v{{APP_VERSION}}&gt;&gt; | [optional] 

### Return type

[**MostDownloaded200Response**](MostDownloaded200Response.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Lists most downloaded movie subtitles  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **popular**
> Subtitle popular(language=language, type=type, user_agent=user_agent)

Popular features

Discover popular features on opensubtitles.com, according to last 30 days downloads.

### Example

* Api Key Authentication (Api-Key):

```python
import opensubtitles_client
from opensubtitles_client.models.subtitle import Subtitle
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
    api_instance = opensubtitles_client.DiscoverApi(api_client)
    language = 'language_example' # str | Language code, 1 language per query, or \"all\" (optional)
    type = 'type_example' # str | Type (movie or tvshow) (optional)
    user_agent = 'user_agent_example' # str | <<{{APP_NAME}} v{{APP_VERSION}}>> (optional)

    try:
        # Popular features
        api_response = api_instance.popular(language=language, type=type, user_agent=user_agent)
        print("The response of DiscoverApi->popular:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscoverApi->popular: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| Language code, 1 language per query, or \&quot;all\&quot; | [optional] 
 **type** | **str**| Type (movie or tvshow) | [optional] 
 **user_agent** | **str**| &lt;&lt;{{APP_NAME}} v{{APP_VERSION}}&gt;&gt; | [optional] 

### Return type

[**Subtitle**](Subtitle.md)

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

