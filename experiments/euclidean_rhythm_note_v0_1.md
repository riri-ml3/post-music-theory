# Euclidean Rhythm and F01 Timing Design v0.1

**Status:** Mathematical note + experimental interpretation; no perceptual or physiological finding.  
**Scope:** Post-Music Theory stimulus design. U-Structure, sleep, time ontology and social allocation theories are out of scope.

## Summary (EN)

A Euclidean rhythm `E(k,n)` distributes `k` onsets through `n` discrete cyclic slots as evenly as possible. The baseline of F01 is the trivial isochronous case `E(8,16)` with onset positions `[0,2,4,6,8,10,12,14]`. F01's Low/Medium/High conditions progressively displace some of these onsets; they do **not** constitute three Euclidean rhythms. Deviations affect inter-onset intervals and metrical placement simultaneously. Physical mathematical evenness is not equivalent to perceived regularity, pleasure, learning efficiency, or integrative depth.

## 1. 数学的定義

`n` 個の離散時間位置のうち `k` 個を発音位置とし、二値周期列 `r_i ∈ {0,1}` で表す。`Σ r_i = k`。循環間隔 `g_1, ..., g_k` は正整数であり、`Σ g_i = n`。

隣接発音間隔の分散 `Σ (g_i-n/k)^2` を最小化する場合、各間隔は `floor(n/k)` または `ceil(n/k)` になる。ただし、この **隣接間隔の最小分散条件だけでは順序まで一意に決められない**。ユークリッドリズムの均等性には、間隔の配置順や円周上の全発音点の距離に関する、より強い数学的性質がある。

具体例：

- `E(8,16)`: 8発音／16位置、循環間隔 `[2,2,2,2,2,2,2,2]`。
- `E(5,16)`: 5発音／16位置、循環間隔の一例 `[3,3,4,3,3]`（円周上の開始位置／回転に依存）。

同じ `E(k,n)` の回転配置も、強拍やアクセントに対する位置関係が変われば音楽知覚に与える作用が異なり得る。

## 2. Family 01との対応

F01基準のオンセット位置は `[0,2,4,6,8,10,12,14]`（1小節16単位）であり、`E(8,16)` に相当する。

既存のFamily 01を変更せず、三条件の**基準位置から移動されたイベント数**を区別する。

| Condition | Displaced event positions / 168 movable positions | Mean IOI (beats) | IOI variance (beat²) |
|---|---:|---:|---:|
| L | 12/168 | 0.5 | 0.0078125 |
| M | 48/168 | 0.5 | 0.0312500 |
| H | 90/168 | 0.5 | 0.0390625 |

**注意：** この逸脱率は「基準時刻と異なる位置へ移動した発音イベントの割合」であり、二値周期列同士のHamming距離をそのまま正規化した値ではない。

移動を受けた小節の一部は等間隔でなくなる。M/HがE(k,n)として新たに均等化されたわけではない。同じ音数・総時間を維持しても、局所IOI分散、同期・アクセント位置、音高と強拍の関係が同時に変化する。

## 3. 物理配置と観測者の経験を分離する

一定速度で回転する16穴の円盤を考える。8本のピンを交互の穴に置けば、センサーを通過するたびに等間隔でイベントが起こる。5本なら、3穴分と4穴分の間隔を組み合わせることで均等性を高められる。この装置は数学的な配置の説明である。自然界が普遍的にこのアルゴリズムを選ぶという物理法則を意味しない。

同じ配置でも観測者の拍節予測、学習歴、注意状態が異なれば、主観的な規則性や複雑さの評価が異なる可能性がある。

**分離すべき三つの量：**
1. `physical_evenness`: 発音間隔の配置性質。
2. `perceived_regularity`: 聴取者が認識した規則性。
3. `learning_or_integration`: 学習、転移、事後の構造理解・統合的経験。

一つ目から残り二つを自動的に導かない。

## 4. 検証仮説・反証フック

- **E1（操作確認）：** F01のL/M/Hは設計上の逸脱率とIOI分散が異なる。聴取者の複雑性評価が同順になるかは別途検証する。
- **E2（知覚と学習）：** 反復後、初回に予測しにくかった配置で次イベント予測や未提示パターンへの転移が改善するかを調べる。
- **E3（非同一性）：** 物理的均等性が高い条件が、必ずしも高い音楽的意味、快楽、K、Rを生むとは予測しない。
- **E4（厳密な対照）：** `E(5,16)` と `E(8,16)` の直接比較は発音数が異なるため、F01の局所逸脱効果を識別する第一実験には使用しない。同一発音数で別の配置指標を比較する設計が必要である。
- **E5（学習効果）：** 反復刺激の単純再認と、未知パターンへの規則転移を区別する。

## 5. Mathematical versus ontological interpretations

「制約下の均等配置」は数学的に定義できる。しかし「全員が均等である社会」や「多様性が全体系を安定させる」とは異なる最適化問題であり、音楽的な均等配置をそのまま倫理・生態・宇宙的安定へ一般化しない。必要なら別研究のBridgeで、目的関数・相互作用・測定値を独立に定義する。

## 6. Literature

- Toussaint, G. (2005). *The Euclidean Algorithm Generates Traditional Musical Rhythms*. Bridges 2005, 47–56. https://www.archive.bridgesmathart.org/2005/bridges2005-47.html
- Demaine, E. D. et al. (2007). *The Distance Geometry of Music*. https://arxiv.org/abs/0705.4085
- Vuust, P. & Witek, M. A. G. (2014). *Rhythmic complexity and predictive coding: a novel approach to modeling rhythm and meter perception in music*. https://doi.org/10.3389/fpsyg.2014.01111

**Status rule:** 既存数学と試験計画を区別する。音楽的優位性、深い統合、脳・意識・宇宙の同型性は本資料で証明しない。
