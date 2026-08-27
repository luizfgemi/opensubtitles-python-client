# Follow-up work

- Add hand-written contract tests for the 23 OpenAPI operations; generated test files are placeholders only.
- Replace generated model-documentation JSON placeholders with valid examples from a sanitized API fixture.
- Add PyPI trusted publishing after the first GitHub release is verified.
- Regenerate when the upstream OpenAPI specification changes and review generated diffs.

## Upstream specification caveat

The supplied OpenAPI document defines an empty property name in `Subtitle.attributes.files`. The Python generator cannot emit a valid identifier for it; the generated model intentionally omits that unusable property.
