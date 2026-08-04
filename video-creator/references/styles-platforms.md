# Style and platform adaptation

## Contents

1. [Style translation](#style-translation)
2. [Genre grammar](#genre-grammar)
3. [Format and aspect ratio](#format-and-aspect-ratio)
4. [Platform packaging](#platform-packaging)

## Style translation

Do not paste “photorealistic live action” into every request. Translate the realism controls:

| Style family | Material/optical anchors | Motion anchors | Avoid |
|---|---|---|---|
| Documentary/live action | motivated practical light, natural texture, restrained grade | observational blocking, breathing, imperfect timing | posing, glamour light, impossible camera |
| Commercial/product | accurate geometry, controlled reflections, clean surfaces | deliberate reveal, precise easing, stable hero frame | morphing labels, floating without support |
| Stop-motion/clay/paper | tactile fabrication, fingerprints/fibers, miniature depth | stepped cadence, small settling, practical shadows | smooth CGI motion, plastic surfaces |
| Anime/2D | consistent line weight, color script, layered backgrounds | held poses, key poses, selective smear/impact frames | random line drift, pseudo-live-action skin |
| Stylized 3D | coherent topology, shaders, scale, lens/render language | mass, rig limits, secondary simulation | rubbery joints, texture swimming |
| Illustration/collage | stable shapes, print/paper texture, deliberate parallax | limited animation, cutout articulation | accidental 3D depth, morphing typography |
| Surreal/fantasy | one explicit impossible rule, consistent world response | plausible cause/effect inside the rule | unrelated spectacle, changing magic logic |
| Archival/historical | period lens/stock logic and sourced detail | era-appropriate blocking and camera language | anachronisms, invented cultural detail |
| UI/motion graphics | grid, typography system, exact hierarchy | deterministic easing and state transitions | long generated text, unstable numbers |

Combine styles by assigning responsibilities. Example: “handcrafted collage subjects; live-action macro lens and lighting; 2D typographic overlays added in post.”

## Genre grammar

- **Education/explainer:** concrete visual metaphor, one concept per beat, comprehension checks, calm hierarchy.
- **Advertisement:** problem → product mechanism → proof/benefit → memorable payoff; show the product doing work.
- **Documentary:** observation, specificity, environmental sound, restrained narration, ethical framing.
- **Narrative short:** desire → obstacle → choice → consequence; maintain performance arc.
- **Music/fashion:** rhythm, silhouette, texture, controlled discontinuity; continuity may follow music rather than plot.
- **Social short:** legible first-frame premise, safe zones, fast visual change without rushed copy.
- **Tutorial:** visible setup and result, but omit unsafe actionable detail when risk is material.
- **Atmospheric/abstract:** define sensory progression and transformation rules instead of forcing exposition.

## Format and aspect ratio

- **9:16:** keep faces/products inside a central safe column; plan top/bottom UI overlays; prefer vertical depth and controlled lateral motion.
- **16:9:** exploit lateral geography and eyelines; protect lower subtitle area.
- **1:1 / 4:5:** simplify groups and preserve central hierarchy.
- **Ultra-wide:** use only when delivery supports it; avoid tiny central subjects.

Treat planning resolution and frame rate as delivery intent, not proof that the generator natively produces them. Recommend final conform/upscale separately.

## Platform packaging

Maintain the canonical scene fields for every platform. Adapt only the wrapper and reference workflow.

### Google Flow / Veo-style workflows

- Present an ingredient/reference manifest first.
- Keep one delimited scene block per clip plus an optional master multi-scene prompt.
- Define start/end frames and reuse the prior end frame as the next reference where available.
- Label characters, locations, and props by stable IDs.

### Sora-style storyboard workflows

- Emphasize timecoded cards, spatial layout, subject persistence, and a clear shot arc.
- Keep each card independently understandable while restating essential continuity anchors.

### Kling / Runway / Luma / Pika and image-to-video workflows

- Prioritize a strong source keyframe, concise motion instruction, motion amplitude, camera intent, and exact final state.
- Separate source-image generation from animation. Avoid asking motion generation to redesign the scene.

### Unknown or changing platforms

- Use generic semantic fields and plain-language controls.
- Do not invent seeds, flags, camera parameters, reference counts, resolution modes, or feature availability.
- If exact syntax is essential, request current documentation or let the user provide the platform UI/options.

### Text and dialogue capability

Generator support varies. Always provide exact dialogue/audio direction as production intent, but add a post-production route. For spelling-critical Vietnamese, disclaimers, prices, interfaces, and subtitles, default to clean plates plus post text unless the user explicitly wants in-generation experimentation.
