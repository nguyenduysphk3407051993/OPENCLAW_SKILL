# Safety, rights, and quality gates

## Contents

1. [Pre-production gate](#pre-production-gate)
2. [Scene gate](#scene-gate)
3. [Package gate](#package-gate)
4. [Failure severity](#failure-severity)

## Pre-production gate

Confirm or disclose:

- Audience age and vulnerable-subject considerations.
- Rights to likeness, voice, music, logos, characters, source images, and reference footage.
- Whether a real person/public figure could be mistaken for authentic footage.
- Whether dangerous activity, self-harm, graphic harm, sexual content, discrimination, medical claims, legal claims, or financial claims require reframing.
- Cultural and historical claims that require sources rather than invention.
- Brand-safe fictional replacements where rights are unknown.

For minors, use age-appropriate wardrobe, action, dialogue, camera distance, and respectful framing. Do not sexualize, exploit vulnerability, or give unsafe procedural detail.

## Scene gate

Every scene must pass:

- One clear narrative job and one dominant visible action.
- Start state matches the previous end state or an explicit jump.
- Stable IDs appear for recurring ingredients.
- Image keyframe prompt describes one instant.
- Motion prompt describes start, action, camera, physics, and final state.
- Timing beats exactly cover scene duration.
- Dialogue fits available time with breathing room.
- Camera, screen direction, gaze, hands, contact, props, light, and material state are coherent.
- Negative constraints target likely failures without negating desired content.
- Text strategy is explicit: generation, post, or none.
- Audio perspective and transition are specified.
- A difficult-shot fallback exists where appropriate.
- Safety check is `PASS`; otherwise revise before delivery.

## Package gate

Verify:

- Scene count and total duration match the brief.
- Timecodes are contiguous and non-overlapping unless overlap is intentional.
- Full narration exactly matches the scene dialogue sequence.
- Emotional, light, color, and sound arcs progress intentionally.
- Continuity ledger has no unexplained state jumps.
- Character, wardrobe, location, product, prop, and graphics locks are non-contradictory.
- Ingredient manifest covers every recurring ID and records rights status.
- Every scene has a usable end-frame handoff.
- Master prompt, if included, agrees with individual scene blocks.
- Assembly map, audio plan, typography plan, and fallback plan are present.
- Platform-specific claims are either sourced/provided by the user or phrased as recommendations.
- Output distinguishes controllable prompt intent from results that a stochastic generator cannot guarantee.

Perform a final “mute test” (story remains understandable without audio), “audio-only test” (narration remains coherent), and “boundary test” (each end frame can logically start the next clip).

## Failure severity

- **ERROR:** unsafe content, rights deception, missing required field, duration/count mismatch, contradictory identity/location state, or dialogue that cannot fit.
- **WARNING:** difficult generation risk, exact text delegated to model, unsupported feature uncertainty, crowded action, or weak transition.
- **NOTE:** creative tradeoff or post-production recommendation.

Do not mark the package ready while an `ERROR` remains.
