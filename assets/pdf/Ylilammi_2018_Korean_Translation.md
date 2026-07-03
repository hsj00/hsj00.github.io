# ALD 성장 kinetics 모델링: 측면 고종횡비(LHAR) 구조에서의 박막 성장

**원문**: "Modeling growth kinetics of thin films made by atomic layer deposition in lateral high-aspect-ratio structures"
**저자**: Markku Ylilammi, Oili M. E. Ylivaara, Riikka L. Puurunen (VTT Technical Research Centre of Finland / Aalto University)
**저널**: *Journal of Applied Physics* **123**, 205301 (2018)
**DOI**: [10.1063/1.5028178](https://doi.org/10.1063/1.5028178)
**번역·주석**: 원문 대조 교정본 (Mo ALD / 3D NAND Wordline 특화 주석 포함)

---

> **번역 방침**
> - 기술 용어는 영문 병기를 원칙으로 한다.
> - 수식 번호(식 N)는 원 논문 기준을 유지한다.
> - 각주(†)는 번역자 보충 설명이다.
> - `【원문 대조】` 블록은 오해 가능성이 있는 구절에 대해 원문의 취지를 명시한다. (저작권상 원문은 짧은 핵심 어구만 인용하고 나머지는 원문 취지로 기술한다.)
> - ⚠ 표시는 원 논문에 없는, 번역자의 도메인 해석·추론임을 뜻한다.
> - 이 문서는 원 논문의 실제 장 구성(I~IX)을 따른다.

---

## 목차

1. [초록](#1-초록)
2. [서론 (Section I)](#2-서론-section-i)
3. [좁은 채널에서의 기체 확산 (Section II)](#3-좁은-채널에서의-기체-확산-section-ii)
4. [박막 성장 모델링 (Section III)](#4-박막-성장-모델링-section-iii)
5. [확산 방정식의 근사해 (Section IV)](#5-확산-방정식의-근사해-section-iv)
6. [두께 프로파일과 침투 깊이 (Section V)](#6-두께-프로파일과-침투-깊이-section-v)
7. [Gordon 모델과의 비교 (Section VI)](#7-gordon-모델과의-비교-section-vi)
8. [실험 (Section VII)](#8-실험-section-vii)
9. [결과 (Section VIII)](#9-결과-section-viii)
10. [결론 (Section IX)](#10-결론-section-ix)
11. [기호 정리](#11-기호-정리)
12. [Mo ALD 적용 시사점 (번역자 해설)](#12-mo-ald-적용-시사점-번역자-해설)

---

## 1. 초록

원자층 증착법(ALD)으로 성장시킨 박막의 등각성(conformality)을, 길고 좁은 측면 채널을 갖는 **전(全)실리콘 테스트 구조(all-silicon LHAR)**를 이용해 연구하였다. 본 연구에서 개발한 **확산 모델(diffusion model)**로 좁은 채널 내 ALD 성장의 전파를 분석한다. 이 확산 모델은 (1) 저압에서의 기체 수송, (2) 박막 성장을 기술하는 **동적 Langmuir 흡착 모델**, (3) 박막 성장에 따른 **채널 협착(channel narrowing)** 효과를 함께 고려한다.

박막 성장은 표면 반응을 포함한 확산 방정식을 풀어 계산하며, 측정된 두께 프로파일에 모델을 맞추기 위한 **효율적인 해석적 근사해(analytic approximate solution)**를 제시한다. 이 피팅으로부터 **흡착 평형상수 K**와 **고착 계수 c(sticking coefficient)**를 얻는다. 본 모델을 Gordon의 plug-flow 모델과 비교하며, 시뮬레이션은 Al₂O₃ 및 TiO₂ ALD 공정의 실험 결과를 잘 예측한다.

> **†각주 1**: ALD에서 등각성(conformality/step coverage)은 3차원 구조 내부까지 균일한 두께로 박막이 증착되는 정도를 뜻한다. 이상적인 ALD는 100% 등각성을 지향하지만, 실제 고종횡비 구조에서는 내부로 갈수록 두께가 감소한다.

【원문 대조】
> 이 논문의 산출물은 **K와 c** 두 파라미터다. (원 번역본이 내세운 무차원 파라미터 `C_tp`는 원문에 존재하지 않는다. §5, §11 참조.)

---

## 2. 서론 (Section I)

반도체 소자의 3차원화(through-silicon-via, FinFET, **3D NAND flash memory**)가 진행되면서 박막 공정이 등각적으로 도달해야 하는 종횡비 요구가 높아지고 있다. ALD는 최소 두 가지 이상의 반응물이 고체 기판 위에서 반복적·자기제한적(self-terminating) 반응을 일으키는 기술로(Puurunen 2005; George 2010), 이러한 등각성 요구를 충족할 수 있다. ALD 등각막은 MEMS, 에너지, 고표면적 촉매 등 본질적으로 3차원성을 요구하는 분야에서도 필요하다.

그럼에도 등각성에 대한 실험 데이터는 문헌에 드물게 보고되어 왔는데, 저자들은 그 원인을 **사용하기 쉬운 표준 분석 구조와 방법의 부재**로 지목한다. (예외로 Dendooven 2010, Rose & Bartha 2009, Schwille 2017, Yanguas-Gil 2017을 든다.)

본 연구는 선행 연구(Gao 2015)를 이어, 측면 고종횡비 구조(LHAR) 프로토타입을 사용한다. 이 구조는 polysilicon 멤브레인 안에 형성된, 높이 약 500 nm의 길고 좁은 측면 갭으로, **수직 트렌치를 90° 눕힌 것과 등가**이며 pillar가 멤브레인을 지지한다. 본 연구는 이전(Gao 2015)과 유사한 공정으로 제작한 **새로운 all-silicon 설계의 PillarHall® 프로토타입**을 사용한다. 제작된 채널 길이는 1 μm~5 mm이며, 전형적 갭 높이 500 nm 기준으로 종횡비는 **2:1~10,000:1** 범위다.

> **†각주 2**: 본 논문이 비교 대상으로 삼는 대표 모델은 **Gordon (2003)** 모델이다. 이는 확산 없이 일정 농도의 전선(front)이 전진한다고 가정하는 plug-flow 모델로, 침투 깊이는 예측하지만 **두께 프로파일의 형상과 반응 kinetics는 제공하지 못한다.** (§7 참조)

【원문 대조】
> 원 논문이 보고하는 핵심 관찰: **채널이 충분히 길면 침투 깊이는 채널 길이 L에 의존하지 않는다.** 즉 침투 깊이는 구조가 아니라 공정·전구체의 고유 특성이다.

본 연구의 목표는 고종횡비 트렌치에서의 ALD 두께 프로파일을 계산하는 모델을 개발하고, 이를 통해 측정된 두께 프로파일로부터 성장 kinetics 정보를 추출하는 것이다. Al₂O₃용 TMA/H₂O 공정과 TiO₂용 염화물(TiCl₄) 공정으로 모델을 검증한다.

---

## 3. 좁은 채널에서의 기체 확산 (Section II)

### 3.1 충돌률과 평균 속력

Hard-sphere 모델(Levine 1978)로 혼합 기체(전구체 A + 캐리어 B)의 충돌률 $z_A$를 기술한다(식 1). 분자 A의 평균 속력은

$$\bar{v}_A = \left(\frac{8RT}{\pi M_A}\right)^{1/2} \tag{2}$$

이며, 기상 확산계수는 $D_A = \dfrac{3\pi}{16}\dfrac{\bar{v}_A^2}{z_A}$ (식 3)이다.

> **†각주 3**: 식 (2)는 $R = k_B N_0$, $M_A = m N_0$ 관계로 $\bar{v}=\sqrt{8k_BT/\pi m}$과 동등하다. 무거운 분자일수록 같은 온도에서 느리다. 이 때문에 원 논문은 가벼운 H₂O가 아니라 **무거운 금속 전구체의 확산이 성장 제한 인자**라고 가정한다.

### 3.2 Knudsen 확산과 Bosanquet 결합 — 이 논문 수송 모델의 핵심

좁은 채널·저압에서는 분자–벽 충돌이 지배적인 **Knudsen(분자류) 영역**이 되며, 확산계수는(Poodt 2017)

$$D_{Kn} = h\left(\frac{8RT}{9\pi M_A}\right)^{1/2} \tag{4}, \qquad h = \frac{2}{\dfrac{1}{H}+\dfrac{1}{W}} \tag{5}$$

이다. 여기서 $h$는 높이 $H$, 폭 $W$인 직사각형 채널의 **수력지름(hydraulic diameter)**이다. 실제 공정은 기상 확산과 Knudsen 확산이 공존하는 **천이 영역**이므로, 두 저항을 합친 **Bosanquet 관계**로 유효 확산계수를 구한다(Poodt 2017).

$$\frac{1}{D_{eff}} = \frac{1}{D_A} + \frac{1}{D_{Kn}} \tag{6}$$

> **†각주 4**: ⚠ 주의 — Knudsen만으로 단순화하는 것은 부정확하다. 원 논문은 식 (6)의 Bosanquet 결합으로 bulk 확산(D_A)과 Knudsen 확산(D_Kn)을 **모두** 반영한다. 다만 좁은 채널·저압에서는 대개 $D_{Kn}\ll D_A$이므로 D_eff는 실질적으로 D_Kn이 지배한다. 또한 $D_{Kn}\propto h$이므로, 막이 자라 채널이 좁아지면 수송도 즉시 느려진다.

### 3.3 분자 지름과 흡착 밀도

전구체 분자 지름은 점도(식 7) 또는 응축상 밀도(식 8)로 추정한다. Knudsen 확산이 병목이고 $D_{Kn}$에는 분자 지름이 들어가지 않으므로, 거친 추정으로 충분하다. 논문 사용값: $d_{H_2O}=418$ pm, $d_{N_2}=374$ pm, $d_{TMA}=591$ pm, $d_{TiCl_4}=703.9$ pm. (TMA는 215 °C 이상에서 96% 이상 단량체이므로 단량체 값 사용; Almenningen 1971.)

한 사이클에 화학흡착되는 양(포화 흡착 밀도 q)은 실측 가능한 값들로부터 계산한다.

$$q = \frac{b_{film}}{b_A}\,\frac{\rho\,gpc_{sat}}{M}\,N_0 \tag{9}$$

여기서 $b_{film}$은 막 formula unit당 금속 원자 수, $b_A$는 전구체 분자당 금속 원자 수다. TMA→Al₂O₃는 $b_{film}=2, b_A=1$; TiCl₄→TiO₂는 $b_{film}=1, b_A=1$.

> **†각주 5**: q가 크다는 것은 벽이 전구체를 많이 소모한다는 뜻이며, 같은 dose로 도달 가능한 침투 깊이가 짧아짐을 의미한다. ⚠ 고밀도 금속막(Mo 등)은 q가 크기 쉬우므로, 산화막 ALD의 침투 경험치를 금속 ALD에 그대로 이관하면 안 된다.

---

## 4. 박막 성장 모델링 (Section III)

### 4.1 1차원 확산-반응 방정식

채널이 납작해(높이 방향 농도 평형 시간상수 $H^2/D_{eff}\approx10$ ns) y·z 방향 농도 구배가 없다고 두면, 문제는 채널 축(x) 1차원으로 환원된다. 지배 방정식은 **수 농도가 아니라 분압 $p_A$** 기준이다.

$$\frac{\partial p_A}{\partial t} = D_{eff}\frac{\partial^2 p_A}{\partial x^2} - g\cdot\frac{4}{h}\cdot\frac{RT}{N_0} \tag{10}$$

- 첫째 항: 확산에 의한 유입·유출.
- 둘째 항(소모항): 벽 흡착에 의한 기체 소모. $g$는 순 흡착률(1/m²s), $4/h$는 채널의 **표면적/부피 비**(W≫H이면 4/h→2/H).

【원문 대조】
> 원 번역본은 이 식을 $\partial n/\partial t = D_K\,\partial^2 n/\partial x^2 - v_{ads}/H$ (농도 n 기준, $D_K=2H\bar v/3$)로 적었으나, 원문은 위 식 (10)과 같이 **분압 기준·$4/h$ 소모항·$D_{eff}$**를 쓴다.

### 4.2 Langmuir 흡착 모델

흡착률은 Hertz–Knudsen flux에 고착 확률과 빈자리 비율을 곱한 형태다.

$$f_{ads} = (1-\theta)\frac{c\,N_0\,p_A}{\sqrt{2\pi M_A RT}} \tag{11}, \qquad f_{des} = q\,\theta\,P_d \tag{12}$$

평형($f_{ads}=f_{des}$)에서 흡착 평형상수 K를 정의한다.

$$K = \frac{\theta_{eq}/p_A}{1-\theta_{eq}} = \frac{cQ}{qP_d} \tag{13}, \qquad Q = \frac{N_0}{\sqrt{2\pi M_A RT}} \tag{14}$$

순 흡착률 $g=f_{ads}-f_{des}$ (식 15), 피복률 변화 $d\theta/dt=g/q$ (식 16).

> **†각주 6**: ⚠ 중요 — 원 논문의 c는 **lumped sticking coefficient**다. 즉 "깨끗한 표면에서의 초기 고착 확률"이 아니라, **물리흡착·화학반응·리간드 제거 등 모든 순차·병렬 표면 과정을 하나로 묶은 유효 확률**이다. 피팅으로 얻은 c를 특정 소반응의 확률로 해석하면 안 된다. 또한 펄스 동안 순 흡착률이 항상 양이므로, **가역/비가역 흡착은 $P_d$ 하나로 포괄**된다(비가역이면 $P_d=0$).

---

## 5. 확산 방정식의 근사해 (Section IV)

이 장이 원 논문의 핵심 기여다. 수천 사이클을 매번 수치해석하는 것은 비현실적이므로, 압력 분포를 **선형 구간 + 지수 꼬리**로 근사한다.

**선형 구간 (x < x_t).** 입구 쪽 포화 표면은 기체를 소모하지 않으므로($g\approx0$) 정상상태에서 압력이 직선으로 감소한다.

$$p_A(x,t) = p_{A0}\left(1-\frac{x}{x_s}\right) \tag{18}, \qquad x_s = \sqrt{Dt} \tag{19}$$

**겉보기 종방향 확산상수 D.** "유입 분자 수 = 흡착 분자 수"라는 물질 수지로부터 유도된다(식 20–23).

$$\boxed{\;D = \frac{p_{A0}\,H\,D_{eff}}{q\,k_B T\left(1-\dfrac{\ln(Kp_{A0}+1)}{Kp_{A0}}\right)}\;} \tag{23}$$

- $p_{A0}$↑, $H$↑, $D_{eff}$↑ → 전선 빨라짐. $q$↑ → 느려짐.
- 괄호 항은 Langmuir 등온선 보정으로, $Kp_{A0}\gg1$이면 1에 수렴한다.

**지수 꼬리 구간 (x > x_t).** 성장 전선 부근은 피복률이 낮아 흡착이 활발하므로 압력이 지수적으로 급락한다. 선형–지수 접합점은

$$x_t = x_s - \sqrt{\frac{h\,N_0\,D_{eff}}{4RT\,cQ}} \quad (\ge 0) \tag{28}$$

여기서 $\sqrt{hN_0D_{eff}/4RTcQ}$는 **반응-확산 길이**로, 꼬리의 폭(=두께 프로파일 기울기)을 정한다. **c가 클수록 꼬리가 짧고 가파르다**(전선에서 즉시 소모). 근사해와 완전 수치해는 Fig. 2·3에서 사실상 일치한다.

【원문 대조】
> 원 번역본의 "핵심 무차원 파라미터 $C_{tp}=9n_ss_0L^2/2\bar vH^2$"와 "$x_p\approx L/\sqrt{C_{tp}}$", "포화시간 $t_{sat}$" 및 "$C_{tp}\le1$이면 100% 등각" 조건은 **원 논문에 없다.** 원 논문의 침투 척도는 $x_s=\sqrt{Dt}$ (식 19)와 식 (23)의 D이며, 침투 깊이 정의는 §6의 절반두께 $x_p$다.

피복률의 시간 발전은 상미분방정식(식 31)으로 기술되며, 피팅당 1만 회 이상 호출되므로 **4차 Runge–Kutta**로 푼다(보통 1 ms 간격 100점).

$$\frac{d\theta}{dt} = \frac{cQ\,p_A}{q} - \left(\frac{cQ\,p_A}{q}+P_d\right)\theta \tag{31}$$

---

## 6. 두께 프로파일과 침투 깊이 (Section V)

### 6.1 절반 두께 침투 깊이

침투 깊이 $x_p$는 **막 두께가 입구 두께의 절반이 되는 지점**으로 정의한다.

$$s(x_p) = \frac{s(0)}{2} \tag{34}$$

두께 곡선의 기울기가 최대인 지점이 절반 두께 지점이므로, 같은 두께 오차 $\Delta s$에 대해 위치 오차 $\Delta x_p=\Delta s/|ds/dx|$ (식 33)가 최소가 된다. → 측정 재현성이 가장 좋은 정의.

### 6.2 채널 협착

막은 위·아래 양면에서 자라므로 N 사이클 후 남은 높이는

$$H(N) = H(0) - 2N\cdot gpc \tag{35}$$

원 논문은 채널 높이를 전 구간 균일하다고 두고 매 펄스 후 입구값으로 갱신한다(단순화). 이 때문에 깊은 쪽 두께 감소를 실제보다 약간 가파르게 예측한다. Fig. 4에서 초기 높이 **0.2 μm** 채널은 1000 사이클 후 **입구가 완전히 폐색(plug-up)**된다.

【원문 대조】
> 원 번역본은 이 현상을 "채널 중간에서 먼저 닫혀 **seam(심)**이 생긴다"고 서술했으나, 원 논문은 **seam을 언급하지 않으며** 다루는 것은 **입구의 완전 폐색**이다. (다만 gap-fill에서의 seam 논의는 ⚠ 도메인 확장으로 §12에서 별도 취급.)

최종 두께 프로파일은 각 사이클의 피복률 기여를 합산해 얻는다: $s(x)=\theta(x)\cdot gpc_{sat}$ (식 36–37).

---

## 7. Gordon 모델과의 비교 (Section VI)

Gordon(2003) 모델은 확산 없이 일정 농도의 전선이 전진한다고 가정한다. 분자류 유량(식 41)을 적분하면 침투 깊이가

$$x_p = H\cdot\frac{\sqrt{1+\tfrac{3}{4}Ct_p}-1}{0.375} \tag{45}, \qquad C = \frac{p_{A0}N_0}{2q\sqrt{2\pi M_A RT}} \tag{44}$$

로 나온다. 여기서 **C는 단위 1/s의 상수이지 무차원 파라미터가 아니며**, 원 번역본의 `C_tp`와 무관하다. Gordon 모델에서 도달 종횡비 $x_p/H$는 H에 무관하다.

| 항목 | Gordon (2003) | 본 논문 확산 모델 |
|---|---|---|
| 침투 깊이 | ○ (Fig. 5에서 꽤 정확) | ○ |
| 두께 프로파일 형상 | ✕ (계단형 가정) | ○ (선형+지수 꼬리) |
| kinetics(c, K) 추출 | ✕ | **○ (본 모델의 존재 이유)** |

---

## 8. 실험 (Section VII)

| 항목 | Al₂O₃ | TiO₂ |
|---|---|---|
| 전구체 | TMA(Al(CH₃)₃) + H₂O | TiCl₄ + H₂O |
| **증착 온도** | **300 °C** | **110 °C** |
| 반응기 | Picosun R-150 (4 reactant lines) | 동일 |
| 펄스/퍼지 | 0.1 s / 4.0 s (양 전구체) | 0.1 s / 4.0 s |
| 사이클 | 500 (≈50 nm) | 1000 (≈50 nm) |
| 챔버 압력 | ≈300 Pa | ≈300 Pa |
| N₂ 유량 | 라인당 150 sccm | 동일 |
| 구조 | PillarHall® 3세대, **H=500 nm**, L=1 mm (구조적 AR **2000**) | 동일 |

측정은 SCI FilmTek 2000M 분광 반사계로 100점 라인스캔(2 μm 스텝, 총 200 μm), 50× 대물(스팟 ≈5 μm). 두께 정밀도 ≈ **3 nm**(채널 표면 거칠기가 제한 인자).

> **†각주 7**: ⚠ LHAR 구조는 all-silicon 설계로 제작되며, "두 장의 웨이퍼 접합"이 아니다. 또한 실험은 단일 종횡비(AR 2000)에서 수행되었다.

---

## 9. 결과 (Section VIII)

### 9.1 추출된 파라미터 (Table I)

| 재료 | Cycles | H (nm) | $p_{A0}$ (Pa) | **c** | **K (Pa⁻¹)** | $gpc_{sat}$ (pm) | rms 오차 (nm) |
|---|---|---|---|---|---|---|---|
| Al₂O₃ | 500 | 500 | 147 | **0.00572** | **219** | 105.6 | 0.974 |
| TiO₂ | 1000 | 500 | 25.7 | **0.10** | **0.252** | 54.4 | 1.525 |

포화 성장률 환산: $gpc_{sat}=\dfrac{1+Kp_A}{Kp_A}\,gpc$ (식 46).

### 9.2 두 재료의 프로파일 형상이 다르다 — 논문의 핵심 결과

- **Al₂O₃ (Fig. 6)**: 입구부터 침투 깊이 근처까지 **두께가 일정**하다가 급락. c가 작고(0.57%) **K가 매우 큼(219)** → 붙기는 어렵지만 사실상 비가역 → 앞에서부터 차례로 완전 포화.
- **TiO₂ (Fig. 7)**: **어디서도 평탄하지 않고** 깊이에 따라 점진적으로 감소. c가 크고(10%) **K가 매우 작음(0.252)** → 잘 붙지만 잘 떨어짐 → 어느 위치도 완전 포화에 못 미침.

【원문 대조】
> 원 번역본은 "TiCl₄의 낮은 s₀ → 더 우수한 step coverage"라 했으나 **정반대**다. TiO₂의 c(0.10)는 Al₂O₃의 c(0.00572)보다 **약 17배 크고**, TiO₂ 프로파일이 오히려 경사형(덜 이상적)이다.

### 9.3 원인 가설: 반응 부산물

저자들은 프로파일 차이의 근본 원인을 부산물로 본다. TiCl₄/H₂O는 **반응성이 큰 HCl**을 내어 성장 표면과 상호작용하는 반면(Knapas & Ritala 2013), TMA/H₂O는 상대적으로 **불활성인 CH₄**를 낸다(Puurunen 2005). 반응 메커니즘을 알면 Langmuir 식(식 31)을 대체해 더 정확히 피팅할 수 있다.

> **†각주 8**: ⚠ **우리 관점의 핵심 시사점** — MoO₂Cl₂·MoCl₅ 등 할라이드계 금속 전구체는 모두 HCl류 부산물을 낸다. TiO₂에서 관찰된 "경사형 프로파일 + 낮은 K"는 Cl계 Mo ALD의 HAR 거동을 이해하는 직접적 참조점이다. (§12 참조)

---

## 10. 결론 (Section IX)

1. 본 모델은 좁은 채널 내 ALD 두께 분포를 잘 기술하며, 새 소자의 증착 공정 설계·최적화에 사용할 수 있다.
2. 측정 프로파일을 피팅하면 성장 반응 모델의 파라미터(**c, K**)를 얻는다.
3. Langmuir는 최소 모델이며, **식 (31)만 교체하면 임의의 반응 메커니즘으로 확장**할 수 있다. 단, 파라미터가 늘수록 더 방대한 측정 데이터가 필요하다.

---

## 11. 기호 정리

| 기호 | 설명 | 단위 |
|---|---|---|
| $p_A$, $p_{A0}$ | 전구체 분압 / 입구 분압 | Pa |
| $\bar v_A$ | 분자 A 평균 속력 | m/s |
| $D_A$, $D_{Kn}$, $D_{eff}$ | 기상 / Knudsen / 유효 확산계수 | m²/s |
| $D$ | 겉보기 종방향 확산상수 (식 23) | m²/s |
| $h$ | 수력지름 | m |
| $H$, $W$, $L$ | 채널 높이 / 폭 / 길이 | m |
| $c$ | **lumped sticking coefficient** | – |
| $K$ | 흡착 평형상수 | Pa⁻¹ |
| $q$ | 포화 흡착 밀도 | m⁻² |
| $\theta$ | 표면 피복률 | – |
| $P_d$ | 단위시간 탈착 확률 | s⁻¹ |
| $Q$ | 단위 압력당 충돌률 | m⁻²s⁻¹Pa⁻¹ |
| $x_s$, $x_t$ | 선형 압력 외삽 0점 / 선형–지수 접합점 | m |
| $x_p$ | 절반 두께 침투 깊이 | m |
| $gpc$, $gpc_{sat}$ | 사이클당 성장 / 포화 성장 | m |

> **†각주 9**: 원 번역본의 기호 $C_{tp}$, $n_s$, $s_0$, $n_0$, $D_K$, $v_{ads}$는 원 논문 기호 체계와 다르다. 원 논문은 위 표의 기호를 사용한다.

---

## 12. Mo ALD 적용 시사점 (번역자 해설)

> **⚠️ 이 섹션은 원 논문에 없는 내용으로, MoO₂Cl₂ 기반 Mo ALD의 3D NAND 워드라인 적용에 대한 번역자의 도메인 해석이다. 원 논문의 결과와 명확히 구분한다.**

### 12.1 구조 대응

워드라인 충진은 슬릿→수평 리세스의 횡방향 HAR 수송 문제로, LHAR와 기하학적으로 상동이다. 리세스 높이→H, 도달 요구 거리→$x_p$ 목표로 대응하되, ⚠ 채널 홀 기둥과 형상 복잡성 때문에 수력지름 h를 실제 형상으로 재계산하고 tortuosity 보정을 D_eff에 반영해야 한다. 현 세대에서 H가 수십 nm면 완전 Knudsen 영역이므로 식 (4)가 지배한다.

### 12.2 지금 할 수 있는 정량 작업

- 식 (8)로 MoO₂Cl₂(M≈198.9 g/mol)·MoCl₅(M≈273.2 g/mol)의 $d_A$ 추정 → 식 (2),(4),(6)으로 $\bar v_A, D_{Kn}, D_{eff}$ 산출 → TMA와 비교표 작성.
- 식 (9)로 Mo ALD의 q 산출(ρ_Mo≈10.2 g/cm³, 실측 gpc_sat). 고밀도 금속막이라 q가 크므로 도달 $x_p$가 산화막보다 짧다.
- 식 (23)+(19)의 $x_p\propto\sqrt{Dt}$, $D\propto p_{A0}HD_{eff}/q$로 dose·펄스·노드 마진을 계산. **침투 2배엔 펄스 4배**이므로 분압 상향이 1차 레버.

> **†각주 10**: ⚠ MoO₂Cl₂, 300 °C(573 K)에서 $\bar v=\sqrt{8RT/\pi M}\approx$ **247 m/s**다. (원 번역본의 130 m/s는 계산 오류.)

### 12.3 c·K 추출로 Mo 공정 진단

LHAR(또는 등가 구조)에 현행 Mo ALD를 태우고 두께 프로파일을 이 모델로 피팅해 c, K를 얻는다.
- **평탄+급락형(Al₂O₃형)** → 흡착 건전, 수송 제한 → dose/펄스 최적화로 개선.
- **경사형(TiO₂형)** → K 낮음 → ⚠ HCl 부산물 재흡착/사이트 차단 또는 가역성 의심 → 퍼지·압력·온도창·co-reactant 등 **화학**을 우선 손봐야 함(dose 증량은 후순위).

⚠ 부산물 가설 검증: 두께뿐 아니라 깊이별 Cl 잔류(XPS)와 비저항 프로파일을 병행 측정하고, 퍼지/압력 split에서 프로파일 경사 변화를 확인한다.

### 12.4 Mo 비저항·불순물 관점 (도메인 지식)

| 불순물 | 기원 | 저감 방향 |
|---|---|---|
| Cl | MoO₂Cl₂ 잔류 | 충분한 퍼지, 적정 고온 증착 |
| O | O 배위·불완전 환원 | 충분한 H₂ 환원 |

> **†각주 11**: ⚠ 이 표와 비저항 목표(벌크 Mo ≈ 5.3 μΩ·cm)는 원 논문 밖 도메인 지식이다. 원 논문은 Mo·비저항·불순물을 다루지 않으며, Al₂O₃·TiO₂만 검증했다. 이 내용을 "원 논문에서 도출된다"고 인용해서는 안 된다.

### 12.5 gap-fill 예측

식 (35)와 Fig. 4의 입구 폐색은 워드라인 gap-fill의 축소판이다. ⚠ 목표 충진 두께·리세스 높이에서 입구 pinch-off까지 잔여 사이클 수를 예측하면, 다단 dose·억제제(inhibitor) 스킴 설계의 정량 근거가 된다. (원 논문은 "seam"을 다루지 않으므로, seam 논의는 도메인 확장임을 명시한다.)

---

## 참고 문헌 (원 논문 서지 기준)

1. M. Ylilammi, O. M. E. Ylivaara, R. L. Puurunen, "Modeling growth kinetics of thin films made by atomic layer deposition in lateral high-aspect-ratio structures," *J. Appl. Phys.* **123**, 205301 (2018).
2. R. G. Gordon, "A kinetic model for step coverage by atomic layer deposition in narrow holes and trenches," *Chem. Vap. Deposition* **9**, 73–78 (2003).
3. R. L. Puurunen, "Surface chemistry of atomic layer deposition: A case study for the trimethylaluminum/water process," *J. Appl. Phys.* **97**, 121301 (2005).
4. P. Poodt et al., "Effect of reactor pressure on the conformal coating inside porous substrates by ALD," *J. Vac. Sci. Technol. A* **35**, 021502 (2017).
5. F. Gao, S. Arpiainen, R. L. Puurunen, "Microscopic silicon-based lateral high-aspect-ratio structures for thin film conformality analysis," *J. Vac. Sci. Technol. A* **33**, 010601 (2015).
6. K. Knapas, M. Ritala, "In situ studies on reaction mechanisms in atomic layer deposition," *Crit. Rev. Solid State Mater. Sci.* **38**, 167–202 (2013).

---

*교정 방침: 본 문서는 원 논문(PDF)과 1:1 대조하여 서지·수식·실험 조건·피팅 결과를 원문에 맞췄다. ⚠ 표시 항목(특히 §12)은 원 논문 밖 도메인 해석임을 명시한다.*
