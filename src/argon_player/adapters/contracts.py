"""Source adapter contracts for Argon Player integrations.

AP-002 defines typed request/response contracts so all providers expose
consistent operations: discover, catalog, search, resolve_stream, health_check.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any

from argon_player.domain.models import CatalogItem, Source, StreamOption


@dataclass(slots=True)
class DiscoverRequest:
    """Input for source discovery (manifest/capability probes)."""

    source_url: str | None = None


@dataclass(slots=True)
class DiscoverResponse:
    """Result of discovering a source endpoint and metadata."""

    source: Source


@dataclass(slots=True)
class CatalogRequest:
    """Input for fetching a page of catalog items."""

    limit: int = 50
    cursor: str | None = None


@dataclass(slots=True)
class CatalogResponse:
    """Result page for catalog queries."""

    items: tuple[CatalogItem, ...]
    next_cursor: str | None = None


@dataclass(slots=True)
class SearchRequest:
    """Input for a provider-side search."""

    query: str
    limit: int = 25


@dataclass(slots=True)
class SearchResponse:
    """Result set for a search query."""

    items: tuple[CatalogItem, ...]


@dataclass(slots=True)
class ResolveStreamRequest:
    """Input for resolving stream options for an item."""

    item_id: str


@dataclass(slots=True)
class ResolveStreamResponse:
    """Resolved streams for playback selection."""

    streams: tuple[StreamOption, ...]


@dataclass(slots=True)
class HealthCheckResponse:
    """Health status for observability and source management UI."""

    ok: bool
    latency_ms: int
    details: dict[str, Any] = field(default_factory=dict)


class SourceAdapter(ABC):
    """Provider-agnostic adapter interface for all source integrations."""

    @property
    @abstractmethod
    def source_id(self) -> str:
        """Unique configured source identifier."""

    @abstractmethod
    def discover(self, request: DiscoverRequest) -> DiscoverResponse:
        """Probe source metadata/capabilities."""

    @abstractmethod
    def catalog(self, request: CatalogRequest) -> CatalogResponse:
        """Fetch source catalog entries."""

    @abstractmethod
    def search(self, request: SearchRequest) -> SearchResponse:
        """Search source catalog by text query."""

    @abstractmethod
    def resolve_stream(self, request: ResolveStreamRequest) -> ResolveStreamResponse:
        """Resolve playable streams for a catalog item."""

    @abstractmethod
    def health_check(self) -> HealthCheckResponse:
        """Perform lightweight source health check."""
