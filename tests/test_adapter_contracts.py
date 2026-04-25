from argon_player.adapters import (
    CatalogRequest,
    DiscoverRequest,
    InMemorySourceAdapter,
    ResolveStreamRequest,
    SearchRequest,
)
from argon_player.domain.errors import ArgonError, ErrorCategory
from argon_player.domain.models import CatalogItem, ContentType, Source, StreamOption, StreamProtocol


def build_adapter() -> InMemorySourceAdapter:
    source = Source(
        id="src.poc",
        name="PoC Source",
        adapter_kind="mock",
        capabilities=("catalog", "search", "resolve_stream", "health_check"),
    )
    items = (
        CatalogItem(
            id="cat.1",
            source_id=source.id,
            title="The First Movie",
            content_type=ContentType.MOVIE,
        ),
        CatalogItem(
            id="cat.2",
            source_id=source.id,
            title="Second Series",
            content_type=ContentType.SERIES,
        ),
        CatalogItem(
            id="cat.3",
            source_id=source.id,
            title="Live Sports Now",
            content_type=ContentType.LIVE,
        ),
    )
    streams = {
        "cat.1": (
            StreamOption(
                id="stream.1",
                source_id=source.id,
                url="https://example.invalid/cat1.m3u8",
                protocol=StreamProtocol.HLS,
                quality_label="1080p",
            ),
        )
    }
    return InMemorySourceAdapter(source=source, catalog_items=items, stream_index=streams)


def test_in_memory_adapter_supports_core_contract_flow() -> None:
    adapter = build_adapter()

    discover = adapter.discover(DiscoverRequest())
    page1 = adapter.catalog(CatalogRequest(limit=2))
    search = adapter.search(SearchRequest(query="live", limit=5))
    resolved = adapter.resolve_stream(ResolveStreamRequest(item_id="cat.1"))
    health = adapter.health_check()

    assert discover.source.id == "src.poc"
    assert len(page1.items) == 2
    assert page1.next_cursor == "2"
    assert search.items[0].id == "cat.3"
    assert resolved.streams[0].quality_label == "1080p"
    assert health.ok is True


def test_resolve_stream_raises_not_found_when_missing() -> None:
    adapter = build_adapter()

    try:
        adapter.resolve_stream(ResolveStreamRequest(item_id="cat.404"))
    except ArgonError as exc:
        assert exc.category == ErrorCategory.NOT_FOUND
        assert exc.source_id == "src.poc"
    else:
        raise AssertionError("Expected ArgonError for missing stream")
