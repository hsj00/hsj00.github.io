---
title: "Wonik IPS products note"
layout: post
date: 2019-10-25 21:45
tag:
    - ALD
    - Atomic Layer Deposition
    - CVD
    - Chemical Vapor Deposition
    - Semiconductor
    - Study
    - Note
    - Wonik IPS
headerImage: false
image:
description: 191025 `Wonik IPS` interview study note
category: blog
author: hsj00
externalLink: true
published: true
comments: true
share: true
use_math: false
---

작년에 면접 준비할겸, 반도체 장비 업계 관련 공부도 할겸 겸사겸사 조사하며 정리한 내용을 공개 포스팅으로 전환한다.

반도체 장비 위주로만 조사했고, 디스플레이나 태양전지쪽 장비들은 추가하진 않았다. 대부분 범용적으로 사용할 수 있는 장비들일테니 구체적인 내용에선 차이가 있더라도 큰 틀에선 차이가 없을거라고 생각한다.

최신 내용이 반영된건 아니지만 나중에 기회가 되면 업데이트해서 다시 정리해볼까 싶다.

ToC는 다음과 같다.

- [1. Semidonductor](#1-semidonductor)
  - [(1). WIDAS](#1-widas)
    - [Introduction](#introduction)
    - [Features](#features)
  - [(2). NOA ALD](#2-noa-ald)
    - [Introduction](#introduction-1)
    - [Features](#features-1)
  - [(3). GEMINI HQ](#3-gemini-hq)
    - [Introduction](#introduction-2)
    - [Features](#features-2)
  - [(4). GEMINI ALD (Kairos PE-ALD)](#4-gemini-ald-kairos-pe-ald)
    - [Introduction](#introduction-3)
    - [Features](#features-3)
  - [(5). GEMINI ALD](#5-gemini-ald)
    - [Introduction](#introduction-4)
    - [Features](#features-4)
  - [(6). HYETA (HyEtaTM Spatial ALD)](#6-hyeta-hyetatm-spatial-ald)
    - [Introduction](#introduction-5)
    - [Features](#features-5)
  - [(7). NOA CVD](#7-noa-cvd)
    - [Introduction](#introduction-6)
    - [Features](#features-6)
  - [(8). QUANTA](#8-quanta)
    - [Introduction](#introduction-7)
    - [Features](#features-7)

----------

![Wonik line-up][00]

## 1. Semidonductor

### (1). WIDAS

-   Thermal system

-   relate: [HYETA](#6-hyeta-hyetatm-spatial-ald), [QUNATA](#8-quanta)

-   Process: Oxidation, Anneal, Alloy, PI bake, Poly, ALD Ox/SiN
-   Applications: STI, Mask, Gap fill, Liner, Spacer, Buffer

#### Introduction

-   <b>WINAS(Diffusion ALD)</b>의 확장 플랫폼
-   배치당 처리 능력 향상
    -   배치당 생산성 능력을 극대화하여 장비 투자 및 유지 비용을 크게 절감
-   더 향상된 핵심 모듈 기술 적용 (Heater, Robot, Controller)
    -   뛰어난 온도 제어 기술 및 독창적이고 안정적인 Chamber 구조를 통하여 균일한 박막형성과 Particle 및 Metal Impuritiy 억제를 극대화

#### Features

-   High productivity : up to 175 wafers per batch
-   High precision temperature / pressure control technology
-   Excellent film thickness uniformity (Within Wafe(WiW), Wafer to Wafer(WtW), Batch to Batch?(BtB)
-   Excellent step coverage (>95%)
-   Fast ramp up & down heater
-   Reliable mechtronics

![widas][01]

---

### (2). NOA ALD

-   ALD deposition

-   relate: [QUANTA](#8-quanta), [HYETA](#6-hyeta-hyetatm-spatial-ald)

-   Process: Ti/ALD–TiN, ALD-TiN, ALD-W, TOT (TiN/Ox/TiN)
-   Applications: Capacitor, Worldline, Plugs, Metal contact, MG

#### Introduction

-   필요에 따라 다양한 조건별 플랫폼으로 확장 가능
    -   하나의 장비에 여러 공정을 적용함으로서 통합적 공정이 가능
-   금속 박막 공정을 통합 사용할 수 있는 고유 기능
-   Ti/Tin, Tungsten, Clean step등을 단일 시스템으로 통합할 수 있는 확장성
    -   점점 미세화 기술 노드로 이동하기 때문에 더욱 작은 contact, Via, WL 등 금속 배선을 균일하게 박막하는 것이 점점 어려워짐
    -   기존 텅스텐 (W) 공정에 비해 불소 함량이 매우 낮고 저항성이 낮은 ALD-W 공정에 대한 솔루션을 제공
    -   Contact, Via, Plug 등 금속 배선 공정에 필요한 Tungsten 박막을 증착
    -   TiN (DRAM용 캐패시터 전극)과 TiN(DRAM/Logic/3D NAND용 Barrier 금속막)을 형성

#### Features

-   Able to Configure In-line Process Modules For Optimum Integration
-   Higher UPEH with Smaller Footprint (6 to 10 Process Modules)
-   Excellent Reliability ALD
-   Excellent Step Coverage (> 95%)
-   Excellent Gap Fill Performance
-   Uniformity Unif (ALD TiN < 1%)
-   Low Cl Content (ALD TiN < 0.5at%)
-   Low F Content (LFW <5.0E17atoms/cc )

![NOA ALD][02]

---

### (3). GEMINI HQ

-   PECVD deposition

-   relate: [NOA ALD](#2-noa-ald), [GEMINI ALD](#5-gemini-ald)

-   Process: SiON, A-Si, [TEOS]
-   Applications: Anti Reflective Coating, Hardmask Dielectric

#### Introduction

-   PE-CVD로 반사막 (Anti-Refective Coating) 및 하드마스크 (Hardmask)와 같은 유전막 필름 형성
-   a-Si 박막은 20nm 노드 이하의 첨단 DRAM 및 Logic 디바이스에서 더블/쿼드로플 패터닝 (DPT/QPT) 하드마스크 용도로 사용
-   공정 미세화로 디바이스 노드가 축소됨에 따라 CD (Critical Dimensions) 영향으로 인해 장치 불량으로 이어질 수 있으므로 균일성 (uniformity)이 중요
-   반도체 소자 절연 기능을 구성하는 데 유전막이 후속 레이어에 영향을 미치기 때문에 매우 부드럽고 균일한 박막을 필요

#### Features

-   High Throughput
-   Extreme Thickness Uniformity (TEOS/SiON - <0.5%)
-   Excellent Tool Matching
    　 → User Friendly New S/W, Distribution Control System, Ether-CAT
-   Process Reliability
    　 → TCS, Precision Moving Assembly
-   Wide TEOS Process Window(Thin to Ultra High Thickness with ESC for Backside Deposition free)

![GEMINI HQ][03]

---

### (4). GEMINI ALD (Kairos PE-ALD)

-   PEALD deposition

-   relate: [HYETA](#6-hyeta-hyetatm-spatial-ald), [GEMINI HQ](#3-gemini-hq)

-   Process: ALD Oxide, SiN_Ternary oxide
-   Applications: Patterning (Spacer for SADP/QP), Hardmask, Liner, Gap fill

#### Introduction

-   여러 패터닝을 증착하는 필름은 CD (Critical Dimension)을 형성하기에 이는 매우 중요한 역할
-   매우 균일한 박막으로 다중 패터닝 애플리케이션을 위한 솔루션을 제공
-   작은 장비 면적과 높은 생산성(UPEH), 매우 뛰어난 균일성으로 여러 경쟁 모델보다 우수한 성능
-   웨이퍼 맵 프로필(map profile) 변경에서 다양한 Knob을 가지고 있으며 하드웨어 변경 없이 간편하게 공정 온도 변경이 가능

#### Features

-   Carefully designed chamber, swappable process kits and pumping system for minimal defect and easy maintenance.
-   Edge and backside control by edge flow and vacuum chucking system: Less edge defect and more DOF(Depth of Field) margin.
    -   High etch selectivity
    -   smooth film surface
    -   adjustable film stress are controled by composition rate

![GEMINI ALD (Kairos PE-ALD)][04]

---

### (5). GEMINI ALD

-   ALD deposition

-   relate: [NOA CVD](#7-noa-cvd), [NOA ALD](#2-noa-ald)

-   Process: ALD Oxide
-   Applications: Patterning (Spacer for SADP/QP), Hardmask, Liner, Gap fill

#### Introduction

-   여러 패터닝을 증착하는 필름은 CD (Critical Dimension)을 형성하기에 이는 매우 중요한 역할
-   매우 균일한 박막으로 다중 패터닝 애플리케이션을 위한 솔루션을 제공
-   작은 장비 면적과 높은 생산성(UPEH), 매우 뛰어난 균일성으로 여러 경쟁 모델보다 우수한 성능
-   웨이퍼 맵 프로필(map profile) 변경에서 다양한 Knob을 가지고 있으며 하드웨어 변경 없이 간편하게 공정 온도 변경이 가능
-   기기 노드가 점점 복잡해짐에 따라 더욱 많은 패터닝과 노광 스텝으로 인해 여러 제약사항이 발생
-   ALD-Oxide는 DRAM 및 Logic 디바이스 제조에 필요한 패터닝 스페이서를 사용하여 해결책 제공
-   SADP(Self-aligned Double Patterning) 및 SAQP(Self-aligned Quadruple Pattern) 용도에 사용

#### Features

-   High Throughput
-   Extreme Thickness Uniformity (ALD Oxide - <0.2%)
-   Excellent Tool Matching
    →User Friendly New S/W, Distribution Control System, Ether-CAT
-   Process Reliability
    →High Speed RF Matching, Precision Moving Assembly

![GEMINI ALD][05]

---

### (6). HYETA (HyEtaTM Spatial ALD)

-   ALD deposition

-   relate: [WIDAS](#1-widas), [NOA ALD](#2-noa-ald)

-   Process: SIO2 Seamless Gap Fill, ZrO2, AlO
-   Applications: DRAM Capacitor, 3D NAND Block Oxide Layer, High Temperature SiO2(→3D NAND Channel Hole Gap Fill)

#### Introduction

-   향후 기술 노드를 위한 지속적인 공정 미세화 시 등가산화물 두께(Equivalent-Oxide-Thickness) 감소가 필요
    -   유전막의 EOT를 만족시키기 위해 HfO2, ZrO2 또는 Al2O3 유전체제와 같은 high-k 재료를 기기에 사용
    -   SGF(Seamless Gap-Fill)의 경우, 3D 아키텍처가 널리 채택됨에 따라 SOD(Spin on Dielectrics)와 유동성 있는 산화물과 같은 현재의 gap-fill 기술은 낮은 품질의 gap-fill 재료와 관련된 많은 문제에 직면
-   새로운 ALD 기술을 기반으로 하는 conformal한 박막으로 gap-fill뿐만 아니라 보편적인 박막증착을 위한 새로운 솔루션을 제공하도록 설계
    -   기존 ALD 공정에서 균일성과 매끄러운 gap-fill을 위해 추가 물질을 활용
    -   공간 분할 컨셉으로 증착 공간이 분리되어 서로 다른 공정가스가 혼합되지 않아 high-k 와 SGF(Seamless Gap-Fill) 공정의 다양한 화학물질을 결함없이 사용 가능하게 함
    -   작은 공간에서 높은 생산성을 제공하기 위해 한 번에 6개의 웨이퍼를 처리하는 미니 배치 시스템을 적용
-   독립적 샤워 헤드와 이중 펌핑 시스템 컨셉으로 다양한 증착 공정과 용도에 최적화
    -   특수 Susceptor, 히터 및 리드 온도 제어 시스템을 통해 300~700°C의 광범위한 온도에서 웨이퍼를 처리할 수 있으며 공정 제어와 다기능성을 제공

#### Features

-   High Throughput
-   High RPM (240RPM)
-   High Process Temprature (HK_ZrO2 : <500℃ ,HK_AlO : <680℃ , SGF : <680℃)
-   Minimal Defect
-   Good Film Quality
-   Excellent Step Coverage @50:1, Hole Pattern
-   Excellent Gap Fill Performance: Void Free @130:1, Hole Pattern \_SGF

![HYEATA][06]

---

### (7). NOA CVD

-   CVD deposition

-   relate: [QUANTA](#8-quanta), [NOA ALD](#2-noa-ald)

-   Process: CVD-Ti/TiN, CVD-TiN, CVD-W, SGW(Seamless Gap Fill W)
-   Applications: Via, Metal Contact, Barrier material

#### Introduction

-   다양한 금속 박막 공정을 통합 사용할 수 있는 유일한 고유 기능
-   사용자 필요에 따라 NOA는 다양한 조건별로 플랫폼을 확장
    -   Ti/TiN, Tungsten, Clean step 등을 단일 시스템으로 통합할 수 있는 확정성 (하나의 장비에 여러 공정을 적용함으로서 통합적 공정이 가능)
    -   FAB 비용 및 공간 절약
-   Contact, Via, Plug 등 금속 배선 공정에 필요한 Tungsten 박막을 증착하고 TiN (DRAM용 캐패시터 전극)과 Ti/TiN(DRAM/Logic/3D NAND용 Barrier 금속막)을 형성
-   기존 텅스텐(W) 공정에 비해 불소 함량이 매우 낮고 저항성이 낮은 ALD-W 공정에 대한 솔루션을 제공

#### Features

-   High Throughput
-   Able to Configure In-line Process Modules For Optimum Integration
-   Higher UPEH with Smaller Footprint (6 to 10 Process Modules)
-   Excellent Reliability CVD
-   Excellent Step Coverage(TiTiN : @A/R 60:1)
-   Excellent Gap Fill Performance(SGW : Seamless gapfill Tungsten)
-   Lower Resistivity and Good Film Quality

![NOA CVD][07]

---

### (8). QUANTA

-   PECVD deposition

-   relate: [GEMINI ALD(Kairos PE-ALD)](#4-gemini-ald-kairos-pe-ald), [GEMINI ALD](#5-gemini-ald)

-   Process: HT-TEOS, HT-SiN, HT-PEOX(Plasma Enhance OXide)
-   Applications: In-situ stack 3D film, TSV(Through Silicon Via) passivation thin film

#### Introduction

-   뛰어난 통합 공정 적응성과 박막 제어성으로 최신 3D NAND 디바이스 제조에 필요한 솔루션을 제공하도록 설계
    -   In-Situ 방식으로 결점 수를 최소화하여 뛰어난 박막의 스트레스와 거칠기 제어로 여러 다른 박막층을 번갈아 증착 가능
    -   고유한 하드웨어 설계로 높은 생산량아 가능하며 최종 사용자에게 탁월한 신뢰성과 향상된 가동 시간을 제공
    -   PECVD 3D NAND 제조 공정의 시작은 SiO2 및 SiN 필름과 같은 막을 여러층 교차하여 수직으로 증착 (높은 웨이퍼 처리량과 고성능 3D NAND 디바이스 제조 솔루션을 제공)
    -   각각의 얇은 박막층은 매우 균일하고 매끄러워야 하며 3D NAND 디바이스 밀도를 증가시키는 데 도움이 될 수 있는 후속 층에 잘 접착되어야 함
-   박막 균일성, 표면 거칠기, WER(Wet Etch Rate)등 사용자가 여러 요인을 손쉽게 관리하고 조절을 함으로서 ON(Oxide/Nitride) 공정에 필요한 솔루션을 제공

#### Features

-   High Throughput
-   Excellent Integration Adaptability & Controllability
    →Stack & Single Stress, Thickness Profile (Center<->Edge ), WER(Wet Etch Rate)
-   Wide Process Tuning Knob
    →Gap, Pressure, Gas Ratio, Wide RF Window.
-   Extreme Stack Film Stability
-   System Performance Reliability
-   Simple Design for Easy Maintenance (High System Reliability & System Uptime)
-   Expanded RF Control Margin

![QUANTA][08]

---

[teos]: https://en.wikipedia.org/wiki/Tetraethyl_orthosilicate
[00]: https://www.ips.co.kr/ko/images/business/intro_product04.jpg
[01]: https://www.ips.co.kr/data/board/product/product_462_board_file1_20190514155606_219679.jpg
[02]: https://www.ips.co.kr/data/board/product/product_376_board_file1_20181220174015_536294.jpg
[03]: https://www.ips.co.kr/data/board/product/product_8_board_file1_20181217165546_943501.jpg
[04]: https://www.ips.co.kr/data/board/product/product_375_board_file1_20181220173538_248403.jpg
[05]: https://www.ips.co.kr/data/board/product/product_109_board_file1_20181217170035_86808.jpg
[06]: https://www.ips.co.kr/data/board/product/product_338_board_file1_20181219142110_235758.jpg
[07]: https://www.ips.co.kr/data/board/product/product_337_board_file1_20181219141121_424554.jpg
[08]: https://www.ips.co.kr/data/board/product/product_110_board_file1_20181217171043_566641.jpg
