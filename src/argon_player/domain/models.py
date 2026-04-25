"""Canonical domain models for Argon Player.

These models are intentionally provider-agnostic so every source adapter
(Stremio, IPTV, Debrid, etc.) maps data into one common contract.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any


class ContentType(str, Enum):
    """Primary media content type for catalog entries."""

    MOVIE = "movie"
    SERIES = "series"
    EPISODE = "episode"
    LIVE = "live"


class StreamProtocol(str, Enum):
    """Transport protocol for resolved stream options."""

    HLS = "hls"
    DASH = "dash"
    PROGRESSIVE = "progressive"
    RTMP = "rtmp"
    OTHER = "other"


@dataclass(slots=True)
class Source:
    """Represents an integrated upstream source/provider."""

    id: str
    name: str
    adapter_kind: str
    enabled: bool = True
    capabilities: tuple[str, ...] = ()
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class CatalogItem:
    """Provider-normalized catalog item used across the app."""

    id: str
    source_id: str
    title: str
    content_type: ContentType
    external_ids: dict[str, str] = field(default_factory=dict)
    year: int | None = None
    description: str | None = None
    artwork_url: str | None = None
    genres: tuple[str, ...] = ()
    language: str | None = None


@dataclass(slots=True)
class StreamOption:
    """One playable stream candidate for an item or channel."""

    id: str
    source_id: str
    url: str
    protocol: StreamProtocol
    quality_label: str | None = None
    bitrate_kbps: int | None = None
    audio_language: str | None = None
    subtitle_languages: tuple[str, ...] = ()
    drm: bool = False
    priority: int = 0


@dataclass(slots=True)
class PlaybackSession:
    """Tracks playback lifecycle for observability and resume support."""

    id: str
    item_id: str | None
    source_id: str
    stream_option_id: str
    started_at: datetime
    position_seconds: int = 0
    buffered_seconds: int = 0
    state: str = "initialized"


@dataclass(slots=True)
class Program:
    """Represents EPG metadata for a scheduled live program."""

    id: str
    title: str
    starts_at: datetime
    ends_at: datetime
    description: str | None = None
    category: str | None = None


@dataclass(slots=True)
class LiveChannel:
    """Canonical live channel model backed by one or more sources."""

    id: str
    source_id: str
    name: str
    number: str | None = None
    logo_url: str | None = None
    group: str | None = None
    programs: tuple[Program, ...] = ()
