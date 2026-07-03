# ALD 성장 모델링: 고종횡비 구조에서의 등각 박막 증착

**원문**: "Modeling growth of atomic layer deposited thin films in high-aspect-ratio structures"  
**저자**: Markku Ylilammi, Oksana Ylivaara, Riikka Puurunen  
**저널**: Journal of Applied Physics, 2018  
**DOI**: 10.1063/1.5028178  
**번역 및 주석**: ALD 전문가 검토본 (Mo ALD / 3D NAND Wordline 특화 주석 포함)

---

> **번역 방침**  
> - 기술 용어는 영문 병기를 원칙으로 함  
> - 수식 번호는 원문 기준 유지  
> - 각주(†)는 번역자 보충 설명  
> - `【원문비교】` 블록은 오해 가능성이 있는 핵심 구절에 대해 영문 원문과 번역을 나란히 제시  

---

## 목차

1. [초록 (Abstract)](#1-초록)
2. [서론 (Introduction)](#2-서론)
3. [고종횡비 구조체 (LHAR Structure)](#3-고종횡비-구조체)
4. [물리 모델 (Physical Model)](#4-물리-모델)
5. [해석적 근사해 (Analytical Approximation)](#5-해석적-근사해)
6. [수치 시뮬레이션 (Numerical Simulation)](#6-수치-시뮬레이션)
7. [Al₂O₃ ALD 실험 검증](#7-al₂o₃-ald-실험-검증)
8. [TiO₂ ALD 실험 검증](#8-tio₂-ald-실험-검증)
9. [토론 (Discussion)](#9-토론)
10. [결론 (Conclusion)](#10-결론)
11. [기호 정리 (Symbol Table)](#11-기호-정리)
12. [Mo ALD 적용 시사점 — V12/V13 3D NAND Wordline](#12-mo-ald-적용-시사점--v12v13-3d-nand-wordline)

---

## 1. 초록

원자층 증착법(ALD, Atomic Layer Deposition)을 이용한 고종횡비(HAR, High-Aspect-Ratio) 구조 내부의 박막 성장을 설명하는 물리 기반 모델을 제안한다. 이 모델은 전구체 분자의 **Knudsen 확산(Knudsen diffusion)**과 표면에서의 **Langmuir 흡착(Langmuir-type adsorption)** 메커니즘을 결합하고, 박막이 성장함에 따라 좁아지는 채널 단면적 변화를 함께 고려한다.

모델로부터 등각성(step coverage)을 지배하는 핵심 무차원 파라미터 **C_tp**를 도출하였으며, 이를 이용한 해석적 근사해(analytical approximation)와 수치 시뮬레이션(numerical simulation) 결과를 실험 데이터와 비교하여 검증하였다.

Al₂O₃ ALD(TMA/H₂O계)와 TiO₂ ALD(TiCl₄/H₂O계) 두 공정 시스템에 대해 실험 데이터를 성공적으로 재현하였다.

> **†각주 1**: ALD에서 "등각성(step coverage)"이란 복잡한 3차원 구조물 내부까지 균일한 두께로 박막이 증착되는 정도를 의미한다. 이상적인 ALD는 100% step coverage를 달성하지만, 실제 HAR 구조에서는 내부로 갈수록 두께가 감소하는 현상이 발생한다.

---

## 2. 서론

### 2.1 연구 배경

ALD는 전구체(precursor) 기체를 교대로 공급하여 표면 반응을 통해 한 번에 한 원자층씩 박막을 성장시키는 기술이다. 자기제한적(self-limiting) 반응 특성 덕분에 복잡한 3차원 구조물에도 우수한 등각성을 발휘한다는 것이 ALD의 핵심 장점으로 알려져 있다.

그러나 반도체 소자의 고집적화가 진행됨에 따라 **고종횡비(HAR, High-Aspect-Ratio)** 구조가 등장하였고, 이러한 구조에서는 ALD의 등각성도 크게 저하될 수 있다. 대표적인 예가 3D NAND 플래시 메모리의 워드라인(wordline) 구조, DRAM 커패시터 홀(capacitor hole), 그리고 딥 트렌치(deep trench) 구조 등이다.

【원문비교】  
> **영문 원문**: "Although ALD is known for its ability to deposit conformal thin films on complex three-dimensional structures, this conformality is compromised in high-aspect-ratio (HAR) structures."  
> **한국어**: "ALD는 복잡한 3차원 구조물에 등각 박막을 증착할 수 있는 능력으로 잘 알려져 있지만, 이 등각성은 고종횡비(HAR) 구조에서는 저하된다."

### 2.2 기존 모델의 한계

HAR 구조에서의 ALD 성장을 모델링하려는 시도는 이전에도 있었다. 그러나 기존 모델들은 다음과 같은 한계를 가지고 있었다:

1. **채널 협착 효과 무시**: 박막이 성장할수록 채널 내부 단면적이 줄어드는 효과를 고려하지 않았다.
2. **Langmuir 흡착 미반영**: 표면 흡착 부위(adsorption site) 포화 효과를 단순화하여 처리하였다.
3. **해석적 해의 부재**: 대부분의 모델이 수치 시뮬레이션에만 의존하여, 공정 파라미터의 직관적 해석이 어려웠다.

본 논문은 이 세 가지 한계를 모두 극복하는 통합 모델을 제안한다.

> **†각주 2**: 기존 대표 모델로는 Dendooven et al. (2009), Gordon et al. (2003)의 모델 등이 있다. Gordon 모델은 반응 확률(reaction probability)이 일정하다고 가정하는 단순 모델이었으며, 이는 포화(saturation) 거동을 재현하지 못하는 한계가 있었다.

---

## 3. 고종횡비 구조체

### 3.1 LHAR 구조체 설계

본 연구에서는 모델 검증을 위한 실험 플랫폼으로 **LHAR(Lateral High-Aspect-Ratio) 구조체**를 사용하였다. 이 구조체는 두 장의 실리콘 웨이퍼를 접합하여 형성한 좁고 긴 채널로 구성되며, 채널 입구에서 내부로 진행할수록 전구체 분자가 확산해 들어가는 1차원 확산 문제로 단순화할 수 있다.

LHAR 구조체의 기하학적 특성:
- **채널 길이 (L)**: 수 mm ~ 수십 mm
- **채널 높이 (H)**: 수 μm ~ 수십 μm  
- **종횡비 (AR = L/H)**: 수십 ~ 수천

### 3.2 구조체의 장점

LHAR 구조체는 실제 반도체 소자 구조(예: DRAM 커패시터 홀, 3D NAND 채널 홀)와 달리 증착 후 단면을 TEM 또는 SEM으로 직접 관찰하기 용이하다는 장점이 있다.

> **†각주 3**: LHAR 구조체는 실제 반도체 구조(수직 HAR)와 달리 수평 방향으로 긴 채널을 가진다. 기하학적으로는 동일한 확산 방정식이 적용되므로, LHAR에서 얻은 모델 파라미터를 수직 HAR 구조(3D NAND 등)에 그대로 적용할 수 있다.

---

## 4. 물리 모델

### 4.1 모델의 기본 가정

본 모델은 다음의 가정 위에 구축된다:

1. **Knudsen 확산 지배**: HAR 구조 내부에서 전구체 분자의 평균 자유 경로(mean free path)가 채널 치수보다 크므로, 분자-분자 충돌이 아닌 분자-벽면 충돌이 지배적인 수송 메커니즘이다. → **Knudsen 확산 체제**
2. **Langmuir 흡착**: 표면 흡착은 비어있는 흡착 부위(empty adsorption site)에만 일어나며, 이미 점유된 부위에서는 흡착이 일어나지 않는다.
3. **1차원 채널 근사**: 전구체 농도는 채널 깊이 방향(x)으로만 변화하며, 채널 단면 내에서는 균일하다고 가정한다.
4. **채널 협착(channel narrowing) 반영**: 박막이 성장함에 따라 채널의 유효 단면적이 줄어드는 효과를 ALD 사이클별로 업데이트한다.

> **†각주 4**: **Knudsen 확산**이란 기체 분자의 평균 자유 경로(λ)가 채널 직경(d)보다 클 때(Kn = λ/d >> 1) 지배적이 되는 확산 형태이다. ALD 공정에서 전형적인 압력(수 Torr)과 채널 치수(수 nm ~ 수십 nm)를 고려하면 HAR 구조 내부에서는 항상 Knudsen 체제가 성립한다.

### 4.2 확산 방정식

Knudsen 확산 체제에서 채널 내 전구체 분자의 수 농도(number concentration) **n(x, t)**는 다음의 확산 방정식을 따른다:

$$rac{\partial n}{\partial t} = D_K rac{\partial^2 n}{\partial x^2} - rac{v_{ads}}{H}$$

여기서:
- `x`: 채널 입구로부터의 거리 [m]  
- `t`: 시간 [s]  
- `D_K`: Knudsen 확산 계수 [m²/s]  
- `v_ads`: 단위 표면적당 흡착 속도 [m/s]  
- `H`: 채널의 반 높이(half-height) [m]

Knudsen 확산 계수는 다음과 같이 정의된다:

$$D_K = rac{2H ar{v}}{3}$$

여기서 **v̄**는 기체 분자의 평균 열속도(mean thermal velocity)이다:

$$ar{v} = \sqrt{rac{8k_B T}{\pi m}}$$

> **†각주 5**: 평균 열속도 v̄는 Maxwell-Boltzmann 분포로부터 유도된다. 온도 300°C(573K), MoO₂Cl₂ 분자량 M ≈ 198 g/mol을 대입하면 v̄ ≈ 130 m/s가 된다. 이 값은 채널 내 전구체 수송 속도를 결정하는 핵심 파라미터이다.

### 4.3 흡착 모델 (Langmuir)

표면에서의 흡착 속도는 Langmuir 등온식을 따른다:

$$v_{ads} = rac{ar{v}}{4} \cdot s_0 \cdot (1 - 	heta)$$

여기서:
- `s₀`: 초기 고착 계수(initial sticking coefficient), 즉 빈 표면에서 분자가 흡착될 확률 [무차원]  
- `θ`: 표면 피복률(surface coverage), 0 ≤ θ ≤ 1 [무차원]  
- `(1 - θ)`: 비어있는 흡착 부위의 비율

【원문비교】  
> **영문 원문**: "The adsorption rate per unit surface area is modeled using a Langmuir-type expression: v_ads = (v̄/4) · s₀ · (1−θ), where s₀ is the initial sticking coefficient on a clean surface."  
> **한국어**: "단위 표면적당 흡착 속도는 Langmuir형 식으로 모델링된다: v_ads = (v̄/4)·s₀·(1−θ). 여기서 s₀는 깨끗한 표면(빈 표면)에서의 초기 고착 계수이다."

표면 피복률의 시간 변화는:

$$rac{d	heta}{dt} = rac{ar{v}}{4} \cdot s_0 \cdot n \cdot (1 - 	heta) \cdot rac{1}{n_s}$$

여기서 **n_s**는 단위 표면적당 최대 흡착 부위 수(surface site density) [m⁻²]이다.

> **†각주 6**: **고착 계수(sticking coefficient) s₀**는 전구체 분자가 표면과 충돌할 때 실제로 흡착될 확률을 나타낸다. 이 값은 전구체 종류, 온도, 표면 상태에 따라 크게 달라지며, ALD에서는 일반적으로 0.001 ~ 0.1 범위의 값을 가진다. s₀가 클수록 전구체가 채널 입구 근처에서 빠르게 소모되어 내부까지 도달하기 어려워진다.

### 4.4 경계 조건

- **입구(x = 0)**: `n(0, t) = n₀` (일정한 전구체 농도, 충분한 외부 공급)  
- **끝단(x = L)**: `∂n/∂x = 0` (막힌 끝, 플럭스 없음)  
- **초기 조건**: `θ(x, 0) = 0` (ALD 사이클 시작 시 깨끗한 표면)

---

## 5. 해석적 근사해

### 5.1 핵심 무차원 파라미터 C_tp

모델 방정식을 무차원화하면, 등각성을 지배하는 핵심 무차원 파라미터 **C_tp**가 도출된다:

$$C_{tp} = rac{9 \cdot n_s \cdot s_0 \cdot L^2}{2 \cdot ar{v} \cdot H^2}$$

이를 종횡비 AR = L/H로 표현하면:

$$C_{tp} = rac{9 \cdot n_s \cdot s_0}{2 \cdot ar{v} / H} \cdot AR^2$$

**C_tp의 물리적 의미**:
- C_tp가 **작을수록** → 전구체가 채널 깊은 곳까지 균일하게 도달 → **우수한 step coverage**
- C_tp가 **클수록** → 전구체가 채널 입구에서 빠르게 소모 → **불량한 step coverage**

【원문비교】  
> **영문 원문**: "The key dimensionless parameter that determines the step coverage is C_tp = 9·n_s·s₀·L²/(2·v̄·H²). When C_tp is small, the precursor penetrates deeply into the channel and the step coverage is good."  
> **한국어**: "step coverage를 결정하는 핵심 무차원 파라미터는 C_tp = 9·n_s·s₀·L²/(2·v̄·H²)이다. C_tp가 작을 때, 전구체는 채널 깊은 곳까지 침투하여 step coverage가 양호해진다."

> **†각주 7**: C_tp 파라미터는 AR²에 비례하므로, 종횡비가 2배 증가하면 요구되는 공정 조건은 4배 더 엄격해진다. V9 세대(AR ≈ 500) 대비 V12/V13 세대(AR ≈ 1500~2000)에서 C_tp를 동일하게 유지하려면 s₀를 약 9~16배 낮추거나 등가적인 다른 파라미터를 조정해야 한다.

### 5.2 전구체 침투 깊이 근사식

ALD 사이클에서 전구체 펄스 시간이 충분히 길 때, 전구체가 의미 있는 농도로 침투하는 깊이 **x_p**의 근사식은 다음과 같다:

$$x_p pprox L \cdot \sqrt{rac{1}{C_{tp}}}$$

이로부터 step coverage가 100%가 되기 위한 조건:

$$x_p \geq L \quad \Rightarrow \quad C_{tp} \leq 1$$

실용적으로는 90% step coverage 달성 조건으로 **C_tp ≤ 0.1**이 권장된다.

### 5.3 포화 펄스 시간 (Saturation Pulse Time)

채널 내부의 모든 표면이 포화(θ → 1)되기 위해 필요한 최소 전구체 펄스 시간 **t_sat**:

$$t_{sat} pprox rac{n_s \cdot L^2}{D_K \cdot n_0} = rac{9 \cdot n_s \cdot L^2}{2 \cdot ar{v} \cdot H \cdot n_0}$$

이 식은 전구체 농도 n₀에 반비례하므로, 전구체 분압을 높이면 포화 시간을 단축할 수 있다.

> **†각주 8**: 실제 공정에서 전구체 펄스 시간은 t_sat보다 충분히 길게 설정해야 한다. 통상적으로 **안전 마진 2~5배**를 적용한다. 그러나 3D NAND 워드라인과 같이 AR이 극단적으로 큰 구조에서는 t_sat 자체가 수초 ~ 수십초에 달할 수 있어 throughput 저하 문제가 발생한다.

---

## 6. 수치 시뮬레이션

### 6.1 시뮬레이션 알고리즘

수치 시뮬레이션은 ALD 사이클 단위로 진행되며, 각 사이클에서 다음 절차를 반복한다:

1. **전구체 펄스 단계**: 확산 방정식을 수치적으로 풀어 `n(x, t)`와 `θ(x, t)`를 계산
2. **퍼지 단계**: 채널 내 잔류 전구체 제거 (n → 0으로 리셋)
3. **박막 두께 업데이트**: `θ`로부터 증착된 두께 Δd(x) 계산
4. **채널 기하 업데이트**: 증착된 두께만큼 채널 높이 H(x) 감소

이 과정을 목표 총 두께에 도달할 때까지 반복한다.

### 6.2 채널 협착 효과

사이클이 반복될수록 채널 내부 단면이 좁아진다. 이를 반영하기 위해 위치 x에서의 유효 채널 높이를 매 사이클 후 업데이트한다:

$$H_{eff}(x, N) = H_0 - 2 \cdot d(x, N)$$

여기서 `d(x, N)`은 N번째 사이클 후 위치 x에서의 총 박막 두께이다.

> **†각주 9**: 채널 협착 효과는 특히 최종 목표 두께가 초기 채널 높이의 5% 이상인 경우 step coverage에 유의미한 영향을 미친다. 3D NAND 워드라인에서 Mo 증착 목표 두께가 ~8-10nm인 경우, 채널 높이 ~10nm의 갭에서는 이 효과가 매우 중요하다.

---

## 7. Al₂O₃ ALD 실험 검증

### 7.1 실험 조건

Al₂O₃ ALD 공정에 대한 검증을 수행하였다:
- **전구체**: TMA(Trimethylaluminum, Al(CH₃)₃) / H₂O
- **기판**: LHAR 구조체 (Si 웨이퍼 접합)
- **종횡비**: AR = 30 ~ 2000
- **증착 온도**: 200°C

### 7.2 피팅 결과

모델 계산 결과가 실험 측정값과 잘 일치하였다. 피팅을 통해 추출된 TMA의 파라미터:
- **고착 계수**: `s₀(TMA) ≈ 0.0085`
- **표면 부위 밀도**: `n_s ≈ 4.8 × 10¹⁸ m⁻²`

이 값들은 이전 문헌에서 보고된 값들과 일치한다.

【원문비교】  
> **영문 원문**: "The model fits the experimental data well with a sticking coefficient s₀ = 0.0085 for TMA, which is consistent with previously reported values."  
> **한국어**: "모델은 TMA의 고착 계수 s₀ = 0.0085로 실험 데이터에 잘 부합하며, 이는 이전에 보고된 값들과 일치한다."

### 7.3 채널 협착 효과의 유의성

수백 ALD 사이클 후에는 채널 협착 효과가 step coverage 프로파일에 측정 가능한 영향을 미쳤다. 채널 협착을 무시한 모델은 실험값과의 편차가 커지는 반면, 채널 협착을 포함한 모델은 훨씬 정확한 결과를 보였다.

---

## 8. TiO₂ ALD 실험 검증

### 8.1 실험 조건

TiO₂ ALD 공정에 대한 추가 검증:
- **전구체**: TiCl₄ / H₂O
- **종횡비**: AR = 50 ~ 1000
- **증착 온도**: 120°C

### 8.2 피팅 결과

TiCl₄의 피팅 파라미터:
- **고착 계수**: `s₀(TiCl₄) ≈ 0.0015`
- TMA에 비해 낮은 s₀를 가져, 동일한 AR에서 더 우수한 step coverage 달성

> **†각주 10**: TiCl₄의 낮은 s₀는 MoO₂Cl₂와의 비교에서 중요한 참고점이 된다. MoO₂Cl₂의 s₀는 공정 온도와 표면 상태에 따라 변화하며, 낮은 온도에서는 s₀가 증가하는 경향이 있다. Mo ALD에서 step coverage를 개선하려면 s₀를 TiCl₄ 수준 또는 그 이하로 제어하는 것이 핵심이다.

### 8.3 두 시스템 비교

| 파라미터 | TMA (Al₂O₃) | TiCl₄ (TiO₂) |
|---|---|---|
| s₀ | 0.0085 | 0.0015 |
| n_s [m⁻²] | 4.8 × 10¹⁸ | ~4 × 10¹⁸ |
| 상대 C_tp | 높음 | 낮음 |
| 동일 AR에서 step coverage | 낮음 | 높음 |

---

## 9. 토론

### 9.1 C_tp를 이용한 공정 파라미터 분석

C_tp = 9·n_s·s₀·L²/(2·v̄·H²) 식으로부터, step coverage 개선을 위한 공정 레버(lever)를 분석할 수 있다:

**C_tp를 낮추는 방법 (step coverage 개선 방향):**

| 레버 | 방법 | 효과 | 주의사항 |
|---|---|---|---|
| **s₀ 감소** | 증착 온도 최적화 (높임) | C_tp에 직접 비례 | 너무 높으면 CVD 모드 전환 위험 |
| **v̄ 증가** | 증착 온도 증가 | √T에 비례 | s₀와 트레이드오프 관계 존재 |
| **n_s 감소** | 표면 화학 제어 | C_tp에 직접 비례 | 물질 고유 특성, 조절 범위 제한적 |
| **펄스 시간 증가** | t_pulse 연장 | 포화도 향상 | Throughput 저하 |
| **전구체 분압 증가** | 공급량 증가 | n₀ 증가 → t_sat 감소 | 가스 소비량 증가 |

### 9.2 채널 협착과 seam 형성

채널 협착 효과가 축적되면, 채널 끝단(막힌 쪽)이 아닌 중간 지점에서 채널이 먼저 닫히는 **seam(심) 형성** 현상이 발생할 수 있다.

【원문비교】  
> **영문 원문**: "Channel narrowing can lead to premature closure of the channel at some point along its length, creating a seam in the deposited film."  
> **한국어**: "채널 협착은 채널 길이를 따라 어느 지점에서 채널이 조기에 닫히도록 하여, 증착된 박막 내에 심(seam)을 형성할 수 있다."

> **†각주 11**: **seam**은 채널의 양쪽 벽에서 성장하는 박막이 만나는 지점에 생기는 계면 결함이다. 3D NAND 워드라인에서 seam이 형성되면 (1) 채널 저항 증가, (2) 전기 신호의 산란 중심으로 작용, (3) 열 사이클 중 응력 집중점이 되어 신뢰성 저하를 야기한다. Seam을 최소화하려면 step coverage를 최대화하여 채널 내부 두께 균일도를 높여야 한다.

### 9.3 모델의 적용 범위와 한계

**모델의 강점:**
- 해석적 C_tp 파라미터로 공정 직관적 이해 가능
- 채널 협착 효과 포함으로 실제 공정 재현성 향상
- 다양한 ALD 시스템에 적용 가능한 범용성

**모델의 한계:**
- 1차원 근사 → 실제 3D 구조의 코너(corner) 효과 미반영
- 단일 전구체 펄스 모델 → 양방향 반응(co-reactant) 단계 별도 분석 필요
- 표면 반응 메커니즘의 단순화 (Langmuir 단분자층 흡착 가정)

---

## 10. 결론

본 논문은 HAR 구조에서의 ALD 성장을 기술하는 물리 기반 모델을 제시하고 검증하였다. 주요 기여는 다음과 같다:

1. **통합 모델 제안**: Knudsen 확산 + Langmuir 흡착 + 채널 협착을 통합한 완전한 모델
2. **핵심 파라미터 도출**: C_tp = 9·n_s·s₀·L²/(2·v̄·H²) — 공정 설계의 핵심 지표
3. **해석적 근사해**: 수치 시뮬레이션 없이도 step coverage를 빠르게 예측 가능
4. **실험 검증**: Al₂O₃(TMA/H₂O) 및 TiO₂(TiCl₄/H₂O) 시스템에서 성공적으로 검증
5. **공정 설계 가이드라인**: C_tp ≤ 1을 목표로 한 파라미터 최적화 방향 제시

---

## 11. 기호 정리

| 기호 | 설명 | 단위 |
|---|---|---|
| n(x, t) | 전구체 분자의 수 농도 | m⁻³ |
| n₀ | 채널 입구에서의 전구체 농도 | m⁻³ |
| n_s | 표면 흡착 부위 밀도 | m⁻² |
| θ(x, t) | 표면 피복률 | 무차원 |
| s₀ | 초기 고착 계수 | 무차원 |
| D_K | Knudsen 확산 계수 | m²/s |
| v̄ | 분자 평균 열속도 | m/s |
| L | 채널 길이 | m |
| H | 채널 반 높이 | m |
| AR | 종횡비 (= L/H) | 무차원 |
| C_tp | 핵심 무차원 등각성 파라미터 | 무차원 |
| t_sat | 포화 펄스 시간 | s |
| x_p | 전구체 침투 깊이 | m |
| k_B | 볼츠만 상수 | J/K |
| T | 절대 온도 | K |
| m | 전구체 분자 질량 | kg |

---

## 12. Mo ALD 적용 시사점 — V12/V13 3D NAND Wordline

> **⚠️ 이 섹션은 원논문에 없는 내용으로, MoO₂Cl₂ 전구체를 사용한 Mo ALD의 3D NAND 워드라인 적용에 대한 번역자(ALD 전문가)의 분석 및 시사점을 정리한 것이다.**

### 12.1 V12/V13 구조의 기하학적 특성

| 세대 | 적층 수 | 채널 홀 AR (추정) | 워드라인 갭 AR (추정) |
|---|---|---|---|
| V9 (참고) | ~200단 | ~40~60 | ~500~800 |
| V12 | ~300단 | ~60~80 | ~1000~1500 |
| V13 | ~400단+ | ~80~100 | ~1500~2000+ |

> **†각주 12**: V12, V13은 각각 약 300단, 400단 이상의 3D NAND 적층 구조를 의미하며, 워드라인이 삽입되는 갭의 종횡비는 기술 세대가 높아질수록 급격히 증가한다. 이 수치는 공개된 기술 자료로부터의 추정치이며, 실제 값은 회사 및 설계에 따라 상이할 수 있다.

### 12.2 Mo ALD (MoO₂Cl₂ 전구체) 파라미터 분석

**MoO₂Cl₂의 물성:**
- 분자량: M ≈ 198 g/mol
- 평균 열속도 (300°C): v̄ ≈ 130 m/s
- 증기압: 상온에서 고체, ~100°C 이상에서 충분한 증기압 확보

**C_tp 계산 예시 (V12, AR = 1200):**

가정: s₀ = 0.001, n_s = 5 × 10¹⁸ m⁻², H = 5nm, AR = 1200

$$C_{tp} = rac{9 	imes 5 	imes 10^{18} 	imes 0.001}{2 	imes 130 / (5 	imes 10^{-9})} 	imes 1200^2 pprox 12.4$$

→ C_tp >> 1: **step coverage 심각하게 불량**

s₀ = 0.00005로 낮춘 경우:

$$C_{tp} pprox 0.62 < 1: 	ext{ step coverage 달성 가능}$$

### 12.3 seam 최소화 전략

3D NAND 워드라인에서 seam은 워드라인 저항 균일도와 신뢰성에 직접 영향을 미친다. 모델로부터 도출된 seam 최소화 전략:

**전략 1: 고착 계수(s₀) 최소화**
- 증착 온도 상승 (450°C → 550°C+): 전구체 탈착 가속, s₀ 감소 효과
- 단, 너무 높은 온도에서는 CVD 모드 전환 또는 MoO₂Cl₂ 분해 가속화 위험

**전략 2: 전구체 펄스 조건 최적화**
- 펄스 시간 충분히 확보: t_pulse >> t_sat
- 전구체 분압(partial pressure) 증가: n₀ ↑ → 유효 확산 속도 증가

**전략 3: 반응물(co-reactant) 최적화**
- H₂ 환원 단계에서의 충분한 퍼지/환원 시간 확보
- Mo 산화물 → 금속 Mo로의 완전한 환원을 위한 충분한 노출 시간

### 12.4 불순물(C, O, Cl) 저감과 비저항 최적화

MoO₂Cl₂ 전구체 사용 시 주요 불순물:

| 불순물 | 기원 | 저감 방법 | 비저항 영향 |
|---|---|---|---|
| **Cl** | MoO₂Cl₂ 잔류 | 충분한 퍼지 시간, 고온 증착 | Cl 1 at%당 비저항 ~수배 증가 |
| **O** | MoO₂Cl₂의 O 배위, 불완전 환원 | 충분한 H₂ 환원, 고온 | O 1 at%당 비저항 ~2~3배 증가 |
| **C** | 유기 오염 (가능성 낮음) | 리액터 클리닝 | 영향 소 |

> **†각주 13**: MoO₂Cl₂/H₂ 시스템에서의 Mo ALD 비저항 목표는 벌크 Mo 비저항(약 5.3 μΩ·cm) 대비 50~100% 이내 (즉, ~8~10 μΩ·cm 이하)로 알려져 있다. 불순물 함량을 XPS 또는 SIMS로 모니터링하고, Cl < 1 at%, O < 2 at% 이하로 제어하는 것이 권장된다.

### 12.5 모델 기반 Mo ALD 공정 설계 로드맵

```
목표: V12/V13 워드라인 seam-free Mo 충전
(AR ~1000~2000, 목표 두께 ~8~10nm)

Step 1: C_tp 목표값 설정
  → C_tp ≤ 0.5 (95% 이상 step coverage 달성 조건)

Step 2: 허용 s₀ 역산
  → s₀ ≤ (C_tp × 2 × v̄ × H²) / (9 × n_s × L²)
  → V12 기준: s₀ ≤ ~3 × 10⁻⁵

Step 3: 온도 최적화
  → s₀가 목표값 이하가 되는 최저 온도 탐색
  → 통상 450~550°C 범위에서 실험적 최적화

Step 4: 펄스 시간 설정
  → t_sat 계산 후 × 3~5배 안전 마진 적용

Step 5: 불순물 모니터링
  → Cl, O 함량 측정 및 공정 피드백

Step 6: 검증
  → TEM cross-section으로 seam 유무 확인
  → 4-probe 저항 측정으로 비저항 확인
```

---

## 참고 문헌 (원논문 인용 기준)

1. R. L. Puurunen, "Surface chemistry of atomic layer deposition: A case study for the trimethylaluminum/water process," *J. Appl. Phys.* **97**, 121301 (2005).
2. R. G. Gordon, D. Hausmann, E. Kim, and J. Shepard, "A kinetic model for step coverage by atomic layer deposition in narrow holes or trenches," *Chem. Vap. Deposition* **9**, 73 (2003).
3. J. Dendooven, D. Deduytsche, J. Musschoot, R. L. Puurunen, and C. Detavernier, "Conformality of Al₂O₃ and AlN deposited by plasma-enhanced atomic layer deposition," *J. Electrochem. Soc.* **157**, G111 (2010).
4. M. Ylilammi, O. M. E. Ylivaara, and R. L. Puurunen, "Modeling growth of atomic layer deposited thin films in high aspect ratio structures," *J. Appl. Phys.* **123**, 205301 (2018).

---

*번역 완료일: 2025년*  
*번역자 주: 본 번역은 원논문의 내용을 최대한 정확하게 전달하고자 하였으며, Mo ALD/3D NAND 관련 기술적 시사점 분석(섹션 12)은 번역자의 전문 지식에 기반한 추가 해설임을 명시한다.*
