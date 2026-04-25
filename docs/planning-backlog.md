# Argon Player Planning Backlog (Single Source of Truth)

This document is the canonical planning backlog for Argon Player.

## Product direction
Argon Player is a Linux-first, provider-agnostic media hub intended to unify discovery and playback across Stremio add-ons, IPTV sources, Debrid resolvers, and live TV modules.

## Prioritization model
- **P0**: Critical for functional product viability.
- **P1**: Important for quality and user adoption.
- **P2**: Valuable later-stage enhancements.

---

## Epic A — Product Contracts & Core Architecture

### AP-001 — Define canonical domain models
- **Priority:** P0
- **Depends on:** —
- **Done when:** `CatalogItem`, `StreamOption`, `Source`, `PlaybackSession`, `LiveChannel`, and `Program` schemas are documented and used by code.

### AP-002 — Define source adapter interface
- **Priority:** P0
- **Depends on:** AP-001
- **Done when:** Adapter contract includes `discover`, `catalog`, `search`, `resolve_stream`, and `health_check` with typed request/response.

### AP-003 — Define error taxonomy
- **Priority:** P0
- **Depends on:** AP-001
- **Done when:** Errors are categorized (network/auth/not_found/geo/unsupported/transient/permanent) and mapped to user-safe messages.

### AP-004 — Create configuration schema
- **Priority:** P0
- **Depends on:** AP-001
- **Done when:** Versioned config supports sources, credential references, playback preferences, and logging level.

### AP-005 — Plugin lifecycle manager
- **Priority:** P0
- **Depends on:** AP-002, AP-004
- **Done when:** Sources can be loaded, unloaded, and disabled with graceful failure isolation.

### AP-006 — Capability flags system
- **Priority:** P1
- **Depends on:** AP-002
- **Done when:** Each source reports capabilities (live, search, subtitles, auth-required, etc.) and UI gates features accordingly.

---

## Epic B — Provider Integrations

### AP-007 — Stremio-compatible adapter skeleton
- **Priority:** P0
- **Depends on:** AP-002, AP-003
- **Done when:** Adapter compiles and returns mock/real catalog plus stream resolution path.

### AP-008 — Stremio manifest + discovery flow
- **Priority:** P0
- **Depends on:** AP-007
- **Done when:** Add-on endpoint is parsed, capabilities extracted, and health-check visible.

### AP-009 — Stremio catalog ingestion
- **Priority:** P0
- **Depends on:** AP-008, AP-001
- **Done when:** Catalog items map into canonical models with stable IDs.

### AP-010 — Stremio stream resolution
- **Priority:** P0
- **Depends on:** AP-009
- **Done when:** User can resolve playable stream options for supported items.

### AP-011 — IPTV adapter skeleton
- **Priority:** P1
- **Depends on:** AP-002, AP-001
- **Done when:** M3U ingestion path maps channels into canonical live model.

### AP-012 — EPG ingestion pipeline
- **Priority:** P1
- **Depends on:** AP-011, AP-001
- **Done when:** Program guide data is attached to channels with now/next queries.

### AP-013 — Debrid resolver abstraction
- **Priority:** P1
- **Depends on:** AP-002, AP-003
- **Done when:** Link resolution contract supports multiple providers behind one interface.

### AP-014 — Source health scoring
- **Priority:** P1
- **Depends on:** AP-005
- **Done when:** Sources are scored by success rate/latency and surfaced for ranking/debugging.

---

## Epic C — Data Layer, Search, and Discovery

### AP-015 — Local index for catalog/search
- **Priority:** P0
- **Depends on:** AP-001, AP-009
- **Done when:** Indexed search across ingested content works with acceptable latency.

### AP-016 — Cross-source dedupe strategy v1
- **Priority:** P1
- **Depends on:** AP-015
- **Done when:** Duplicate titles collapse into one display entity while retaining source details.

### AP-017 — Search ranking rules
- **Priority:** P1
- **Depends on:** AP-015, AP-014
- **Done when:** Ranking considers relevance, source health, language match, and content type.

### AP-018 — Home rails query engine
- **Priority:** P1
- **Depends on:** AP-015
- **Done when:** Rails like Continue Watching, Live Now, and Popular are generated from local state.

### AP-019 — Metadata enrichment hooks
- **Priority:** P2
- **Depends on:** AP-001, AP-015
- **Done when:** Optional enrichers decorate canonical items without breaking core pipeline.

---

## Epic D — Playback Engine

### AP-020 — Playback abstraction layer
- **Priority:** P0
- **Depends on:** AP-001, AP-003
- **Done when:** Generic player API (`load/play/pause/seek/stop/events`) is wired to one Linux backend.

### AP-021 — Stream selection policy
- **Priority:** P0
- **Depends on:** AP-010, AP-020
- **Done when:** Automatic default stream is chosen using quality + reliability heuristics.

### AP-022 — Retry and fallback behavior
- **Priority:** P0
- **Depends on:** AP-021, AP-014
- **Done when:** On stream failure, app retries and/or switches candidates with visible status.

### AP-023 — Subtitle pipeline
- **Priority:** P1
- **Depends on:** AP-020
- **Done when:** Embedded/external subtitle selection and offset persist per session.

### AP-024 — Playback state persistence
- **Priority:** P0
- **Depends on:** AP-020
- **Done when:** Resume position is saved/restored per media item.

### AP-025 — Live playback handling
- **Priority:** P1
- **Depends on:** AP-011, AP-020
- **Done when:** Live streams start reliably with reconnect behavior for transient interruptions.

---

## Epic E — UX Shell & Product Flows

### AP-026 — App shell/navigation
- **Priority:** P0
- **Depends on:** AP-001
- **Done when:** User can navigate Home, Search, Details, Player, and Settings.

### AP-027 — Source management UI
- **Priority:** P0
- **Depends on:** AP-005, AP-008
- **Done when:** Add, edit, disable sources and run source health checks from UI.

### AP-028 — Search UI + filters
- **Priority:** P0
- **Depends on:** AP-015, AP-026
- **Done when:** Search supports content type and source filter chips.

### AP-029 — Details page model
- **Priority:** P0
- **Depends on:** AP-009, AP-010
- **Done when:** Title metadata, stream options, and actions render consistently.

### AP-030 — Player UI controls
- **Priority:** P0
- **Depends on:** AP-020, AP-026
- **Done when:** Core controls and playback status indicators are functional.

### AP-031 — Live TV guide view
- **Priority:** P1
- **Depends on:** AP-012, AP-026
- **Done when:** Channels + now/next list and quick-tune action are functional.

### AP-032 — Watchlist/history UI
- **Priority:** P1
- **Depends on:** AP-024, AP-026
- **Done when:** User can add/remove watchlist items and review playback history.

---

## Epic F — User Data & Settings

### AP-033 — Local persistence layer
- **Priority:** P0
- **Depends on:** AP-004
- **Done when:** Config, history, watchlist, and lightweight cache persist safely.

### AP-034 — Settings schema migrations
- **Priority:** P1
- **Depends on:** AP-033
- **Done when:** Backward-compatible migration path exists for config changes.

### AP-035 — Profiles (basic)
- **Priority:** P2
- **Depends on:** AP-033, AP-026
- **Done when:** Separate profile-level preferences and history are supported.

### AP-036 — Import/export settings
- **Priority:** P1
- **Depends on:** AP-033
- **Done when:** User can export and restore app settings/state snapshots.

---

## Epic G — Security, Privacy, and Trust

### AP-037 — Credential vault abstraction
- **Priority:** P0
- **Depends on:** AP-004
- **Done when:** Provider secrets are not stored in plaintext config.

### AP-038 — Plugin permission model
- **Priority:** P1
- **Depends on:** AP-005
- **Done when:** Sources declare required permissions and user consents in UI.

### AP-039 — Safe logging policy
- **Priority:** P0
- **Depends on:** AP-003
- **Done when:** Logs redact secrets/tokens and avoid sensitive payload dumps.

### AP-040 — Privacy controls
- **Priority:** P1
- **Depends on:** AP-039
- **Done when:** User can opt in/out of telemetry and clear local usage data.

---

## Epic H — Observability & Quality

### AP-041 — Structured logging + correlation IDs
- **Priority:** P0
- **Depends on:** AP-003
- **Done when:** Operations are traceable from source query to playback outcome.

### AP-042 — Smoke test suite (core flows)
- **Priority:** P0
- **Depends on:** AP-026, AP-010, AP-020
- **Done when:** Automated checks validate launch, search, resolve, play, and resume.

### AP-043 — Contract tests for adapters
- **Priority:** P1
- **Depends on:** AP-002, AP-007
- **Done when:** Every adapter passes a common conformance harness.

### AP-044 — Failure injection harness
- **Priority:** P2
- **Depends on:** AP-022, AP-041
- **Done when:** Simulated outages/timeouts validate fallback behavior and UX messaging.

### AP-045 — Release readiness checklist
- **Priority:** P1
- **Depends on:** AP-042, AP-043
- **Done when:** Standardized quality gate exists for promotable builds.

---

## Dependency-first execution order (no time gating)
1. Core contracts first: AP-001 → AP-005, AP-003, AP-004
2. First vertical slice: AP-007/008/009/010 + AP-020/021 + AP-026/029/030
3. Stability floor: AP-022/024/033/037/039/041/042
4. Second-source expansion: AP-011/012/025/031
5. Quality hardening: AP-043/045 + remaining P1/P2 tickets
