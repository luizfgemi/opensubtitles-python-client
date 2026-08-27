# opensubtitles_client.SubtitlesApi

All URIs are relative to *https://api.opensubtitles.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subtitles**](SubtitlesApi.md#subtitles) | **GET** /subtitles | Search for subtitles


# **subtitles**
> Subtitles200Response subtitles(id=id, imdb_id=imdb_id, tmdb_id=tmdb_id, type=type, query=query, languages=languages, moviehash=moviehash, uploader_id=uploader_id, hearing_impaired=hearing_impaired, foreign_parts_only=foreign_parts_only, trusted_sources=trusted_sources, machine_translated=machine_translated, ai_translated=ai_translated, order_by=order_by, order_direction=order_direction, parent_feature_id=parent_feature_id, parent_imdb_id=parent_imdb_id, parent_tmdb_id=parent_tmdb_id, season_number=season_number, episode_number=episode_number, year=year, moviehash_match=moviehash_match, page=page, user_agent=user_agent)

Search for subtitles

Find subtitle for a video file. All parameters can be combined following various logics: searching by a specific external id (imdb, tmdb), a file moviehash, or a simple text query.

<!-- theme: warning -->
> Something wrong? Read about [common mistakes and best practices](docs/2-Best-Practices.md). 

> Getting no results? Follow HTTP redirects! ```curl --location``` and use verbose mode

> Use ```imdb_id for``` movie or episode. Use ```parent_imdb_id``` for TV Shows



Implement the logic that best fits your needs, keeping in mind the following guidelines:

- If you can obtain the moviehash from the file, please send it along.
- If you possess the ID, whether it's IMDB or TMDB, send it instead of a query, as an ID provides more precision.
- When searching for TV show episodes, it is recommended to send the parent ID, along with the episode and season number for optimal results.  If you have the unique ID of an episode, only send this ID, excluding the episode or season number.
- Include the filename as a query parameter along with the moviehash for improved results. If your filenames are generally irrelevant, such as dynamically generated filenames from a streaming service, there's no need to include them.
- Consider treating parameters as filters rather than additional criteria. If you have a specific ID and send a query with conflicting data, like a wrong year, it could result in fewer matches.
- Explore querying the /features endpoint to gather the exact list of available episodes.
- Keep in mind that this is a collaborative project where subtitles are submitted by users, filtered by admins, and movie/show results are processed through various APIs. Occasionally, errors may occur, and we depend on user feedback to address and rectify them.


> Avoid http redirection by sending request parameters sorted and without default values, and send all queries in lowercase. Remove leading zeroes in ID parameters (IMDB ID, TMDB ID...)

### Moviehash 
If a ```moviehash``` is sent with a request, a ```moviehash_match``` boolean field will be added to the response.

The matching subtitles will always come first in the response.


### Ordering

<!-- theme: warning -->
> If possible, don't order results, because sorting on server is "expensive, time consuming operation" and also you have much higher chance to get cached result when not using this function.

You can order the results using the ```order_by``` parameter. Ordering is possible on the following fields:
```language```, ```download_count```, ```new_download_count```, ```hearing_impaired```, ```hd```, ```fps```, ```votes```, ```points```, ```ratings```, ```from_trusted```, ```foreign_parts_only```, ```ai_translated```, ```machine_translated```, ```upload_date```, ```release```, ```comments```

Change the order direction with *order_direction* (asc/desc)

### Final notes
```ai_translated``` (default include in search results) subtitles should be much better quality than ```machine_translated``` subtitles (excluded in search results).

### Example

* Api Key Authentication (Api-Key):

```python
import opensubtitles_client
from opensubtitles_client.models.subtitles200_response import Subtitles200Response
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
    api_instance = opensubtitles_client.SubtitlesApi(api_client)
    id = 56 # int | ID of the movie or episode (optional)
    imdb_id = 56 # int | IMDB ID of the movie or episode (optional)
    tmdb_id = 56 # int | TMDB ID of the movie or episode (optional)
    type = 'type_example' # str | movie, episode or all, (default: all)  (optional)
    query = 'query_example' # str | file name or text search (optional)
    languages = 'languages_example' # str | Language code(s), comma separated, sorted in alphabetical order (en,fr) (optional)
    moviehash = 'moviehash_example' # str | Moviehash of the moviefile (optional)
    uploader_id = 56 # int | To be used alone - for user uploads listing (optional)
    hearing_impaired = 'hearing_impaired_example' # str | include, exclude, only. (default: include) (optional)
    foreign_parts_only = 'foreign_parts_only_example' # str | exclude, include, only (default: include) (optional)
    trusted_sources = 'trusted_sources_example' # str | include, only (default: include) (optional)
    machine_translated = 'machine_translated_example' # str | exclude, include  (default: exclude) (optional)
    ai_translated = 'ai_translated_example' # str | exclude, include  (default: include) (optional)
    order_by = 'order_by_example' # str | Order of the returned results, accept any of above fields (optional)
    order_direction = 'order_direction_example' # str | Order direction of the returned results (asc,desc) (optional)
    parent_feature_id = 56 # int | For Tvshows (optional)
    parent_imdb_id = 56 # int | For Tvshows (optional)
    parent_tmdb_id = 56 # int | For Tvshows (optional)
    season_number = 56 # int | For Tvshows  (optional)
    episode_number = 56 # int | For Tvshows (optional)
    year = 56 # int | Filter by movie/episode year (optional)
    moviehash_match = 'moviehash_match_example' # str | include, only (default: include) (optional)
    page = 56 # int | Results page to display (optional)
    user_agent = 'user_agent_example' # str | <<{{APP_NAME}} v{{APP_VERSION}}>> (optional)

    try:
        # Search for subtitles
        api_response = api_instance.subtitles(id=id, imdb_id=imdb_id, tmdb_id=tmdb_id, type=type, query=query, languages=languages, moviehash=moviehash, uploader_id=uploader_id, hearing_impaired=hearing_impaired, foreign_parts_only=foreign_parts_only, trusted_sources=trusted_sources, machine_translated=machine_translated, ai_translated=ai_translated, order_by=order_by, order_direction=order_direction, parent_feature_id=parent_feature_id, parent_imdb_id=parent_imdb_id, parent_tmdb_id=parent_tmdb_id, season_number=season_number, episode_number=episode_number, year=year, moviehash_match=moviehash_match, page=page, user_agent=user_agent)
        print("The response of SubtitlesApi->subtitles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubtitlesApi->subtitles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the movie or episode | [optional] 
 **imdb_id** | **int**| IMDB ID of the movie or episode | [optional] 
 **tmdb_id** | **int**| TMDB ID of the movie or episode | [optional] 
 **type** | **str**| movie, episode or all, (default: all)  | [optional] 
 **query** | **str**| file name or text search | [optional] 
 **languages** | **str**| Language code(s), comma separated, sorted in alphabetical order (en,fr) | [optional] 
 **moviehash** | **str**| Moviehash of the moviefile | [optional] 
 **uploader_id** | **int**| To be used alone - for user uploads listing | [optional] 
 **hearing_impaired** | **str**| include, exclude, only. (default: include) | [optional] 
 **foreign_parts_only** | **str**| exclude, include, only (default: include) | [optional] 
 **trusted_sources** | **str**| include, only (default: include) | [optional] 
 **machine_translated** | **str**| exclude, include  (default: exclude) | [optional] 
 **ai_translated** | **str**| exclude, include  (default: include) | [optional] 
 **order_by** | **str**| Order of the returned results, accept any of above fields | [optional] 
 **order_direction** | **str**| Order direction of the returned results (asc,desc) | [optional] 
 **parent_feature_id** | **int**| For Tvshows | [optional] 
 **parent_imdb_id** | **int**| For Tvshows | [optional] 
 **parent_tmdb_id** | **int**| For Tvshows | [optional] 
 **season_number** | **int**| For Tvshows  | [optional] 
 **episode_number** | **int**| For Tvshows | [optional] 
 **year** | **int**| Filter by movie/episode year | [optional] 
 **moviehash_match** | **str**| include, only (default: include) | [optional] 
 **page** | **int**| Results page to display | [optional] 
 **user_agent** | **str**| &lt;&lt;{{APP_NAME}} v{{APP_VERSION}}&gt;&gt; | [optional] 

### Return type

[**Subtitles200Response**](Subtitles200Response.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

