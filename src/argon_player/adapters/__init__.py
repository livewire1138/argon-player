"""Source adapter contracts and PoC implementations."""

from argon_player.adapters.contracts import (
    CatalogRequest,
    CatalogResponse,
    DiscoverRequest,
    DiscoverResponse,
    HealthCheckResponse,
    ResolveStreamRequest,
    ResolveStreamResponse,
    SearchRequest,
    SearchResponse,
    SourceAdapter,
)
from argon_player.adapters.mock import InMemorySourceAdapter

__all__ = [
    "CatalogRequest",
    "CatalogResponse",
    "DiscoverRequest",
    "DiscoverResponse",
    "HealthCheckResponse",
    "ResolveStreamRequest",
    "ResolveStreamResponse",
    "SearchRequest",
    "SearchResponse",
    "SourceAdapter",
    "InMemorySourceAdapter",
]
