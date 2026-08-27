# opensubtitles_client.AuthenticationApi

All URIs are relative to *https://api.opensubtitles.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](AuthenticationApi.md#login) | **POST** /login | Login
[**logout**](AuthenticationApi.md#logout) | **DELETE** /logout | Logout


# **login**
> Login200Response login(content_type, user_agent=user_agent, login_request=login_request)

Login

Create a token to authenticate a user. If response code is ```401 Unathorized``` stop sending further requests with the same credentials, login is "expensive" operation.

Request rate limit is 1 request per 1 second, 10 requests per minute and 30 requests per hour because some clients just endlessly sending wrong credentials in loop.

Further API requests must continue on returned ```base_url``` host, which can have different cache time for search results and different request rate limits. If ```base_url``` equals ```vip-api.opensubtitles.com``` make sure you always send with every request JWT token (if available), otherwise request might fail with 4xx code.

### Example

* Api Key Authentication (Api-Key):

```python
import opensubtitles_client
from opensubtitles_client.models.login200_response import Login200Response
from opensubtitles_client.models.login_request import LoginRequest
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
    api_instance = opensubtitles_client.AuthenticationApi(api_client)
    content_type = 'application/json' # str | application/json (default to 'application/json')
    user_agent = 'user_agent_example' # str | <<{{APP_NAME}} v{{APP_VERSION}}>> (optional)
    login_request = opensubtitles_client.LoginRequest() # LoginRequest |  (optional)

    try:
        # Login
        api_response = api_instance.login(content_type, user_agent=user_agent, login_request=login_request)
        print("The response of AuthenticationApi->login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| application/json | [default to &#39;application/json&#39;]
 **user_agent** | **str**| &lt;&lt;{{APP_NAME}} v{{APP_VERSION}}&gt;&gt; | [optional] 
 **login_request** | [**LoginRequest**](LoginRequest.md)|  | [optional] 

### Return type

[**Login200Response**](Login200Response.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Create session and token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> object logout(user_agent=user_agent)

Logout

Destroy a user token to end a session. Bearer token is required for this endpoint.

### Example

* Bearer (JWT) Authentication (Bearer):
* Api Key Authentication (Api-Key):

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
    api_instance = opensubtitles_client.AuthenticationApi(api_client)
    user_agent = 'user_agent_example' # str | <<{{APP_NAME}} v{{APP_VERSION}}>> (optional)

    try:
        # Logout
        api_response = api_instance.logout(user_agent=user_agent)
        print("The response of AuthenticationApi->logout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->logout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_agent** | **str**| &lt;&lt;{{APP_NAME}} v{{APP_VERSION}}&gt;&gt; | [optional] 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer), [Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Destroy session and current token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

