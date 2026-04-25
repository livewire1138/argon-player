from datetime import datetime, timedelta

from argon_player.config.schema import AppConfig, LogLevel, SourceConfig
from argon_player.domain.errors import ArgonError, ErrorCategory
from argon_player.domain.models import (
    CatalogItem,
    ContentType,
    LiveChannel,
    PlaybackSession,
    Program,
    Source,
    StreamOption,
    StreamProtocol,
)


def test_canonical_models_can_be_instantiated() -> None:
    source = Source(id="src.stremio", name="Stremio", adapter_kind="stremio")
    item = CatalogItem(
        id="cat.1",
        source_id=source.id,
        title="Example Movie",
        content_type=ContentType.MOVIE,
    )
    stream = StreamOption(
        id="stream.1",
        source_id=source.id,
        url="https://example.invalid/stream.m3u8",
        protocol=StreamProtocol.HLS,
    )
    now = datetime.utcnow()
    session = PlaybackSession(
        id="sess.1",
        item_id=item.id,
        source_id=source.id,
        stream_option_id=stream.id,
        started_at=now,
    )
    program = Program(
        id="prog.1",
        title="News",
        starts_at=now,
        ends_at=now + timedelta(minutes=30),
    )
    channel = LiveChannel(id="ch.1", source_id=source.id, name="World News", programs=(program,))

    assert channel.programs[0].title == "News"
    assert session.state == "initialized"


def test_error_taxonomy_exposes_user_safe_message() -> None:
    error = ArgonError(ErrorCategory.AUTH, "token expired", source_id="src.stremio")

    assert error.user_message() == "Authentication failed. Verify source credentials."
    assert "token expired" in str(error)


def test_config_schema_defaults_are_versioned() -> None:
    config = AppConfig(
        sources=[SourceConfig(id="src.stremio", adapter_kind="stremio")],
        log_level=LogLevel.INFO,
    )

    assert config.version == 1
    assert config.sources[0].enabled is True
