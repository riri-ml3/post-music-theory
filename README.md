# Post-Music Theory

## Overview

**EN**

This repository presents a foundational theoretical draft of **post-music theory**.

The central claim of this project is that music should not be reduced to entertainment, aesthetic decoration, or mere external meaning transmission. Instead, music is modeled here as a **structured temporal system that modulates the observer’s internal reachability distribution**.

Within this framework, music is treated as something that changes not only perception itself, but also which internal states become more reachable: memory states, emotionally stabilized states, meaning-bearing states, motivational states, and states of restored self-continuity.

Here, **post-music** refers to a future-oriented expansion of music beyond conventional listening-centered forms, toward a framework in which music functions as a measurable and designable modulation of internal reachability.

This repository currently focuses on the **core theoretical layer**.  
Detailed supplements, implementation notes, and experimental designs will be added incrementally.

**JP**

本リポジトリは、**ポスト音楽理論（Post-Music Theory）** の基礎理論ドラフトを提示するものである。

本研究の中心命題は、音楽を単なる娯楽、美的装飾、あるいは外的な意味伝達へ還元すべきではない、という点にある。本理論では、音楽を、**観測者の内的到達可能性分布を変調する構造化時間系**として扱う。

この枠組みにおいて音楽は、単に知覚内容を変えるだけではなく、どの内的状態がより到達しやすくなるか――すなわち、記憶状態、情動安定状態、意味形成状態、動機づけ状態、自己連続性回復状態など――を変えるものとして位置づけられる。

本リポジトリでいう **ポスト音楽** とは、従来の聴取中心的な音楽概念を越えて拡張された、未来志向の音楽概念を指す。より具体的には、音楽を、内的到達可能性を測定可能かつ設計可能に変調する枠組みとして捉えるものである。

現段階では、主として **中核理論層** を扱う。  
補論、実装ノート、実験設計などは今後段階的に追加する予定である。

---

## Current Status

**EN**

**Status:** Foundational draft / core theoretical outline (v0.1)

This repository is not intended as a finalized empirical theory at the current stage.  
It should be read as a structured theoretical foundation from which more explicit modeling, implementation, and falsifiability can be developed.

**JP**

**ステータス:** 基礎理論ドラフト / 中核理論アウトライン（v0.1）

本リポジトリは、現段階では完成した経験理論を提示するものではない。  
今後の定式化、実装、反証可能化へ進むための構造的理論基盤として読むべきである。

---

## Main Document

**EN**

The current main document is:

- [`post_music_theory.md`](./post_music_theory.md)

This file contains the minimal core formulation of the theory, including:

- the distinction between **sound** and **music**
- music as **modulation of internal reachability**
- internal reachability-information mass
- bodily / cognitive / integrative layers of musical effect
- the transition toward **post-music** as an engineering framework

**JP**

現在の中核文書は以下である。

- [`post_music_theory.md`](./post_music_theory.md)

この文書には、理論の最小中核として、主に以下が含まれる。

- **音** と **音楽** の区別
- 音楽を **内的到達可能性の変調** として捉える定義
- 内的到達可能性情報質量
- 音楽作用の身体層 / 認知層 / 統合層
- **ポスト音楽** を工学的枠組みとして位置づける導入

---

## Research Direction

**EN**

The broader direction of this project includes:

- quantitative modeling of internal reachability modulation
- structured non-linear rhythm design (including prime-based or zeta-related modulation)
- experimental comparison between periodic, structured non-linear, and noise-like rhythm streams
- integration with memory access, emotional regulation, and meaning formation
- future development toward post-music as measurable and designable dynamic gate modulation

**JP**

本研究の今後の方向性には、主に以下が含まれる。

- 内的到達可能性変調の定量モデル化
- 素数構造や ζ 関連変調を含む非線形リズム設計
- 周期リズム・構造化非線形リズム・ノイズ的刺激の比較実験
- 記憶アクセス、情動調整、意味形成との統合
- ポスト音楽を、測定可能かつ設計可能な動的ゲート変調として発展させること

---

## Note

**EN**

This repository is part of an ongoing theoretical research program.  
Definitions, notation, and document structure may continue to evolve as the framework becomes more explicit and testable.

**JP**

本リポジトリは、進行中の理論研究プログラムの一部である。  
定義、記法、文書構造は、理論がより明示的かつ検証可能になるにつれて、今後も更新されうる。

---

## Research Materials / 研究資料

**EN:** The following are *methodological candidates* and mathematical notes for the first controlled rhythm study. They do not report participant data or validated psychological effects, and do not supersede the theoretical Core.

- [F01 candidate specification — 24 bars, 192 notes](./experiments/f01_pitch_v1.md)
- [F01 canonical pitch data (JSON)](./experiments/f01_pitch_v1.json)
- [F01 event-table generator and validation checks (Python)](./experiments/f01_stimulus_build_v0_1_1.py)
- [Measurement and falsifiability audit](./experiments/measurement_audit_v0_1.md)
- [Euclidean rhythm and timing-design note](./experiments/euclidean_rhythm_note_v0_1.md)

**JP:** 以下は、第1段階のリズム比較に向けた**実験方法論の候補資料**および数学的補論である。人間を対象とする実験結果や、音楽の心理的効果が実証されたことを意味しない。従来のCore定義を上書きしない。

- [F01候補仕様（24小節・192音）](./experiments/f01_pitch_v1.md)
- [F01共通音高データ（JSON）](./experiments/f01_pitch_v1.json)
- [イベント表生成・検査コード（Python）](./experiments/f01_stimulus_build_v0_1_1.py)
- [測定・反証可能性監査](./experiments/measurement_audit_v0_1.md)
- [ユークリッドリズムと時間配置の補論](./experiments/euclidean_rhythm_note_v0_1.md)

**Reproducibility note / 再現性:** `python experiments/f01_stimulus_build_v0_1_1.py --self-test` はPython標準ライブラリのみを使用して、手元でL/M/HのCSVイベント表を生成・検査する候補コマンドである。GitHub上での自動CIテスト、音声レンダリング、聴取予備調査はまだ完了していない。

