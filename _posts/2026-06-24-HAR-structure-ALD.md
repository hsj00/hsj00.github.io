---
title: "HAR 구조에서 Step Coverage를 지배하는 공정 파라미터 - Feeding Time과 Purge Time의 물리적 근거"
layout: post
date: 2026-06-24 10:00 +0900
tag:
    - ALD
    - Atomic Layer Deposition
    - Step coverage
    - HAR
    - Molybdenum
    - ALD-Mo
    - NAND Flash
    - Wordline Metallization
    - Semiconductor
    - Memory Device
    - Chemical Kinetics
    - Transport Modeling
    - Knudsen diffusion
    - Study
    - Note
headerImage: false
image: 
description: 260624 `Step Coverage in High Aspect Ratio Structures - Why Feeding Time and Purge Time Matter in ALD`
category: blog
author: hsj00
externalLink: true
published: true
giscus_comments: true
share: true
use_math: true
toc:
  beginning: true
  sidebar: left
---

> ALD(Atomic Layer Deposition) 기반 공정에서 Precursor Feeding Time과 Purge Time이
> HAR Hole/Trench의 Step Coverage를 어떻게 결정하는가

---

## 서론

### 1.1 3D NAND의 수직 집적화와 HAR 구조의 등장

3D NAND 플래시 메모리는 수평 방향 scaling의 물리적 한계를 극복하기 위해 수직 방향으로 메모리 셀을 적층하는 전략을 채택했다. V(Vertical)-NAND 세대가 V6(128-layer)에서 V8(236-layer), V9(286-layer)를 거쳐 V12(500+ layer) 이상으로 진화하게되면, 구조의 종횡비(Aspect Ratio, AR)는 단순히 증가하는 것이 아니라 **지수적 수준의 공정 난이도**를 만들어낸다. 이 과정에서 wordline 금속 재료로 가장 널리 사용된 텅스텐(W)을 증착하는 공정은 핵심 병목 구간 중 하나로 부상하였다.

Wordline 구조는 폭 약 25~30 nm, 깊이 수백 nm에 달하는 **lateral cavity**(수평 방향 개구 구조)로, stack의 층수가 증가할수록 cavity 깊이가 증가하고 유효 AR이 상승한다. 더욱 중요한 것은, **ALD 증착이 진행될수록 금속 막이 양 벽면에 동시에 성장하면서 cavity의 CD(Critical Dimension)가 점진적으로 좁아진다**는 점이다. 이는 공정 초기와 후기에서 precursor가 마주치는 확산 저항이 현저히 달라짐을 의미하며, 동일한 recipe를 사용하더라도 마지막 ALD cycle에서의 step coverage가 가장 취약해지는 구조적 딜레마를 형성한다.

### 1.2 Step Coverage와 Diffusion Limit

Step coverage는 HAR feature 내부(bottom/sidewall)의 막 두께와 feature 외부(top surface)의 막 두께의 비로 정의할 수 있다. ALD는 self-limiting surface reaction을 기반으로 하기 때문에 CVD 대비 우수한 conformality를 제공하는 것으로 알려져 있지만 AR이 극단적으로 커지면 ALD 역시 **diffusion-limited** 거동을 보이며, 이상적인 100% step coverage로부터 이탈하기 시작한다. 이 현상의 근본 원인은 precursor 분자가 feature 최심부까지 확산되어 표면 반응을 완결 짓기 전에 pulse가 종료되거나, 불완전 purge로 인해 self-limiting 거동 자체가 훼손되는 데 있다.

이번 글은 이러한 고민에서 출발했다. AI의 도움을 받아서 HAR hole과 HAR trench에서 diffusion limit이 발생하는 물리적 메커니즘을 정량적으로 조사하고, **precursor feeding time**과 **purge time**이 step coverage를 결정하는 핵심 변수임을 정리했다.

---

## 본론

### 2.1 HAR 구조에서의 기체 수송: Knudsen Diffusion Regime

ALD 공정의 전형적인 reactor 압력(수 mTorr~수 Torr)과 feature 폭(수 nm~수십 nm) 조건에서, 기체 분자의 **평균 자유 경로(mean free path, λ)**는 feature 폭 *d*보다 훨씬 크다(전형적으로 10²~10³배 수준).[^1] 이를 정량화하는 지표가 **Knudsen Number(Kn)**이다:

$$Kn = \lambda / d$$

**Kn ≫ 1**인 free molecular flow 영역에서는 분자간 충돌보다 분자–벽면 충돌이 지배적이다.[^1][^2] 이 regime의 특성은 다음과 같다.

- 분자는 벽면에서 **cosine 분포로 확산 반사(diffuse reflection)**되며 wall-to-wall random walk(Knudsen diffusion)로 이동하므로, 분자간 산란 없이도 feature 최심부까지 도달 가능성이 유지된다.[^2]
- **정규화된 saturation profile(=AR 단위 침투)은 오직 exposure(P × t)와 sticking probability에만 의존하며, 압력 단독·채널 높이에는 독립적이다.**[^2][^3] 다만 이때 침투는 exposure에 **선형이 아니라 제곱근**으로 증가한다. AR ∝ √(exposure) (Gordon의 $E_{sat}\propto s_0^{-1}(\mathrm{EAR})^2$과 동치). 절대 침투 길이는 Knudsen 확산계수가 feature 치수에 비례하므로($D_K\propto d$) 채널 높이에도 의존한다.
- 따라서 압력이나 공급 시간을 늘리면 침투가 증가하되, 목표 AR을 2배로 늘리려면 exposure를 약 4배 늘려야 한다. (동일 AR에서 hole은 trench 대비 약 4배 exposure 요구.)
- **Kn이 감소해 transition 영역에 가까워지면** exposure-only universality가 깨지고, 같은 exposure 대비 침투가 줄며 saturation profile이 압력·채널 높이에 개별적으로 의존하게 된다. 다만 현실적 ALD 압력에서 nm급 HAR feature 내부는 λ ≫ d(Kn ~ 수백)이라 사실상 항상 free molecular flow이며 continuum으로의 전이는 일어나지 않는다.

결국 ALD의 step coverage는 "precursor 양이 충분한가"가 아니라, **주어진 공정 시간 내에 Knudsen diffusion을 통한 saturation front가 목표 AR까지 도달하는가**의 문제다.

---

### 2.2 ALD Self-limiting 반응과 Adsorption Front

ALD의 본질적 강점은 각 half-cycle에서 표면 반응이 자기제한(self-limiting)된다는 점이다.[^4] Precursor 분자가 표면의 reactive site와 화학흡착(chemisorption)으로 반응해 표면을 덮으면 그 site는 비활성화되고, 이후 유입되는 분자는 더 깊이 이동하여 아직 반응하지 않은 site를 찾아 반응한다(입체 장애(steric hindrance)로 인해 실제 포화 피복률은 대개 1 monolayer 미만이다). 이 과정이 feature 최심부까지 순차적으로 진행되면서 **adsorption front**가 형성되고, 이 front가 bottom에 도달해야만 비로소 완전한 step coverage가 달성된다.[^3]

CVD와의 결정적 차이는 여기서 나타난다. CVD는 precursor가 공급되는 한 반응이 지속되므로 feature 상단에서 급격한 막 성장이 일어나 **pinch-off**(cavity 입구 폐쇄)가 발생한다.[^4][^7] ALD는 상단이 일단 포화되면 추가 반응이 억제되므로 분자가 더 깊이 침투할 수 있다. 그러나 이 self-limiting 메커니즘이 온전히 작동하려면 **purge step에서 이전 반응의 부산물과 잔류 precursor가 완전히 제거**되어야 한다.[^8] 불완전 purge는 self-limiting 거동 자체를 훼손하고, ALD가 아닌 CVD로 반응 양상이 달라지는 결과를 낳는다.[^8]

---

### 2.3 Gordon-Hausmann 모델: 정량적 스케일링 법칙

HAR 구조에서 ALD conformality를 정량적으로 기술한 가장 영향력 있는 이론 체계는 **Gordon, Hausmann, Kim, Shepard(2003)**의 모델이다.[^3] 예전에 이 모델을 바탕으로 Streamlit calculator를 만들기도 했다. 이 모델은 Knudsen regime에서의 반응-확산 문제를 풀어 다음의 핵심 관계를 도출하였다.

**Saturation dose:**[^3]

Sticking coefficient가 1인 이상적인 경우, 직경 *d*, 깊이 *L*인 hole을 포화시키는 데 필요한 exposure는 다음과 같다(*a* = *L/d*):

$$P \cdot t_{sat} = \rho_s \sqrt{2\pi m k_B T}\left(1 + \frac{19}{4}a + \frac{3}{2}a^2\right)$$

- **ρ_s**: 표면 흡착 site 밀도 (단위 면적당 필요한 precursor 분자 수)
- **m**: precursor 분자 질량, **T**: 공정 온도
- 괄호 안 첫 항은 flat surface 포화, 둘째 항은 벽면 도포(ballistic), 셋째 항이 Knudsen 확산 제한을 나타내며 **고 AR에서는 a² 항이 지배**한다.

Sticking coefficient s₀ < 1인 일반적인 경우까지 포함하면, 고 AR 극한에서의 스케일링은 다음과 같이 요약된다:[^3]

$$E_{sat} \propto s_0^{-1} \times (EAR)^2$$

- **E_sat**: feature 전체를 포화시키기 위해 필요한 최소 exposure (단위: Langmuir = 10⁻⁶ Torr·s)
- **s₀**: initial sticking coefficient (precursor가 표면 site에 반응할 확률)
- **EAR**: Equivalent Aspect Ratio

**Penetration depth (saturation front 침투 깊이):**

확산-반응 관점에서 saturation front의 침투 깊이 $z_{sat}$은 다음과 같이 표현된다:

$$z_{sat}^2 \approx \frac{2\, D_K\, n\, t}{\rho_s \,(P_w/A)}, \qquad n = \frac{P}{k_B T}$$

여기서 $D_K$는 Knudsen diffusivity, *n*은 precursor 수밀도, $P_w/A$는 단면적당 벽 둘레(hole: 4/*d*, trench: 2/*w*)이다. $D_K \propto d$를 대입하면 $(z_{sat}/d)^2 \propto P \times t$, 즉 **AR 단위 침투 깊이는 exposure의 제곱근에 비례**하며, 이는 위의 $E_{sat} \propto (EAR)^2$ 스케일링과 동치이다. 완전한 conformality를 위해서는 $z_{sat} \geq L$ 조건이 충족되어야 한다.

**Feeding time 조건:**

Exposure는 $E = P \times t_{feed}$이므로, 필요한 최소 feeding time은:[^3]

$$t_{feed,min} \propto \frac{\rho_s \sqrt{2\pi m k_B T}}{P} \times (EAR)^2$$

**즉, 필요한 최소 feeding time은 EAR의 제곱에 비례하고 압력에 반비례한다.**[^3] AR이 2배 증가하면 필요한 feeding time은 이론적으로 4배 증가한다는 것이 이 모델의 핵심 예측이다.[^3] 두 가지 점에 유의해야 한다.

- 필요 exposure(Torr·s)는 **feature의 절대 치수와 무관하게 EAR에만 의존**한다. Knudsen diffusivity의 치수 의존성($D_K \propto d$)이 AR² 스케일링 안에 이미 내재되어 있기 때문이며, 따라서 이 식에 확산계수를 별도의 인자로 추가해서는 안 된다.
- 온도가 오르면 확산은 빨라지지만($D_K \propto \sqrt{T}$) 압력당 충돌 flux가 감소하므로, 필요 exposure는 오히려 $\sqrt{T}$에 비례해 **증가**한다. "고온일수록 확산이 빨라 feeding time을 줄일 수 있다"는 직관은 이 모델에서는 성립하지 않는다.

---

### 2.4 HAR Hole vs HAR Trench: 기하학적 비대칭성

Hole과 trench는 겉보기 AR이 동일하더라도 precursor 수송 관점에서 본질적으로 다른 difficulty를 가진다. Gordon-Hausmann 모델은 이를 **Equivalent Aspect Ratio(EAR)**의 개념으로 정형화하였다.[^3][^1]

| 구조 유형 | EAR 정의 | AR=20 기준 EAR | 상대 E_sat |
|:---|:---|---:|---:|
| **Trench** (상부 개구 slot) | L / (2w) [^1] | 10 | 1x |
| **Hole** (원통형 단일 개구) | L / w [^1] | 20 | **4x** |

이 2배 인자의 물리적 근거는 **수력 직경(hydraulic diameter, $D_h = 4A/P_w$)**이다. 폭 *w*인 slot형 trench는 단면적당 벽 둘레가 2/*w*로 hole(4/*d*)의 절반이므로, precursor 소모 대비 수송 단면이 유리하여 **직경 2w인 hole과 등가**로 거동한다($D_h = 2w$). 즉 EAR = L/(2w)는 trench의 벽 면적/단면적 비가 hole의 절반이라는 기하학적 사실에서 나오는 것이지, 개구부 개수와는 무관하다. 따라서 **동일한 AR을 가진 hole에는 trench 대비 4배의 exposure가 필요하다**는 결론이 EAR의 제곱 비례 관계에서 직접 유도된다.[^1][^3]

$$E_{hole} \propto (L/w)^2 = 4 \times (L/2w)^2 = 4 \times E_{trench}$$

한 가지 주의할 점: 만약 구조가 실제로 **양 끝이 열려** precursor가 양방향에서 유입되는 경우라면, 유효 확산 거리 L 자체가 절반이 되어 EAR이 추가로 절반, 필요 exposure가 4배 더 감소한다. 이는 위의 수력 직경 효과와는 **별개의 효과**이므로 두 인자를 혼동해서는 안 된다.

이 기하학적 비대칭성은 채널홀과 워드라인 공정에서 동일 재료를 증착할 때도 feeding time을 완전히 다르게 설계해야 하는 이유를 물리적으로 설명한다.[^4]

3D NAND 구조별 EAR 특성을 정리하면 다음과 같다:

- **Channel hole**: 전형적인 cylindrical hole 형태 → EAR = AR, exposure 요구 최대
- **Wordline cavity**: lateral 방향 trench 형태이나, slit을 통한 단방향 가스 진입 경로를 가지므로 실질적 EAR은 단순 trench와 hole의 중간 어딘가에 위치하며, 정밀한 분석이 필요하다.
- **Gate slit**: 상부가 열린 수직 trench(slot) 기하 → 수력 직경 논리에 따라 EAR = AR/2

---

### 2.5 Precursor Feeding Time의 역할: Saturation Front가 Bottom에 도달하는가

Feeding time은 단순히 "precursor를 얼마나 오래 흘려 보내는가"의 문제가 아니다. 이것은 **adsorption front가 feature 최심부에 도달하기 위한 충분한 dose(P × t)가 공급되는가**를 결정하는 변수이다.[^3]

**Feeding time이 부족한 경우의 시나리오:**

1. Feature 상단 근처에서 saturation이 완료되지만, adsorption front가 bottom에 도달하기 전에 precursor pulse가 종료된다.
2. Bottom은 미반응 상태로 남으며 step coverage < 100%를 기록한다.
3. Top-heavy thickness profile: 상단 두껍고 하단 얇은 비균일한 막이 형성된다.
4. 3D NAND에서는 이것이 wordline별 저항 불균일로 직결되어 cell-to-cell Vth 산포를 악화시킨다.

**실제 수치 사례 (HfO₂ ALD in HAR holes):**

Gordon 그룹의 이론 모델에 따르면, AR 수십(깊이 수 μm 수준)의 HAR hole에서 완전한 step coverage를 달성하기 위해 **수천~수만 Langmuir(10⁻³~10⁻² Torr·s 수준)** 이상의 exposure가 필요하다.[^3] Saturation dose 식의 괄호항을 직접 계산해 보면, 이는 동일 재료의 flat surface 포화에 필요한 dose 대비 **수백~수천 배**에 해당한다(예: EAR = 20인 hole은 약 700배, EAR = 40이면 약 2,600배). 이 이론적 예측은 Gordon-Hausmann의 (EAR)² 스케일링과 일관성을 가지며, HAR 구조에서 feeding time의 극적인 연장이 불가피함을 정량적으로 뒷받침한다.[^3]

**Feeding time 증가의 대안적 방법:**

- **Partial pressure 증가**: $E = P \times t_{feed}$이므로 압력을 높이면 동일 dose를 더 짧은 시간에 달성 가능하나, 반응기 설계 제약이 있다.[^3]
- **Heavy inert gas(예: Kr) 첨가**: AlN ALD(TMA/NH₃)에 Kr을 공동 주입한 실험에서 AR 18:1 수직 trench의 step coverage가 **1.0 → 1.6으로 향상**되었다(상단 GPC는 억제되고 하단 GPC는 유지되는 superconformal 거동).[^5] 저자들은 무거운 Kr(84 amu)이 가벼운 NH₃(17 amu)의 trench 내부 확산을 촉진하는 것으로 **추정(speculate)**하고 있으며, 메커니즘 규명을 위한 추가 연구 필요성을 명시하였다.[^5] 또한 lateral HAR 구조에서는 deposition depth 증가 효과가 관찰되지 않아 수직 trench에 특이적인 효과임을 유의해야 한다.[^5]
- **다중 pulse(dose segmentation)**: 단일 long pulse 대신 여러 번의 짧은 pulse + 중간 purge 조합으로 byproduct buildup을 방지하면서 누적 dose를 확보하는 방식.[^8]

---

### 2.6 Purge Time의 역할: ALD를 CVD로 만들지 않기 위한 조건

Purge time 증가는 throughput 관점에서의 비용(cycle time 증가)으로만 인식되기도 한다. 그러나 HAR 구조에서 purge time의 부족은 단순한 불순물 문제를 넘어 **step coverage 자체를 저하시키는 직접적 메커니즘**으로 작용한다.

**불완전 purge의 연쇄 효과:**

**1. Parasitic CVD 발생**

잔류 precursor가 co-reactant pulse 도입 시 gas-phase에서 반응하여 non-self-limiting 성장이 유발된다. GPC(Growth Per Cycle)가 saturation plateau를 벗어나 계속 증가하는 것이 parasitic CVD의 진단 지표이다.[^8]

**2. Feature 상단의 과잉 성장**

Parasitic CVD에 의한 excess deposition은 반응 농도가 가장 높은 feature 입구 근처에 집중된다. 이는 opening CD를 추가로 좁히는 결과를 낳는다.[^7][^8]

**3. 양성 피드백(positive feedback) 메커니즘**

과잉 성장으로 좁아진 CD는 다음 feeding step에서 precursor의 내부 확산을 더욱 어렵게 만든다. 즉, 불완전 purge는 cycle이 진행될수록 step coverage가 점점 악화되는 피드백 루프를 형성한다.[^1][^8]

**4. Byproduct re-adsorption에 의한 막질 저하**

반응 부산물이 충분히 탈출하기 전에 다음 pulse가 시작되면, 이 fragment들이 막 내에 편입되어 불순물로 남는다. **HZO PE-ALD에서 metal precursor purge time을 90초에서 3초로 단축한 실험에서 ferroelectric → antiferroelectric-like 상전환이 관찰**되었다.[^6] 구체적으로, 3초 purge 조건에서 탄소(C) 및 질소(N) 불순물 함량이 현저히 증가하여 antipolar o-I phase(공간군 Pbca, orthorhombic)가 안정화되었고, 90초 조건에서는 ferroelectric Pca2₁ 상이 우세하였다.[^6] 동일한 precursor 조합과 공칭 조성 조건에서 공정 파라미터만으로 결정상이 제어된 사례이지만, XPS 분석상 Hf:Zr 비율도 purge time에 따라 미세하게 변화(3초 79:100 → 90초 74:100)했으므로 조성이 완전히 불변인 것은 아니며, 저자들은 상전환의 주 원인을 불순물 편입으로 해석하였다.[^6]

**HAR 구조에서 purge time 설계의 특수성:**

HAR feature 내부의 byproduct는 Knudsen diffusion 메커니즘으로 feature에서 서서히 탈출하기 때문에, flat substrate 기준 purge time은 HAR 구조에 결코 충분하지 않다.[^1] HAR feature의 경우 flat substrate 대비 purge time을 수 배에서 수십 배 수준으로 연장해야 하는 것이 일반적이다. 최적 purge time은 GPC가 자기제한적 plateau에 도달하는 최소 시간, 즉 HAR feature 내부까지 포함하여 완전 퇴출이 일어나는 시간으로 정의되어야 한다.[^8]

---

### 2.7 V12-class 3D NAND Wordline의 동적 AR 변화: 가장 나쁜 조건에서의 설계

앞서 언급한 모든 물리적 제약이 3D NAND wordline ALD에서는 한 가지 추가적인 복잡성과 결합된다. 바로 **증착이 진행될수록 cavity의 유효 AR이 단조적으로(monotonically) 증가**한다는 점이다.

초기 상태의 wordline cavity 폭을 w₀, 목표 금속 막 두께를 t_target이라 하면:

- n번째 cycle에서의 유효 CD: $w_n = w_0 - 2 \cdot n \cdot GPC$
- n번째 cycle에서의 유효 AR: $AR_n = L / w_n$

이 AR_n을 feeding time 스케일링 법칙에 대입하면, **같은 recipe로 증착하더라도 후기 cycle일수록 saturation에 필요한 feeding time이 더 길어야 함**을 의미한다.[^3] 만약 공정 초기의 AR을 기준으로 feeding time을 설계하면, 증착 후반부에는 step coverage가 점진적으로 저하되는 현상이 나타난다.[^3][^1]

따라서 단일 recipe로 전체 공정을 커버하려면, **feeding time과 purge time은 반드시 증착 종료 직전(AR이 최대인 시점)을 기준으로 설계**되어야 한다.[^3][^1] 이 설계 원칙은 초반 cycle에서의 과잉 dose를 허용하는 대신 전체 공정 구간에서의 step coverage 보증을 최우선 목표로 삼는다. 이 접근이 throughput(총 공정 시간)에 불리하다는 것은 명확한 trade-off이며, 이것이 현업에서 ALD recipe 개발이 단순 saturation curve 측정을 넘어 복잡한 최적화 문제가 되는 이유다.

---

### 2.8 실제 산업 사례들

#### Lam Research: ALD Tungsten for 3D NAND

Lam Research는 ALTUS 장비군에서 PNL(Pulsed Nucleation Layer) 기술을 통해 HAR lateral cavity에서 **≥90% step coverage**를 달성한다.[^9] Low-Fluorine Tungsten(LFW) ALD 공정은 CVD 대비 불소 함량 100배 감소, 응력 10배 감소, 비저항 30% 감소를 실현하였다.[^9] ICEFill 공정은 lateral wordline cavity에서 void-free fill을 목표로 설계되었으며[^9], 이는 purge 불량으로 인한 feature 상단 과잉 성장이 HAR fill에 얼마나 치명적인지를 역으로 증명하는 사례다.

#### Applied Materials: Centura™ iSprint™ SSW (Seam Suppressed Tungsten)

ALD nucleation layer(두께 12~50 Å, CVD nucleation layer 대비 두께 대폭 절감) + post-treatment step으로 feature 상단 성장을 선택적으로 억제하고 bottom-up fill을 유도하여 seam/void를 제거한다.[^7] 100–176+ layer 3D NAND wordline fill에 특화 설계된 이 시스템은 접촉저항을 CVD 대비 15% 개선하였다.[^7]

#### Mo(몰리브덴)로의 전환

200 layer 이상의 초고적층 구조에서는 WF₆ 기반 precursor의 불소 오염(dielectric으로의 F 확산 → 누설전류 증가) 문제가 부각되면서 몰리브덴(Mo)으로의 전환이 진행 중이다.[^10][^11] Mo wordline의 누설 불량률은 W 대비 약 1/100 수준으로 보고되었다.[^11] Lam Research는 2025년 2월 세계 최초 Mo ALD 양산 장비 **ALTUS® Halo**를 발표하였다.[^10] 이 장비는 불소 프리 precursor(MoO₂Cl₂)를 사용하여 F 오염을 원천 제거하고, barrier layer가 불필요하여 전체 단면이 도전성 재료로 채워지므로 wordline 저항 15~30% 감소를 실현한다.[^10] Micron(2yyL G9 세대)과 Kioxia가 3D NAND Mo ALD 공정 검증을 완료하였다.[^11]

#### PillarHall 테스트 구조

ALD conformality를 lateral HAR 구조에서 직접 정량 평가하는 방법으로 **PillarHall** 개념이 개발되었다.[^12][^13] 이 테스트 패턴은 AR > 1,000:1 ~ 10,000:1의 극한 종횡비를 포함한 lateral cavity 어레이로 구성되어, 단일 웨이퍼 처리 후 SEM/TEM으로 두께 프로파일을 추출한다.[^12] LHAR(lateral) 구조에서의 conformality 측정 결과가 vertical HAR 구조에서의 거동 예측에 활용될 수 있음이 확인되어 있어, 실제 device 구조를 cross-section하지 않고도 공정 최적화가 가능하다.[^12] 이를 통해 feeding time-AR 관계를 실험적으로 도출하고 Gordon-Hausmann 모델과의 정합성을 검증할 수 있다.[^3][^12]

---

## 결론

HAR 구조에서 ALD step coverage를 결정하는 물리적 메커니즘과 공정 변수 간의 인과 관계를 아래와 같이 정리해보고자 한다.

**첫째, HAR feature 내부에서의 기체 수송은 Knudsen diffusion regime으로 진입하며, 이 조건에서 step coverage의 실질적 결정 인자는 total exposure(P × t_feed)이다.** 분자 간 충돌이 아닌 분자-벽면 충돌이 지배적인 이 regime에서, 단위 시간당 precursor 공급량(flux)이 아니라 누적 dose가 adsorption front의 침투 깊이를 결정한다. 단, 침투 깊이(AR 단위)는 exposure에 선형이 아니라 **제곱근으로 비례**함에 유의해야 한다.

**둘째, Gordon-Hausmann 모델에 따라 필요 feeding time은 AR²에 비례하므로, 스택 높이 증가에 따른 AR 상승은 공정 시간에 비선형적 부담을 가한다.** HAR hole은 동일 AR의 trench 대비 4배의 exposure를 요구한다는 기하학적 비대칭성은, channel hole과 wordline cavity의 recipe를 독립적으로 최적화해야 하는 근거다.

**셋째, 3D NAND wordline과 같이 증착 중 CD가 좁아지는 동적 구조에서는, 공정 후반부의 최악 AR 조건을 기준으로 feeding time을 설계해야 step coverage를 전 구간에 걸쳐 보증할 수 있다.** 초반 cycle에서의 과잉 dose는 step coverage의 margin으로 수용해야 한다.

**넷째, purge time은 ALD의 self-limiting 특성을 보존하기 위한 필요 조건으로, 불완전 purge는 parasitic CVD → feature 상단 과잉 성장 → CD 추가 감소 → 다음 cycle의 diffusion 제한이라는 양성 피드백을 형성하여 step coverage를 사이클마다 누적적으로 악화시킨다.** HAR feature 내부 byproduct의 Knudsen diffusion에 의한 느린 탈출 속도를 고려하면, flat substrate 기준 purge time은 HAR 구조에 항상 과소 설계이다.

결론적으로, **HAR 구조에서 step coverage는 feeding time이 결정하는 "내부 침투(adsorption front penetration)의 충분성"과 purge time이 결정하는 "self-limiting 거동의 온전성"이라는 두 독립적 조건이 모두 충족될 때만 달성된다.** 이 두 변수를 분리하여 독립적으로 최적화하되, 증착 중 동적으로 변화하는 구조 geometry를 반영하여 worst-case 기준으로 설계하는 것이 HAR ALD 공정 개발의 핵심 원칙이다. V12-class 이상의 3D NAND나 수직 방향으로 극한까지 scaling되는 미래 구조에서 이 원칙의 중요성은 더욱 커질 것이다.

---

## 참고문헌

[^1]: Cremers, V.; Puurunen, R. L.; Dendooven, J. "Conformality in atomic layer deposition: Current status overview of analysis and modelling." *Appl. Phys. Rev.* **2019**, *6*, 021302. DOI: [10.1063/1.5060967](https://pubs.aip.org/aip/apr/article/6/2/021302/570185/Conformality-in-atomic-layer-deposition-Current) — EAR 개념(trench = L/2w, hole = L/w) 정의; Knudsen regime에서 total exposure (P × t)가 침투 깊이를 결정함을 이론적으로 정리; HAR feature 내부 byproduct의 느린 탈출 특성 기술.

[^2]: Puurunen, R. L. et al. "Simulated Conformality of Atomic Layer Deposition in Lateral Channels: The Impact of the Knudsen Number on the Saturation Profile Characteristics." *ChemRxiv* preprint, **2024**. DOI: [10.26434/chemrxiv-2024-83lwd](https://chemrxiv.org/doi/pdf/10.26434/chemrxiv-2024-83lwd) — Kn >> 1(free molecular flow) 조건에서 정규화된 saturation profile이 trench 높이·partial pressure에 독립적임을 시뮬레이션으로 확인; Knudsen cosine law(diffuse reflection) 설명; Kn 감소 시 penetration depth 감소 확인.

[^3]: Gordon, R. G.; Hausmann, D.; Kim, E.; Shepard, J. A. "A Kinetic Model for Step Coverage by Atomic Layer Deposition in Narrow Holes or Trenches." *Chem. Vap. Dep.* **2003**, *9*(2), 73–78. Available at: [gordon.faculty.chemistry.harvard.edu](https://gordon.faculty.chemistry.harvard.edu/file_url/102) — HAR ALD conformality의 핵심 이론 모델; hole 기준 saturation dose 식 $Pt = \rho_s\sqrt{2\pi m k_B T}(1 + 19a/4 + 3a^2/2)$ 및 고 AR 극한의 E_sat ∝ s₀⁻¹ × (EAR)² 스케일링 도출; HAR hole이 동일 AR trench 대비 4배의 exposure를 요구함을 정량적으로 제시.

[^4]: Puurunen, R. L. "Basic Insights into ALD Conformality: A Closer Look at ALD and Thin Film Conformality." *Atomiclimits.com*, Feb. 8, 2020. Available at: [atomiclimits.com](https://www.atomiclimits.com/2020/02/08/basic-insights-into-ald-conformality-a-closer-look-at-ald-and-thin-film-conformality/) — ALD self-limiting 반응과 adsorption front 형성 메커니즘 해설; CVD vs ALD의 pinch-off 거동 비교; hole/trench EAR 차이와 4배 exposure 요구량 설명.

[^5]: Choolakkal, A. H.; Mpofu, P.; Niiranen, P.; Birch, J.; Pedersen, H. "Using a Heavy Inert Diffusion Additive for Superconformal Atomic Layer Deposition." *J. Phys. Chem. Lett.* **2025**, *16*, 2453–2457. DOI: [10.1021/acs.jpclett.4c03545](https://pubs.acs.org/doi/10.1021/acs.jpclett.4c03545) — AlN ALD(TMA/NH₃) 공정에서 Kr 공동주입 시 AR 18:1 수직 trench에서 step coverage 1.0 → 1.6(superconformal)으로 향상; lateral HAR 구조에서는 침투 깊이 증가 효과 없음을 실험적으로 규명; Kr에 의한 경량 분자 확산 촉진 메커니즘은 저자들의 추정(speculation)으로 제시되며 추가 연구 필요성 명시.

[^6]: Choi, Y. K.; Holsgrove, K.; Watson, A. et al. "Effect of Precursor Purge Time on Plasma-Enhanced Atomic Layer Deposition-Prepared Ferroelectric Hf₀.₅Zr₀.₅O₂ Phase and Performance." *ACS Omega* **2025**, *10*(20), 20524–20535. DOI: [10.1021/acsomega.5c01112](https://pmc.ncbi.nlm.nih.gov/articles/PMC12120649/) — HZO PE-ALD에서 metal precursor purge time 3초 → C·N 불순물 증가로 antipolar o-I phase(공간군 Pbca) 안정화, 90초 → ferroelectric Pca2₁ 상 우세; XPS상 Hf:Zr 비율도 purge time에 따라 미세 변화(79:100 → 74:100) 관찰.

[^7]: Applied Materials. "Centura™ iSprint™ SSW ALD/CVD." *Applied Materials Product Library*. Available at: [appliedmaterials.com](https://www.appliedmaterials.com/us/en/product-library/centura-isprint-ssw-ald-cvd.html) — ALD nucleation layer(12~50 Å) + treatment step으로 feature 상단 성장 억제 및 bottom-up fill 유도; seam/void 제거; CVD 대비 접촉저항 15% 개선; 100–176+ layer 3D NAND wordline fill 특화.

[^8]: Puurunen, R. L. "ALD Process Development: 10 Steps to Successfully Develop, Optimize and Characterize ALD Recipes." *Atomiclimits.com*, Feb. 12, 2019. Available at: [atomiclimits.com](https://www.atomiclimits.com/2019/02/12/atomic-layer-deposition-process-development-10-steps-to-successfully-develop-optimize-and-characterize-ald-recipes/) — 불완전 purge → GPC 자기제한 plateau 이탈(상승) → parasitic CVD 진단 방법론 제시; HAR 구조에서 purge time 연장 필요성 기술; multi-pulse/dose segmentation 전략 소개.

[^9]: Lam Research. "ALD Tungsten Solves Capacity Challenges in 3D NAND Device Manufacturing." *Lam Research Newsroom*. Available at: [newsroom.lamresearch.com](https://newsroom.lamresearch.com/ALD-Tungsten-Solves-Capacity-Challenges-in-3D-NAND-Device-Manufacturing?blog=true) — Lam ALTUS PNL(Pulsed Nucleation Layer) 기술로 HAR lateral cavity에서 ≥90% step coverage 달성; LFW ALD: 불소 100배 감소, 응력 10배 감소, 비저항 30% 감소.

[^10]: Lam Research. "Lam Research Ushers in New Era of Semiconductor Metallization with ALTUS® Halo for Molybdenum Atomic Layer Deposition." *Lam Research Newsroom*, Feb. 19, 2025. Available at: [newsroom.lamresearch.com](https://newsroom.lamresearch.com/2025-02-19-Lam-Research-Ushers-in-New-Era-of-Semiconductor-Metallization-with-ALTUS-R-Halo-for-Molybdenum-Atomic-Layer-Deposition) — 세계 최초 Mo ALD 양산 장비 ALTUS® Halo 발표(2025.02.19); 불소 프리 precursor(MoO₂Cl₂) 사용으로 F 오염 원천 제거; barrier layer 불필요로 전체 단면 도전성 확보, wordline 저항 15~30% 감소.

[^11]: "Molybdenum: The Precursor Changing the Future of Advanced Chip Designs." *Semiconductor Digest*. Available at: [semiconductor-digest.com](https://www.semiconductor-digest.com/molybdenum-the-precursor-changing-the-future-of-advanced-chip-designs/) — Mo wordline 누설 불량률 W 대비 1/100 수준(TechInsights, Kioxia 데이터); Micron 2yyL G9 및 Kioxia에서 3D NAND Mo ALD 공정 검증 완료 보고.

[^12]: Puurunen, R. L. "Advancing Thin Film Metrology in 3D Structures: The Benefits of the PillarHall Concept." *Atomiclimits.com*, Apr. 24, 2025. Available at: [atomiclimits.com](https://www.atomiclimits.com/2025/04/24/advancing-thin-film-metrology-in-3d-structures-the-benefits-of-the-pillarhall-concept/) — PillarHall lateral HAR cavity 어레이 구조 설명; AR > 1,000~10,000:1 포함; LHAR 측정 결과의 vertical HAR 거동 예측 활용 가능성 기술.

[^13]: Chipmetrics. "ALD Bottleneck Effects in 3D Semiconductors – PillarHall." *Chipmetrics*. Available at: [chipmetrics.com](https://chipmetrics.com/ald-bottleneck-effects-3d-semiconductors-pillarhall/) — PillarHall 기반 LHAR5 상용 테스트 칩; AR별 step coverage 정량 추출 및 공정 최적화 플랫폼으로서의 활용 사례.
