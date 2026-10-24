# Works / fails / not tested — later console, 24 October 2026

This acceptance covers the map-led synthetic console and scenario-bound AI Watch/Copilot. Earlier acceptance of a documentation assistant does not validate this workflow. The implementation remains private.

## Works observed

- **Real implementation, synthetic input:** FUSE reports `real_engine`; SENSE reports `validated_evidence`; Python REASON remains `deterministic`. The separate analyst reports local `qwen3:4b` available. SENSE's retained evidence is not incoming camera inference.
- **Desktop timeline:** actual browser playback from t=0 to t=90 in about 51.4 seconds, recorded as 52 sampled screenshots. All integer frames are supported; the recording samples roughly once per second and therefore does not show each one.
- **Controls:** Watch pause/resume stayed independent of playback. Playback advanced while Watch remained paused. Repeated Play/Pause ended stopped. Restart and the existing end-of-timeline loop were observed.
- **Track/scenario binding:** hostile FT-001, unknown FT-002 and friendly FT-003 settled to correctly bound local-model packets. Changing track immediately cleared the old Copilot context. The approved friendly-track question returned a correctly bound, labelled deterministic response when model validation fell back.
- **Mobile viewport, 390×844 CSS pixels:** map and usable timeline above the collapsed detail sheet, playback, repeated toggles, Watch pause/resume, bounded Copilot, and immediate question pending state with duplicate clicks disabled. This is a desktop-browser viewport review, not physical-device certification.
- **Automated checks:** 152 Python tests and five JavaScript runtime regression checks passed. They are different test units, not a combined performance score. Existing Python deprecation warnings remain.

## Fails found and repaired

Acceptance found overlapping/superseded local-model requests, cached old numeric explanation values, repeated Copilot requests during redraw, delayed question pending feedback, and a mobile timeline that collapsed to zero width under the closed sheet. The private acceptance fix serializes requests, discards superseded work, renders current frame values into validated slot templates, disables duplicate pending questions, and repairs the mobile transport layout. Regression checks cover request ordering, latest selection, current values and question state.

## Known behavior and limits

- Playback loops at the end. Scenario seconds do not equal viewing seconds.
- A Qwen request can outlast a short crossing interval. Catalog content stays visible while checking; late responses do not overwrite a newer selection. No real-time latency guarantee is made.
- Some crossing-map labels can clip on a narrow map; the selected-track sheet and Copilot preserve explicit identity and facts.
- `LOCAL MODEL DRAFT` means a schema-valid approved-slot selection. It is not verified judgment, calibrated probability or field performance. Visible prose and factual values come from approved templates and fetched synthetic frames.
- The video samples the actual browser approximately once per second. It is not a continuous high-frame-rate recording, a smoothness benchmark or original hackathon footage. Export margins were cropped; UI facts and geometry were not invented.

## Not tested

Docker image build (local daemon unavailable), cloud deployment, physical mobile devices, live field sensors, continuous camera-to-detector integration, field reliability and operational decision quality.

The [capture record](../visuals/runtime-capture-record.json) identifies the source base, finalized private acceptance-fix commit, viewport setup, cropping and timing. Current regression results do not replace the original-event test declarations or reproduce historical detector evaluation.
