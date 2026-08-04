# Production output contract

## Contents

1. [Global package](#global-package)
2. [Continuity objects](#continuity-objects)
3. [Scene architecture](#scene-architecture)
4. [Canonical scene block](#canonical-scene-block)
5. [Prompt construction](#prompt-construction)
6. [Assembly package](#assembly-package)

## Global package

Always emit these fields, using `NONE` only when intentionally absent:

```text
PROJECT_TITLE:
LOGLINE:
OBJECTIVE:
AUDIENCE:
DELIVERY_PLATFORM:
TOTAL_DURATION:
SCENE_COUNT:
ASPECT_RATIO:
PLANNING_RESOLUTION:
FRAME_RATE:
LANGUAGE:
VOICE_PROFILE:
STYLE_FAMILY:
REALISM_MODE: photographic | world-consistent | hybrid
ASSUMPTIONS_LOCKED:

SAFETY_CLASS:
RISKS:
RIGHTS_STATUS:
MITIGATIONS:
POLICY_CHECK: PASS | REVISE
```

Add a creative north star with: premise, audience promise, emotional curve, visual grammar, palette/light arc, edit rhythm, sound arc, and final payoff.

## Continuity objects

Assign stable IDs. Record invariant traits separately from evolving state.

```text
CHARACTER_01
- identity anchors: age range, face geometry, skin/fur, hair, body proportions
- performance anchors: posture, gait, gesture scale, gaze behavior
- wardrobe layers: garment, material, color, wear, accessories
- invariants: traits that never change
- allowed evolution: dirt, wetness, emotion, damage, aging, costume change
- forbidden drift: unwanted changes

LOCATION_01
- geometry: entrances, windows, furniture, horizon, cardinal/screen direction
- light sources and direction
- materials, palette, atmosphere, scale
- invariant landmarks
- allowed evolution: time, weather, crowd, damage, practical lights

PROP_01 / PRODUCT_01
- dimensions and proportions
- material and surface state
- readable marks or explicit absence of branding
- owner/handedness and starting location
- allowed state changes

STYLE_01 / AUDIO_01 / GRAPHICS_01
- medium, texture, motion cadence, lens/render logic, palette, typography strategy
- voice identity, delivery, ambience, music motif, recurring SFX
```

Create an ingredient/reference manifest: ID, purpose, source needed, preferred reference view, reuse scenes, and rights status. For a recurring human, request neutral front/three-quarter/full-body anchors when available. For products, request front/back/side and a clean hero view.

## Scene architecture

Before writing prompts, provide a compact table with:

`ID | timecode | duration | narrative job | visible change | main action | shot grammar | transition/handoff | dialogue words`

Durations must sum to the requested total. A scene may contain internal beats, but keep one dominant action.

Add a state ledger:

`ID | pre-state | trigger | post-state | continuity carried forward`

## Canonical scene block

Use exact begin/end markers and keep field names stable:

```text
=== VIDEO_SCENE_SC01_BEGIN ===
SCENE_ID: SC01
TIMECODE: 00:00–00:08
DURATION: 8 seconds
ROLE: [narrative purpose]
USE_INGREDIENTS: [stable IDs]

CONTINUITY_FROM: [previous handoff or OPENING]
START_STATE: [subject positions, gaze, hands, prop state, light, motion]
MAIN_ACTION: [one dominant visible action]
END_STATE: [exact resulting state]
CONTINUITY_TO: [next handoff or END]

VISUAL_PROMPT: [human-readable production direction]
IMAGE_KEYFRAME_PROMPT: [standalone first/hero frame prompt]
VIDEO_MOTION_PROMPT: [start → action → end, timed and physically plausible]
CAMERA_AND_MOTION: [shot, angle, lens intent, camera path, focus, motion blur]
LIGHT_COLOR_MATERIAL: [sources, direction, exposure intent, palette, texture]

TIMING_BEATS:
0–2s: ...
2–4s: ...
4–6s: ...
6–8s: ...

DIALOGUE: SPEAKER_ID: “...” | NONE
VOICE_DIRECTION: [performance, pace, pronunciation, pauses] | NONE
AUDIO: [ambience, SFX, music cue, perspective]
ON_SCREEN_TEXT: “...” | NONE
TEXT_RENDER_STRATEGY: IN_GENERATION | POST | NONE

REALISM_CONTROLS: [style-appropriate anatomy/physics/material/temporal rules]
NEGATIVE_CONSTRAINTS: [scene-specific failures only]
DIFFICULTY_AND_RECOVERY: [risk and fallback generation plan]
SAFETY_CHECK: PASS | REVISE
END_FRAME_FOR_NEXT_SCENE: [composition usable as next reference]
=== VIDEO_SCENE_SC01_END ===
```

Use timing intervals that exactly cover the scene. Adjust interval count for durations other than eight seconds.

## Prompt construction

### Image keyframe

Write a complete still-image prompt in this order:

`subject + stable ID traits → pose/action state → environment geometry → composition → lens/viewpoint → light → materials → mood/style → continuity anchors → exclusions`

Describe a single instant. Never ask a still image to show a time sequence.

### Motion prompt

Write a temporal instruction in this order:

`first-frame state → timed action beats → camera path and motivation → subject/object physics → facial/secondary motion → exact final-frame state → continuity exclusions`

Name contacts and supports: which hand touches what, where weight rests, what drives motion, what remains still. Avoid stacking unrelated actions.

### Negative constraints

Target likely failures: identity morphing, geometry drift, temporal flicker, duplicated props, wrong screen direction, impossible contact, unwanted text, or style contamination. Do not create a giant universal negative list and do not negate something required in the positive prompt.

### Dialogue and text

- Keep full dialogue identical between the narration section and scene blocks.
- Estimate spoken duration from an actual read when possible.
- Leave roughly 10–20% breathing room for natural delivery.
- Keep generated text short. For exact Vietnamese diacritics, long UI, legal copy, prices, or subtitles, prefer `POST` and describe a clean plate plus safe area.

## Assembly package

After scene blocks, include:

- `MASTER_MULTI_SCENE_PROMPT` when the target supports or benefits from it; otherwise state `NOT_RECOMMENDED`.
- An assembly map: order, reference end frame, transition method, overlap/handles, and audio bridge.
- Audio cue sheet: timecode, dialogue, ambience, SFX, music, loudness relationship.
- Typography/subtitle plan with safe areas and exact copy.
- Fallback plan for difficult shots: alternate angle, insert, clean plate, cutaway, or post-production composite.
- Export target as a recommendation, not a claim about generator capability.
