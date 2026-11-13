#!/usr/bin/env python3
"""F01 deterministic event-table generator; no audio synthesis or efficacy claim.

Usage:
    python experiments/f01_stimulus_build_v0_1_1.py --self-test
Requires Python 3.9+ only. Output CSV is created locally in --out-dir.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

BASE = (0, 2, 4, 6, 8, 10, 12, 14)
SCHEDULE = tuple("ABCD" "BCDA" "CDAB" "DABC" "ACDB" "BDAC")
PATTERNS = {
    "L": {
        "A": (0, 2, 4, 6, 8, 10, 12, 14),
        "B": (0, 2, 4, 6, 8, 10, 12, 14),
        "C": (0, 2, 4, 7, 8, 10, 12, 14),
        "D": (0, 2, 4, 6, 8, 10, 12, 15),
    },
    "M": {
        "A": (0, 2, 4, 7, 8, 10, 13, 14),
        "B": (0, 3, 4, 6, 8, 9, 12, 14),
        "C": (0, 2, 3, 6, 8, 10, 12, 15),
        "D": (0, 2, 4, 5, 8, 11, 12, 14),
    },
    "H": {
        "A": (0, 1, 4, 7, 9, 10, 13, 14),
        "B": (0, 3, 5, 6, 9, 11, 12, 14),
        "C": (0, 1, 3, 6, 8, 11, 13, 14),
        "D": (0, 3, 4, 5, 8, 10, 12, 15),
    },
}
PITCHES = {"C4": 60, "D4": 62, "E4": 64, "G4": 67, "A4": 69}
PREFIX = (
    ("C4", "D4", "E4", "G4", "E4", "D4", "C4", "D4"),
    ("E4", "G4", "A4", "G4", "E4", "D4", "C4", "D4"),
    ("C4", "E4", "G4", "A4", "G4", "E4", "D4", "C4"),
    ("D4", "E4", "G4", "E4", "D4", "C4", "D4", "C4"),
)
UNIT_US = 156_250  # 96 BPM, quarter-beat grid
NOTE_US = 120_000
END_US = 60_000_000
DELTA_COUNTS = {"L": 12, "M": 48, "H": 90}
VARIANCE_BEAT2 = {
    "L": Fraction(1, 128), "M": Fraction(1, 32), "H": Fraction(5, 128)
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def pitch_data(path):
    obj = json.loads(path.read_text(encoding="utf-8"))
    require(obj.get("family_id") == "F01", "wrong family")
    require(obj.get("pitch_version") == "F01-PITCH-v1.0-candidate", "wrong version")
    bars = obj.get("bars")
    require(isinstance(bars, list) and len(bars) == 24, "24 bars required")
    require(all(isinstance(b, list) and len(b) == 8 for b in bars), "8 events/bar required")
    require(tuple(tuple(b) for b in bars[:4]) == PREFIX, "original first 32 notes changed")
    notes = [p for b in bars for p in b]
    require(len(notes) == 192 and all(p in PITCHES for p in notes), "invalid pitches")
    require(max(abs(PITCHES[a] - PITCHES[b]) for a, b in zip(notes, notes[1:])) <= 5,
            "pitch leap exceeds 5 semitones")
    require(len({tuple(notes[i:i + 32]) for i in range(0, 192, 32)}) == 6,
            "four-bar phrases must be distinct")
    return notes


def validate_pattern(pattern):
    require(len(pattern) == 8 and all(type(x) is int for x in pattern),
            "eight integer onset positions required")
    require(pattern[0] == 0 and all(0 <= x < 16 for x in pattern),
            "onset out of bar bounds or missing downbeat")
    intervals = [b - a for a, b in zip(pattern, pattern[1:])]
    intervals.append(16 - pattern[-1])
    require(min(intervals) >= 1, "onsets overlap or go backwards")
    return intervals


def build(notes, condition, duration_us=NOTE_US):
    require(condition in PATTERNS, "unknown condition")
    require(type(duration_us) is int and 0 < duration_us < UNIT_US,
            "invalid note gate duration")
    require(len(SCHEDULE) == 24 and all(SCHEDULE.count(x) == 6 for x in "ABCD"),
            "unbalanced or truncated schedule")
    events = []
    for bar_index, label in enumerate(SCHEDULE):
        pattern = PATTERNS[condition][label]
        validate_pattern(pattern)
        for event_index_in_bar, local_unit in enumerate(pattern):
            event_index = 8 * bar_index + event_index_in_bar
            pitch = notes[event_index]
            onset_unit = 16 * bar_index + local_unit
            velocity = (84 if event_index_in_bar == 0 and bar_index % 4 == 0
                        else 80 if event_index_in_bar == 0 else 72)
            events.append({
                "event_index": event_index,
                "phrase_index": bar_index // 4 + 1,
                "bar_index": bar_index + 1,
                "event_in_bar": event_index_in_bar + 1,
                "pitch": pitch,
                "midi_pitch": PITCHES[pitch],
                "onset_unit": onset_unit,
                "onset_us": onset_unit * UNIT_US,
                "duration_us": duration_us,
                "velocity": velocity,
            })
    require(len(events) == 192, "wrong event count")
    require(events[-1]["onset_us"] + duration_us <= END_US, "audio exceeds 60 seconds")
    require(all(a["onset_us"] + duration_us <= b["onset_us"]
                for a, b in zip(events, events[1:])), "overlapping note gates")
    return events


def metrics(condition):
    starts = []
    delta_count = 0
    for bar_index, label in enumerate(SCHEDULE):
        p = PATTERNS[condition][label]
        starts.extend(16 * bar_index + t for t in p)
        delta_count += sum(a != b for a, b in zip(p[1:], BASE[1:]))
    intervals = [b - a for a, b in zip(starts, starts[1:] + [384])]
    variance = sum((Fraction(x, 4) - Fraction(1, 2)) ** 2 for x in intervals) / 192
    require(delta_count == DELTA_COUNTS[condition], "deviation count changed")
    require(variance == VARIANCE_BEAT2[condition], "IOI variance changed")
    require(sum(intervals) == 384 and min(intervals) == 1, "IOI invariant failed")
    return {
        "deviation_events": delta_count,
        "potential_events": 168,
        "mean_ioi_beats": 0.5,
        "min_ioi_beats": 0.25,
        "variance_ioi_beats_squared": float(variance),
        "gap_units_histogram": dict(sorted(Counter(intervals).items())),
    }


def check_cross_condition(tables):
    reference = tables["L"]
    for cond in ("M", "H"):
        for field in ("pitch", "midi_pitch", "duration_us", "velocity",
                      "phrase_index", "bar_index", "event_in_bar"):
            require([e[field] for e in reference] == [e[field] for e in tables[cond]],
                    "condition mismatch for " + field)
    require(len({tuple(e["onset_unit"] for e in tables[c]) for c in "LMH"}) == 3,
            "conditions have identical timing")


def self_test(notes):
    assert len(notes) == 192
    for bad in (
        (0, 0, 4, 6, 8, 10, 12, 14),
        (1, 2, 4, 6, 8, 10, 12, 14),
        (0, 2, 4, 6, 8, 10, 12, 16),
        (0, 2, 4, 6, 8, 10, 14, 12),
    ):
        try:
            validate_pattern(bad)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid onset accepted: " + str(bad))
    try:
        build(notes, "H", UNIT_US)
    except ValueError:
        pass
    else:
        raise AssertionError("too-long note gate accepted")


def run(input_path, output_dir, do_self_test):
    notes = pitch_data(input_path)
    if do_self_test:
        self_test(notes)
    tables = {c: build(notes, c) for c in "LMH"}
    check_cross_condition(tables)
    report = {
        "status": "PASS",
        "meaning": "structural conformance only; no perceptual or efficacy evidence",
        "family_id": "F01",
        "spec_version": "PM-SDS-0.1.1",
        "pitch_version": "F01-PITCH-v1.0-candidate",
        "metadata": {c: metrics(c) for c in "LMH"},
        "csv_sha256": {},
        "self_test": bool(do_self_test),
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    for cond, events in tables.items():
        path = output_dir / ("f01_events_" + cond + ".csv")
        fields = list(events[0])
        import io
        buff = io.StringIO(newline="")
        writer = csv.DictWriter(buff, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(events)
        data = buff.getvalue().encode("utf-8")
        path.write_bytes(data)
        report["csv_sha256"][path.name] = hashlib.sha256(data).hexdigest()
    (output_dir / "f01_validation_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pitch", type=Path, default=Path(__file__).with_name("f01_pitch_v1.json"))
    parser.add_argument("--out-dir", type=Path, default=Path("generated_events"))
    parser.add_argument("--self-test", action="store_true")
    a = parser.parse_args()
    run(a.pitch, a.out_dir, a.self_test)
