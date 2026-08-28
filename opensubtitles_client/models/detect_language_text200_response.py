# coding: utf-8

"""Model for the ``detect_language_text`` response."""

from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict
from typing_extensions import Self

from opensubtitles_client.models.detect_language_text200_response_data import (
    DetectLanguageText200ResponseData,
)


class DetectLanguageText200Response(BaseModel):
    """Response returned by the text language detection endpoint."""

    data: Optional[DetectLanguageText200ResponseData] = None
    __properties: ClassVar[List[str]] = ["data"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        excluded_fields: Set[str] = set()
        result = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        if self.data:
            result["data"] = self.data.to_dict()
        return result

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        return cls.model_validate(
            {
                "data": DetectLanguageText200ResponseData.from_dict(obj["data"])
                if obj.get("data") is not None
                else None,
            }
        )
