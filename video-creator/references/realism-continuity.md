# Realism and continuity system

## Contents

1. [Choose the realism model](#choose-the-realism-model)
2. [Separate invariants from state](#separate-invariants-from-state)
3. [Continuity dimensions](#continuity-dimensions)
4. [Motion and camera realism](#motion-and-camera-realism)
5. [High-risk subjects](#high-risk-subjects)
6. [Transition engineering](#transition-engineering)

## Choose the realism model

Use **photographic realism** for live-action humans, documentary, product cinematography, architecture, nature, or historical recreation. Anchor camera height, lens intent, shutter/motion blur, light sources, anatomy, material response, atmospheric depth, and sound perspective.

Use **world-consistent realism** for stop-motion, anime, illustration, clay, paper, 3D, pixel art, surrealism, or fantasy. Preserve the medium’s fabrication logic: paper fibers and stepped poses for cut-paper stop-motion; held drawings and controlled smear frames for anime; mass, joints, and surface response for stylized 3D; stable graphic shapes for motion design.

Use **hybrid realism** when media mix. State which layer owns each property. Example: paper characters move at a stepped cadence while the macro camera, glass reflections, focus pulls, and shadows remain optically realistic.

## Separate invariants from state

An invariant never changes unless the story explicitly changes it: face geometry, handedness, body scale, product proportions, room layout, window side, costume base, prop identity.

A state may evolve: pose, gaze, emotion, dirt, wetness, damage, time of day, weather, fill level, UI value, object position.

Track scene boundaries with a compact vector:

```text
SUBJECT: identity / pose / gaze / screen position
HANDS_OR_CONTACT: left/right hand / contact point / held object
PROP: location / orientation / condition / value
LOCATION: camera side / landmarks / door-window geometry
LIGHT: source / direction / color / intensity
MOTION: direction / speed / phase at cut
AUDIO: ambience / music phrase / sound crossing cut
```

Never write “same as previous” without restating the few anchors that matter to generation.

## Continuity dimensions

Check all applicable dimensions:

- **Identity:** face, hair, age, wardrobe, markings, voice.
- **Spatial:** screen direction, eyeline, axis, entrances, object placement, scale.
- **Temporal:** time, weather, sun direction, damage, dirt, liquid level, UI/data state.
- **Action:** motion direction, leading limb, contact, momentum, start/end phase.
- **Optical:** aspect ratio, lens family, camera height, depth of field, grain/render logic.
- **Lighting/color:** motivated source, shadow direction, exposure and palette arc.
- **Material:** stiffness, weight, friction, transparency, moisture, deformation.
- **Audio:** room tone, distance, reverb, music key/tempo, speech identity.
- **Narrative:** knowledge, motivation, stakes, causal connection.

Continuity does not mean visual sameness. Change shot size, angle, energy, or lighting when motivated while preserving state.

## Motion and camera realism

- Give the camera a reason to move: reveal, follow, reframe, approach, retreat, or track an object.
- Prefer one camera move and one dominant subject action per short generation.
- Specify start velocity and end behavior when the cut depends on motion.
- Keep mass and inertia plausible; include anticipation, contact, follow-through, and settling.
- Describe secondary motion sparingly: breathing, cloth lag, hair, dust, reflections, foliage, water ripples.
- Use optical terms only when they clarify framing. Do not stack incompatible lenses or movements.
- Reserve stable head/tail frames for editing when needed.

For photographic humans, request natural blink rate, restrained micro-expression, breathing, realistic joint limits, consistent skin texture, and anatomically plausible hands. Avoid simultaneous talking, walking, object manipulation, and complex camera moves unless essential.

## High-risk subjects

| Risk | Primary control | Recovery strategy |
|---|---|---|
| Face/identity drift | stable reference, fewer profile changes, facial anchors | cutaway, over-shoulder, hands/detail insert |
| Hands/contact | slow single-hand action, visible contact point, simple grip | crop, occlude fingers naturally, use tool insert |
| Product geometry | orthographic references, fixed dimensions, no morphing | clean product plate, composite in post |
| Readable UI/text | short isolated labels, front-facing screen, stable plate | render UI/text in post |
| Liquids/smoke/fire | describe source, gravity, containment, flow direction | shorter insert, practical plate/composite |
| Crowds | define hero subjects and background behavior bands | split layers, shallow focus, fewer people |
| Animals/creatures | anatomy, gait cycle, contact, scale | simpler lateral motion, fewer limbs visible |
| Mirrors/screens | state what is reflected and camera exclusion | change angle or composite reflection |
| Historical/cultural detail | source-backed wardrobe, tools, architecture | disclose uncertainty; avoid false specificity |

## Transition engineering

Choose transitions by shared state, not decoration:

- **Action match:** same limb/object continues the motion.
- **Motion-direction match:** both shots travel along the same screen vector.
- **Shape/color match:** one stable silhouette or color field becomes another.
- **Occlusion wipe:** a motivated object fully covers the frame.
- **Sound bridge:** ambience, dialogue, or SFX crosses the cut.
- **Hard causal cut:** consequence immediately follows cause.
- **Time jump:** disclose the elapsed time and show at least one unmistakable change.

Define the final frame as a usable reference image: subject placement, object state, light, focus, motion phase, and clean edge space. Generate small handles when the editing workflow allows it.
