"""Versioned configuration schema for Argon Player runtime settings."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class LogLevel(str, Enum):
    DEBUG = "debug"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"


@dataclass(slots=True)
class SourceConfig:
    """Configuration for a single source plugin/adapter."""

    id: str
    adapter_kind: str
    enabled: bool = True
    credential_ref: str | None = None
    base_url: str | None = None


@dataclass(slots=True)
class PlaybackPreferences:
    """User playback preferences influencing stream selection."""

    preferred_languages: tuple[str, ...] = ()
    max_bitrate_kbps: int | None = None
    prefer_subtitles: bool = False
    subtitle_languages: tuple[str, ...] = ()


@dataclass(slots=True)
class AppConfig:
    """Top-level versioned application configuration."""

    version: int = 1
    sources: list[SourceConfig] = field(default_factory=list)
    playback: PlaybackPreferences = field(default_factory=PlaybackPreferences)
    log_level: LogLevel = LogLevel.INFO
