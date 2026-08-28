#!/usr/bin/env bash
set -euo pipefail

root_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
spec_path="$root_dir/openapi/open_api.json"

docker run --rm \
  -v "$spec_path:/spec/open_api.json:ro" \
  -v "$root_dir:/out" \
  openapitools/openapi-generator-cli:v7.12.0 generate \
  -i /spec/open_api.json \
  -g python \
  -o /out \
  --package-name opensubtitles_client \
  --additional-properties=packageVersion=0.1.1,projectName=opensubtitles-python-client
