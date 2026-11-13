# F01-PITCH-v1.0 — Common Pitch Sequence (Candidate)

**Status:** structurally validated candidate; auditory/pilot validation pending. 研究文書であり、聴取効果の実証結果ではない。

## 1. Purpose / 目的

本資料は、Post-Music Theory の Family 01 刺激に用いる **全192音の共通音高系列**を固定する候補資料である。初めの4小節32音は従前の設計から変更していない。残り20小節160音を追加した。L/M/Hの条件間では音高の順序を一切変更せず、オンセット配置のみを条件別規則で変える。

- Scale / pitch vocabulary: C4, D4, E4, G4, A4 (MIDI 60, 62, 64, 67, 69).
- Monophonic; 24 bars × 8 events = 192 notes; 6 phrases × 4 bars.
- 96 BPM, 4/4, 60 seconds; each note gate 120 ms; same MIDI pitch order in all conditions.
- No claims of cultural neutrality or universal musical appeal are made for the pentatonic material.

## 2. Canonical 24-bar pitch content

```text
Phrase 1 — A: baseline
Bar 01: C4 D4 E4 G4 E4 D4 C4 D4
Bar 02: E4 G4 A4 G4 E4 D4 C4 D4
Bar 03: C4 E4 G4 A4 G4 E4 D4 C4
Bar 04: D4 E4 G4 E4 D4 C4 D4 C4

Phrase 2 — A′: controlled variation
Bar 05: C4 D4 E4 G4 A4 G4 E4 D4
Bar 06: E4 G4 A4 G4 E4 G4 E4 D4
Bar 07: C4 E4 G4 A4 E4 G4 D4 C4
Bar 08: D4 E4 G4 E4 D4 C4 E4 C4

Phrase 3 — B: development
Bar 09: E4 D4 C4 D4 E4 G4 A4 G4
Bar 10: E4 G4 A4 G4 E4 G4 E4 D4
Bar 11: C4 D4 E4 G4 A4 G4 E4 C4
Bar 12: D4 E4 G4 E4 D4 C4 D4 C4

Phrase 4 — C: contrast
Bar 13: C4 E4 G4 E4 D4 C4 D4 E4
Bar 14: E4 G4 A4 G4 E4 D4 G4 E4
Bar 15: C4 E4 G4 A4 G4 E4 C4 D4
Bar 16: D4 E4 G4 A4 G4 E4 D4 C4

Phrase 5 — A″: reprise
Bar 17: C4 D4 E4 G4 E4 D4 E4 G4
Bar 18: E4 G4 A4 G4 E4 D4 C4 E4
Bar 19: C4 E4 G4 A4 E4 G4 E4 D4
Bar 20: D4 E4 G4 E4 D4 C4 D4 C4

Phrase 6 — Coda: closure
Bar 21: E4 D4 C4 D4 E4 G4 E4 D4
Bar 22: E4 G4 A4 G4 E4 D4 C4 D4
Bar 23: C4 E4 G4 A4 G4 E4 D4 C4
Bar 24: D4 E4 G4 E4 D4 C4 D4 C4

```

**Preservation rule:** Bars 01–04 coincide exactly with the earlier approved 32-note prefix. All later edits require a version increment.

## 3. Generation rationale / 変化の設計意図

6フレーズは「基準提示 → 限定的変奏 → 展開 → 対照 → 再提示 → 終止」の便宜的な構成である。これは実験前の設計意図であり、参加者にそのように知覚されるという実証結果ではない。各小節の音数8、音域、音色、発音長は固定し、音高側で過度な高揚や大跳躍が起きないようにした。

| Phrase | Bars | Differences from Phrase 1 (aligned 32 notes) | Intended structural role |
|---|---|---:|---|
| 1 | 01–04 | 0 | Baseline material |
| 2 | 05–08 | 8 | Limited variation |
| 3 | 09–12 | 14 | Development |
| 4 | 13–16 | 14 | Contrasting contour |
| 5 | 17–20 | 7 | Modified return |
| 6 | 21–24 | 5 | Return and closure |

## 4. Computed structural checks / 計算済み監査

| Check | Result |
|---|---|
| Note events | 192 / PASS |
| Bars × events | 24 × 8 / PASS |
| Distinct four-bar phrases | 6 / 6 |
| Distinct bars | 18 / 24 (recurrence intentionally retained) |
| Maximum adjacent pitch leap | 5 semitones, including bar transitions |
| Retained prior prefix | first 32 notes identical / PASS |
| Note counts | A4: 15, C4: 33, D4: 44, E4: 57, G4: 43 |
| Timing compatibility | L/M/H each 192 nonoverlapping note gates / PASS |
| Total render length | 60 s, by event specification |

**Interpretation:** these are computational conformance checks, not perceptual, behavioral, or physiological validation. “Music-like” and “well matched across emotional impact” remain unverified.

## 5. Condition timing summary

| Condition | Deviation δ | Mean IOI (beats) | IOI variance (beat²) |
|---|---:|---:|---:|
| L | 12/168 | 0.500 | 0.0078125 |
| M | 48/168 | 0.500 | 0.0312500 |
| H | 90/168 | 0.500 | 0.0390625 |

L/M/Hでは音高・音域・イベント数・音価・強弱規則・全長・パターン順序を共有する。ただし時刻を変えると音高と強拍の位置関係も変化するため、「純粋な予測性だけの操作」とまでは言えない。実際には **局所的な時間逸脱・IOI分散・拍節位置**の複合操作である。

## 6. Files and reproducibility

- `f01_pitch_v1.json`: 24 × 8 canonical pitch array.
- `f01_stimulus_build_v0_1_1.py`: deterministic event generator and structural negative tests; no audio synthesis.
- `generated_events/f01_events_L.json`, `f01_events_M.json`, `f01_events_H.json`: 192 events per condition with exact onset timestamps expressed in integer microseconds.
- `generated_events/f01_validation_report.json`: structural checks, cross-condition checks, and SHA-256 file hashes.

Run from the same directory: `python f01_stimulus_build_v0_1_1.py --self-test`. No third-party dependencies.

## 7. Pre-experiment limitations and required review

1. **Listening screening is still required.** Auditory flow, perceived phrase boundaries, musical coherence, valence, arousal, and the intended load ordering must be independently checked in a pilot. No such results are available now.
2. **Pitch-timing interaction persists.** The identical pitch order may be heard differently when shifted relative to the beat; this is part of the timing manipulation, not evidence of pure surprisal isolation.
3. **Learning and recurrence must be tracked.** 18 unique bars out of 24 and 6 different phrases deliberately balance repetition and change. This does not prove suitable familiarity or avoid confounds from learning pitch motifs.
4. **No calculated generator surprisal yet.** Deterministic pattern choice alone does not specify the observer predictive probability distribution.
5. **Do not use outcome-derived predictors circularly.** Earlier definitions of R contained a persistence component while delayed persistence was also an intended outcome. For an honest test, compute an *immediate R* independently and reserve delayed retention as a held-out outcome. Similarly, a geometric mean of the three layer engagement scores measures joint activation, not temporal coherence K by itself.
6. **Keep causality constrained.** Manipulated timing condition and pre-stimulus observer measures can support causal contrasts under randomization; self-reported effective load obtained after listening is a post-treatment measure and should not automatically be treated as an independent causal predictor.

## 8. Placement and change control

本資料は `post_music_theory.md` の Core 定義を改変せず、独立した **stimulus design / methodology** として公開可能な候補である。推奨配置例は `experiments/f01_pitch_v1.md` および `experiments/f01_pitch_v1.json`、`experiments/f01_stimulus_build_v0_1_1.py` である。現時点では正式な実験刺激の確定ではなく **candidate** と記載すべきである。

### Next gate

1. Author/peer review of the melody series and code; 2. Render reproducible test audio; 3. Independent listening/pilot screening; 4. Freeze accepted stimuli and preregister the confirmatory experiment.
## 9. Audit amendment (2026-11-13)

本資料の音高・配置検証値は生成規則に関する計算結果であり、聴覚的・心理学的な効果を示さない。`f01_stimulus_build_v0_1_1.py` はCSV形式のイベント表を生成する。実際の演奏音（WAV/MIDIレンダリング）は生成しない。三条件間で固定されるのは音高順・音数・名目テンポ等である。拍節上の音高配置、IOI分散および強拍との相互作用まで単一変数として切り離したものではない。

ユークリッドリズムのE(8,16)は等間隔基準配置に該当するが、Medium/Highは一般に厳密なユークリッドリズムではない。発音数を変えるE(5,16)との単純比較は、音密度の差と混同するため初期実験では行わない。

**Evidence status:** code/metadata reproducibility candidate; no participant data, no auditory validation, no claim of causal efficacy.
