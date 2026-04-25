"""In-memory proof-of-concept adapter implementing SourceAdapter."""

from __future__ import annotations

from dataclasses import dataclass

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
from argon_player.domain.errors import ArgonError, ErrorCategory
from argon_player.domain.models import CatalogItem, Source, StreamOption


@dataclass(slots=True)
class InMemorySourceAdapter(SourceAdapter):
    """Basic adapter for PoC and tests without network dependencies."""

    source: Source
    catalog_items: tuple[CatalogItem, ...]
    stream_index: dict[str, tuple[StreamOption, ...]]

    @property
    def source_id(self) -> str:
        return self.source.id

    def discover(self, request: DiscoverRequest) -> DiscoverResponse:
        _ = request
        return DiscoverResponse(source=self.source)

    def catalog(self, request: CatalogRequest) -> CatalogResponse:
        start = int(request.cursor) if request.cursor else 0
        stop = start + max(request.limit, 0)
        items = self.catalog_items[start:stop]
        next_cursor = str(stop) if stop < len(self.catalog_items) else None
        return CatalogResponse(items=items, next_cursor=next_cursor)

    def search(self, request: SearchRequest) -> SearchResponse:
        query = request.query.strip().lower()
        if not query:
            return SearchResponse(items=())

        matches = tuple(item for item in self.catalog_items if query in item.title.lower())
        return SearchResponse(items=matches[: request.limit])

    def resolve_stream(self, request: ResolveStreamRequest) -> ResolveStreamResponse:
        streams = self.stream_index.get(request.item_id)
        if not streams:
            raise ArgonError(
                category=ErrorCategory.NOT_FOUND,
                detail=f"No stream options found for item_id={request.item_id}",
                source_id=self.source_id,
            )
        return ResolveStreamResponse(streams=streams)

    def health_check(self) -> HealthCheckResponse:
        return HealthCheckResponse(
            ok=True,
            latency_ms=1,
            details={"adapter": "in-memory", "catalog_size": len(self.catalog_items)},
        )
