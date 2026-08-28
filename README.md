Condensed README validated: 61 lines.
# OpenSubtitles Python Client

Typed Python client for the OpenSubtitles REST API, generated from the OpenAPI 3.0.3 specification.

> This is an independent client library. It is not affiliated with or endorsed by OpenSubtitles.

## Installation

```bash
pip install opensubtitles-python-client
```

To upgrade:

```bash
pip install --upgrade opensubtitles-python-client
```

## Quick start

```python
import opensubtitles_client
from opensubtitles_client.rest import ApiException

configuration = opensubtitles_client.Configuration()
configuration.api_key["Api-Key"] = "your-api-key"

with opensubtitles_client.ApiClient(configuration) as api_client:
    subtitles = opensubtitles_client.SubtitlesApi(api_client)
    try:
        response = subtitles.subtitles(query="The Matrix", languages="en")
        print(response)
    except ApiException as error:
        print(error)
```

For authenticated endpoints, set `configuration.access_token` to the JWT returned by `AuthenticationApi.login`.

## API coverage

The package includes all 23 operations described by the bundled OpenAPI specification: authentication, subtitle search/download, discovery, metadata, account/credits, AI translation/transcription, language detection, and filename parsing.

- [API endpoint reference](docs/)
- [Model reference](docs/)
- [OpenAPI specification](openapi/open_api.json)
- [Release notes](https://github.com/luizfgemi/opensubtitles-python-client/releases)
- [PyPI project](https://pypi.org/project/opensubtitles-python-client/)

## Development

Regenerate the client from the bundled specification with Docker:

```bash
./scripts/generate-client.sh
```

See [TODO.md](TODO.md) for known follow-up work and an upstream specification caveat.

## License

[MIT](LICENSE)
