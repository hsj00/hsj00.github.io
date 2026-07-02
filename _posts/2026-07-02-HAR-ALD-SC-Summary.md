---
title: "HAR structure에서의 ALD step coverage - Process parameter와 mechanism"
layout: post
date: 2026-07-02 10:00 +0900
tags:
   - ALD
   - Atomic Layer Deposition
   - Metal ALD
   - Step coverage
   - HAR
   - Chemical Kinetics
   - Study
   - Note
description: 260702 `ALD Step Coverage - Process parameter & Mechanism`
categories: blog
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

기존에 감각적으로 알고 있었던 내용들을 좀 더 명확하게 정리하기 위해서 관련 논문들을 추려서 AI를 활용해 내용을 정리했다. 요즘 내 최대 관심사가 HAR 구조에서의 ALD여서 그런지 step coverage를 개선하기 위해서 계속 이것저것 찾아보게 된다. 3D NAND W/L과 같은 HAR 구조에서의 ALD 공정 조건을 잡으려면 어떤 점들을 고려해야하는지, 물리적 한계는 어디까지인지 알기 위해서 계속 공부해야할 것 같다. 나중에 공부할 때 참고하기 위해서 포스팅으로 남겨둔다. ToC는 위와 같다.

---

# HAR structure에서의 ALD step coverage - 3D NAND W/L을 목표로

깊고 좁은 구조 위에 두께가 고른 박막을 올리는 것은 ALD로 가장 잘할 수 있는 일이면서, 동시에 가장 어려운 일이기도 하다. 여기서 얼마나 두께가 고르게 올랐는지를 재는 지표가 step coverage다. 구조 위쪽(입구)에 쌓인 두께에 대해 아래쪽(바닥)에 쌓인 두께가 몇 %인지를 보는 값으로, 100%에 가까울수록 위아래가 똑같이 덮였다는 뜻이다.

이 글은 High Aspect Ratio(HAR) 구조, 즉 폭에 비해 깊이가 아주 깊은 홀이나 트렌치를 대상으로 한다. thermal ALD(oxide, nitride, metal)에서 step coverage가 왜 나빠지는지를 확산(diffusion), 반응 속도론(kinetics), 핵생성(nucleation), 반응 부산물 네 가지 축으로 나눠서 보고자 한다.[^cremers] 특히 metal ALD가 왜 유독 까다로운지, 그리고 nm 스케일에서 자주 잘못 이해되는 "압력과 확산 체계"의 관계를 숫자로 확인해보고자 한다.

핵심 메시지를 먼저 한 줄로 요약하면 이렇다. **step coverage가 나쁠 때는 "precursor가 바닥까지 못 온 것"인지 "왔는데 반응이 안 끝난 것"인지부터 가려야 하고, 이 둘은 해결책이 완전히 다르다.**

---

## 1. Step Coverage를 떨어뜨리는 두 가지 근본 원인

개선의 출발점은 병목이 어디인지 구분하는 것이다. 크게 두 갈래로 나뉜다.[^cremers]

### 1.1 물질 전달 제한 (Mass Transport / Diffusion Limited) - "도달"의 문제

precursor나 reactant가 구조 바닥까지 아예 **도착하지 못하는** 경우다. 반응이 느린 게 아니라, 반응에 필요한 재료가 아직 안 온 것이다. 이때 속도를 결정하는 단계 RLS(rate-limiting step)는 확산이다.

좁은 구조 안에서는 분자의 평균자유행로 λ(다른 분자와 부딪히지 않고 날아가는 평균 거리)가 구조 직경 d보다 크다. 이런 조건에서는 분자가 벽에만 부딪히며 튕겨 들어가는 Knudsen 확산이 지배한다.

해결은 단순하다. **노출(pulse 시간)을 늘리면** 바닥까지 도달할 시간을 벌 수 있어 바로 개선된다.

### 1.2 반응 속도론 제한 (Reaction Kinetics Limited) - "반응"의 문제

반응에 필요한 재료는 표면에 도착했는데, **표면 반응 자체가 느린** 경우다. 대표적인 예가 H₂로 금속을 환원하는 thermal metal ALD다. 이때 속도를 결정하는 단계는 확산이 아니라 surface reaction이다.

해결 방향이 1.1과 다르다. 반응이 느린 게 문제이므로, 온도를 올리거나 반응성이 더 좋은 reactant로 바꾸는 쪽이 효과적이다.

물론 sticking probability(표면에 도달한 분자가 실제로 반응할 확률)가 0만 아니라면, 노출을 아주 길게 늘려서 느린 반응을 억지로 보상할 수는 있다. 다만 sticking probability가 낮을수록 포화에 필요한 노출량이 급격히 커져 비현실적이 된다. 그래서 실제 ALD 공정에서는 pulse를 무한정 늘리는 것보다 온도를 올리는 편이 훨씬 낫다.[^cremers]

정리하면, 두 원인은 증상이 비슷해 보여도(둘 다 바닥에서의 두께가 얇다) 처방이 반대다. 그래서 뒤에서 다룰 saturation curve로 어느 쪽인지 먼저 판별하는 것이 중요하다.

---

## 2. Pulse / Purge 시간이 Step Coverage에 미치는 영향

### 2.1 Pulse 시간 - precursor가 표면을 다 덮었는가(포화)

HAR 구조 안에서 precursor 분자는 Knudsen 확산으로 바닥까지 흘러 들어간다. 여기서 ALD의 가장 큰 장점이 등장한다. ALD 반응은 자기제한(self-limiting)이라, 표면이 한 겹 덮이면 더는 반응하지 않는다. 따라서 **표면만 완전히 포화시키면 이상적인 step coverage가 나온다.** 문제는 그 포화에 시간이 걸린다는 점이다.

| Pulse 시간 | 결과 |
|-----------|------|
| 너무 짧음 | 위쪽만 겨우 포화되고 아래쪽은 precursor가 부족 → step coverage 나쁨 |
| 충분함 | 위아래 모두 포화, 자기제한 반응 완결 → step coverage 최대 |
| 과도하게 김 | 포화 이후에는 아무 변화 없음(self-limiting이라 더 안 쌓임) → 시간 낭비 |

실제 ALD 공정에서는 pulse 시간을 바꿔가며 GPC(Growth Per Cycle, cycle당 두께)를 재서 saturation curve를 그린다. GPC가 더 이상 안 올라가고 평평해지는(plateau) 최소 시간을 찾고, 거기에 안전 마진을 더해 조건을 잡는다. 이 조건을 이론적으로 정량화한 것이 Gordon 모델로, 깊은 홀을 완전히 덮으려면 (1) 최소한의 vapor 공급량과 (2) 입구에서의 최소 "분압 × 노출시간(P·t)" 곱이 필요하다는 두 조건을 제시한다.[^gordon] 수직 홀이 아니라 옆으로 긴 lateral HAR 테스트 구조에 대해서는 Ylilammi 등의 확장 모델이 잘 정리되어 있다.[^ylilammi]

### 2.2 Purge 시간 - 다음 반응물과 미리 섞이지 않게

purge는 그냥 가스를 밀어내는 청소 단계가 아니다. ALD의 자기제한 특성을 지키는 핵심 단계다. purge가 부족해 이전 precursor나 부산물이 남아 있으면, 다음 reactant가 들어올 때 표면이 아니라 기체 상태에서 둘이 반응해버린다. 이렇게 되면 ALD가 아니라 CVD처럼 마구 쌓이고(CVD-mode), step coverage가 급격히 나빠진다.

| Purge 시간 | 결과 |
|-----------|------|
| 너무 짧음 | 잔류 precursor·부산물 + 다음 reactant → 기상 반응(CVD mode) → step coverage 악화 |
| 충분함 | 자기제한 유지 → 고른 conformal 증착 |
| 과도하게 김 | step coverage는 그대로인데 throughput만 감소 |

특히 좁은 HAR 안쪽은 잔류 가스가 잘 빠져나가지 못하고 갇히기 쉽다. 그래서 평탄한 기판보다 더 긴 purge가 필요하다.

### 2.3 그 밖에 챙길 파라미터

| 파라미터 | Step Coverage에 미치는 영향 |
|----------|--------------------------|
| 종횡비 (Aspect Ratio) | 높을수록(깊고 좁을수록) 더 긴 pulse/purge 필요 |
| 공정 온도 | 높으면 확산은 빨라지나 precursor 분해 위험 |
| 공정 압력 | 어느 스케일을 보느냐에 따라 영향이 다름 (2.4 참조) |
| Precursor 분자 크기 | 크고 무거운 분자일수록 확산이 느려 더 긴 pulse 필요 |

여기서 압력 이야기는 자주 오해를 산다. "압력을 올리면 λ가 줄고, Knudsen에서 viscous 유동으로 넘어가서 HAR 안쪽 확산이 불리해진다"는 설명을 흔히 볼 수 있었다. 이 말은 챔버나 배관처럼 cm 스케일의 큰 공간에서는 맞지만 nm 스케일의 feature **안쪽**에서는 현실적인 공정 압력으로 유동 체계가 바뀌지 않는다. 왜 그런지 다음에서 숫자로 확인한다.

### 2.4 Knudsen 체계와 압력 - 숫자로 확인하기

먼저 두 가지 양을 정의한다. 평균자유행로 λ는 분자가 다른 분자와 부딪히기 전까지 날아가는 평균 거리이고, Knudsen 수 Kn은 그 λ를 구조 직경으로 나눈 값이다.

$$
\lambda = \frac{k_B T}{\sqrt{2}\,\pi d_m^2 P}, \qquad
\mathrm{Kn} = \frac{\lambda}{d_{\text{feature}}}
$$

Kn의 의미는 직관적이다. Kn이 크면 분자가 서로 부딪히기보다 벽에 먼저 부딪힌다는 뜻이고(= Knudsen), Kn이 작으면 분자끼리 자주 부딪히며 흐른다는 뜻이다(= viscous). 경계는 대략 다음과 같다.[^vacuum]

| Kn 범위 | 유동 체계 |
|---------|----------|
| Kn < 0.01 | Viscous / Continuum(연속체) |
| 0.01 ~ 0.1 | Slip flow |
| 0.1 ~ 10 | Transition(중간) |
| Kn > 10 | Free molecular (Knudsen) |

문헌마다 분류 단계와 경계값이 조금씩 다르다(예: 진공공학에서는 viscous/transition/molecular 3단계 분류도 흔하다). 여기서는 희박기체역학 관례의 4단계를 따르되, 보수적으로 Kn > 10을 완전한 free molecular로 본다.

전형적인 ALD 조건(약 300 °C, T ≈ 573 K)에서 압력에 따라 λ가 어떻게 변하는지 보자.

| 압력 (Torr) | λ (N₂) | λ (H₂) | λ (bulky precursor, d≈6 Å) |
|------------|--------|--------|-----------------------------|
| 0.1 | ~976 μm | ~1,599 μm | ~371 μm |
| 1 | ~98 μm | ~160 μm | ~37 μm |
| 10 | ~9.8 μm | ~16 μm | ~3.7 μm |
| 100 | ~0.98 μm | ~1.6 μm | ~0.37 μm |
| 760 | ~0.13 μm | ~0.21 μm | ~0.05 μm |

여기서 눈여겨볼 점은, 일반적인 ALD 압력(약 1 Torr)에서도 λ가 수십~수백 μm라는 것이다. nm 스케일 feature보다 서너 자릿수나 크다. 즉 분자 입장에서 nm 홀 안은 "부딪힐 상대가 거의 없는" 공간이다.

그리고 결정적인 사실 하나. **전환 압력은 절대적인 값이 아니라 구조 크기에 반비례한다.** 같은 압력이라도 d가 작으면 Kn이 커지기 때문에, "Knudsen에서 viscous로 바뀌는 압력"은 어떤 크기를 두고 하는 말인지 밝히지 않으면 의미가 없다.

- 챔버·배관 스케일(d ~ cm)에서는 대략 1 Torr 이상이면 viscous, 1 ~ 10⁻³ Torr가 transition, 10⁻³ Torr 이하가 free molecular다.
- 반면 step coverage를 실제로 좌우하는 feature 스케일(d ~ nm)에서는 이야기가 완전히 달라진다.

50 nm 홀을 기준으로, 각 체계에 도달하려면 압력이 얼마나 필요한지 거꾸로 계산해 보자.

| 목표 Kn | 필요 압력 (50 nm) | 의미 |
|---------|------------------|------|
| Kn = 10 | ~195 Torr | 여기까지도 여전히 Knudsen |
| Kn = 1 | ~2×10³ Torr | transition 한가운데 |
| Kn = 0.1 | ~2×10⁴ Torr | 겨우 slip flow 진입 |
| Kn = 0.01 | ~2×10⁵ Torr (≈260 atm) | 그제서야 viscous |

viscous로 넘어가려면 수백 기압이 필요하다는 뜻이다. ALD 공정에서는 있을 수 없는 압력이다.

반대로, 현실적인 ALD 압력(0.1–10 Torr)에서 feature 안쪽의 실제 Kn을 계산하면 이렇다.

| Feature 직경 | Kn (1 Torr, N₂, 573 K) | 체계 |
|-------------|------------------------|------|
| 10 nm | ~9,800 | 압도적 free molecular |
| 50 nm | ~1,950 | 압도적 free molecular |
| 100 nm | ~980 | 압도적 free molecular |
| 150 nm | ~650 | 압도적 free molecular |

결론은 분명하다. **현재 반도체 nm 스케일 HAR 구조에서는 가스를 아무리 많이 넣어도 feature 안쪽은 항상 Knudsen(free molecular)이다.** 유동 체계가 바뀔 일은 없다.

이 사실이 압력에 대한 직관을 바로잡아 준다. Knudsen 확산계수는 $$D_K \approx \tfrac{d}{3}\bar{v}$$로, **압력과 무관하다.** 확산을 지배하는 것이 분자–분자 충돌이 아니라 분자–벽 충돌이기 때문이다. 그래서 바닥으로 향하는 flux는 입구 분압에 비례하고(정확히는 노출 P·t에 비례), Knudsen이 유지되는 한 분압을 올리는 것은 오히려 침투에 **유리하게** 작용한다.[^gordon] 과량 공급이 나쁘게 작용하는 진짜 이유는 확산 체계가 바뀌어서가 아니라 화학·kinetics 쪽 부작용 때문인데, 이건 6.4에서 다룬다.

---

## 3. Thermal Metal ALD(H₂ 환원)가 유독 까다로운 이유

oxide ALD와 달리, H₂로 금속을 환원하는 metal ALD에는 반응 속도론 제한이 한 층 더 얹힌다.[^cremers]

### 3.1 병목이 하나 더 있다

oxide ALD의 병목은 (1) precursor 확산과 (2) 표면 흡착 반응 정도다. metal ALD(H₂)는 여기에 (3) H₂ 환원 반응 속도라는 병목이 추가된다.

```
Oxide ALD 병목: Metal ALD (H₂) 병목:

[Precursor 확산] [Precursor 확산]
+ +
[표면 흡착 반응] [표면 흡착 반응]
+
[H₂ 환원 반응 속도] ← 추가 병목
```

이 세 번째 병목이 metal ALD의 step coverage를 나쁘게 만드는 주범이다.

### 3.2 H₂가 반응물로서 약한 이유

H₂는 반응물치고 반응성이 낮다. 다른 산화·질화 반응물과 비교하면 차이가 뚜렷하다.

| 항목 | H₂ (Metal ALD) | O₃/NH₃ (Oxide/Nitride ALD) |
|------|---------------|---------------------------|
| 분자 반응성 | 낮음 (비극성, H-H 결합이 강함) | 높음 (극성이거나 산화력이 강함) |
| 활성화 에너지 | 높음 | 낮음 |
| 표면에서 쪼개져야 하나 | 필수 (dissociative chemisorption) | 상대적으로 쉬움 |
| HAR 안에서 반응 완결 | 어려움 | 비교적 쉬움 |

핵심은 H₂가 표면에서 반응하려면 먼저 두 개의 H로 쪼개져야 하는데(dissociative chemisorption), 이 쪼개는 과정 자체가 어렵다는 점이다.

### 3.3 환원이 덜 되면 연쇄적으로 문제가 생긴다

H₂ pulse가 부족하거나 반응이 느리면, precursor의 리간드(F, Cl, Cp 등)가 표면에 다 떨어지지 않고 남는다. 그러면 두 가지가 동시에 나빠진다. 하나는 그 잔류 원소가 그대로 불순물이 되는 것이고(F, Cl, C 오염), 다른 하나는 리간드가 표면을 덮고 있어 다음 cycle의 nucleation을 방해하는 것이다. 결과적으로 GPC가 떨어지고, 바닥으로 갈수록 두께가 얇아지는 기울기가 생긴다.

```
H₂ pulse 불충분 또는 kinetics 제한
↓
리간드가 덜 떨어짐 (F, Cl, Cp 잔류)
↓
┌─────────────────────────────────┐
│ 불순물 증가 다음 Cycle │
│ (F, Cl, C) + nucleation │
│ 막 품질 저하 방해 │
└─────────────────────────────────┘
↓
GPC 감소 + step coverage 기울기
```

### 3.4 부산물이 남기는 위험

환원 반응에서 나오는 부산물도 종류에 따라 위험도가 다르다.

| Precursor | H₂ 환원 부산물 | 위험성 |
|-----------|-------------|--------|
| WF₆ | HF | 하지 산화막(SiO₂ 등)·계면 공격, F 잔류 오염, adhesion 저하 (금속 W 자체는 HF에 강함) |
| WCl₅, MoCl₅ | HCl | Cl 잔류 오염; 국부적으로 아주 진하게 갇히면 MoClₓ 휘발 역반응 가능성 (단, 증착 조건에서 역반응은 열역학적으로 불리) |
| CoCp₂, RuCp₂ | CpH (사이클로펜타디엔) | 비교적 안정, 다만 탄소 오염 가능 |

여기서 한 가지 오해를 짚어둔다. 할로겐 부산물(HF·HCl)이 HAR 안에 남았을 때 걱정거리는 "이미 쌓인 금속막을 직접 녹이는 것"이 아니다. 실제 주된 위험은 **하지막·계면을 공격하는 것과 할로겐이 오염원으로 남는 것**이다. 예를 들어 HF는 금속 W보다 아래에 깔린 SiO₂와 계면을 먼저 공격해 adhesion을 떨어뜨리고 F 오염을 남긴다. HCl은 Cl 오염원으로 작용하고, 국부적으로 아주 진하게 갇히면 금속 클로라이드가 다시 휘발하는 역반응이 이론적으로 가능하다. 다만 증착이 진행되는 조건에서는 역반응이 열역학적으로 불리하므로 "조건부 위험" 정도로 보는 것이 정확하다.

또 하나 중요한 단서. 위 표의 WF₆ + H₂ 조합은 메커니즘 설명용 예시로 읽는 게 좋다. 실제 thermal W ALD의 표준 환원제는 순수 H₂가 아니라 SiH₄·Si₂H₆·B₂H₆ 계열이며,[^klaus][^elam] 순수 H₂ 환원은 반응성이 낮아 매우 높은 온도를 요구하는 것으로 알려져 있다. 따라서 이 글의 "H₂ 환원" 논의는 일반 원리로 읽되, Mo 계열 공정(MoO₂Cl₂·MoCl₅ + H₂ 또는 NH₃)에 적용할 때는 환원제 선택과 그에 따른 부산물(HCl 등)을 따로 고려해야 한다.

### 3.5 Incubation Period - 시작이 늦는 문제

metal ALD는 oxide·nitride ALD보다 핵생성이 시작되기까지 걸리는 지연(incubation period)이 길다. 특히 산화물 기판 위에서 금속 핵생성이 늦다. 그 결과 구조 바닥은 위쪽보다 한참 늦게 성장을 시작한다.

```
Metal ALD (H₂) 두께 vs. Cycle:
← 상부 (nucleation 빠름)
두께 ▁▂▄▆████
___▁▂▄▆█ ← 중부
______▁▂ ← 하부 (incubation 지연)
└────────────────────▶ Cycle 수
```

이 지연은 pulse/purge를 아무리 잘 잡아도 사라지지 않는다. 근본 해법은 표면 전처리(pre-treatment)나 seed layer다.

---

## 4. Nitride Seed Layer가 Metal ALD를 돕는 이유

### 4.1 반응물의 반응성부터 다르다

metal ALD의 H₂와 nitride ALD의 NH₃는 반응성이 크게 차이 난다.

| 항목 | H₂ (Metal ALD) | NH₃ (Nitride ALD) |
|------|---------------|--------------------|
| 분자 반응성 | 낮음 | 높음 (N-H 결합이 많음) |
| 활성화 에너지 | 높음 | 낮음 |
| 열적 반응 완결성 | 불완전하기 쉬움 | 비교적 완전 |
| HAR 안 반응 완결 | 어려움 | 상대적으로 쉬움 |
| Rate-limiting step | Surface reaction (kinetics) | 주로 diffusion |

NH₃는 kinetics 제한이 작아서 대체로 확산만 챙기면 되는 반면, H₂는 반응 자체가 병목이라는 점이 핵심 차이다.

### 4.2 핵생성 거동 비교

```
Metal ALD (H₂): Nitride ALD (NH₃):

두께 두께
│ ▁▂▄▆████ ← 상부 │ ▁▂▄▆█████ ← 상부
│ ___▁▂▄▆█ ← 중부 │ ▁▂▄▆████ ← 중부
│ ______▁▂ ← 하부 │ ▁▂▄▆███ ← 하부
└─────────────▶ Cycle 수 └─────────────▶ Cycle 수
→ incubation period 뚜렷 → 비교적 균일한 nucleation
→ step coverage 불량 → step coverage 양호
```

### 4.3 nitride가 좋은 seed가 되는 세 가지 이유

**첫째, 표면 화학적 친화성.** 금속은 산화물 표면보다 질화물(TiN, TaN) 표면에서 훨씬 잘 nucleation된다. 구조 전체에 nitride seed를 고르게 깔아두면 위아래가 동시에 성장을 시작해 step coverage가 좋아진다.

**둘째, barrier와 seed 두 역할을 겸한다.** nitride 막은 diffusion barrier이면서 동시에 nucleation seed로도 작동한다. 그래서 metal ALD의 최대 약점인 incubation period를 줄여준다.

**셋째, 부산물이 덜 공격적이다.** NH₃ 환원 부산물(HCl, NH₄Cl 등)은 HF보다 하지막·금속막에 대한 화학적 공격성이 낮다. 다만 NH₄Cl이 고체로 석출되면 좁은 HAR을 막을 수 있다는 위험은 남는다.

### 4.4 nitride ALD에도 한계는 있다

| 조건 | Step Coverage 영향 |
|------|------------------|
| Thermal NH₃ | 비교적 양호 |
| N₂/H₂ Plasma Nitride ALD | 불량 (radical이 벽면에서 재결합해 소실됨) |
| NH₄Cl 부산물 (아주 좁은 HAR) | 고체 석출로 구조 막힘(clogging) 위험 |
| 낮은 공정 온도 | NH₃ 반응 속도 저하 → step coverage 악화 |

plasma ALD가 HAR에서 잘 안 되는 이유로 흔히 "plasma의 방향성"을 든다. 그런데 실제로 반응을 일으키는 중성 radical에는 방향성이 없다. 진짜 원인은 **radical의 표면 재결합(recombination loss)**이다. radical이 HAR 벽면에 부딪힐 때마다 일정 확률로 재결합해 사라지므로, 그 확률이 0만 아니라면 깊이 들어갈수록 radical이 살아남지 못한다. 그래서 침투 깊이가 근본적으로 제한된다.[^cremers]

### 4.5 전체 비교 요약

| 비교 항목 | Thermal Metal ALD (H₂) | Nitride ALD (Thermal NH₃) |
|----------|----------------------|--------------------------|
| Reactant 반응성 | 낮음 | 높음 |
| 반응 속도론 제한 | 크다 | 작다 |
| Incubation period | 길다 | 짧다 |
| HAR step coverage | 불량 | 비교적 양호 |
| 부산물 위험성 | 높다 (하지 공격·할로겐 오염) | 중간 (clogging 가능) |
| Seed layer 효과 | — | metal ALD nucleation 개선 |

---

## 5. H₂ 환원이 왜 가장 느린 단계(RLS, rate-limiting step)가 되는가

3.2에서 "H₂를 쪼개는 게 어렵다"고 한 부분을 조금 더 풀어본다.

### 5.1 H₂는 먼저 쪼개져야 반응한다 (Dissociative Chemisorption)

H₂는 기체 상태에서 아주 안정한 비극성 이원자 분자다. 금속 표면과 반응하려면 반드시 먼저 두 개의 H로 쪼개져야 한다.[^hammer]

```
H₂(g) → 2H*(ads)

에너지
│ ‡ ← Ea,diss (쪼개는 데 필요한 활성화 에너지)
│ ╱╲
│ ╱ ╲
│ ╱ ╲__________ 2H*(ads)
H₂(g)
└──────────────────────▶ 반응 좌표
```

H–H 결합 에너지는 436 kJ/mol로 매우 크다. 게다가 이 쪼개짐은 H₂의 σ* 궤도와 금속의 d-band가 상호작용해야 일어나기 때문에, 활성화 에너지가 표면 상태에 크게 좌우된다. 이 부분은 5.4에서 다시 본다.

### 5.2 반응 순서 (Langmuir-Hinshelwood 메커니즘)

H₂ 환원은 대체로 다음 순서를 따른다. 반응물이 모두 표면에 흡착된 뒤 서로 만나 반응하는 방식이라 Langmuir-Hinshelwood(L-H) 메커니즘이라고 부른다.

```
Step 1: H₂ 쪼개짐 (해리 흡착) H₂(g) + 2* → 2H* [Ea 높음 → 여기가 RLS]
Step 2: 표면 리간드 교환 M-L* + H* → M* + H-L* [Ea 중간]
Step 3: 부산물 탈착 H-L* → H-L(g) + * [Ea 낮음]
```

여기서 `*`는 표면의 반응 자리, `M-L*`는 표면에 붙은 metal-ligand 복합체, `H-L`은 부산물(HF, HCl, Cp-H 등)이다. 기체 H₂가 쪼개지지 않은 채 표면의 M-L*와 바로 반응하는 경로(Eley-Rideal)는 H₂의 결합이 워낙 강해 에너지적으로 불리하므로 거의 일어나지 않는다. 결국 Step 1이 전체 속도를 결정한다.

### 5.3 그래서 온도에 민감하다 (Arrhenius)

각 단계의 속도는 다음과 같이 온도에 의존한다.

$$k_i = A_i \cdot \exp\left(-\frac{E_{a,i}}{RT}\right)$$

| Step | 활성화 에너지 | 온도 의존성 |
|------|------------|-----------|
| H₂ 쪼개짐 | 높음 | 강함 |
| 리간드 교환 | 중간 | 중간 |
| 부산물 탈착 | 낮음 | 약함 |

활성화 에너지가 클수록 온도에 더 민감하다. Step 1(H₂ 쪼개짐)이 가장 큰 Ea를 갖고 있으므로, 낮은 온도에서 전체 속도는 사실상 Step 1에 의해 결정된다.

$$r_{overall} \approx r_1 \propto \exp\left(-\frac{E_{a,diss}}{RT}\right)$$

즉 온도를 조금만 올려도 이 지수 항 덕분에 속도가 크게 좋아진다. 이것이 kinetics limited일 때 온도가 가장 효과적인 이유다.

### 5.4 금속마다 H₂를 쪼개는 난이도가 다르다 (d-band center 모델)

왜 어떤 금속은 H₂를 잘 쪼개고 어떤 금속은 못 쪼갤까. Hammer-Nørskov의 d-band center 이론이 이를 설명한다. 요지는, H₂ 쪼개짐의 활성화 에너지가 금속 d-band 중심 에너지(εd)와 관계있다는 것이다.

- εd가 Fermi 준위에 가까우면, H₂ σ*와 상호작용해 만들어지는 반결합 상태가 비어 있어 쪼개기 쉽다(장벽 낮음).
- d-band가 꽉 차서 εd가 깊이 내려간 noble metal(Cu, Ag, Au)은 장벽이 높아 쪼개기 어렵다.[^hammer]

| 금속 | d-band 특성 | H₂ 쪼개짐 Ea | H₂ 환원 반응성 |
|------|-----------|-----------|-------------|
| W, Mo | d-band 넓고 부분적으로 비어 있음 | 낮음 | 비교적 양호 |
| Co, Ru | 중간 | 중간 | 조건에 따라 다름 |
| Pt, Ir | εd 높음 (d-band 부분 채움) | 낮음 | 양호하나 precursor 선택지 제한 |
| Cu, Ag, Au (noble) | d-band 꽉 참, εd 깊음 | 높음 | 불량 |
| 리간드에 덮인 표면 | d-band가 가려짐 | 매우 높음 | 문제 발생 |

여기서 실제 ALD 공정에서 가장 중요한 내용은 맨 아래다. **흡착된 리간드가 금속의 d-band를 가리면 H₂ 쪼개짐이 급격히 어려워진다.**

```
초기 사이클 (깨끗한 금속 표면): 후속 사이클 (리간드에 덮인 표면):

M M M M L L L L
↑ ↑ ↑ ↑ M M M M
d-band 노출 d-band 가려짐
H₂ 쪼개기 쉬움 H₂ 쪼개기 어려움 (Ea 증가)
```

실제 ALD 조건에서는 표면이 precursor 리간드로 덮여 있는 상태가 많으므로, 깨끗한 금속 표면일 때보다 H₂ 쪼개짐 장벽이 훨씬 높다.

### 5.5 두 가지 구체 사례

**Case 1: W ALD (WF₆ + H₂)**

| 단계 | 반응 | 특이사항 |
|------|------|---------|
| WF₆ pulse | WF₆(g) → W-Fₓ*(ads) | 빠른 자기제한 반응 |
| H₂ pulse | 2H* + W-Fₓ* → W⁰ + x·HF(g) | 느린 반응, kinetics limited |
| 부산물 | HF | 잔류 시 하지막·계면 공격, F 오염 |

F 리간드는 전기음성도가 커서 금속 표면 d-band를 크게 흔든다. 그 결과 H₂ 쪼개짐 Ea가 크게 올라간다. 환원이 덜 되면 F 불순물이 남고 GPC도 떨어진다. 환원 단계의 노출이 부족할 때 반응 미완결과 성장 저하가 나타나는 현상은 Si₂H₆ 환원제 기반 W ALD의 kinetics 연구에서도 동일하게 관찰된다.[^elam]

**Case 2: Co ALD (CoCp₂ + H₂)**

| 단계 | 반응 | 특이사항 |
|------|------|---------|
| CoCp₂ pulse | CoCp₂(g) → Co-Cp*(ads) | 흡착 비교적 쉬움 |
| H₂ pulse | 2H* + Co-Cp* → Co⁰ + Cp-H(g) | Cp 제거가 RLS |
| 부산물 | Cp-H (사이클로펜타디엔) | 탄소 오염 가능 |

Cp 리간드는 크고 부피가 있어 하나 떼는 데 H*가 여러 개 순차적으로 필요하다. HAR 바닥은 H* 농도가 낮아 반응 완결이 더 어렵고, 그래서 탄소 불순물이 깊이 방향으로 기울기를 갖고 분포한다.

### 5.6 HAR 안에서 H*가 아래로 갈수록 줄어드는 이유

```
HAR 구조 단면
┌──┐ ┌──┐
│ │ │ │ 표면 H* 농도: 높음 → 반응 완결: ✓
│ │ │ │
│ │ │ │ 표면 H* 농도: 중간 → 반응 완결: △
│ │ │ │
│ │ │ │ 표면 H* 농도: 낮음 → 반응 완결: ✗
│ │ │ │ ↑ Kinetics 제한 구간
└──┘ └──┘
```

H*가 아래에서 낮아지는 데는 세 가지가 겹친다.

첫째, H₂ 자체는 확산이 빠르지만, 그 H₂를 쪼갤 활성 자리가 바닥에는 부족하다. 둘째, 위쪽 표면이 기체 H₂를 먼저 소모하기 때문에 바닥에 도달하는 H₂ flux가 줄어든다. 여기서 주의할 점은, H*는 표면에 붙어 있는 흡착종이라 그 자체가 바닥으로 이동하는 것이 아니라는 것이다. 셋째, 리간드로 덮인 표면은 쪼개짐 Ea가 높아 그 자리에서도 쪼개는 속도가 느리다.

---

## 6. H₂를 많이 넣으면 좋아질까 - 한계와 부작용

### 6.1 이론적으로 보면 (Langmuir-Hinshelwood 속도식)

H₂는 쪼개져 흡착하므로 인접한 자리 두 개가 필요하다.

$$H_2(g) + 2^* \rightleftharpoons 2H^*$$

이때 표면을 덮은 H*의 비율(커버리지)은 dissociative Langmuir 등온선을 따른다.

$$\theta_{H^*} = \frac{\sqrt{K_{H_2} \cdot P_{H_2}}}{1 + \sqrt{K_{H_2} \cdot P_{H_2}}}$$

그리고 전체 반응 속도는 다음과 같다.

$$r = k \cdot \frac{\sqrt{K \cdot P_{H_2}}}{1 + \sqrt{K \cdot P_{H_2}}} \cdot \theta_{M-L^*}$$

수식이 복잡해 보여도 읽는 법은 간단하다. 분압 P가 낮을 때는 θ가 P에 따라 올라가지만, P가 커지면 θ가 1에 가까워지며 더는 안 올라간다(포화). 즉 표면을 다 덮고 나면 H₂를 더 넣어도 소용이 없다.

### 6.2 분압을 올릴 때 속도가 어떻게 변하나

| H₂ 분압 구간 | 속도 의존성 | 실제 의미 |
|------------|-----------|---------|
| 저압 (K·P ≪ 1) | r ∝ P_H2^(1/2) | H₂ 증량이 속도에 직접 도움 |
| 중압 | 증가하나 체감 | 수율 감소 구간 |
| 고압 (K·P ≫ 1) | r → k·θ_M-L* (상수) | P_H2와 무관, 완전 포화 |

숫자로 보면 한계가 뚜렷하다. 기준(1x)을 $$\sqrt{K \cdot P_{H_2}} = 1$$, 즉 θ = 0.50인 상태로 두고 증량해 보자.

| H₂ 증량 배수 | θ_H* | 속도 향상 (기준 대비) |
|------------|------|------------|
| 1x (기준) | 0.50 | — |
| 100x | 0.91 | +82% |
| 1000x | 0.97 | +94% (100x 대비 상대적으로 ~7% 추가) |

H₂를 100배에서 다시 10배 더(1000배) 늘려도 추가 향상은 몇 %p에 그친다. 이 정도 이득은 온도를 20~30 °C 올려서 얻는 효과에도 못 미치는 경우가 많다.

한 가지 구분해 둘 것이 있다. 여기서 말하는 "고압"은 **H₂ 분압(= 표면 포화)**의 축이지, 앞 2.4에서 다룬 **확산 체계(Knudsen/viscous)**의 축이 아니다. 분압을 아무리 올려도 nm feature 안쪽은 여전히 Knudsen이므로, 분압 증가가 한계에 부딪히는 이유는 확산 체계 전환이 아니라 Langmuir 포화 때문이다.

### 6.3 왜 H₂만으로는 근본 한계를 못 넘나

$$k_{diss} = A \cdot \exp\left(-\frac{E_{a,diss}}{RT}\right)$$

분압을 높이면 표면에 부딪히는 H₂ flux가 늘어 흡착 속도가 부분적으로 좋아진다. 하지만 활성화 에너지 Ea,diss 자체는 그대로다. 압력은 속도식의 flux(분압) 항으로만 들어오고, 지수 항은 오직 온도에만 의존하기 때문이다. 결국 표면 θ_H*는 어떤 수렴값에 접근하고 만다.

```
압력 효과: r ∝ P^(1/2) → 포화로 수렴 (Langmuir 한계)
온도 효과: r ∝ exp(-Ea/RT) → 지수적 향상 (훨씬 효과적)
```

### 6.4 오히려 H₂를 과하게 넣으면 생기는 부작용

앞에서 확인했듯, 과량 공급이 step coverage에 불리하게 작용하는 진짜 원인은 확산 체계 전환이 아니라 다음의 화학·kinetics 부작용이다.

**H* 재결합(recombination) 증가.** θ_H*가 높아질수록 인접한 H*끼리 다시 결합해 기체 H₂로 떨어져 나가는 속도도 커진다.

$$H^* + H^* \rightarrow H_2(g) + 2^*$$

결국 유효 H* 농도가 스스로 억제되는(self-quenching) 셈이다.

**기상 반응(CVD-mode)과 purge 부담.** 과량의 reactant나 precursor가 챔버와 feature 안에 남으면 다음 pulse와 기체 상태에서 반응할 위험이 커지고, 이를 막으려 purge를 더 길게 해야 한다. 특히 좁은 HAR 안쪽은 부산물(HF·HCl) 잔류가 하지막·계면 공격과 할로겐 오염으로 이어질 수 있어 더 취약하다. 물론 고압이 유동에 전혀 영향을 안 준다는 뜻은 아니다. 챔버·배관 스케일(cm)에서는 압력이 높아지면 유동이 viscous로 바뀌어 gas dynamics·throughput·mixing에 영향을 준다. 다만 이는 feature 안쪽 conformality를 좌우하는 인자가 아니고, feature 안쪽(nm)은 어떤 현실적 압력에서도 Knudsen을 유지한다.

**표면 자리 경쟁(site blocking).** L-H 메커니즘에서 반응은 H*와 M-L*가 나란히 붙어 있어야 일어난다. θ_H*가 1에 가까워지면 M-L*가 H*에 둘러싸여 고립되고, 역설적으로 반응 속도가 떨어질 수 있다.

**과환원과 부산물 위험(WF₆ 계열).** 이미 환원이 끝난 금속에 H*를 더 넣어도 추가 반응은 없다. 오히려 HF 부산물이 HAR 안에 남아 하지막·계면을 공격하고 F 오염을 남길 수 있다.

```
정상: W-Fₓ* + x·H* → W⁰ + x·HF(g) ← 목표 반응
과잉: W⁰ + 추가 H* → 반응 없음
HF 부산물 HAR 잔류 → 하지막·계면 공격, F 오염 ← 위험
```

### 6.5 그럼 H₂ 증량이 실제로 통하는 구간은

정리하면, H₂ 공급은 공정이 **mass transport(diffusion) 제한** 상태일 때에만 직접적인 효과를 낸다.

| 공정 상태 | H₂ 증량 효과 | 근본 해결책 |
|---------|-----------|-----------|
| Diffusion limited | 직접 속도 향상, step coverage 개선 가능 | H₂ 유량/분압 증가 |
| Kinetics limited | 효과 제한적, 포화로 수렴 | 온도 증가 |

실제 ALD 공정에서는 H₂ 유량 saturation curve에서 GPC가 plateau에 도달하는 지점을 찾으면 된다. 그 이후로도 계속 증량하고 있다면, 이미 kinetics limited 영역에 들어섰다는 신호다.

---

## 7. Step Coverage 개선 전략

### 7.1 방법별 효과 비교

| 개선 방법 | 원리 | 효과 | 한계 |
|---------|------|------|------|
| Pulse 시간 연장 | 확산 완결 시간(노출) 확보 | diffusion limited에 직접 효과 | kinetics limited에는 제한적 |
| Purge 시간 연장 | CVD mode 억제, 자기제한 유지 | step coverage 유지에 필수 | throughput 감소 |
| 온도 증가 | Arrhenius (지수적 속도 향상) | kinetics limited에 가장 효과적 | ALD window 이탈, precursor 분해 위험 |
| H₂ 분압 증가 | 충돌 flux 증가, 평형 이동 | diffusion limited 영역에서만 유효 | Langmuir 포화로 수렴 |
| Plasma H₂ | H* 직접 생성 (쪼갤 필요 없음) | 반응성 매우 높음 | HAR conformality 불량 (radical 벽면 재결합) |
| NH₃ (Nitride) | N-H 결합 이용, 높은 반응성 | kinetics 제한 낮음, step coverage 양호 | 막 조성이 nitride로 바뀜 |
| Nitride Seed Layer | 우수한 nucleation 제공 | metal ALD incubation period 해소 | 추가 공정 단계 필요 |

### 7.2 판단 흐름 - 무엇부터 볼 것인가

가장 먼저 할 일은 병목이 어느 쪽인지 가리는 것이다. saturation curve를 그려 RLS를 판별한 다음, 그에 맞는 처방을 고른다.

```
Step coverage 불량 확인
│
▼
┌─────────────────────────┐
│ Pulse saturation curve │
│ 그려서 RLS 파악 │
└─────────────────────────┘
│
┌─────┴──────┐
│ │
▼ ▼
Pulse 미포화 Pulse 포화
(Diffusion (Kinetics
Limited) Limited)
│ │
▼ ▼
Pulse/Purge 온도 최적화
시간 연장 또는
Reactant 변경 (NH₃ 등)
또는
Seed Layer 도입
```

### 7.3 Metal ALD 최적화 가이드

precursor의 포화와 H₂의 포화는 서로 다른 조건에서 도달할 수 있으므로 따로따로 확인하는 것이 좋다.

우선순위는 온도다. 온도가 너무 낮으면 H₂ 환원이 부족해 불완전 환원이 일어나고, 너무 높으면 precursor가 열분해(CVD mode)되거나 금속이 응집(agglomeration)한다. 그 사이의 창을 찾는 것이 핵심이다.

HAR 구조에서는 purge를 평탄 기판보다 충분히 늘려야 한다. 부산물(HF·HCl) 잔류가 하지막·계면 공격과 할로겐 오염으로 이어질 수 있기 때문이다.

incubation period는 pulse/purge만으로는 해결되지 않는다. TiN·TaN 같은 nitride seed layer를 도입하는 것이 근본적인 해법이고, 표면 전처리를 병행하는 것도 검토할 만하다.

마지막으로, H₂ 유량을 지나치게 늘리는 것은 비효율적이다. Langmuir 포화 때문에 수백~수천 배 증량의 실질 효과는 미미하고, nm feature 안쪽은 어차피 항상 Knudsen이므로 분압 증가의 진짜 한계는 포화와 화학 부작용에 있지 확산 체계 전환에 있지 않다.

---

## 참고: 핵심 용어 정리

| 용어 | 정의 |
|------|------|
| Step Coverage | HAR 구조의 상부 대비 하부 두께 비율 (이상: 100%) |
| ALD Window | 자기제한 반응이 유지되는 온도 범위 |
| Self-limiting | 표면이 포화되면 반응이 저절로 멈추는 ALD의 핵심 특성 |
| GPC (Growth Per Cycle) | 1 ALD cycle당 두께 |
| Incubation Period | 핵생성이 시작되기까지 반응이 지연되는 초기 cycle 구간 |
| Knudsen Diffusion | λ > 구조 직경일 때 지배적인 확산 체계 (분자–벽 충돌이 지배) |
| Dissociative Chemisorption | 분자가 쪼개지면서 표면에 강하게 흡착되는 현상 |
| d-band Center | 금속 전자구조에서 d-orbital 상태밀도의 중심 에너지 |
| Langmuir-Hinshelwood | 두 반응물이 모두 표면에 흡착된 뒤 반응하는 메커니즘 |
| Rate-Limiting Step (RLS) | 전체 반응 속도를 결정하는 가장 느린 단계 |
| Recombination Loss | radical이 벽면 충돌 시 재결합해 소실되는 현상 (plasma ALD HAR 침투 제한의 주원인) |
| Knudsen number (Kn) | λ/d. Kn>10이면 free molecular, Kn<0.01이면 viscous |

---

### 계산 근거 (재현용)

평균자유행로는 $$\lambda = k_B T / (\sqrt{2}\,\pi d_m^2 P)$$로 계산했고, $$k_B = 1.381\times10^{-23}$$ J/K, T = 573 K를 사용했다. 분자 직경은 N₂ = 3.70 Å, H₂ = 2.89 Å, bulky precursor ≈ 6.0 Å(유효값)로 두었고, 1 Torr = 133.322 Pa로 환산했다. 전환 압력은 $$P = k_B T / (\sqrt{2}\,\pi d_m^2 \cdot \mathrm{Kn}\cdot d_{\text{feature}})$$로 역산했다. 6.2절의 Langmuir 표는 기준(1x)에서 $$\sqrt{K \cdot P_{H_2}} = 1$$ (θ = 0.50)을 가정했고, 증량 시 θ는 $$\theta = \sqrt{n}/(1+\sqrt{n})$$ (n = 증량 배수)로 계산했다.

---

## References

[^cremers]: V. Cremers, R. L. Puurunen, J. Dendooven, "Conformality in atomic layer deposition: Current status overview of analysis and modelling," *Applied Physics Reviews* **6**, 021302 (2019). DOI: 10.1063/1.5060967. — gas transport regime, sticking probability와 필요 exposure의 관계, radical recombination loss, HAR growth type 종합.

[^gordon]: R. G. Gordon, D. Hausmann, E. Kim, J. Shepard, "A Kinetic Model for Step Coverage by Atomic Layer Deposition in Narrow Holes or Trenches," *Chemical Vapor Deposition* **9**(2), 73–78 (2003). — step coverage 모델, 최소 vapor 공급량 및 최소 (분압 × 노출시간) 조건.

[^hammer]: B. Hammer, J. K. Nørskov, "Theoretical surface science and catalysis—calculations and concepts," *Advances in Catalysis* **45**, 71–129 (2000). — d-band center 이론, 전이금속 표면 흡착/해리 활성 경향.

[^klaus]: J. W. Klaus, S. J. Ferro, S. M. George, "Atomic layer deposition of tungsten using sequential surface chemistry with a sacrificial stripping reaction," *Thin Solid Films* **360**, 145–153 (2000). — W ALD 표면화학 (Si₂H₆ 환원제 기반 sacrificial stripping).

[^elam]: J. W. Elam, C. E. Nelson, R. K. Grubbs, S. M. George, "Kinetics of the WF₆ and Si₂H₆ surface reactions during tungsten atomic layer deposition," *Surface Science* **479**, 121–135 (2001). — WF₆/Si₂H₆ 표면반응 kinetics, 노출 부족 시 반응 미완결·성장 저하.

[^vacuum]: J. F. O'Hanlon, *A User's Guide to Vacuum Technology*, 3rd ed. (Wiley, 2003). — 평균자유행로, Knudsen 수, 유동 체계 분류의 기초 참고 (O'Hanlon 자체는 viscous/transition/molecular 3단계 분류; 본문의 4단계 경계는 희박기체역학 관례를 따름).

[^ylilammi]: M. Ylilammi, O. M. E. Ylivaara, R. L. Puurunen, "Modeling growth kinetics of thin films made by atomic layer deposition in lateral high-aspect-ratio structures," *Journal of Applied Physics* **123**, 205301 (2018). — lateral HAR diffusion–reaction 모델.