# ALD Step Coverage 개선 — 공정 파라미터 및 메커니즘 종합 정리

> **작성 기준:** Patterned Wafer 상의 High Aspect Ratio (HAR) 구조를 대상으로 하며,  
> Thermal ALD (Oxide / Nitride / Metal) 공정에서의 Step Coverage 개선 관점으로 정리함.

---

## 목차

1. [Step Coverage의 근본 제한 요인](#1-step-coverage의-근본-제한-요인)
2. [Pulse / Purge 시간과 Step Coverage](#2-pulse--purge-시간과-step-coverage)
3. [Thermal Metal ALD (H₂ 환원)의 추가 복잡성](#3-thermal-metal-ald-h₂-환원의-추가-복잡성)
4. [Nitride Seed Layer vs. Metal ALD Step Coverage 비교](#4-nitride-seed-layer-vs-metal-ald-step-coverage-비교)
5. [H₂ 환원이 RLS인 경우의 이론적 배경](#5-h₂-환원이-rls인-경우의-이론적-배경)
6. [H₂ 초과 공급의 효과와 한계](#6-h₂-초과-공급의-효과와-한계)
7. [Step Coverage 개선 전략 종합](#7-step-coverage-개선-전략-종합)

---

## 1. Step Coverage의 근본 제한 요인

ALD 공정에서 Step Coverage를 결정하는 병목은 크게 두 가지로 분류된다.

### 1.1 물질 전달 제한 (Mass Transport / Diffusion Limited)

- Precursor 또는 Reactant가 HAR 구조 하부까지 **도달하지 못함**
- Rate-limiting step: **확산(Diffusion)**
- 지배 확산 체계: Knudsen Diffusion (평균자유경로 λ > 구조 직경 d)
- 해결 방향: **Pulse 시간 연장**으로 직접 개선 가능

### 1.2 반응 속도론 제한 (Reaction Kinetics Limited)

- Reactant가 표면에 도달했더라도 **표면 반응 자체가 느림**
- Rate-limiting step: **Surface Reaction**
- Pulse 시간 연장만으로는 근본적 해결 불가
- 해결 방향: **온도 증가, Reactant 종류 변경**
- 대표 사례: **H₂ 환원 Thermal Metal ALD**

> **핵심 원칙:** 두 제한 중 어느 쪽이 지배적인지를 먼저 파악해야 올바른 개선 방향을 찾을 수 있다.

---

## 2. Pulse / Purge 시간과 Step Coverage

### 2.1 Pulse 시간 — Precursor 포화(Saturation)의 관점

HAR 구조에서 Precursor 분자는 Knudsen 확산을 통해 구조 하부까지 도달한다.  
ALD는 **자기제한(Self-limiting) 반응**이므로, 표면이 충분히 포화(saturate)되기만 하면 이상적인 step coverage를 달성할 수 있다.

| Pulse 시간 | 결과 |
|-----------|------|
| 너무 짧음 | 구조 상부만 포화, 하부는 Precursor 부족 → Step coverage 저하 |
| 충분함 | 전체 표면 포화, 자기제한 반응 완결 → 최대 Step coverage |
| 과도하게 김 | 이미 포화 이후 추가 시간 → 무의미 (self-limiting 특성) |

**실무 포인트:** Pulse saturation curve를 그려 GPC(Growth Per Cycle)가 plateau에 도달하는 최소 시간을 확인하고, 안전 마진을 더해 최적 조건을 설정한다.

### 2.2 Purge 시간 — CVD-mode 억제의 관점

Purge는 단순히 가스를 제거하는 것이 아니라, **ALD의 자기제한 특성을 유지**하기 위한 핵심 단계이다.

| Purge 시간 | 결과 |
|-----------|------|
| 너무 짧음 | 잔류 Precursor/부산물 + 다음 Reactant → 기상 반응(CVD mode) 유발 → Step coverage 급격 악화 |
| 충분함 | 자기제한 메커니즘 유지 → 균일한 conformal 증착 |
| 과도하게 김 | Step coverage 추가 향상 없음, Throughput 감소만 발생 |

**특히 HAR 구조에서의 위험:**  
좁은 구조 내부에 excess Precursor나 반응 부산물이 잔류하기 쉬우므로, 일반 평탄 기판 대비 더 긴 Purge 시간이 필요하다.

### 2.3 추가 고려 요소

| 파라미터 | Step Coverage에 미치는 영향 |
|----------|--------------------------|
| 종횡비 (Aspect Ratio) | 높을수록 더 긴 Pulse/Purge 시간 필요 |
| 공정 온도 | 높을수록 확산 빠르나 Precursor 분해 위험 |
| 공정 압력 | 고압 → λ 감소 → Knudsen → Viscous 전환 → HAR 확산 불리 |
| Precursor 분자 크기 | 크고 무거운 분자일수록 확산 느려 더 긴 Pulse 필요 |

---

## 3. Thermal Metal ALD (H₂ 환원)의 추가 복잡성

Oxide ALD와 달리, H₂를 Reactant로 사용하는 Metal ALD는 **반응 속도론 제한이 추가**된다.

### 3.1 Oxide ALD와의 병목 비교

```
Oxide ALD 병목:          Metal ALD (H₂) 병목:

[Precursor 확산]          [Precursor 확산]
       +                         +
[표면 흡착 반응]           [표면 흡착 반응]
                                 +
                          [H₂ 환원 반응 속도]  ← 추가 병목
```

### 3.2 H₂ Reactant의 구조적 취약성

| 항목 | H₂ (Metal ALD) | O₃/NH₃ (Oxide/Nitride ALD) |
|------|---------------|---------------------------|
| 분자 반응성 | 낮음 (비극성, 강한 H-H 결합) | 높음 (극성 또는 산화력 강함) |
| 활성화 에너지 | 높음 | 낮음 |
| 표면 해리 필요 여부 | **필수** (Dissociative Chemisorption) | 상대적으로 용이 |
| HAR 내 반응 완결성 | 어려움 | 비교적 용이 |

### 3.3 불완전 환원의 연쇄 문제

```
H₂ pulse 불충분 또는 Kinetics 제한
         ↓
리간드 불완전 제거 (F, Cl, Cp 등 잔류)
         ↓
┌─────────────────────────────────┐
│  불순물 증가         다음 Cycle   │
│  (F, Cl, C)    +   Nucleation   │
│  막 품질 저하       방해         │
└─────────────────────────────────┘
         ↓
GPC 감소 + Step coverage 기울기 발생
```

### 3.4 부산물의 추가 위험

| Precursor | H₂ 환원 부산물 | 위험성 |
|-----------|-------------|--------|
| WF₆ | **HF** | 강산 → 이미 증착된 W 막 불균일 식각 |
| WCl₅, MoCl₅ | **HCl** | 금속 부식 위험 |
| CoCp₂, RuCp₂ | CpH (사이클로펜타디엔) | 비교적 안정, 단 탄소 오염 가능 |

> HF/HCl는 HAR 구조 내 잔류 시 이미 증착된 금속막을 **불균일하게 식각**하여  
> Step coverage를 역방향으로 악화시키는 치명적 문제를 일으킬 수 있다.

### 3.5 Incubation Period 문제

Metal ALD는 Oxide/Nitride ALD에 비해 **핵생성 지연(Incubation Period)**이 현저히 길다.  
특히 산화물 기판 위에서 금속 핵생성이 지연되므로, HAR 구조 하부는 상부보다 훨씬 늦게 성장이 시작된다.

```
Metal ALD (H₂) 두께 vs. Cycle:
                                          ← 구조 상부 (빠른 nucleation)
두께  ▁▂▄▆████
      ___▁▂▄▆█                           ← 구조 중부
            ______▁▂                     ← 구조 하부 (incubation 지연)
      └────────────────────▶  Cycle 수
```

- Pulse/Purge 최적화만으로는 해결 불가
- **표면 전처리(pre-treatment) 또는 seed layer**가 근본적 해결책

---

## 4. Nitride Seed Layer vs. Metal ALD Step Coverage 비교

### 4.1 Reactant 반응성 비교

| 항목 | H₂ (Metal ALD) | NH₃ (Nitride ALD) |
|------|---------------|--------------------|
| 분자 반응성 | 낮음 | 높음 (풍부한 N-H 결합) |
| 활성화 에너지 | 높음 | 낮음 |
| 열적 반응 완결성 | 불완전하기 쉬움 | 비교적 완전 |
| HAR 내 반응 완결 | 어려움 | 상대적으로 용이 |
| Rate-limiting step | **Surface Reaction** (kinetics) | 주로 Diffusion |

### 4.2 Nucleation 거동 비교

```
Metal ALD (H₂):                  Nitride ALD (NH₃):

두께                              두께
│  ▁▂▄▆████   ← 상부              │  ▁▂▄▆█████   ← 상부
│  ___▁▂▄▆█   ← 중부              │  ▁▂▄▆████    ← 중부
│  ______▁▂   ← 하부              │  ▁▂▄▆███     ← 하부
└─────────────▶ Cycle 수          └─────────────▶ Cycle 수
→ Incubation period 뚜렷           → 비교적 균일한 nucleation
→ Step coverage 불량               → 양호한 Step coverage
```

### 4.3 Nitride가 Metal ALD의 Seed Layer로서 효과적인 이유

1. **표면 화학적 친화성:**  
   금속은 산화물 표면보다 **질화물(TiN, TaN) 표면**에서 훨씬 유리하게 Nucleation됨  
   → 구조 전체에 균일한 seed → 상·하부 동시 nucleation → Step coverage 향상

2. **Barrier + Seed 이중 역할:**  
   Nitride 막이 Diffusion Barrier와 Nucleation Seed 역할을 동시에 수행  
   → Metal ALD의 최대 약점(Incubation period)을 완화

3. **부산물 식각 위험 없음:**  
   NH₃ 환원 부산물(HCl, NH₄Cl 등)은 금속막을 직접 식각하지 않음  
   (단, NH₄Cl 고체 석출로 인한 HAR 구조 Clogging 위험은 존재)

### 4.4 Nitride ALD의 한계

| 조건 | Step Coverage 영향 |
|------|------------------|
| Thermal NH₃ | 비교적 양호한 Step coverage |
| N₂/H₂ Plasma Nitride ALD | **매우 불량** (Plasma 방향성으로 HAR 하부 도달 불가) |
| NH₄Cl 부산물 (매우 좁은 HAR) | 고체 석출로 구조 막힘(Clogging) 위험 |
| 낮은 공정 온도 | NH₃ 반응 속도 저하 → Step coverage 악화 |

### 4.5 전체 Step Coverage 비교 요약

| 비교 항목 | Thermal Metal ALD (H₂) | Nitride ALD (Thermal NH₃) |
|----------|----------------------|--------------------------|
| Reactant 반응성 | 낮음 | 높음 |
| 반응 속도론 제한 | **크다** | 작다 |
| Incubation Period | **길다** | 짧다 |
| HAR Step coverage | **불량** | 비교적 양호 |
| 부산물 위험성 | **높다** (식각성) | 중간 (Clogging 가능) |
| Seed layer 효과 | — | Metal ALD Nucleation 개선 |

---

## 5. H₂ 환원이 RLS인 경우의 이론적 배경

### 5.1 H₂ 해리 흡착 (Dissociative Chemisorption)

H₂는 기체 상태에서 매우 안정된 비극성 이원자 분자이다.  
금속 표면과 반응하려면 반드시 **해리(Dissociation)**가 선행되어야 한다.

```
H₂(g) → 2H*(ads)

에너지
 │      ‡ ← Ea,diss (활성화 에너지)
 │     ╱╲
 │    ╱  ╲
 │   ╱    ╲__________  2H*(ads)
 H₂(g)
 └──────────────────────▶ 반응 좌표
```

| 항목 | 수치 / 내용 |
|------|-----------|
| H–H 결합 에너지 | **436 kJ/mol** (매우 강한 공유결합) |
| 해리 방식 | 분자 σ* 궤도와 금속 d-band의 상호작용 필요 |
| 결과 | 표면 의존적 활성화 에너지 존재 |

### 5.2 반응 메커니즘: Langmuir-Hinshelwood (L-H) 모델

Metal ALD H₂ 환원 반응은 주로 **L-H 메커니즘**을 따른다.

```
Step 1: H₂ 해리 흡착         H₂(g) + 2* → 2H*           [Ea 높음 → RLS]
Step 2: 표면 리간드 교환      M-L* + H* → M* + H-L(g)     [Ea 중간]
Step 3: 부산물 탈착           H-L(g) → 기체상 제거         [Ea 낮음]
```

- `*` : 표면 활성 사이트
- `M-L*` : 표면에 흡착된 Metal-Ligand 복합체
- `H-L` : 부산물 (HF, HCl, Cp-H 등)

**Eley-Rideal (E-R) 메커니즘이 지배적이지 않은 이유:**  
기체상 H₂가 직접 표면 M-L*와 반응하는 E-R 경로는 H₂의 강한 결합 에너지로 인해  
에너지적으로 매우 불리하여 실제로는 거의 일어나지 않는다.

### 5.3 Arrhenius 식으로 보는 온도 의존성

$$k_i = A_i \cdot \exp\left(-\frac{E_{a,i}}{RT}\right)$$

| Step | 활성화 에너지 | 온도 의존성 |
|------|------------|-----------|
| H₂ 해리 흡착 | **높음** | 강함 |
| 리간드 교환 | 중간 | 중간 |
| 부산물 탈착 | 낮음 | 약함 |

낮은 온도 영역에서 전체 반응 속도:

$$r_{overall} \approx r_1 \propto \exp\left(-\frac{E_{a,diss}}{RT}\right)$$

→ **H₂ 해리 흡착이 RLS (Rate-Limiting Step)**

### 5.4 d-band Center 모델 — 금속별 H₂ 해리 장벽의 차이

Hammer-Nørskov d-band center 이론에 따르면,  
H₂ 해리 흡착의 활성화 에너지는 금속의 **d-band 중심 에너지(εd)**와 상관관계가 있다.

| 금속 | d-band 특성 | H₂ 해리 Ea | H₂ 환원 반응성 |
|------|-----------|-----------|-------------|
| W, Mo | d-band 폭 넓고 비어있음 | 낮음 | 비교적 양호 |
| Co, Ru | 중간 | 중간 | 조건 의존적 |
| Ir, Pt | d-band 채워짐 | 낮음 (noble) | 양호하나 Precursor 선택지 제한 |
| **리간드 피복 표면** | **d-band 차단** | **매우 높음** | **문제 발생** |

**핵심: 흡착 리간드가 H₂ 해리를 방해한다**

```
초기 사이클 (깨끗한 금속 표면):    후속 사이클 (리간드 피복 표면):

  M  M  M  M                        L  L  L  L
  ↑  ↑  ↑  ↑                        M  M  M  M
  d-band 노출                        d-band 차단됨
  H₂ 해리 용이                       H₂ 해리 어려움 (Ea 증가)
```

실제 ALD 조건에서는 표면이 전구체 리간드로 덮여 있으므로  
**H₂ 해리 장벽이 순수 금속 표면보다 훨씬 높아진다.**

### 5.5 물질별 구체 사례

#### Case 1: W ALD (WF₆ + H₂)

| 단계 | 반응 | 특이사항 |
|------|------|---------|
| WF₆ Pulse | WF₆(g) → W-Fₓ*(ads) | 빠른 자기제한 반응 |
| H₂ Pulse | 2H* + W-Fₓ* → W⁰ + x·HF(g) | **느린 반응, Kinetics limited** |
| 부산물 | HF | 잔류 시 W 막 식각 위험 |

- F 리간드의 강한 전기음성도 → 금속 표면 d-band 강하게 교란
- H₂ 해리 Ea 크게 증가
- 불완전 환원 → **잔류 F 불순물 + GPC 감소**

#### Case 2: Co ALD (CoCp₂ + H₂)

| 단계 | 반응 | 특이사항 |
|------|------|---------|
| CoCp₂ Pulse | CoCp₂(g) → Co-Cp*(ads) | 흡착 비교적 용이 |
| H₂ Pulse | 2H* + Co-Cp* → Co⁰ + Cp-H(g) | **Cp 리간드 제거가 RLS** |
| 부산물 | Cp-H (사이클로펜타디엔) | 탄소 오염 가능 |

- Cp 리간드는 크고 부피가 커 제거에 **복수의 H*가 순차적으로 필요**
- HAR 구조 하부는 H* 표면 농도가 낮아 반응 완결이 더 어려움
- 결과: **탄소 불순물의 깊이 방향 기울기 발생**

### 5.6 HAR 구조 내 H* 농도 프로파일

```
      HAR 구조 단면
      ┌──┐    ┌──┐
      │  │    │  │   표면 H* 농도: 높음 → 반응 완결: ✓
      │  │    │  │
      │  │    │  │   표면 H* 농도: 중간 → 반응 완결: △
      │  │    │  │
      │  │    │  │   표면 H* 농도: 낮음 → 반응 완결: ✗
      │  │    │  │              ↑ Kinetics 제한 구간
      └──┘    └──┘
```

**H*가 하부에서 낮은 이유:**
1. H₂는 확산이 빠르지만, **해리에 필요한 활성 사이트 자체가 부족**
2. 상부에서 먼저 H* 소비 → 하부로 전달되는 H* 부족
3. 리간드 피복 표면에서의 높은 Ea → 해리 속도 자체가 느림

---

## 6. H₂ 초과 공급의 효과와 한계

### 6.1 이론적 분석 — Langmuir-Hinshelwood 속도식

H₂는 해리 흡착이므로 2개의 인접 사이트가 필요하다.

$$H_2(g) + 2^* \rightleftharpoons 2H^*$$

표면 커버리지 (Dissociative Langmuir 등온선):

$$\theta_{H^*} = \frac{\sqrt{K_{H_2} \cdot P_{H_2}}}{1 + \sqrt{K_{H_2} \cdot P_{H_2}}}$$

전체 반응 속도:

$$r = k \cdot \frac{\sqrt{K \cdot P_{H_2}}}{1 + \sqrt{K \cdot P_{H_2}}} \cdot \theta_{M-L^*}$$

### 6.2 H₂ 분압 의존성

| H₂ 분압 구간 | 속도 의존성 | 실제 의미 |
|------------|-----------|---------|
| 저압 (K·P ≪ 1) | r ∝ P_H2^(1/2) | H₂ 증량 → 속도 향상 유효 |
| 중압 | r 증가 but 체감 | 수율 감소 구간 |
| 고압 (K·P ≫ 1) | r → k·θ_M-L* (상수) | **P_H2 무관, 완전 포화** |

**수치 예시:**

| H₂ 증량 배수 | θ_H* (해리 Langmuir 기준) | 속도 추가 향상 |
|------------|------------------------|------------|
| 1x (기준) | 0.50 | — |
| 100x | 0.91 | +82% |
| 1000x | 0.97 | +94% → 기준 대비 단 6% 추가 |

> **핵심:** H₂ 1000배 증량이 주는 속도 향상 효과는 **온도 20~30°C 상승 효과에도 미치지 못하는 경우**가 많다.

### 6.3 왜 H₂를 아무리 늘려도 근본 한계가 있는가

$$k_{diss} = A \cdot \exp\left(-\frac{E_{a,diss}}{RT}\right)$$

- H₂ 농도 증가 → **충돌 빈도(pre-exponential A)** 는 향상 → 부분적 속도 향상
- **Ea,diss 자체는 불변** → 지수 항은 오직 온도에만 의존
- Langmuir 등온선 포화 → 표면 θ_H*는 수렴값에 접근

```
압력 효과:    r ∝ P^(1/2) → 포화 수렴 (Langmuir 한계)
온도 효과:    r ∝ exp(-Ea/RT) → 지수적 향상 (훨씬 효과적)
```

### 6.4 H₂ 초과량 공급 시 발생하는 부작용

#### (1) H* 재결합 (Recombination) 증가

$$H^* + H^* \rightarrow H_2(g) + 2^*$$

θ_H*가 높아질수록 인접 H* 재결합으로 기체 H₂로 탈착하는 속도도 증가.  
→ 실제 유효 H* 농도 증가를 **자기 억제(self-quenching)**

#### (2) 공정 압력 상승 → 확산 체계 변화

| 조건 | 확산 체계 | Step Coverage 영향 |
|------|---------|------------------|
| ALD 정상 (저압) | **Knudsen 확산** (λ > d) | HAR 내 분자 운동 자유 → 유리 |
| H₂ 대량 공급 (고압) | **점성 유동** (λ < d) 전환 | 분자간 충돌 증가 → HAR 내 확산 저해 → **불리** |

> HAR Step coverage 개선이 목적이라면 H₂를 과도하게 공급하는 것이 **오히려 역효과**를 낼 수 있다.

#### (3) 표면 사이트 경쟁 (Site Blocking)

L-H 메커니즘에서 반응은 H*와 M-L*가 **인접**해야 발생.  
θ_H* → 1이 되면 M-L*가 고립 → H*와 반응할 기회를 잃음  
→ 역설적으로 **반응 속도가 감소**할 수 있음

#### (4) 과환원 및 부산물 위험 (WF₆ 계열)

```
정상:   W-Fₓ* + x·H* → W⁰ + x·HF(g)       ← 목표 반응
과잉:   W⁰ + 추가 H* → 반응 없음
        HF 부산물 HAR 잔류 → W 막 재식각 가능  ← 위험
```

### 6.5 H₂ 증량이 실제로 효과 있는 구간

H₂ 공급이 **Mass Transport (Diffusion) 제한 상태**일 때만 직접 효과적이다.

| 공정 상태 | H₂ 증량 효과 | 근본 해결책 |
|---------|-----------|-----------|
| Diffusion Limited | 직접 속도 향상, Step coverage 개선 가능 | H₂ 유량/분압 증가 |
| **Kinetics Limited** | 제한적 효과, 포화 수렴 | **온도 증가** |

**실무 판별법:** H₂ 유량 saturation curve에서 GPC가 plateau에 도달하는 지점  
→ 그 이후 증량은 Kinetics limited 영역임을 의미

---

## 7. Step Coverage 개선 전략 종합

### 7.1 공정 파라미터별 개선 효과 비교

| 개선 방법 | 원리 | 효과 | 한계 |
|---------|------|------|------|
| **Pulse 시간 연장** | 확산 완결 시간 확보 | Diffusion limited 해소에 직접 효과 | Kinetics limited에는 제한적 |
| **Purge 시간 연장** | CVD mode 억제, 자기제한 유지 | Step coverage 유지에 필수 | Throughput 감소 |
| **온도 증가** | Arrhenius (지수적 속도 향상) | Kinetics limited 해소에 가장 효과적 | ALD window 이탈, Precursor 분해 위험 |
| **H₂ 분압 증가** | 충돌 빈도 증가, 평형 이동 | Diffusion limited 영역에서만 유효 | Langmuir 포화로 수렴, 고압 시 역효과 |
| **Plasma H₂** | H* 직접 생성 (Ea 불필요) | 반응성 매우 높음 | HAR Step coverage 불량 (방향성) |
| **NH₃ (Nitride)** | N-H 결합 이용, 높은 반응성 | Kinetics 제한 낮음, Step coverage 양호 | 막 조성이 Nitride로 변화 |
| **Nitride Seed Layer** | 우수한 Nucleation 제공 | Metal ALD Incubation period 해소 | 추가 공정 단계 필요 |

### 7.2 HAR 구조 Step Coverage 개선을 위한 의사결정 흐름

```
Step coverage 불량 확인
          │
          ▼
    ┌─────────────────────────┐
    │ Pulse saturation curve  │
    │ 그려서 RLS 파악           │
    └─────────────────────────┘
          │
    ┌─────┴──────┐
    │            │
    ▼            ▼
Pulse 미포화   Pulse 포화
(Diffusion     (Kinetics
  Limited)      Limited)
    │            │
    ▼            ▼
Pulse/Purge   온도 최적화
시간 연장     또는
공정 압력     Reactant 변경
최적화        (NH₃ 등)
              또는
              Seed Layer 도입
```

### 7.3 Metal ALD Step Coverage 최적화 실무 가이드

1. **Precursor saturation과 H₂ saturation을 독립적으로 확인**  
   → 두 saturation curve가 서로 다른 조건에서 도달할 수 있음

2. **온도 최적화가 가장 우선순위**  
   - 너무 낮으면 → H₂ 환원 반응 속도 부족 → 불완전 환원  
   - 너무 높으면 → Precursor 열분해(CVD mode) 또는 금속 응집(Agglomeration)

3. **HAR 구조에서는 Purge 시간을 평탄 기판 대비 충분히 연장**  
   - 부산물(HF, HCl)의 잔류가 막 식각으로 이어질 수 있음

4. **Incubation period는 Pulse/Purge 최적화만으로 해결 불가**  
   - Nitride Seed Layer (TiN, TaN) 도입이 근본적 해결책  
   - 표면 전처리(pre-treatment)와 병행 검토

5. **H₂ 유량을 과도하게 증가시키는 것은 비효율적**  
   - Langmuir 포화로 인해 수백~수천 배 증량의 실질 효과는 미미  
   - 고압화로 Knudsen → Viscous 전환 시 오히려 HAR step coverage 악화

---

## 참고: 핵심 용어 정리

| 용어 | 정의 |
|------|------|
| **Step Coverage** | HAR 구조의 상부 대비 하부 박막 두께 비율 (이상: 100%) |
| **ALD Window** | 자기제한 반응이 유지되는 온도 범위 |
| **Self-limiting** | 표면이 포화되면 반응이 자동으로 멈추는 ALD 핵심 특성 |
| **GPC (Growth Per Cycle)** | 1 ALD cycle당 박막 성장 두께 |
| **Incubation Period** | 핵생성이 시작되기까지 반응이 지연되는 초기 cycle 구간 |
| **Knudsen Diffusion** | 평균자유경로(λ) > 구조 직경(d)일 때 지배적인 확산 체계 |
| **Dissociative Chemisorption** | 분자가 해리되면서 표면에 강하게 흡착되는 현상 |
| **d-band Center** | 금속의 전자 구조에서 d-orbital 상태밀도의 중심 에너지 |
| **Langmuir-Hinshelwood** | 두 반응물이 모두 표면에 흡착된 후 반응하는 메커니즘 |
| **Rate-Limiting Step (RLS)** | 전체 반응 속도를 결정하는 가장 느린 단계 |

---

*본 문서는 Patterned Wafer ALD 공정에서의 Step Coverage 개선을 목적으로,  
Diffusion 제한 / Kinetics 제한 / Nucleation 거동 / 반응 부산물 관점을 종합하여 정리하였음.*
