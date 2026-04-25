# argon-player
A lightweight media content hub for Linux-based systems, compatible with Stremio add-ons, as well as IPTV, Debridio, and other live-TV modules.
Planned to include functionality common to Stremio, Omni, etc.

## Planning docs
- Single source of truth backlog: `docs/planning-backlog.md`
- Ticket template: `docs/ticket-template.md`

## First codebase scaffold
This repository now includes an initial Python package with foundational product contracts:
- Canonical domain models (`CatalogItem`, `StreamOption`, `Source`, `PlaybackSession`, `LiveChannel`, `Program`)
- Error taxonomy with user-safe messages
- Versioned configuration schema primitives

## Local checks
```bash
python -m pytest
```
