# opensubtitles_client.DownloadApi

All URIs are relative to *https://api.opensubtitles.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download**](DownloadApi.md#download) | **POST** /download | Download


# **download**
> Download200Response download(user_agent=user_agent, body=body)

Download

Request a download url for a subtitle. Subtitle file in temporary URL will be always in UTF-8 encoding.

<!-- theme: warning -->

> VERY IMPORTANT: In HTTP request must be both headers: ```Api-Key``` and ```Authorization``` stoplight.io doesn't allow to use in shown example both headers


> The download count is calculated on this action, not the file download itself

> IN and OUT FPS must be indicated for subtitle conversions, we want to make sure you know what you are doing, and therefore collected the current FPS from the subtitle search result, or calculated it somehow.

<!-- theme: warning -->

> The download URL is temporary, and cannot be used more than 3 hours, so do not cache it, but you can download the file more than once if needed.

### Example

* Bearer (JWT) Authentication (Bearer):
* Api Key Authentication (Api-Key):

```python
import opensubtitles_client
from opensubtitles_client.models.download200_response import Download200Response
from opensubtitles_client.models.download_request import DownloadRequest
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

# Configure Bearer authorization (JWT): Bearer
configuration = opensubtitles_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: Api-Key
configuration.api_key['Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Api-Key'] = 'Bearer'

# Enter a context with an instance of the API client
with opensubtitles_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opensubtitles_client.DownloadApi(api_client)
    user_agent = 'user_agent_example' # str | <<{{APP_NAME}} v{{APP_VERSION}}>> (optional)
    body = {"file_id":123} # DownloadRequest |  (optional)

    try:
        # Download
        api_response = api_instance.download(user_agent=user_agent, body=body)
        print("The response of DownloadApi->download:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DownloadApi->download: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_agent** | **str**| &lt;&lt;{{APP_NAME}} v{{APP_VERSION}}&gt;&gt; | [optional] 
 **body** | [**DownloadRequest**](DownloadRequest.md)|  | [optional] 

### Return type

[**Download200Response**](Download200Response.md)

### Authorization

[Bearer](../README.md#Bearer), [Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request a download URL for a subtitle.   |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

