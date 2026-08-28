# OpenSubtitles Python Client

Python client for the [OpenSubtitles API](https://opensubtitles.stoplight.io/).

> Independent client library; not affiliated with or endorsed by OpenSubtitles.

## Install

```bash
pip install opensubtitles-python-client
```

## Before you start

You need an [OpenSubtitles account](https://www.opensubtitles.com/) and an API key created for your application.

- **API key:** identifies your application and is required for API requests.
- **JWT token:** identifies a logged-in user. Obtain it with `AuthenticationApi.login` and use it only for authenticated operations, such as downloading subtitles. VIP access is associated with this user token.

## Search subtitles

Pass the API key to the client. The library does not read environment variables or configuration files.

```python
import opensubtitles_client

configuration = opensubtitles_client.Configuration()
configuration.api_key["Api-Key"] = "your-api-key"

with opensubtitles_client.ApiClient(configuration) as client:
    api = opensubtitles_client.SubtitlesApi(client)
    response = api.subtitles(query="The Matrix", languages="en")
    print(response)
```

## Download a subtitle

Downloading requires both your API key and the JWT returned by `AuthenticationApi.login`.

```python
configuration.access_token = "your-jwt"

with opensubtitles_client.ApiClient(configuration) as client:
    api = opensubtitles_client.DownloadApi(client)
    response = api.download(body={"file_id": 123})
    print(response.link)  # Temporary download URL
```

## Reference

- [Endpoint and model documentation](docs/)
- [Bundled OpenAPI specification](openapi/open_api.json)
- [PyPI package](https://pypi.org/project/opensubtitles-python-client/)
- [Releases](https://github.com/luizfgemi/opensubtitles-python-client/releases)

## License

[MIT](LICENSE)
