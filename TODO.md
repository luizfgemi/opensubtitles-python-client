# Roadmap

- Add hand-written tests for authentication, subtitle search, and download flows.
- Add practical examples for the main workflows.
- Improve generated documentation with sanitized API-response examples.
- Regenerate from the upstream OpenAPI specification when it changes and review the generated diff.

## Known specification limitation

The supplied OpenAPI document defines an empty property name in `Subtitle.attributes.files`. Python cannot represent that property as an identifier, so the generated model omits it.
