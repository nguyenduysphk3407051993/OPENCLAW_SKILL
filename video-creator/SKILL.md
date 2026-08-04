---
name: video-creator
description: Use when a user needs an AI video concept, storyboard, shot list, keyframe prompts, image-to-video or text-to-video prompts, multi-scene continuity, dialogue timing, production blueprint, or prompt package for Flow, Veo, Sora, Kling, Runway, Luma, Pika, or another video generator.
---

# Video Creator

## Core principle

Design the video as a stateful production plan, not a list of attractive shots. Preserve identity, geometry, screen direction, light, props, material behavior, audio, and narrative causality from one scene to the next.

Treat “realistic” as two layers:

- **Photographic realism:** believable camera, anatomy, skin, light, materials, sound, and motion for live action.
- **World realism:** internally consistent physics, craft, timing, and material behavior for anime, stop-motion, 3D, collage, surreal, abstract, or mixed media.

## Load the right references

- Read [references/output-contract.md](references/output-contract.md) before drafting any production package.
- Read [references/realism-continuity.md](references/realism-continuity.md) whenever scenes share characters, locations, products, props, creatures, UI, or an ongoing action.
- Read [references/styles-platforms.md](references/styles-platforms.md) when a style, genre, aspect ratio, or named generator matters.
- Read [references/quality-gates.md](references/quality-gates.md) before final delivery.

## Workflow

### 1. Normalize the brief

Extract: topic, objective, audience, runtime, scene count, aspect ratio, delivery platform, language, voice, style, characters, locations, props, CTA, references, and rights constraints.

Ask only about a choice that would materially change the concept and cannot be safely inferred. Otherwise choose sensible defaults and expose them under `ASSUMPTIONS_LOCKED`.

Default to 16:9, 24 fps, 1080p planning resolution, the user’s language, original/non-infringing assets, and a production package detailed enough for per-scene generation. Never claim a generator supports a parameter unless the user supplies current documentation; express uncertain controls semantically.

### 2. Establish safety and rights

Classify risk before creative expansion. Avoid deceptive impersonation, sexualization of minors, actionable dangerous instruction, graphic harm, or unauthorized copyrighted identity/voice/logo use. Replace real brands, UI, books, music, and celebrity voices with fictional or licensed equivalents unless the user confirms rights.

Emit `SAFETY_CLASS`, `RISKS`, `RIGHTS_STATUS`, `MITIGATIONS`, and `POLICY_CHECK: PASS | REVISE`.

### 3. Build one coherent visual thesis

Write a one-sentence premise, audience promise, emotional curve, visual grammar, color/light arc, sound arc, and ending payoff. Use the structure best suited to the request—not every video needs a conventional hook or CTA.

Prefer one primary action per scene. Convert exposition into visible cause and effect. Make every scene change at least one story state: knowledge, position, emotion, object condition, time, light, or stakes.

### 4. Lock the world before scenes

Create stable IDs for every recurring character, location, prop/product, wardrobe, graphic language, voice, and music motif. Separate invariants from evolving state.

Create a continuity ledger for each scene:

`PRE_STATE → TRIGGER → MAIN_ACTION → POST_STATE → HANDOFF_FRAME`

The next scene’s `PRE_STATE` must equal the previous scene’s `POST_STATE`, except for an explicitly described transition or time jump.

### 5. Architect timing and narration

Allocate runtime first, then write dialogue to fit it. Reserve breathing room and picture-only beats. Estimate speech from the requested performance rate; shorten copy when uncertain rather than forcing rushed delivery.

Write full narration once, then divide it by scene without changing words. Mark intentional silence as `NONE`. Keep on-screen text shorter than speech and define whether text is generated in-camera or added in post.

### 6. Write generation-ready scene packets

Follow the exact scene schema in `output-contract.md`. For every scene:

- Describe the first frame, one main action, and final frame.
- Supply a standalone image keyframe prompt and a separate motion prompt.
- Use observable instructions instead of abstract adjectives.
- State camera motivation, lens behavior, movement path, focus, motion speed, and physical contacts.
- Carry only relevant locks into the prompt; do not paste contradictory global negatives.
- Include a recovery strategy for difficult faces, hands, liquids, crowds, UI, or readable text.

Write generator prompts in clear English by default because most video models parse it reliably. Keep dialogue, titles, subtitles, and user-facing production notes in the requested language.

### 7. Package for generation and assembly

Deliver the full production pack in this order:

1. Project setup and assumptions
2. Safety and rights lock
3. Creative north star
4. Continuity bible and state ledger
5. Full narration/dialogue
6. Scene architecture table
7. Ingredient/reference manifest
8. One delimited block per scene
9. Master multi-scene prompt when useful
10. Assembly map, audio plan, text plan, and fallback plan
11. QA report

For named platforms, adapt labels and packaging without deleting the canonical fields. If a platform cannot reliably render text, reserve layout-safe space and specify post-production text instead of asking the model to spell long copy.

### 8. Validate before delivery

Check content against `quality-gates.md`. When the blueprint is saved as text, run:

```powershell
python scripts/validate_blueprint.py blueprint.txt --expected-scenes 6 --expected-total 48
```

Fix every error. Disclose warnings that depend on generator behavior rather than pretending they are guaranteed.

## Decision rules

| Situation | Preferred decision |
|---|---|
| Missing non-critical details | Lock and disclose assumptions |
| Complex readable text or UI | Generate clean plates; add exact text in post |
| Identity drift risk | Use reference manifest, stable IDs, anchor frames, simpler angles |
| Motion drift risk | Reduce simultaneous actions; specify contact and end state |
| Style is non-photographic | Preserve world realism, not live-action clichés |
| Short scene with too much copy | Cut copy before speeding the voice |
| Platform feature is uncertain | Use semantic prompt, do not invent syntax |
| Continuity conflicts with spectacle | Preserve continuity unless user prioritizes spectacle |

## Common failure modes

- **Beautiful but disconnected scenes:** add a state ledger and explicit handoff frames.
- **Prompt soup:** remove redundant adjectives; order subject → action → environment → camera → light → material → continuity → exclusions.
- **Generic “cinematic” wording:** specify lens intent, light source, blocking, pace, and sound perspective.
- **Characters morphing:** freeze facial anchors, wardrobe layers, handedness, scale, and screen position; keep reference images stable.
- **Unreal hands or object contact:** show fewer fingers, slower contact, clear occlusion, and physically supported objects.
- **Incorrect Vietnamese text:** move typography to post or generate short isolated labels only.
- **One realism add-on for every style:** translate realism into the chosen medium’s materials and motion cadence.
- **Negative prompts that erase desired content:** make exclusions scene-specific and never negate required ingredients.

## Output discipline

Return a complete usable blueprint, not commentary about how one could be made. Use `NONE` for deliberately absent fields so completeness is machine-checkable. If the user requests only a concept or compact shot list, scale the package down explicitly; otherwise default to the full production pack.
