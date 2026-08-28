# OpenSubtitles Python Client

Python client for the [OpenSubtitles API](https://opensubtitles.stoplight.io/).

> Independent client library; not affiliated with or endorsed by OpenSubtitles.

## Install

```bash
pip install opensubtitles-python-client
```

## Search subtitles

Create an API key at OpenSubtitles, then pass it to the client. The library does not read environment variables or configuration files.

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
