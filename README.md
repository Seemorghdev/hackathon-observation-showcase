# A common view for mismatched observations

**Solo hackathon origin · later synthetic-scenario application · public evidence showcase**

A map-led workspace for inspecting contradictory sensor reports, fused tracks and their evidence boundaries. The original hackathon explored observation formats, units, timestamps and identifiers. The later console adds full synthetic-timeline playback and a bounded local-model explanation layer.

## See the working interface

![Actual later-console runtime: synthetic tracks over a grayscale Munich reference map, with selected-track facts and AI Watch](visuals/runtime-desktop-2026-10-24.jpg)

[Watch the recorded synthetic timeline (MP4)](visuals/synthetic-timeline-walkthrough-2026-10-24.mp4) · [Desktop Copilot](visuals/copilot-desktop-2026-10-24.jpg) · [Mobile map](visuals/runtime-mobile-2026-10-24.jpg) · [Mobile Copilot](visuals/copilot-mobile-2026-10-24.jpg)

These are genuine browser captures of the later application, recorded on 24 October 2026. They are follow-on work, not screens from the original event. The video samples browser frames approximately once per second; it is not evidence of smooth video playback or real-time latency. All tracks, sensor positions, classifications, uncertainty and RF bearings are synthetic. Munich is a reference basemap; it identifies no field installation. OpenStreetMap attribution is retained.

## What the demo establishes

- The real FUSE implementation produces the deterministic synthetic scenario, with all **91 integer timesteps, t=0–90**. The separate offline adapter has only six saved bookmarks.
- Playback waits for each fetched frame; positions are not interpolated. The recorded run took about 51 seconds to reach t=90. Playback currently loops, and is stopped manually in the review.
- AI Watch matches a catalogued scenario before requesting Qwen 3 4B. The model selects approved explanation slots; catalog templates and fetched-frame values supply the visible text. `LOCAL MODEL DRAFT` identifies accepted slot selection, not verified judgment.
- Scenario Copilot uses the same bounded packets and button-only approved questions. Track and scenario identity constrain every answer. It cannot recommend or execute a response.
- RF is bearing-only. Synthetic demonstrations and retained field observations remain separate.

Read the [acceptance note: works / fails / not tested](docs/runtime-acceptance-2026-10-24.md), [architecture](docs/runtime-architecture.md), and [capture provenance](visuals/runtime-capture-record.json).

## What recruiters can access

This public repository supplies screenshots, a downloadable MP4, architecture, acceptance results, and historical documentation. It is **documentation-only** and **not an installable application**. GitHub may show an MP4 file page; use **View raw / Download raw file** to play it locally. The [portfolio walkthrough](https://mehridian.tech/projects/common-observation-view) supplies an inline player and the same access boundaries.

The application source remains private. There is no public interactive endpoint, model API, raw sensor feed, dataset or model weight in this package. A source review or live walkthrough can be discussed with the owner; access is not granted by this repository.

## Original hackathon record

- [Project overview](docs/overview.md)
- [Historical artifact inventory](docs/artifacts.md)
- [Historical testing and limitations](docs/evaluation.md)
- [Access and reproduction boundaries](docs/availability.md)
- [Earlier static interface inspection](docs/interface-review.md)
- [Screened presentation excerpt](assets/presentation-excerpt.html)

The older excerpt and empty source-shell capture are retained as historical documentation. They are not the primary demo evidence. Original-event test declarations, current regression tests and scenario timesteps are different units and are not added together.

See [screening](docs/screening.md) and [SHA256SUMS.txt](SHA256SUMS.txt). Checksums establish file identity, not correctness of model judgments or historical claims.
