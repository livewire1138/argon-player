"""Error taxonomy and user-facing mappings for Argon Player."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class ErrorCategory(str, Enum):
    NETWORK = "network"
    AUTH = "auth"
    NOT_FOUND = "not_found"
    GEO = "geo"
    UNSUPPORTED = "unsupported"
    TRANSIENT = "transient"
    PERMANENT = "permanent"


USER_SAFE_MESSAGES: dict[ErrorCategory, str] = {
    ErrorCategory.NETWORK: "Network issue while contacting source. Please retry.",
    ErrorCategory.AUTH: "Authentication failed. Verify source credentials.",
    ErrorCategory.NOT_FOUND: "Requested media could not be found on this source.",
    ErrorCategory.GEO: "This stream is unavailable in your current region.",
    ErrorCategory.UNSUPPORTED: "This source does not support the requested operation.",
    ErrorCategory.TRANSIENT: "Temporary upstream issue detected. Please retry shortly.",
    ErrorCategory.PERMANENT: "Operation failed due to a permanent source-side error.",
}


@dataclass(slots=True)
class ArgonError(Exception):
    """Typed error that adapters can raise and the UI can safely display."""

    category: ErrorCategory
    detail: str
    source_id: str | None = None

    def user_message(self) -> str:
        """Return a user-safe message with no sensitive details."""

        return USER_SAFE_MESSAGES[self.category]

    def __str__(self) -> str:
        source = f" source={self.source_id}" if self.source_id else ""
        return f"{self.category.value}: {self.detail}{source}"
