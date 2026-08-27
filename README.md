# opensubtitles-python-client
Python client generated from the official OpenSubtitles OpenAPI 3.0.3 specification.

This Python package is generated from the official OpenSubtitles OpenAPI 3.0.3 specification using [OpenAPI Generator](https://openapi-generator.tech).

- API version: 1.0.1
- Package version: 0.1.0
- Generator version: 7.12.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
This is an independent client library and is not affiliated with or endorsed by OpenSubtitles.

## Requirements.

Python 3.8+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/luizfgemi/opensubtitles-python-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/luizfgemi/opensubtitles-python-client.git`)

Then import the package:
```python
import opensubtitles_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import opensubtitles_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
    except ApiException as e:
        print("Exception when calling AITranscribeApi->transcribe: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.opensubtitles.com/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AITranscribeApi* | [**transcribe**](docs/AITranscribeApi.md#transcribe) | **POST** /ai/transcribe | AI Transcribe
*AITranscribeApi* | [**transcribe_status**](docs/AITranscribeApi.md#transcribe_status) | **GET** /ai/transcribe/{correlation_id} | AI Transcribe status
*AITranslateApi* | [**translate**](docs/AITranslateApi.md#translate) | **POST** /ai/translate | AI Translate
*AITranslateApi* | [**translate_status**](docs/AITranslateApi.md#translate_status) | **GET** /ai/translate/{correlation_id} | AI Translate status
*AuthenticationApi* | [**login**](docs/AuthenticationApi.md#login) | **POST** /login | Login
*AuthenticationApi* | [**logout**](docs/AuthenticationApi.md#logout) | **DELETE** /logout | Logout
*DiscoverApi* | [**latest**](docs/DiscoverApi.md#latest) | **GET** /discover/latest | Latest subtitles
*DiscoverApi* | [**most_downloaded**](docs/DiscoverApi.md#most_downloaded) | **GET** /discover/most_downloaded | Most downloaded subtitles
*DiscoverApi* | [**popular**](docs/DiscoverApi.md#popular) | **GET** /discover/popular | Popular features
*DownloadApi* | [**download**](docs/DownloadApi.md#download) | **POST** /download | Download
*FeaturesApi* | [**features**](docs/FeaturesApi.md#features) | **GET** /features | Search for features
*InfosApi* | [**formats**](docs/InfosApi.md#formats) | **GET** /infos/formats | Subtitle Formats
*InfosApi* | [**languages**](docs/InfosApi.md#languages) | **GET** /infos/languages | Languages
*InfosApi* | [**transcription**](docs/InfosApi.md#transcription) | **GET** /ai/info/transcription | AI Transcription
*InfosApi* | [**translation**](docs/InfosApi.md#translation) | **GET** /ai/info/translation | AI Translation
*SubtitlesApi* | [**subtitles**](docs/SubtitlesApi.md#subtitles) | **GET** /subtitles | Search for subtitles
*UserApi* | [**buy_credits**](docs/UserApi.md#buy_credits) | **GET** /ai/credits/buy | Buy Credits
*UserApi* | [**get_credits**](docs/UserApi.md#get_credits) | **GET** /ai/credits | User Credits Informations
*UserApi* | [**userinfo**](docs/UserApi.md#userinfo) | **GET** /infos/user | User Informations
*UtilitiesApi* | [**detect_language_audio**](docs/UtilitiesApi.md#detect_language_audio) | **POST** /ai/detect_language_audio | Detect Language Audio
*UtilitiesApi* | [**detect_language_audio_status**](docs/UtilitiesApi.md#detect_language_audio_status) | **GET** /ai/detect_language_audio/{correlation_id} | Detect Language Audio Status
*UtilitiesApi* | [**detect_language_text**](docs/UtilitiesApi.md#detect_language_text) | **POST** /ai/detect_language_text | Detect Language Text
*UtilitiesApi* | [**guessit**](docs/UtilitiesApi.md#guessit) | **GET** /utilities/guessit | Guessit


## Documentation For Models

 - [BuyCredits200Response](docs/BuyCredits200Response.md)
 - [BuyCredits200ResponseDataInner](docs/BuyCredits200ResponseDataInner.md)
 - [DetectLanguageText200ResponseData](docs/DetectLanguageText200ResponseData.md)
 - [DetectLanguageText200ResponseDataLanguage](docs/DetectLanguageText200ResponseDataLanguage.md)
 - [Download200Response](docs/Download200Response.md)
 - [DownloadRequest](docs/DownloadRequest.md)
 - [FeatureEpisode](docs/FeatureEpisode.md)
 - [FeatureEpisodeAttributes](docs/FeatureEpisodeAttributes.md)
 - [FeatureEpisodeAttributesSubtitlesCounts](docs/FeatureEpisodeAttributesSubtitlesCounts.md)
 - [FeatureMovie](docs/FeatureMovie.md)
 - [FeatureMovieAttributes](docs/FeatureMovieAttributes.md)
 - [FeatureMovieAttributesSubtitlesCounts](docs/FeatureMovieAttributesSubtitlesCounts.md)
 - [FeatureTvshow](docs/FeatureTvshow.md)
 - [FeatureTvshowAttributes](docs/FeatureTvshowAttributes.md)
 - [FeatureTvshowAttributesSeasonsInner](docs/FeatureTvshowAttributesSeasonsInner.md)
 - [FeatureTvshowAttributesSeasonsInnerEpisodesInner](docs/FeatureTvshowAttributesSeasonsInnerEpisodesInner.md)
 - [FeatureTvshowAttributesSubtitlesCounts](docs/FeatureTvshowAttributesSubtitlesCounts.md)
 - [Features200Response](docs/Features200Response.md)
 - [Formats200Response](docs/Formats200Response.md)
 - [Formats200ResponseData](docs/Formats200ResponseData.md)
 - [GetCredits200Response](docs/GetCredits200Response.md)
 - [GetCredits200ResponseData](docs/GetCredits200ResponseData.md)
 - [Guessit200Response](docs/Guessit200Response.md)
 - [Languages200Response](docs/Languages200Response.md)
 - [Languages200ResponseDataInner](docs/Languages200ResponseDataInner.md)
 - [Latest200Response](docs/Latest200Response.md)
 - [Latest200ResponseDataInner](docs/Latest200ResponseDataInner.md)
 - [Latest200ResponseDataInnerAttributes](docs/Latest200ResponseDataInnerAttributes.md)
 - [Latest200ResponseDataInnerAttributesFeatureDetails](docs/Latest200ResponseDataInnerAttributesFeatureDetails.md)
 - [Latest200ResponseDataInnerAttributesFilesInner](docs/Latest200ResponseDataInnerAttributesFilesInner.md)
 - [Latest200ResponseDataInnerAttributesRelatedLinks](docs/Latest200ResponseDataInnerAttributesRelatedLinks.md)
 - [Latest200ResponseDataInnerAttributesUploader](docs/Latest200ResponseDataInnerAttributesUploader.md)
 - [Login200Response](docs/Login200Response.md)
 - [Login200ResponseUser](docs/Login200ResponseUser.md)
 - [LoginRequest](docs/LoginRequest.md)
 - [MostDownloaded200Response](docs/MostDownloaded200Response.md)
 - [Subtitle](docs/Subtitle.md)
 - [SubtitleAttributes](docs/SubtitleAttributes.md)
 - [SubtitleAttributesFeatureDetails](docs/SubtitleAttributesFeatureDetails.md)
 - [SubtitleAttributesFilesInner](docs/SubtitleAttributesFilesInner.md)
 - [SubtitleAttributesUploader](docs/SubtitleAttributesUploader.md)
 - [Subtitles200Response](docs/Subtitles200Response.md)
 - [Subtitles200ResponseDataInner](docs/Subtitles200ResponseDataInner.md)
 - [Subtitles200ResponseDataInnerAttributes](docs/Subtitles200ResponseDataInnerAttributes.md)
 - [Subtitles200ResponseDataInnerAttributesFeatureDetails](docs/Subtitles200ResponseDataInnerAttributesFeatureDetails.md)
 - [Subtitles200ResponseDataInnerAttributesFilesInner](docs/Subtitles200ResponseDataInnerAttributesFilesInner.md)
 - [Subtitles200ResponseDataInnerAttributesRelatedLinksInner](docs/Subtitles200ResponseDataInnerAttributesRelatedLinksInner.md)
 - [Subtitles200ResponseDataInnerAttributesUploader](docs/Subtitles200ResponseDataInnerAttributesUploader.md)
 - [Transcription200Response](docs/Transcription200Response.md)
 - [Translation200Response](docs/Translation200Response.md)
 - [Translation200ResponseDataInner](docs/Translation200ResponseDataInner.md)
 - [Translation200ResponseDataInnerLanguagesSupportedInner](docs/Translation200ResponseDataInnerLanguagesSupportedInner.md)
 - [Userinfo200Response](docs/Userinfo200Response.md)
 - [Userinfo200ResponseData](docs/Userinfo200ResponseData.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="Api-Key"></a>
### Api-Key

- **Type**: API key
- **API key parameter name**: Api-Key
- **Location**: HTTP header

<a id="Bearer"></a>
### Bearer

- **Type**: Bearer authentication (JWT)


## Author

support@opensubtitles.org
