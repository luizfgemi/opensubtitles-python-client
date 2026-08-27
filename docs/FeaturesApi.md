# opensubtitles_client.FeaturesApi

All URIs are relative to *https://api.opensubtitles.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**features**](FeaturesApi.md#features) | **GET** /features | Search for features


# **features**
> Features200Response features(query=query, type=type, feature_id=feature_id, imdb_id=imdb_id, tmdb_id=tmdb_id, year=year, user_agent=user_agent, query_match=query_match, full_search=full_search)

Search for features

With the "query" parameter, search for a Feature from a simple text input. Typically used for a text search or autocomplete.

With an ID, get basic information and subtitles count for a specific title.

With the "query_match" you can define the matched applied to the query: 
 - "start" is the default behavior, it will query on the first letter entered to offer suggestions
 - "word" will return the match on the word, but not always matching the fulll title, for example searching "roma" will return "holiday in roma"
 - "exact" will exactly match the title, so here searching for "roma" will only return the movie(s) named "roma" 

With the "full_search" you can extend the search to the translations of the title, so "roma" will also return "rome" 

<!-- theme: warning -->

> ### Watch Out!
>
> If you create an autocomplete, don't set a too small refresh limit, remember you must not go over 40 requests per 10 seconds!

### Example

* Api Key Authentication (Api-Key):

```python
import opensubtitles_client
from opensubtitles_client.models.features200_response import Features200Response
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
    api_instance = opensubtitles_client.FeaturesApi(api_client)
    query = 'query_example' # str | query to search, release/file name accepted (optional)
    type = 'type_example' # str | empty to list all or **movie**, **tvshow** or **episode**. (optional)
    feature_id = 56 # int | opensubtitles **feature_id** (optional)
    imdb_id = 'imdb_id_example' # str | IMDB ID, delete leading zeroes (optional)
    tmdb_id = 'tmdb_id_example' # str | TheMovieDB ID - combine with type to avoid errors (optional)
    year = 56 # int | Filter by year. Can only be used in combination with a query (optional)
    user_agent = 'user_agent_example' # str | <<{{APP_NAME}} v{{APP_VERSION}}>> (optional)
    query_match = 'query_match_example' # str | Type of matching applied to the query: **start** (default), **word**, **exact**   (optional)
    full_search = True # bool | Search on original title and title aka (translations) (default false) (optional)

    try:
        # Search for features
        api_response = api_instance.features(query=query, type=type, feature_id=feature_id, imdb_id=imdb_id, tmdb_id=tmdb_id, year=year, user_agent=user_agent, query_match=query_match, full_search=full_search)
        print("The response of FeaturesApi->features:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeaturesApi->features: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| query to search, release/file name accepted | [optional] 
 **type** | **str**| empty to list all or **movie**, **tvshow** or **episode**. | [optional] 
 **feature_id** | **int**| opensubtitles **feature_id** | [optional] 
 **imdb_id** | **str**| IMDB ID, delete leading zeroes | [optional] 
 **tmdb_id** | **str**| TheMovieDB ID - combine with type to avoid errors | [optional] 
 **year** | **int**| Filter by year. Can only be used in combination with a query | [optional] 
 **user_agent** | **str**| &lt;&lt;{{APP_NAME}} v{{APP_VERSION}}&gt;&gt; | [optional] 
 **query_match** | **str**| Type of matching applied to the query: **start** (default), **word**, **exact**   | [optional] 
 **full_search** | **bool**| Search on original title and title aka (translations) (default false) | [optional] 

### Return type

[**Features200Response**](Features200Response.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Search for a feature |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

