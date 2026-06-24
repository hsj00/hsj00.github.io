---
title: "HAR 구조에서 Step Coverage를 지배하는 공정 파라미터: Feeding Time과 Purge Time의 물리적 근거"
layout: post
date: 2026-06-24 10:00
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
description: 2600624 `Step Coverage in High Aspect Ratio Structures: Why Feeding Time and Purge Time Matter in ALD`
category: blog
author: hsj00
externalLink: true
published: true
giscus_comments: true
share: true
use_math: true
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

ALD 공정의 전형적인 reactor 압력(수 mTorr~수 Torr)과 feature 폭(수 nm~수십 nm) 조건에서, 기체 분자의 **평균 자유 경로(mean free path, λ)**는 feature 폭 *d*와 비교 가능하거나 그보다 크다.[^1] 이를 정량화하는 지표가 **Knudsen Number(Kn)**이다:

$$Kn = \lambda / d$$

Kn > 1인 영역, 즉 **Knudsen flow regime**에서는 분자 간 충돌보다 분자와 벽면 사이의 충돌이 지배적이다.[^1][^2] 이 regime의 중요한 특성은 다음과 같다:

- **Penetration depth가 total exposure(P × t)에만 비례**하고, channel 높이나 partial pressure 단독에는 독립적이다.[^2][^3] 즉, 압력을 높이거나 공급 시간을 늘릴 경우 penetration depth가 증가하는 효과를 얻을 수 있다.
- 분자가 벽면을 따라 **cosine 분포로 반사(diffuse reflection)**되며 이동하기 때문에 intermolecular scattering 없이 feature 최심부까지 도달 가능성이 유지된다.[^2]
- 반면 continuum flow 영역에서는 feature 입구 근처에서의 농도 구배가 steep해져 내부 확산이 크게 제한된다.[^1][^2]

**이런 관점에서 ALD의 step coverage 문제는 단순히 "precursor 양이 충분한가"의 문제가 아니라, 주어진 공정 시간 내에 Knudsen diffusion을 통해 saturation front가 feature 최심부까지 도달하는가의 문제임을 알 수 있다.**

---

### 2.2 ALD Self-limiting 반응과 Adsorption Front

ALD의 본질적 강점은 각 half-cycle에서 표면 반응이 자기제한(self-limiting)된다는 점이다.[^4] Precursor 분자가 표면의 reactive site와 단층(monolayer)으로 반응하면 그 site는 비활성화되고, 이후 유입되는 분자는 더 깊이 이동하여 아직 반응하지 않은 site를 찾아 반응한다. 이 과정이 feature 최심부까지 순차적으로 진행되면서 **adsorption front**가 형성되고, 이 front가 bottom에 도달해야만 비로소 완전한 step coverage가 달성된다.[^3]

CVD와의 결정적 차이는 여기서 나타난다. CVD는 precursor가 공급되는 한 반응이 지속되므로 feature 상단에서 급격한 막 성장이 일어나 **pinch-off**(cavity 입구 폐쇄)가 발생한다.[^4][^7] ALD는 상단이 일단 포화되면 추가 반응이 억제되므로 분자가 더 깊이 침투할 수 있다. 그러나 이 self-limiting 메커니즘이 온전히 작동하려면 **purge step에서 이전 반응의 부산물과 잔류 precursor가 완전히 제거**되어야 한다.[^8] 불완전 purge는 self-limiting 거동 자체를 훼손하고, ALD가 아닌 CVD로 반응 양상이 달라지는 결과를 낳는다.[^8]

---

### 2.3 Gordon-Hausmann 모델: 정량적 스케일링 법칙

HAR 구조에서 ALD conformality를 정량적으로 기술한 가장 영향력 있는 이론 체계는 **Gordon, Hausmann, Kim, Shepard(2003)**의 모델이다.[^3] 예전에 이 모델을 바탕으로 Streamlit calculator를 만들기도 했다. 이 모델은 Knudsen regime에서의 반응-확산 연립 방정식을 풀어 다음의 핵심 관계를 도출하였다.

**Saturation dose 스케일링:**[^3]

$$E_{sat} \propto s_0^{-1} \times (EAR)^2$$

- **E_sat**: feature 전체를 포화시키기 위해 필요한 최소 exposure (단위: Langmuir = 10⁻⁶ Torr·s)
- **s₀**: initial sticking coefficient (precursor가 표면 site에 반응할 확률)
- **EAR**: Equivalent Aspect Ratio

**Penetration depth:**[^3]

$$\lambda \approx \sqrt{2kDE / s_0}$$

여기서 D는 Knudsen diffusivity, E는 실효 exposure이다. 완전한 conformality를 위해서는 λ ≥ L(feature 깊이) 조건이 충족되어야 한다. Exposure는 $E = P \times t_{feed}$이므로, 이 조건을 feeding time으로 표현하면:[^3][^1]

$$t_{feed,min} \propto \frac{(L/w)^2}{P \times D}$$

**즉, 필요한 최소 feeding time은 aspect ratio의 제곱에 비례하고, 압력과 Knudsen diffusivity에 반비례한다.**[^3] AR이 2배 증가하면 필요한 feeding time은 이론적으로 4배 증가한다는 것이 이 모델의 핵심 예측이다.[^3]

---

### 2.4 HAR Hole vs HAR Trench: 기하학적 비대칭성

Hole과 trench는 겉보기 AR이 동일하더라도 precursor 수송 관점에서 본질적으로 다른 difficulty를 가진다. Gordon-Hausmann 모델은 이를 **Equivalent Aspect Ratio(EAR)**의 개념으로 정형화하였다.[^3][^1]

| 구조 유형 | EAR 정의 | AR=20 기준 EAR | 상대 E_sat |
|:---|:---|---:|---:|
| **Trench** (양방향 개구) | L / (2w) [^1] | 10 | 1x |
| **Hole** (단방향 개구) | L / w [^1] | 20 | **4x** |

Trench는 양쪽 열린 개구부에서 precursor가 동시에 유입되므로 실질적 확산 거리가 절반에 불과하다.[^1][^3] 반면 hole은 단일 개구부를 통해 precursor가 진입하여 bottom까지 전체 깊이를 이동해야 한다. 따라서 **동일한 AR을 가진 hole에는 trench 대비 4배의 exposure가 필요하다**는 것은 EAR의 제곱 비례 관계에서 직접 유도된다.[^1][^3]

$$E_{hole} \propto (L/w)^2 = 4 \times (L/2w)^2 = 4 \times E_{trench}$$

이 기하학적 비대칭성은 채널홀과 워드라인 공정에서 동일 재료를 증착할 때도 feeding time을 완전히 다르게 설계해야 하는 이유를 물리적으로 설명한다.[^4]

3D NAND 구조별 EAR 특성을 정리하면 다음과 같다:

- **Channel hole**: 전형적인 cylindrical hole 형태 → EAR = AR, exposure 요구 최대
- **Wordline cavity**: lateral 방향 trench 형태이나, slit을 통한 단방향 가스 진입 경로를 가지므로 실질적 EAR은 단순 trench와 hole의 중간 어딘가에 위치하며, 정밀한 분석이 필요하다.
- **Gate slit**: 수직 방향 trench로 양방향 개구 → EAR = AR/2

---

### 2.5 Precursor Feeding Time의 역할: Saturation Front가 Bottom에 도달하는가

Feeding time은 단순히 "precursor를 얼마나 오래 흘려 보내는가"의 문제가 아니다. 이것은 **adsorption front가 feature 최심부에 도달하기 위한 충분한 dose(P × t)가 공급되는가**를 결정하는 변수이다.[^3]

**Feeding time이 부족한 경우의 시나리오:**

1. Feature 상단 근처에서 saturation이 완료되지만, adsorption front가 bottom에 도달하기 전에 precursor pulse가 종료된다.
2. Bottom은 미반응 상태로 남으며 step coverage < 100%를 기록한다.
3. Top-heavy thickness profile: 상단 두껍고 하단 얇은 비균일한 막이 형성된다.
4. 3D NAND에서는 이것이 wordline별 저항 불균일로 직결되어 cell-to-cell Vth 산포를 악화시킨다.

**실제 수치 사례 (HfO₂ ALD in HAR holes):**

Gordon 그룹의 이론 모델에 따르면, 수십 nm 깊이의 HAR hole에서 완전한 step coverage를 달성하기 위해 **수천~수만 Langmuir(~10⁻³ Torr·s 수준)** 이상의 exposure가 필요하다.[^3] 이는 동일 재료의 flat surface 포화에 필요한 dose 대비 수십 배에 해당하는 값이다. 이 이론적 예측은 Gordon-Hausmann의 (EAR)² 스케일링과 일관성을 가지며, HAR 구조에서 feeding time의 극적인 연장이 불가피함을 정량적으로 뒷받침한다.[^3]

**Feeding time 증가의 대안적 방법:**

- **Partial pressure 증가**: $E = P \times t_{feed}$이므로 압력을 높이면 동일 dose를 더 짧은 시간에 달성 가능하나, 반응기 설계 제약이 있다.[^3]
- **Heavy inert gas(예: Kr) 첨가**: AlN ALD에 Kr을 공동 주입한 실험에서 AR 18:1 trench의 step coverage가 **1.0 → 1.6으로 향상**되었다.[^5] Kr(84 amu)이 반응성 기체 분자(NH₃, 17 amu)의 trench 내부 확산을 물리적으로 촉진하는 메커니즘으로, Graham's law에 기반한 분자량 차이에 의한 momentum transfer로 설명된다.[^5] 단, lateral HAR 구조에서는 deposition depth 증가 효과가 관찰되지 않아 수직 trench에 특이적인 효과임을 유의해야 한다.[^5]
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

반응 부산물이 충분히 탈출하기 전에 다음 pulse가 시작되면, 이 fragment들이 막 내에 편입되어 불순물로 남는다. **HZO 막에서 purge time을 90초에서 3초로 단축한 실험에서 ferroelectric → antiferroelectric 상변환이 관찰**되었다.[^6] 구체적으로, 3초 purge 조건에서 탄소(C) 및 질소(N) 불순물 함량이 현저히 증가하여 antipolar o-I phase(Pbca 결정계)가 안정화되었으며, 이는 공정 파라미터 단독으로 재료 조성 변경 없이 결정상 전환이 가능함을 보여준다.[^6]

**HAR 구조에서 purge time 설계의 특수성:**

HAR feature 내부의 byproduct는 Knudsen diffusion 메커니즘으로 feature에서 서서히 탈출하기 때문에, flat substrate 기준 purge time은 HAR 구조에 결코 충분하지 않다.[^1] HAR feature의 경우 flat substrate 대비 purge time을 10~50배 이상 연장해야 한다는 경험적 기준이 있다.[^8] 최적 purge time은 GPC가 자기제한적 plateau에 도달하는 최소 시간, 즉 HAR feature 내부까지 포함하여 완전 퇴출이 일어나는 시간으로 정의되어야 한다.[^8]

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

ALD nucleation layer(두께 12~50 Å, CVD nucleation layer 대비 ~300 Å 절감) + post-treatment step으로 feature 상단 성장을 선택적으로 억제하고 bottom-up fill을 유도하여 seam/void를 제거한다.[^7] 100–176+ layer 3D NAND wordline fill에 특화 설계된 이 시스템은 접촉저항을 CVD 대비 15% 개선하였다.[^7]

#### Mo(몰리브덴)로의 전환

200 layer 이상의 초고적층 구조에서는 WF₆ 기반 precursor의 불소 오염(dielectric으로의 F 확산 → 누설전류 증가) 문제가 부각되면서 몰리브덴(Mo)으로의 전환이 진행 중이다.[^10][^11] Mo wordline의 누설 불량률은 W 대비 약 1/100 수준으로 보고되었다.[^11] Lam Research는 2025년 2월 세계 최초 Mo ALD 양산 장비 **ALTUS® Halo**를 발표하였다.[^10] 이 장비는 불소 프리 precursor(MoO₂Cl₂)를 사용하여 F 오염을 원천 제거하고, barrier layer가 불필요하여 전체 단면이 도전성 재료로 채워지므로 wordline 저항 15~30% 감소를 실현한다.[^10] Micron(2yyL G9 세대)과 Kioxia가 3D NAND Mo ALD 공정 검증을 완료하였다.[^11]

#### PillarHall 테스트 구조

ALD conformality를 lateral HAR 구조에서 직접 정량 평가하는 방법으로 **PillarHall** 개념이 개발되었다.[^12][^13] 이 테스트 패턴은 AR > 1,000:1 ~ 10,000:1의 극한 종횡비를 포함한 lateral cavity 어레이로 구성되어, 단일 웨이퍼 처리 후 SEM/TEM으로 두께 프로파일을 추출한다.[^12] LHAR(lateral) 구조에서의 conformality 측정값이 vertical HAR 구조와 통계적으로 등가임이 검증되어 있어, 실제 device 구조를 cross-section하지 않고도 공정 최적화가 가능하다.[^12] 이를 통해 feeding time-AR 관계를 실험적으로 도출하고 Gordon-Hausmann 모델과의 정합성을 검증할 수 있다.[^3][^12]

---

## 결론

HAR 구조에서 ALD step coverage를 결정하는 물리적 메커니즘과 공정 변수 간의 인과 관계를 아래와 같이 정리해보고자 한다.

**첫째, HAR feature 내부에서의 기체 수송은 Knudsen diffusion regime으로 진입하며, 이 조건에서 step coverage의 실질적 결정 인자는 total exposure(P × t_feed)이다.** 분자 간 충돌이 아닌 분자-벽면 충돌이 지배적인 이 regime에서, 단위 시간당 precursor 공급량(flux)이 아니라 누적 dose가 adsorption front의 침투 깊이를 결정한다.

**둘째, Gordon-Hausmann 모델에 따라 필요 feeding time은 AR²에 비례하므로, 스택 높이 증가에 따른 AR 상승은 공정 시간에 비선형적 부담을 가한다.** HAR hole은 동일 AR의 trench 대비 4배의 exposure를 요구한다는 기하학적 비대칭성은, channel hole과 wordline cavity의 recipe를 독립적으로 최적화해야 하는 근거다.

**셋째, 3D NAND wordline과 같이 증착 중 CD가 좁아지는 동적 구조에서는, 공정 후반부의 최악 AR 조건을 기준으로 feeding time을 설계해야 step coverage를 전 구간에 걸쳐 보증할 수 있다.** 초반 cycle에서의 과잉 dose는 step coverage의 margin으로 수용해야 한다.

**넷째, purge time은 ALD의 self-limiting 특성을 보존하기 위한 필요 조건으로, 불완전 purge는 parasitic CVD → feature 상단 과잉 성장 → CD 추가 감소 → 다음 cycle의 diffusion 제한이라는 양성 피드백을 형성하여 step coverage를 사이클마다 누적적으로 악화시킨다.** HAR feature 내부 byproduct의 Knudsen diffusion에 의한 느린 탈출 속도를 고려하면, flat substrate 기준 purge time은 HAR 구조에 항상 과소 설계이다.

결론적으로, **HAR 구조에서 step coverage는 feeding time이 결정하는 "내부 침투(adsorption front penetration)의 충분성"과 purge time이 결정하는 "self-limiting 거동의 온전성"이라는 두 독립적 조건이 모두 충족될 때만 달성된다.** 이 두 변수를 분리하여 독립적으로 최적화하되, 증착 중 동적으로 변화하는 구조 geometry를 반영하여 worst-case 기준으로 설계하는 것이 HAR ALD 공정 개발의 핵심 원칙이다. V12-class 이상의 3D NAND나 수직 방향으로 극한까지 scaling되는 미래 구조에서 이 원칙의 중요성은 더욱 커질 것이다.

---

## 참고문헌

[^1]: Cremers, V.; Puurunen, R. L.; Dendooven, J. "Conformality in atomic layer deposition: Current status overview of analysis and modelling." *Appl. Phys. Rev.* **2019**, *6*, 021302. DOI: [10.1063/1.5060967](https://pubs.aip.org/aip/apr/article/6/2/021302/570185/Conformality-in-atomic-layer-deposition-Current) — EAR 개념(trench = L/2w, hole = L/w) 정의; Knudsen regime에서 total exposure (P × t)가 침투 깊이를 결정함을 이론적으로 정리; HAR feature 내부 byproduct의 느린 탈출 특성 기술.

[^2]: Puurunen, R. L. et al. "Simulated Conformality of Atomic Layer Deposition in Lateral Channels: The Impact of the Knudsen Number on the Saturation Profile Characteristics." *ChemRxiv* preprint, **2024**. DOI: [10.26434/chemrxiv-2024-83lwd](https://chemrxiv.org/doi/pdf/10.26434/chemrxiv-2024-83lwd) — Kn >> 1(free molecular flow) 조건에서 saturation profile이 trench 높이·partial pressure에 독립적임을 시뮬레이션으로 확인; Knudsen cosine law(diffuse reflection) 설명; Kn 감소 시 penetration depth 감소 확인.

[^3]: Gordon, R. G.; Hausmann, D.; Kim, E.; Shepard, J. A. "A Kinetic Model for Step Coverage by Atomic Layer Deposition in Narrow Holes or Trenches." *Chem. Vap. Dep.* **2003**, *9*(2), 73–78. Available at: [gordon.faculty.chemistry.harvard.edu](https://gordon.faculty.chemistry.harvard.edu/file_url/102) — HAR ALD conformality의 핵심 이론 모델; E_sat ∝ s₀⁻¹ × (EAR)² 스케일링 법칙 도출; HAR hole이 동일 AR trench 대비 4배의 exposure를 요구함을 정량적으로 제시.

[^4]: Puurunen, R. L. "Basic Insights into ALD Conformality: A Closer Look at ALD and Thin Film Conformality." *Atomiclimits.com*, Feb. 8, 2020. Available at: [atomiclimits.com](https://www.atomiclimits.com/2020/02/08/basic-insights-into-ald-conformality-a-closer-look-at-ald-and-thin-film-conformality/) — ALD self-limiting 반응과 adsorption front 형성 메커니즘 해설; CVD vs ALD의 pinch-off 거동 비교; hole/trench EAR 차이와 4배 exposure 요구량 설명.

[^5]: Kim, M. S. et al. "Superconformal Atomic Layer Deposition of AlN with Krypton Coflow." *PMC/Peer-reviewed*, **2025**. PMC Accession: [PMC11891899](https://pmc.ncbi.nlm.nih.gov/articles/PMC11891899/) — AlN ALD 공정에서 Kr 공동주입 시 AR 18:1 수직 trench에서 step coverage 1.0 → 1.6으로 향상; lateral HAR 구조에서는 효과 없음을 실험적으로 규명.

[^6]: Choi, Y. K. et al. "Effect of Precursor Purge Time on Plasma-Enhanced Atomic Layer Deposition-Prepared Ferroelectric Hf₀.₅Zr₀.₅O₂ Phase and Performance." *ACS Omega* **2025**, *10*(20), 20524–20535. PMC Accession: [PMC12120649](https://pmc.ncbi.nlm.nih.gov/articles/PMC12120649/) — HZO PE-ALD에서 purge time 3초 → antiferroelectric, 90초 → ferroelectric으로 전환; 단축 purge time이 C, N 불순물 증가를 유발하여 antipolar o-I phase(Pbca) 안정화로 이어짐.

[^7]: Applied Materials. "Centura™ iSprint™ SSW ALD/CVD." *Applied Materials Product Library*. Available at: [appliedmaterials.com](https://www.appliedmaterials.com/us/en/product-library/centura-isprint-ssw-ald-cvd.html) — ALD nucleation layer(12~50 Å) + treatment step으로 feature 상단 성장 억제 및 bottom-up fill 유도; seam/void 제거; CVD 대비 접촉저항 15% 개선; 100–176+ layer 3D NAND wordline fill 특화.

[^8]: Puurunen, R. L. "ALD Process Development: 10 Steps to Successfully Develop, Optimize and Characterize ALD Recipes." *Atomiclimits.com*, Feb. 12, 2019. Available at: [atomiclimits.com](https://www.atomiclimits.com/2019/02/12/atomic-layer-deposition-process-development-10-steps-to-successfully-develop-optimize-and-characterize-ald-recipes/) — 불완전 purge → GPC 자기제한 plateau 이탈(상승) → parasitic CVD 진단 방법론 제시; HAR에서 purge time을 flat substrate 대비 10~50배 이상 연장 필요성 기술; multi-pulse/dose segmentation 전략 소개.

[^9]: Lam Research. "ALD Tungsten Solves Capacity Challenges in 3D NAND Device Manufacturing." *Lam Research Newsroom*. Available at: [newsroom.lamresearch.com](https://newsroom.lamresearch.com/ALD-Tungsten-Solves-Capacity-Challenges-in-3D-NAND-Device-Manufacturing?blog=true) — Lam ALTUS PNL(Pulsed Nucleation Layer) 기술로 HAR lateral cavity에서 ≥90% step coverage 달성; LFW ALD: 불소 100배 감소, 응력 10배 감소, 비저항 30% 감소.

[^10]: Lam Research. "Lam Research Ushers in New Era of Semiconductor Metallization with ALTUS® Halo for Molybdenum Atomic Layer Deposition." *Lam Research Newsroom*, Feb. 19, 2025. Available at: [newsroom.lamresearch.com](https://newsroom.lamresearch.com/2025-02-19-Lam-Research-Ushers-in-New-Era-of-Semiconductor-Metallization-with-ALTUS-R-Halo-for-Molybdenum-Atomic-Layer-Deposition) — 세계 최초 Mo ALD 양산 장비 ALTUS® Halo 발표(2025.02.19); 불소 프리 precursor(MoO₂Cl₂) 사용으로 F 오염 원천 제거; barrier layer 불필요로 전체 단면 도전성 확보, wordline 저항 15~30% 감소.

[^11]: "Molybdenum: The Precursor Changing the Future of Advanced Chip Designs." *Semiconductor Digest*. Available at: [semiconductor-digest.com](https://www.semiconductor-digest.com/molybdenum-the-precursor-changing-the-future-of-advanced-chip-designs/) — Mo wordline 누설 불량률 W 대비 1/100 수준(TechInsights, Kioxia 데이터); Micron 2yyL G9 및 Kioxia에서 3D NAND Mo ALD 공정 검증 완료 보고.

[^12]: Puurunen, R. L. "Advancing Thin Film Metrology in 3D Structures: The Benefits of the PillarHall Concept." *Atomiclimits.com*, Apr. 24, 2025. Available at: [atomiclimits.com](https://www.atomiclimits.com/2025/04/24/advancing-thin-film-metrology-in-3d-structures-the-benefits-of-the-pillarhall-concept/) — PillarHall lateral HAR cavity 어레이 구조 설명; AR > 1,000~10,000:1 포함; LHAR 측정값이 vertical HAR 구조와 통계적으로 등가임을 검증.

[^13]: Chipmetrics. "ALD Bottleneck Effects in 3D Semiconductors – PillarHall." *Chipmetrics*. Available at: [chipmetrics.com](https://chipmetrics.com/ald-bottleneck-effects-3d-semiconductors-pillarhall/) — PillarHall 기반 LHAR5 상용 테스트 칩; AR별 step coverage 정량 추출 및 공정 최적화 플랫폼으로서의 활용 사례.
