#!/usr/bin/env python3
"""Validate the structural completeness of an AI video blueprint text file."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


GLOBAL_FIELDS = (
    "PROJECT_TITLE", "TOTAL_DURATION", "SCENE_COUNT", "ASPECT_RATIO",
    "SAFETY_CLASS", "RIGHTS_STATUS", "POLICY_CHECK",
)

SCENE_FIELDS = (
    "SCENE_ID", "TIMECODE", "DURATION", "ROLE", "USE_INGREDIENTS",
    "CONTINUITY_FROM", "START_STATE", "MAIN_ACTION", "END_STATE",
    "CONTINUITY_TO", "VISUAL_PROMPT", "IMAGE_KEYFRAME_PROMPT",
    "VIDEO_MOTION_PROMPT", "CAMERA_AND_MOTION", "LIGHT_COLOR_MATERIAL",
    "TIMING_BEATS", "DIALOGUE", "VOICE_DIRECTION", "AUDIO",
    "ON_SCREEN_TEXT", "TEXT_RENDER_STRATEGY", "REALISM_CONTROLS",
    "NEGATIVE_CONSTRAINTS", "DIFFICULTY_AND_RECOVERY", "SAFETY_CHECK",
    "END_FRAME_FOR_NEXT_SCENE",
)

SCENE_RE = re.compile(
    r"=== VIDEO_SCENE_(SC\d+)_BEGIN ===(?P<body>.*?)"
    r"=== VIDEO_SCENE_\1_END ===",
    re.DOTALL,
)


def field_present(text: str, field: str) -> bool:
    return re.search(rf"(?m)^\s*{re.escape(field)}\s*:\s*\S", text) is not None


def parse_duration_seconds(text: str) -> float | None:
    match = re.search(
        r"(?im)^\s*DURATION\s*:\s*([0-9]+(?:\.[0-9]+)?)\s*(?:seconds?|s|giây)",
        text,
    )
    return float(match.group(1)) if match else None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("blueprint", type=Path)
    parser.add_argument("--expected-scenes", type=int)
    parser.add_argument("--expected-total", type=float, help="Expected total duration in seconds")
    args = parser.parse_args()

    try:
        text = args.blueprint.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        print(f"ERROR: cannot read {args.blueprint}: {exc}")
        return 2

    errors: list[str] = []
    warnings: list[str] = []

    for field in GLOBAL_FIELDS:
        if not field_present(text, field):
            errors.append(f"missing global field {field}")

    scenes = list(SCENE_RE.finditer(text))
    if not scenes:
        errors.append("no complete VIDEO_SCENE_SCxx blocks found")

    seen_ids: set[str] = set()
    duration_sum = 0.0
    for match in scenes:
        scene_id = match.group(1)
        body = match.group("body")
        if scene_id in seen_ids:
            errors.append(f"duplicate scene marker {scene_id}")
        seen_ids.add(scene_id)

        declared = re.search(r"(?m)^\s*SCENE_ID\s*:\s*(SC\d+)\s*$", body)
        if not declared or declared.group(1) != scene_id:
            errors.append(f"{scene_id}: SCENE_ID does not match marker")

        for field in SCENE_FIELDS:
            if not field_present(body, field):
                errors.append(f"{scene_id}: missing field {field}")

        seconds = parse_duration_seconds(body)
        if seconds is None:
            errors.append(f"{scene_id}: duration is not parseable as seconds")
        else:
            duration_sum += seconds

        strategy = re.search(r"(?im)^\s*TEXT_RENDER_STRATEGY\s*:\s*(\S+)", body)
        if strategy and strategy.group(1).upper() not in {"IN_GENERATION", "POST", "NONE"}:
            warnings.append(f"{scene_id}: non-canonical TEXT_RENDER_STRATEGY")

        if re.search(r"(?im)^\s*SAFETY_CHECK\s*:\s*REVISE", body):
            errors.append(f"{scene_id}: SAFETY_CHECK requires revision")

    expected_scenes = args.expected_scenes
    if expected_scenes is None:
        declared_count = re.search(r"(?im)^\s*SCENE_COUNT\s*:\s*(\d+)", text)
        expected_scenes = int(declared_count.group(1)) if declared_count else None
    if expected_scenes is not None and len(scenes) != expected_scenes:
        errors.append(f"scene count is {len(scenes)}, expected {expected_scenes}")

    if args.expected_total is not None and abs(duration_sum - args.expected_total) > 0.01:
        errors.append(f"scene durations total {duration_sum:g}s, expected {args.expected_total:g}s")

    if "IMAGE_KEYFRAME_PROMPT" not in text or "VIDEO_MOTION_PROMPT" not in text:
        errors.append("prompt package is incomplete")
    if "POST" not in text and re.search(r"[À-ỹ]", text):
        warnings.append("Vietnamese text detected but no POST text strategy found; verify spelling reliability")

    for message in warnings:
        print(f"WARNING: {message}")
    for message in errors:
        print(f"ERROR: {message}")

    print(f"SUMMARY: {len(scenes)} scenes, {duration_sum:g}s, {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
