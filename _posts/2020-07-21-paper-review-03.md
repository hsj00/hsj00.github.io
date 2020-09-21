---
title: "논문 읽기 03: 'Structural, Optical and Electrical Properties of HfO2 Thin Films Deposited at Low-Temperature Using Plasma-Enhanced Atomic Layer Deposition', Materials (2020), 13, 2008"
layout: post
date: 2020-07-21 19:50
tag:
    - Chemical Engineering
    - Precursor
    - Atomic Layer Deposition
    - ALD
    - Thin Film Deposition
    - Semiconductor
    - Paper
    - Study
    - Note
headerImage: false
image:
description: 200703 `Structural, Optical and Electrical Properties of HfO2 Thin Films Deposited at Low-Temperature Using Plasma-Enhanced Atomic Layer Deposition` paper review
category: blog
author: hsj00
externalLink: true
published: true
comments: true
share: true
use_math: true
---

오늘 `Science`에 게재된 논문[^00] 한 편에 대한 기사[^01][^02]가 올라왔다.

내용을 간략하게 요약하자면, 개별 소자가 1bit의 정보를 저장하는 도메인 역할을 하던 것에서 [HfO2][01] 결정의 산소 원자 4개 묶음으로 1bit를 구현하여 집적도를 대폭 올릴 수 있는 이론적 배경을 [삼성미래기술육성사업][02] 지원을 받아 `UNIST` [이준희 교수 연구실][03]에서 연구 결과물로 내놓은 것이다.

이해를 돕기 위해 기사에 나온 사진을 첨부해본다.

<center>
<img src="https://image.chosun.com/sitedata/image/202007/02/2020070203905_1.png" alt="Scheme image" title="Scheme image">
<br>
<figure><figcaption><b>정보 1비트 저장/처리에 원자 수천개가 필요한 기존 평면 메모리 반도체(왼쪽), 같은 작업을 원자 4개만으로 구현 가능한 새로운 메모리 반도체(오른쪽)</b></figcaption></figure>
</center>

수년내에 상용화를 목표로 추가적인 실험 연구들이 진행될 것으로 보이는데, [HfO2][01]는 이미 반도체 제조 공정에서 쓰이는 물질이기 때문에 막질 제어가 변수가 될지도 모르겠단 생각이 들었다.

[High-K][04] 물질과 관련하여 자세한 내용은 공부한적이 없어서 쉬워보이는 논문 한 편 골라서 읽으며 개략적인 흐름을 파악한 이후에 `Hf` 전구체들 종류를 알아볼까 한다. 전구체별 박막 특성이나 성장 거동을 공부하다보면 지금 개선 방향을 전구체 쪽에서 접근할지 아니면 박막 증착 공정에서 접근할지 알 수 있지 않을까 싶다. 일단 공부 방향은 이런 쪽으로 잡았다.

ToC는 다음과 같다.

- [Structural, Optical and Electrical Properties of HfO2 Thin Films Deposited at Low-Temperature Using Plasma-Enhanced Atomic Layer Deposition](#structural-optical-and-electrical-properties-of-hfo2-thin-films-deposited-at-low-temperature-using-plasma-enhanced-atomic-layer-deposition)
  - [Abstract](#abstract)
  - [1. Introduction](#1-introduction)
  - [2. Materials and Methods](#2-materials-and-methods)
  - [3. Results and Discussion](#3-results-and-discussion)
  - [4. Conclusions](#4-conclusions)
  - [Note](#note)

---

# Structural, Optical and Electrical Properties of HfO2 Thin Films Deposited at Low-Temperature Using Plasma-Enhanced Atomic Layer Deposition

서지 정보는 다음과 같다

-   `Open Access`, `Article`
-   `Materials` 2020, 13(9), 2008
-   https://doi.org/10.3390/ma13092008

---

## Abstract

초록에는 박막 특성 비교를 위해 선택한 증착 방법, 증착 방법에 따른 ALD window의 이동, 80℃에서 증착한 박막 각각의 밀도와 특징, 굴절률과 광학 밴드갭의 비교, 누설 전류 감소 효과와 PET 필름 적용 가능성, 커패시턴스의 차이 등에 대해 요약해놨다.

일단 온도 조건에 따른 성장 거동과 특성 변화, 전기적 특성 쪽에 초점을 두고 읽어보겠다. 다음에 리마인드할 수 있게 논문 내용의 요약이나 서술 위주로 작성해본다.

## 1. Introduction

도입부에서는 반도체 산업의 흐름과, 그로인해 high-k 물질이 중요해진 이유에 대해서 언급하고있다.

웨어러블 기기가 주목을 받으며 낮은 온도에서의 증착 필요성이 높아졌고, 그에 대한 여러 연구들이 있었지만 막질이나 박막 내 잔여 탄소 불순물이 문제가 됐다고 한다. HfO<sub>2</sub> ALD는 일반적으로 200℃에서 진행되는데, 전구체가 고온에서 완전히 분해되기 때문에 그렇다고 한다.[^ref11] 그래서 플라즈마를 이용한 Oxygen radicals를 이용해 문제를 해결하는 쪽으로 방향을 잡았고[^ref17], 전기화학적으로 O<sub>3</sub>와 Oxygen radical의 oxidation potential 값을 비교하며 근거로 삼고있다. (Oxygen radical: 2.42V, O<sub>3</sub>: 2.08V)[^ref18], [^ref19], [^ref20] ALD 공정에서 electrochemical oxidation potential은 산화 반응의 민감함과 ligand-decomposing power를 나타낸다고 한다.[^ref21], [^ref22], [^ref23], [^ref24] 높은 oxidation potential을 가질수록 낮은 온도에서의 공정을 가능하게 하는데, 전구체 소스의 분해에 필요한 열에너지가 적게 필요하기 때문이라고 한다.[^ref16]

oxidation potential과 전구체의 반응성에 대해서 깊게 생각해본적은 없는데, 더 높은 포텐셜을 가질수록 더 낮은 온도에서의 공정이 가능하다는 내용은 ALD 장비를 다뤄보며 경험적으로 익힌 사실과 부합한다. 연구실에 있을 때 전기화학 내용을 접할 기회가 있었는데 그때 열심히 공부할걸....

논문에서 다루는 내용들은 다음과 같다

-   Compare with properties by using Thermal-ALD, PE-ALD at 80, 150 and 250℃
    -   film structure, surface morphology, surface compenents
    -   densities, refractive index, optical bandgap (deposited at 80℃)
    -   electrical characteristics of MOS capacitor (C-V, I-V, Q<sub>f</sub>)

## 2. Materials and Methods

실험에 사용된 물질과 장비들, 분석 조건들이 정리되어있다. 해당 내용을 표로 작성해서 정리해보았다.

| Materials & Methods        | note                                                                                 |
| -------------------------- | ------------------------------------------------------------------------------------ |
| ALD system                 | automated ALD system / iCV d300 (ISAC Research)                                      |
| Substrate                  | p-type doped Si (100) wafer (ρ ~ 15Ωcm)                                              |
|                            | Ultrasonic cleaning: 10min acetone -> 10min ethanol -> 10min IPA                     |
|                            | Ar blowing dry: immediately drying                                                   |
|                            | loaded in a range of 80-250℃                                                         |
| Main pump                  | base pressure ~10mtorr / MVP-90 (WOOSUNG VACUUM PUMP)                                |
| By-pass pump               | for constant flow / ISP-90 (ANEST IWATA Corporation)                                 |
| Plasma generator           | direct, 150W, 13.56MHz RF power supply / REX2-3K (RF Power Tech)                     |
| Hf precursor               | Tetrakis(ethylmethylamino)hafnium (TEMAH) 99.999%, (UP Chemical)                     |
| Canister                   | maintained at 75℃                                                                    |
| Flow line/Chamber          | maintained at 80℃                                                                    |
| Ozone generator            | LAB-II (Ozonetech)                                                                   |
| Carrier/Purge gas          | Ar gas 99.999%                                                                       |
| Spectroscopic Ellipsometry | thickness, refractive index and absorption coefficient / SE M2000D (J.A. WOOLLAM CO) |
| Reflectometer              | thickness / ST2000 (K-MAC)                                                           |
| XRD/XRR                    | film structure and density / Cu Kα radiation GIXRD/MXD10 (Rigaku)                    |
| AFM                        | RMS roughness / XE7 (Park Systems)                                                   |
| XPS                        | chemical bonding states and components / K-Alpha+ (Thermo Fisher Scientific)         |
|                            | to remove carbon- and nigrogen-contaminant layers from air                           |
|                            | ~7 to 10nm, removed via Ar etching, at 1keV, for 30s [^ref25], [^ref26]              |
| UV-vis spectroscopy        | transmittance, 190~1100nm normal incidence / HP8453 (Agilent)                        |
|                            | HfO<sub>2</sub> (50nm) at 550nm on the PET substrate (ST510, DuPont Teijin Films)    |
| I-V, C-V                   | MOS capacitor electrical properties, Manual Probe Station / SUMMIT 11862B (Cascade)  |
|                            | C-V: 1MHz, -7 to +7V, I-V: -2 to +2V                                                 |
| E-beam evaporator          | Cu/Ti top electrodes using shadow mask / KVET-C500200 (Korea Vacuum)                 |

## 3. Results and Discussion

fig.1은 박막의 증착 거동 검증 내용을 다루고 있다. 전구체 공급 시간, 반응물 공급 시간, 퍼지 시간, 플라즈마 작동 시간 등을 고려하여 ALD 공정 조건을 결정한 후 GPC와 ALD window 확인 실험을 진행했다. PE-ALD와 Thermal-ALD의 ALD window 온도 범위가 차이나는 이유는 반응에 필요한 에너지를 충분히 공급하느냐와 관련이 있다. Thermal-ALD의 경우, ALD window보다 낮은 온도에서는 condensation이, 높은 온도에서는 thermal decomposition이 일어나게된다. 공급되는 열은 곧 반응에 필요한 에너지와 같다고 볼 수 있기 때문에 Thermal-ALD에선 온도가 올라갈수록 GPC도 같이 올라간다. PE-ALD의 경우, O2 plasma가 낮은 온도에서도 안정적으로 증착할 수 있을만큼 높은 반응성을 가지고 있는 반면, 온도가 올라갈수록 plasma의 ion energy가 HfO<sub>2</sub> 표면 etching에 기여해서 GPC가 내려간다. [^ref27], [^ref28]

| Type        | Recipe (Source-Purge-Reactant-Purge)                   | ALD window Temp. (℃) |
| ----------- | ------------------------------------------------------ | -------------------- |
| Thermal-ALD | 2s - 15s - 1.5s - 15s                                  | 150-200              |
| PE-ALD      | 3s - 25s - 1.5s - 1.5s (O<sub>2</sub> plasma-on) - 25s | 80-150               |

fig.2는 박막의 결정성과 밀도, 표면 거칠기에 대한 내용을 다루고 있다. 250℃ PE-ALD를 제외한 모든 증착 조건에서 amorphous 구조를 갖는 것을 확인할 수 있었다.[^ref30] 같은 온도에서 PE-ALE가 Thermal-ALD보다 결정성이 조금 더 좋았고, 250℃ PE-ALD는 polycrystalline한 구조를 갖는다. PE-ALD가 Thermal-ALD보다 낮은 온도에서 결정질의 박막을 얻는다는 것을 알 수 있다.[^ref31] fig.2(c)는 XRR 분석 그래프로서 박막의 두께와 밀도를 나타낸다. PE-ALD 박막이 더 밀도높은 박막을 형성하는 것을 알 수 있다. fig.2(d)-(f)보면 박막 표면의 거칠기를 알 수 있는데, 80℃에선 둘 다 비슷한 정도의 RMS를 갖고, 온도가 올라갈수록 표면의 거칠기와 결정 형성 정도느 증가하게 된다.[^ref32]

fig.3은 50nm 두께의 박막을 XPS로 분석한 결과들을 보여준다. 박막 성분들의 결합 에너지 deconvolution을 통해서 박막이 얼마나 stoichimetric한지, oxidative condition등을 알 수 있다. Hf 4f spectra deconvolution의 경우, 18.31, 19.99eV 위치에서 peak point를 보고 HfO<sub>2</sub>와 연관지어 해석하고[^ref33], 16.93, 18.63eV에 위치한 suboxide peak은 HfO<sub>2-x</sub>와 연관지어 해석한다. 낮은 온도에서 Thermal-ALD 박막의 경우, 많은 결함과 C, N, -OH 불순물이 박막 내에 자리하고 있기 때문에 Hf 구성 비율이 낮게 나타난다. 낮은 온도에서 증착한 PE-ALD 박막은 높은 온도에서 증착한 Thermal-ALD와 큰 차이를 보이지 않았다. O1s peak의 deconvolution은 HfO<sub>2</sub>와 관련있는 530.03eV, C-O와 관련있는 531.68eV 두 위치에서 peak position을 잡고 해석한다[^ref33]. C-O peak은 O와 C impurity가 결합된 결함과 연관있고, 전자기기의 성능과 효율 감소의 원인이 된다[^ref34], [^ref35]. 이 결과를 보면, 두 Thermal/PE-ALD 모두 증착 온도가 올라갈수록 C-O peak은 감소 경향을 보인다. XPS binding energy 결과를 볼 때, 전체 온도 범위에서 PE-ALD 박막이 Thermal-ALD 박막보다 stoichimeric한 박막을 형성한다.

fig.3(e)는 박막 표면의 조성비를 나타내는데, C와 N은 박막 내에서 결함으로 작용하여 밀도를 낮추고 특성을 감소시키는 역할을 한다. 80℃ Thermal-ALD 박막에서 C와 N의 비율이 높은 것을 보면, 전구체가 증착 후 완전히 분해되지 않았다고 볼 수 있다. 그러나 80℃ PE-ALD의 경우 매우 낮은 C, N 비율을 갖는데, 전구체와 반응할 때 O<sub>2</sub> plasma가 O<sub>3</sub>보다 분해력이 크다고 볼 수 있다. 이를 통해 낮은 온도에서 Thermal-ALD 박막보다 PE-ALD 박막의 결함이 더 적다고 결론내릴 수 있다.

fig.4는 80℃에서 증착한 50nm 두께의 박막을 분석한 결과다. fig.4(a)는 Photon energy (eV)의 함수 그래프로 굴절률(n)과 흡광계수(k) 결과를 나타낸다. 굴절률(n)과 흡광계수(k)는 엘립소미터를 이용해 유전함수(ε = ε<sub>1</sub> + iε<sub>2</sub>)의 실수부와 허수부 계산으로 구했다[^ref36]. 굴절률(n)은 박막의 밀도와 연관있는데[^ref37], [^ref38], PE-ALD HfO<sub>2</sub>는 탄소 함량이 낮고 O/Hf 비율이 Thermal-ALD HfO<sub>2</sub>보다 낮기 대문에 모든 photon energy range에서 더 높은 밀도를 갖고, 더 큰 굴절률(n)을 갖는다.

fig.4(b)는 흡수계수(absorptioncoefficient, α = 4πk/λ)를 이용해 구한 optical band gap 값이다. 이전 연구들[^ref39], [^ref40]에서 밴드갭은 5.6에서 5.7eV였는데, Thermal-ALD HfO<sub>2</sub>의 밴드갭은 5.1eV로 낮게 나왔다. 반면 PE-ALD HfO<sub>2</sub>의 밴드갭은 5.6eV로 커지는 것을 볼 수 있었다. Optical band gap이 작을 경우 절연체로 기능할 수 없다. Tauc method를 사용해 optical band gap이 도시되고, 그 식[^ref41]은 다음과 같다. 수식에서 밴드갭만 놔두고 이항시킨 후 직선으로 fitting해서 구하는 방식을 쓴 것 같다.

(αhν)<sup>1/2</sup>=A(hν−E<sub>g</sub>)

-   흡수계수, absorption coefficient: α = 4πk/λ
-   플랑크 상수, Planck's constant: h
-   광자 진동수, Photon frequency: ν
-   비례상수, Proportionality constant: A
-   광학밴드갭, Optical band gap: E<sub>g</sub>

fig.4(c)는 80℃에서 50nm 두께로 PET 기판 위에 박막을 증착하여 투과율을 측정한 결과를 보여준다. 80℃에서 증착한 이유로는 아무래도 PET 기판의 열분해나 변형을 방지하기 위해서 그런 것 같다. PE-ALD 박막은 가시광선 영역대에서도 84% 이상의 높은 투과율을 보였다. 550nm 파장대에서 Bare PET는 89.7%, Thermal-ALD 샘플은 87.2%, PE-ALD 샘플은 84.3%의 투과율을 보였다. PE-ALD 박막에서 근소하게 투과율이 낮은 이유는 박막이 상대적으로 높은 밀도를 갖기 때문이다[^ref42].

fig.5는 전기적 특성을 측정한 그래프들을 보여준다. 박막의 두께는 모두 10nm로 보인다. fig.5(a), (b)는 Thermal-ALD/PE-ALD 박막의 Capacitance-Voltage curve를 나타낸다. PE-ALD 박막의 경우 커패시턴스가 444.9nF/cm<sup>2</sup>에서 540.1nF/cm<sup>2</sup>까지 약 21% 증가했다. 유전상수(dielectric constant, κ-value)의 경우, 80℃ PE-ALD 박막은 12.6으로 Thermal-ALD 박막의 8.7보다 큰 값을 갖는다. 유전상수를 계산할 때 native oxide (~3nm)의 두께를 고려해서 계산했다고 한다[^ref43], [^ref44]. 커패시턴스 값을 이용해 유전상수를 계산하는 방법도 있다. 다음 식을 따라서 계산하면 구할 수 있다. 아래 식에서 C<sub>OX</sub>는 MOS 커패시터의 overall capacitance를 의미한다. 온도에 따라 값이 유의미하게 변하지는 않았다고 한다.

$$
{\frac{1}{C_{HfO_2}}} = {\frac{1}{C_{OX}}} - {\frac{1}{C_{SiO_2}}}
$$

fig.5(c), (d)는 Thermal-ALD/PE-ALD 박막의 Current-Voltage curve를 나타낸다. negative voltage에서 누설 전류를 보면, PE-ALD 샘플이 Thermal-ALD 샘플보다 전체적으로 낮은 전류값을 갖는다는걸 알 수 있다. 80℃에서 보면, Thermal-ALD 샘플은 1.4 x 10<sup>-2</sup>A/cm<sup>2</sup>의 전류밀도를 갖지만 PE-ALD 샘플은 2.5 x 10<sup>-5</sup>A/cm<sup>2</sup>로 현저하게 낮은 값을 갖는걸 알 수 있다. 250℃의 Thermal-ALD 샘플보다 작은 전류밀도 값임을 그래프를 통해 알 수 있다. 그 이유로는, 낮은 온도에서 PE-ALD로 증착한 박막은 상대적으로 더 높은 밀도와 적은 오염물질을 갖기 때문이다[^ref45]. p-type Si 기판을 사용해 NMOS capacitor 구조로 샘플을 만들고, 표면에서의 depletion layer는 전압이 +일 때 형성된다. 이 샘플에서, 커패시터가 inversion state이기 때문에 전류가 거의 흐르지 않는다.

_**MOS 커패시터 구조 관련해서 공부한지 너무 오래된 탓에 정확한 내용이 기억이 안나서 해당 내용들은 나중에 전공책을 따로 복습하고 정리해야겠다.**_

fig.5(e)는 Capacitance-Voltage curve에서 추출한 플랫 밴드 전압 (V<sub>fb</sub>)과 고정 전하 밀도 (Q<sub>f</sub>)를 나타낸다. 80℃ PE-ALD 샘플의 V<sub>fb</sub>는 같은 온도에서 증착한 Thermal-ALD 샘플보다 작은 값을 갖는다. 그리고 Q<sub>f</sub>는 80℃ PE-ALD 샘플에서 9.5 x 10<sup>12</sup>cm<sup>-2</sup>를 갖고, 250℃ PE-ALD 샘플에서 1.0 x 10<sup>12</sup>cm<sup>-2</sup>으로 90% 가까이 감소하는 것을 확인할 수 있다. 80℃를 제외한 모든 온도에서 V<sub>fb</sub>와 Q<sub>f</sub>는 거의 동일한 값을 보여줬다.

Q<sub>f</sub>는 (+) 전하를 가지며 Si와 HfO<sub>2</sub> 박막 사이의 접합 지점에 분포하는데, 이는 장치를 (+) 상태로 만들어 더 높은 전압에서 작동하게 한다. 이는 약 80 °C의 저온에서 PE-ALD HfO<sub>2</sub> 커패시터는 Thermal-ALD HfO<sub>2</sub> 커패시터보다 전기적 특성이 더 우수함을 시사한다. 그러나 PE-ALD HfO<sub>2</sub>의 Q<sub>f</sub> 값은 온도가 상승함에 따라 상승하는 경향이 있었다. 증착 온도가 높아지면서 증착 과정에서 플라즈마 이온 에너지가 증가해 기판이 손상됐다는 의미다[^ref46], [^ref47].

## 4. Conclusions

이 연구에선 80℃ 증착 조건에서 O<sub>2</sub> 플라즈마를 이용한 PE-ALD HfO<sub>2</sub>가 Thermal-ALD HfO<sub>2</sub>보다 나은 특성을 보여주는 것을 확인했다. PE-ALD의 ALD window는 Thermal-ALD 의 ALD window보다 저온에서 형성되는 것을 확인했고, 그로인해 저온에서 안정적인 증착이 가능했다. 저온에서 PE-ALD의 증착 박막은 Thermal-ALD 증착 박막보다 평탄한 표면과 높은 밀도를 보였고, C나 N처럼 박막 내 오염물질의 양도 감소했다. PE-ALD HfO<sub>2</sub> 박막은 굴절률 증가, optical band gap 향상 (5.6eV), 약 84%의 높은 투과율을 보였다. 높은 밀도와 적은 불순물을 갖는 PE-ALD HfO<sub>2</sub> 박막은 약 21%의 커패시턴스 향상, 2.5 x 10<sup>-5</sup>A/cm<sup>2</sup>의 낮은 누설 전류, 1.0 x 10<sup>12</sup>cm<sup>-2</sup>의 가장 낮은 고정 전하 밀도를 갖는 것을 확인했다. 그 결과, O<sub>2</sub> 플라즈마의 높은 분해력에 의해 저온에서 증착된 PE-ALD HfO<sub>2</sub>는 Thermal-ALD HfO<sub>2</sub>와 비교해 향상된 특성들을 갖는 것으로 확인됐다.

## Note

이 논문을 읽으면서 HfO<sub>2</sub>의 박막 증착 방법이나 특성들에 대해서 대략적으로 가늠해볼 수 있었다. 실험 조건이나 측정 조건들도 비교적 상세하게 나와있어서 비슷한 실험을 진행할 때 많은 도움이 될 것 같다. 막질을 위해서는 PE-ALD가 나은 선택이지만 기판 표면에 손상이 생길 가능성이 있다는 점이 유연 기판 소재에 적용할 때 신경써야할 부분이 아닐까 싶다. PE-ALD의 경우, 이 논문에서는 한 cycle당 걸리는 시간이 Thermal-ALD보다 많이 걸려서 경제성에서 손해를 볼 수밖에 없다. 대용량의 양산형 장비에선 더 나은 증착 퍼포먼스를 보여줄거라고 생각하지만 전구체나 부산물의 purge가 쉽지 않은 경우라면 어떻게 해야할까? 펌프의 성능 향상이나 챔버 디자인 개량으로 한계가 있을텐데, 결국 열에 안정적이고 기화가 잘되는 전구체일수록 유리하지 않을까? 논문들을 좀 더 찾아봐야겠다. 짬짬이 논문 읽는 속도를 높일 방법을 고민해야봐야지.

<!-- references -->

[^00]: <https://doi.org/10.1126/science.aba0067>{: target="\_blank"}
[^01]: <https://biz.chosun.com/site/data/html_dir/2020/07/02/2020070203923.html?utm_source=naver&utm_medium=original&utm_campaign=biz>{: target="\_blank"}
[^02]: <https://bit.ly/2Zp8kOH>{: target="\_blank"}
[^ref11]: <https://doi.org/10.5757/ASCT.2016.25.3.56>{: target="\_blank"}
[^ref17]: <https://doi.org/10.1038/srep40061>{: target="\_blank"}
[^ref18]: <https://doi.org/10.29356/jmcs.v58i3.133>{: target="\_blank"}
[^ref19]: <https://doi.org/10.1007/s11270-009-0065-1>{: target="\_blank"}
[^ref20]: <https://doi.org/10.1007/978-3-540-79210-9_4>{: target="\_blank"}
[^ref21]: <https://doi.org/10.1116/1.3609974>{: target="\_blank"}
[^ref22]: <https://doi.org/10.1116/1.4937991>{: target="\_blank"}
[^ref23]: <https://doi.org/10.1039/C4CC08004A>{: target="\_blank"}
[^ref24]: <https://doi.org/10.3390/ma12162605>{: target="\_blank"}
[^ref16]: <https://doi.org/10.3390/cryst10020136>{: target="\_blank"}
[^ref25]: <https://doi.org/10.1116/1.590296>{: target="\_blank"}
[^ref26]: <https://doi.org/10.1016/j.elspec.2008.10.004>{: target="\_blank"}
[^ref27]: <https://doi.org/10.1016/B978-0-444-63304-0.00027-5>{: target="\_blank"}
[^ref28]: <http://www.jkps.or.kr/journal/download_pdf.php?doi=10.3938/jkps.51.978>{: target="\_blank"}
[^ref30]: <https://doi.org/10.1007/s13391-015-4490-6>{: target="\_blank"}
[^ref31]: <https://doi.org/10.3390/cryst8060248>{: target="\_blank"}
[^ref32]: <https://doi.org/10.1016/j.apsusc.2019.144188>{: target="\_blank"}
[^ref33]: <https://doi.org/10.1155/2009/439065>{: target="\_blank"}
[^ref34]: <https://doi.org/10.1109/PVSC.2010.5616552>{: target="\_blank"}
[^ref35]: <https://doi.org/10.1063/1.1728089>{: target="\_blank"}
[^ref36]: <https://doi.org/10.1063/1.1448384>{: target="\_blank"}
[^ref37]: <https://doi.org/10.1016/j.carbon.2017.02.023>{: target="\_blank"}
[^ref38]: <https://doi.org/10.1016/j.ceramint.2014.05.148>{: target="\_blank"}
[^ref39]: <https://doi.org/10.1063/1.2697551>{: target="\_blank"}
[^ref40]: <https://doi.org/10.1088/0268-1242/22/5/011>{: target="\_blank"}
[^ref41]: <https://doi.org/10.1002/pssb.201552007>{: target="\_blank"}
[^ref42]: <http://www.revistacubanadefisica.org/index.php/rcf/article/view/RCF_2017_34_2_125>{: target="\_blank"}
[^ref43]: <https://doi.org/10.1007/s13204-018-0866-x>{: target="\_blank"}
[^ref44]: <https://doi.org/10.3390/mi10060361>{: target="\_blank"}
[^ref45]: <https://doi.org/10.1149/2.0111907jss>{: target="\_blank"}
[^ref46]: <https://www.narcis.nl/publication/RecordID/oai:ris.utwente.nl:publications%2F98229008-f336-4329-acd6-c964bb1787fd>{: target="\_blank"}
[^ref47]: <https://doi.org/10.1063/1.1590418>{: target="\_blank"}

<!-- links -->

[01]: https://en.wikipedia.org/wiki/Hafnium_dioxide
[02]: https://www.samsungstf.or.kr/guid/matr/openPage.do?pageId=020201
[03]: https://junhee.wixsite.com/qmec
[04]: https://en.wikipedia.org/wiki/High-%CE%BA_dielectric

---

<!-- pictures -->
