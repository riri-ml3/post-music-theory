# Post-Music Theory v0.1  
## Music as Structured Modulation of Internal Reachability

**Status:** Foundational draft / core theoretical outline (v0.1)  
**状態:** 基礎理論ドラフト / 核心理論概要（v0.1）

---

## 0. Scope

**EN**

This document presents a minimal theoretical core of *post-music theory*.  
Its central claim is that music should not be reduced to entertainment, aesthetic decoration, or external symbolic transmission. Rather, music is modeled here as a structured temporal system that modulates the observer’s **internal reachability distribution**.

Within this framework, music changes not only what is perceived, but also which internal states become more reachable: memory states, emotional stabilizations, meaning-formation states, motivational states, and states of restored self-continuity.

This document focuses only on the core theory.  
Detailed integrations with broader ontological frameworks, forgetting dynamics, and implementation notes are treated separately.

**JP**

本稿は、*post-music theory* の最小理論核を提示するものである。  
その中心命題は、音楽を単なる娯楽、美的装飾、あるいは外的な意味伝達に還元すべきではない、という点にある。むしろ本理論では、音楽を、観測者の **内的到達可能性分布** を変調する構造化時間系として扱う。

この枠組みにおいて、音楽は単に「何が知覚されるか」を変えるだけではない。  
それは、どの内的状態がより到達しやすくなるか――すなわち、記憶状態、情動安定状態、意味形成状態、動機づけ状態、自己連続性回復状態など――を変える。

本稿はあくまで中核理論に限定する。  
より広い存在論的枠組み、忘却ダイナミクスの詳細、実装ノートとの統合は別文書に委ねる。

---

## 1. Core Distinction: Sound and Music

**EN**

A basic distinction is required.

### Sound
Sound is a physical-temporal input medium.  
It is characterized by:

- high immediacy,
- strong bodily accessibility,
- low retention unless externally encoded,
- and the capacity to affect the observer even before semantic fixation.

### Music
Music is not identical to sound itself.  
Music is sound **organized as structured temporal information**, typically involving:

- repetition,
- ratio,
- periodicity,
- deviation,
- hierarchy,
- expectation,
- tension,
- release.

Thus:

- **sound** is the medium of entry,
- **music** is the structured operation performed through that medium.

**JP**

まず、「音」と「音楽」は区別される必要がある。

### Sound
音とは、物理的かつ時間的な入力媒体である。  
その主な特性は、

- 即時性が高い
- 身体へ入りやすい
- 外部記録されない限り保持性が低い
- 意味が固定される以前に観測者へ作用しうる

という点にある。

### Music
音楽は、音そのものと同一ではない。  
音楽とは、音を **構造化された時間情報** として組織したものであり、典型的には

- 反復
- 比
- 周期
- 逸脱
- 階層
- 期待
- 緊張
- 解放

を含む。

したがって、

- **音** は入口となる媒体であり、
- **音楽** はその媒体を通して行われる構造化操作である。

---

## 2. Immediacy: Why Sound Acts on the Present

**EN**

Music builds on a property already present in sound itself: **immediacy**.  
Sound tends to affect the observer’s present state before durable symbolic fixation takes place. In this sense, sound is especially suited to changing current bodily, affective, and attentional conditions.

Music extends this property by giving temporal structure to such input.  
Because of this, music is especially suited to transiently stabilizing, redirecting, or reopening internal reachability in the present, even when its longer-term effects vary across context and individual state.

This also implies a distinction between:

- **sound entering the observer**, and
- **music being deeply experienced as music**.

The first is relatively general under ordinary hearing conditions; the second is state-dependent.

**JP**

音楽は、音そのものにすでに含まれている性質、すなわち **即時性** の上に成立する。  
音は、持続的な象徴固定が成立する以前に、観測者の現在状態へ作用しやすい。この意味で音は、現在の身体状態、情動状態、注意状態を変えるのに特に適している。

音楽は、この性質の上に時間構造を与える。  
そのため音楽は、長期効果が文脈や個体状態に依存するとしても、少なくとも現在における内的到達可能性を一時的に安定化・再方向づけ・再開通させるのに適している。

ここから、次の区別も重要になる。

- **音が観測者に入ること**
- **音楽が音楽として深く経験されること**

前者は通常の聴覚条件のもとで比較的一般的であるが、後者は観測者状態に依存する。

---

## 3. Main Theoretical Claim

**EN**

The main claim of this theory is:

> Music is modeled as a structured temporal operation that modulates the observer’s internal reachability distribution.

Let $G_{\mathrm{int}}$ denote an internal target set, such as:

- an autobiographical memory state,
- an emotionally stabilized state,
- a meaning-bearing state,
- a motivation-ready state,
- a restored self-state.

Let

$$
p_t(G_{\mathrm{int}})
$$

denote the probability that the observer can reach that internal state within a relevant horizon.

Then music is not treated primarily as the transmission of external information, but as an operation that changes this probability.

**JP**

本理論の中心命題は次の通りである。

> 音楽とは、観測者の内的到達可能性分布を変調する構造化時間操作としてモデル化される。

ここで $G_{\mathrm{int}}$ を内的目標集合とする。たとえば、

- 自伝的記憶状態
- 情動安定状態
- 意味が立ち上がる状態
- 行動準備が整った状態
- 自己連続性が回復した状態

などである。

また、

$$
p_t(G_{\mathrm{int}})
$$

を、時刻 $t$ においてその状態へ到達できる確率とする。

このとき、音楽は外的情報の単純伝達としてではなく、この到達確率を変える作用として扱われる。

---

## 4. Reachability-Information Mass

**EN**

To quantify this change, define the internal reachability-information mass as:

$$
M_{\mathrm{info}}^{\mathrm{int}}(t)=\log\frac{p_t(G_{\mathrm{int}})}{1-p_t(G_{\mathrm{int}})}
$$

Interpretation:

- large $M_{\mathrm{info}}^{\mathrm{int}}(t)$: the internal target state is more reachable,
- small or negative $M_{\mathrm{info}}^{\mathrm{int}}(t)$: the target state is relatively closed.

Within this framework, a primary effect of music is:

$$
\Delta M_{\mathrm{info}}^{\mathrm{int}}(t) > 0
$$

for some relevant internal state or family of internal states.

**JP**

この変化を定量化するため、内的到達可能性情報質量を

$$
M_{\mathrm{info}}^{\mathrm{int}}(t)=\log\frac{p_t(G_{\mathrm{int}})}{1-p_t(G_{\mathrm{int}})}
$$

と定義する。

解釈は次の通りである。

- $M_{\mathrm{info}}^{\mathrm{int}}(t)$ が大きい：その内的状態へ到達しやすい
- $M_{\mathrm{info}}^{\mathrm{int}}(t)$ が小さい、または負である：その状態は相対的に閉じている

本理論では、音楽の主要な作用の一つを、

$$
\Delta M_{\mathrm{info}}^{\mathrm{int}}(t) > 0
$$

すなわち、ある内的状態群への到達可能性情報質量を増加させることとして扱う。

---

## 5. State-Dependence of Musical Experience

**EN**

The modulation produced by music is not expected to be uniform across all observer states.  
A crucial distinction must therefore be made between the stimulus itself and the observer’s condition at the time of reception.

Let $O(t)$ denote the observer’s current state, including, for example:

- stress level,
- attentional availability,
- cognitive load,
- bodily fatigue,
- emotional rigidity or openness,
- prior learning and familiarity.

Then the effective modulation should be understood not as a function of music alone, but more precisely as:

$$
\Delta p_t(G_{\mathrm{int}}) = f(P(t), O(t))
$$

where $P(t)$ is the musical stimulus.

This means that under high stress or heavy information load, sound may still enter the observer while the full musical experience remains weak, shallow, or blocked.  
Accordingly, music may be humanly general as an input medium, while its depth of effect remains strongly state-dependent.

**JP**

音楽による変調は、あらゆる観測者状態に対して一様に生じるとは想定されない。  
したがって、刺激そのものと、受容時点の観測者条件は区別されなければならない。

ここで $O(t)$ を観測者の現在状態とする。これには例えば、

- ストレス水準
- 注意の空き容量
- 認知負荷
- 身体疲労
- 情動の硬直性または開放性
- 学習履歴や親和性

などが含まれる。

このとき、音楽による実効的変調は、音楽単独ではなく、より正確には

$$
\Delta p_t(G_{\mathrm{int}}) = f(P(t), O(t))
$$

として理解されるべきである。ここで $P(t)$ は音楽刺激である。

これは、高ストレスや高情報負荷状態では、音そのものは観測者に入っても、音楽体験としての深い作用は弱くなったり、浅くなったり、遮断されたりしうることを意味する。  
したがって、音楽は入力媒体としては人間一般に近いが、その効果の深さは強く状態依存である。

---

## 6. Why Music Appears Primarily Psychological

**EN**

Historically, music has participated in:

- ritual synchronization,
- labor coordination,
- transmission,
- collective affect regulation,
- symbolic and cultural continuity.

However, in modernity, many explicit external information-preservation and transmission functions have been partially externalized to:

- writing,
- print,
- visual media,
- digital archives,
- networked communication systems.

As a result, music’s internal function becomes more visible.  
This does not mean that music has ceased to be structural. Rather, its structural force appears less as explicit external encoding and more as internal state modulation.

Thus, the contemporary psychological centrality of music is not a degeneration of music’s function, but an exposure of one of its deeper functions.

**JP**

歴史的に音楽は、

- 儀礼的同期
- 労働同期
- 伝承
- 集団情動調整
- 文化的連続性の維持

などに関与してきた。

しかし近代以降、外的情報の明示的保存・伝達機能の多くは、

- 文字
- 印刷
- 映像
- デジタル記録
- ネットワーク通信

へと部分的に外部化された。

その結果、音楽の内的機能がより可視化されるようになった。  
これは、音楽が構造性を失ったことを意味しない。むしろ、その構造作用の主たる現れ方が、外的符号化よりも内的状態変調として前景化したのである。

したがって、現代において音楽が心理中心に見えるのは、音楽機能の劣化ではなく、その深層機能の露出である。

---

## 7. Layered Interpretation of Musical Effect

**EN**

Music should not be treated as operating at only one level.  
Its effects can be decomposed into at least two major layers, with a possible third integrative layer.

### Layer 1: Bodily-Physiological Layer
At this level, music acts through:

- rhythmic entrainment,
- breathing alignment,
- motor synchronization,
- immediate affective stabilization.

This layer is close to preservation-oriented functioning.

### Layer 2: Cognitive-Meaning Layer
At this level, music acts through:

- expectation and deviation,
- memory activation,
- emotional reframing,
- symbolic or narrative resonance,
- motivational redirection.

This layer is closer to exploratory and meaning-forming functioning.

### Layer 3: Integrative Layer
In some cases, music may contribute to:

- states of coherence,
- self-reorganization,
- aesthetic ecstasy,
- deep meaning unification,
- creative jump states.

Thus, music is not reducible either to bodily pleasure or to symbolic meaning alone.  
It is a multi-layer temporal structure capable of modulating several levels of internal reachability.

**JP**

音楽は単一層で作用するものとして扱うべきではない。  
その効果は少なくとも二つの主要層、さらに場合によっては第三の統合層に分解できる。

### Layer 1: 身体‐生理層
この層で音楽は、

- リズム同調
- 呼吸整列
- 運動同期
- 即時的情動安定

などを通して作用する。

これは保存志向の機能に近い。

### Layer 2: 認知‐意味層
この層で音楽は、

- 期待と逸脱
- 記憶活性化
- 感情の再意味化
- 象徴的・物語的共鳴
- 動機づけの再配向

などを通して作用する。

これは探索・意味形成の機能に近い。

### Layer 3: 統合層
場合によっては音楽は、

- 整合状態
- 自己再構成
- 美的エクスタシー
- 深い意味統合
- 創造的ジャンプ状態

にも関与しうる。

したがって、音楽は身体快にも、象徴意味にも単純還元できない。  
それは複数層の内的到達可能性を変調しうる多層時間構造である。

---

## 8. Music, Mathematics, and Structured Temporal Compression

**EN**

The statement that “music originates in mathematics” should be reformulated with care.

Music is not mathematical merely because it contains numerical ratios.  
Rather, music is grounded in structured temporal compressibility. Its mathematical character lies in its use of:

- periodicity,
- recurrence,
- proportion,
- hierarchy,
- controlled deviation,
- and transitions between stability and instability.

These properties make music especially suited to changing internal prediction and access dynamics.

In this sense, music can be understood as a compressed temporal structure capable of reorganizing internal reachability.

**JP**

「音楽の起源は数学にある」という表現は、慎重に再定義されるべきである。

音楽は単に数比を含むから数学的なのではない。  
むしろ音楽は、構造化された時間圧縮可能性に基づく。  
その数学性は、

- 周期性
- 再帰性
- 比例
- 階層性
- 制御された逸脱
- 安定と不安定の遷移

にある。

これらの性質によって、音楽は観測者の予測やアクセス動態を変化させるのに適している。

この意味で音楽は、内的到達可能性を再編成しうる圧縮時系列構造として理解できる。

---

## 9. Post-Music

**EN**

Within this framework, post-music is proposed as the explicit, measurable, and designable continuation of functions that traditional music often performs only implicitly.

Post-music aims to engineer internal reachability modulation through controlled stimulus design, potentially using measurable variables such as:

- stimulus-observer coupling,
- rhythmic synchronization,
- entropy shifts,
- estimated reachability change,
- frustration accumulation.

Accordingly, post-music should not be understood merely as a new musical style.  
It is better understood as a framework for engineering dynamic gate modulation across memory, emotion, meaning, and self-structure.

In this limited sense, post-music may also be understood as a framework for shaping state transitions in consciousness through temporal structure.

**JP**

この枠組みにおいて、ポスト音楽とは、従来音楽がしばしば暗黙的に行っていた機能を、明示的・測定可能・設計可能に継承するものとして提案される。

ポスト音楽は、刺激設計を通じて内的到達可能性変調を工学化することを目指す。  
その際には、たとえば以下のような測定量が利用されうる。

- 刺激‐観測者結合
- リズム同期
- エントロピー変化
- 推定到達可能性変化
- フラストレーション蓄積

したがって、ポスト音楽は単なる新しい音楽様式ではない。  
それは、記憶・感情・意味・自己構造にまたがる動的ゲート変調を工学化する枠組みとして理解されるべきである。

この限定的な意味において、ポスト音楽は、時間構造を通じて意識の状態遷移を方向づける枠組みとして理解することもできる。

---

## 10. Minimal Falsifiability and Research Direction

**EN**

At the present stage, the theory should be treated as a foundational theoretical draft rather than a completed empirical framework.  
However, several core claims are already partially testable.

Examples:

1. Whether music changes self-reported internal reachability to target states.
2. Whether structured non-linear rhythm modulation differs from both simple periodic rhythm and unstructured noise.
3. Whether frustration accumulation predicts aversion, dropout, or breakdown in temporal experience.
4. Whether familiar music transiently increases access to autobiographical memory states.
5. Whether the depth of musical effect varies systematically with observer state variables such as stress, cognitive load, and attentional availability.

The theory gains strength only insofar as such claims become operationally testable.

**JP**

現段階では、本理論は完成した経験科学というより、基礎理論ドラフトとして扱われるべきである。  
しかし、いくつかの中核命題はすでに部分的に検証可能である。

例として、

1. 音楽が内的目標状態への主観的到達可能性を変えるか  
2. 構造化された非線形リズム変調が、単純周期や無構造ノイズと異なるか  
3. フラストレーション蓄積が嫌悪・離脱・破綻を予測するか  
4. 懐かしい音楽が自伝的記憶状態へのアクセスを一時的に高めるか  
5. ストレス、認知負荷、注意余力などの観測者状態変数に応じて、音楽効果の深さが系統的に変化するか  

などである。

本理論の強度は、こうした命題がどこまで操作化され、検証可能になるかに依存する。

---

## 11. Condensed Proposition Set

**EN**
- **P1**: Sound and music must be distinguished: sound is an input medium, music is structured temporal organization through that medium.
- **P2**: Sound has strong immediacy effects on the observer’s present state, and music builds on this immediacy through temporal structuring.
- **P3**: Music is modeled primarily as modulation of internal reachability rather than mere external information transmission.
- **P4**: A useful quantitative proxy for this modulation is internal reachability-information mass.
- **P5**: The contemporary psychological centrality of music reflects the foregrounding of music’s internal modulation function.
- **P6**: Post-music is the explicit engineering continuation of this internal modulation function.

**JP**
- **P1**：音と音楽は区別されるべきである。音は入力媒体であり、音楽はその媒体を通した構造化時間組織である。
- **P2**：音は観測者の現在状態へ強い即時作用を持ち、音楽はその即時性を時間構造化によって拡張する。
- **P3**：音楽は、外的情報伝達というより、内的到達可能性の変調として主にモデル化される。
- **P4**：その変調の有用な定量代理が、内的到達可能性情報質量である。
- **P5**：現代において音楽が心理中心に見えるのは、その内的変調機能が前景化したためである。
- **P6**：ポスト音楽は、この内的変調機能を明示的に工学化する延長である。
