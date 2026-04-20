---
title: "AI report - ALE & Selective Etch 장비·기술 심층분석 (2023–2026)"
layout: post
date: 2026-04-20 17:35 +0900
tagㄴ:
- ALE
- Atomic Layer Etch
- Semiconductor
- Thermal ALE
- Plasma ALE
- Selective Etch
- Study
- Report
description: "260420, AI report - ALE & Selective Etch Advanced Equipment and Tech Analysis (2023–2026)"
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

# AI report - ALE & Selective Etch: Advanced Equipment and Tech Analysis (2023–2026)

지금까지 METAL 공정만, 그것도 Mo ALD만 해서 내 스스로 확장성이 너무 떨어진다는 느낌을 강하게 받았다. 다른 공정들도 경험해 봐야지 내 자산이 되고 무기가 될 텐데 그럴 기회가 없어서 공부라도 해봐야겠다고 결심했다. 최근에 회사에서 ALE와 Selective Etch 관련하여 이런저런 이야기를 나눌 기회가 있었고, LAM에서 하는 공정들 이것저것 알아보던 와중에 ALE와 Selective Etch에 관심이 생겨서 그쪽 공정과 장비들은 어떤 것들이 있는지, Player로 참여하고 있는 업체들은 어떤 곳들이 있는지 궁금해서 AI tool에 보고서를 작성해달라고 했다. 그 결과물이 이 포스팅이다. 전체 내용은 AI로 작성하였고, 몇 번 읽어보면서 여전히 잘 모르겠는 부분이나 불확실해 보이는 부분들은 빼는 방향으로 최종 원고를 마무리 지었다. 이 리포트를 시작으로 좀 더 차근차근 ALE 공부를 해 볼 생각이다.

---

## 시작하며 — 이 글을 읽는 분께

이 글은 AI tool을 사용하여 **ALE(Atomic Layer Etching)** 와 **Selective Etch(선택 식각)** 분야의 장비·기술 현황을 실무 엔지니어가 참고할 수 있는 수준으로 정리한 기술 레퍼런스입니다. sub-10nm 로직, GAA nanosheet, 3D NAND 200-layer 이상, MoN/Mo 박막 통합 같은 영역에서 “지금 어느 회사가 뭘 갖고 있고, 어디까지 왔는가”를 **공식 1차 소스** 기준으로 확인하는 것을 목표로 했습니다.

내용은 원칙적으로 다음 소스만 인용했습니다.

- 제조사 공식 press release, 제품 페이지, SEC 10-K / DART 공시, IR 자료
- peer-reviewed 논문 (JVST A, Acc. Chem. Res., J. Phys. Chem. Lett. 등)
- 공식 보도를 2차 인용한 신뢰도 높은 매체 (EE Times, GlobeNewswire, Nikkei 등)

### 수치 신뢰도 표기 규약

본 문서에서는 숫자와 주장의 신뢰도를 아래 세 단계로 구분합니다.

- **(공식)** — 제조사 공식 press release, 제품 페이지, 10-K/DART 공시, peer-reviewed 논문에 직접 기재된 수치
- **(공식 비공개 — 추정)** — 업계 관행·installed base 간접 자료 기반이며 제조사 공식 수치는 공개되지 않음
- **(공식 확인 불가)** — 공개 소스에서 검증되지 않음, 또는 secondary 중개상·비공식 자료에서만 보이는 명칭

-----

## 1. 개요 — ALE와 Selective Etch가 왜 필요한가

### 1.1 핵심 개념부터

> **📘 용어: ALE (Atomic Layer Etching)**
> 식각을 **“① 표면 반응 → ② 제거”** 두 단계로 쪼개서 사이클로 반복하는 방식입니다. 각 단계가 스스로 멈추도록(**self-limiting**) 설계되어, 가스 노출이 조금 더 길거나 짧아져도 결과가 거의 같게 나옵니다. 한 사이클 당 대체로 원자 한 층(~1 Å 수준)만 깎입니다.
> 왜 중요한가? sub-10nm 소자나 GAA nanosheet 같은 구조에서는 “몇 nm를 얼마나 정확하게” 깎느냐가 소자 특성을 결정하기 때문에, 재현성이 무엇보다 중요합니다.

> **📘 용어: Selective Etch (선택 식각)**
> 두 종류 이상의 재료가 같이 있는 구조에서, 원하는 재료**만** 선택적으로 제거하는 공정입니다. 예: SiGe와 Si가 교대로 쌓인 구조에서 SiGe만 녹여내기. 선택비(selectivity)가 수백 대 1 이상이어야 실용적.
> ALE와 어떻게 다른가? ALE의 핵심은 **self-limiting(스스로 멈춤)** 이고, Selective Etch의 핵심은 **재료별 선택비**입니다. 둘은 부분적으로 겹치지만 같은 개념이 아닙니다. Applied Materials의 기술자 Matt Cogorno도 2016년 공개 인터뷰에서 “우리 Selectra는 시간으로 제어하므로 self-limiting 화학이 필요 없다. 그래서 ALE가 아니다”라고 명확히 구분한 바 있습니다.

> **📘 용어: EPC (Etch Per Cycle)** — 한 사이클 당 식각되는 두께. ALE의 이상적 EPC는 원자 한 층(~1 monolayer), Si 기준 대략 1.4 Å/cycle입니다.

### 1.2 왜 지금 중요한가 — 소자 로드맵 관점

반도체 device가 3D화·미세화되면서 기존 plasma etch만으로는 해결이 안 되는 공정이 급격히 늘고 있습니다.

- **FinFET → GAA nanosheet 전환 (N3, N2)**: Si/SiGe가 교대로 쌓인 super-lattice에서 **SiGe만** 제거해서 채널을 공중에 띄워야 함 → 선택 식각 필수.
- **3D NAND 200–400 layer**: 세로로 10 μm 깊이 구멍을 뚫는데, 직진성(profile)이 조금만 틀어져도 layer bottom에서 채널이 막혀버림 → **Cryogenic etch(극저온 식각)** 가 tool-of-record.
- **3D DRAM, 4F² cell**: capacitor aspect ratio 증가 + HKMG(High-K Metal Gate) 주변 공정에서 ALE 급 정밀도 필요.

> **📘 용어: GAA (Gate-All-Around) / nanosheet**
> 트랜지스터 채널을 Gate가 “4면에서” 둘러싸는 구조. FinFET(3면 둘러쌈)의 다음 세대로, 누설 전류와 제어성에서 유리합니다. Samsung은 **MBCFET™**, TSMC는 **N2 GAA**로 부릅니다. 채널을 여러 개의 얇은 Si 판(sheet) 모양으로 만들기 때문에 nanosheet라고 불립니다.

> **📘 용어: HAR / HARC**
> High Aspect Ratio(높은 종횡비). 폭 대비 깊이 비율이 크다는 뜻. 3D NAND의 channel hole은 HAR >50:1, HARC(High Aspect Ratio Contact)는 더 극단적. 3D NAND의 “몇 layer”가 늘어난다 = 구멍이 더 깊어진다 = HAR가 더 높아진다.

### 1.3 시장 규모

ALE 전용 TAM(Total Addressable Market, 잠재 시장 규모)은 대부분의 market research 기관이 별도 공개하지 않지만, 간접 지표는 확인할 수 있습니다.

- **CY2024 Dry Etch market share** (Gartner 인용, TEL IR 자료 수록, 2025.4.30) **(공식)**
- Lam Research 1위
- Tokyo Electron (TEL) 27%, 2위
- Applied Materials 3위
- 후속: Hitachi High-Tech, AMEC(중국)
- **Lam Research FY2024 매출 $14.91B** (10-K 공시, 회계연도 2024.6.30 종료) **(공식)**. 업계 추정상 etch가 전사의 45–55% 수준이지만 공식 분리 공시 없음 **(공식 비공개 — 추정)**.
- **Applied Materials FY2024 Semiconductor Systems 매출 $19.91B**, 전사 $27.18B (10-K 공시, 2024.10.27 종료) **(공식)**.

> **📘 용어: WFE (Wafer Fab Equipment)** — 팹에서 웨이퍼를 처리하는 장비 전체를 묶어 부르는 용어. Deposition, Etch, Litho, CMP, Metrology 등 포함.

> **📘 용어: 10-K** — 미국 상장사가 SEC에 의무적으로 제출하는 연간 공시. 매출·이익·사업 부문·주요 고객이 기재되어 1차 소스로 가치가 높음.

-----

## 2. 기술 분류 — ALE는 한 종류가 아니다

### 2.1 Plasma ALE vs Thermal ALE

> **📘 왜 두 가지로 나뉘는가?**
> 원자 한 층만 정확히 깎으려면 두 번의 반응이 필요합니다. 첫 번째로 표면을 “바꾸고”(modification), 두 번째로 그 바뀐 층만 “떼어냅니다”(removal). 이 “떼어내기”를 **플라즈마 이온의 물리적 충격**으로 하면 Plasma ALE, **열에너지와 화학 반응**으로만 하면 Thermal ALE입니다.

|구분 |Plasma ALE (방향성) |Thermal ALE (등방성) |
|-------|--------------------------------------------------------|---------------------------------------------------------------|
|① 표면 변환|Cl₂, HBr, BCl₃ 등 radical이 표면에 흡착 |무수 HF 노출로 **fluorination**(표면에 금속-F 층 형성) |
|② 제거 |Ar⁺ 등 저에너지 이온 충격 (ALE window 내) |**ligand exchange**(Sn(acac)₂, TMA, DMAC, BCl₃)로 휘발성 complex 생성|
|Profile|수직(anisotropic) |전방위(isotropic) |
|대표 재료 |Si, SiO₂, Si₃N₄, W, Ta, Ru, GaN |HfO₂, ZrO₂, Al₂O₃, ZnO, **MoO₃**, TiN 등 |
|온도 |실온 ~ 60 °C |150 – 300 °C |
|대표 장비 |Lam Kiyo/Akara/Vantex, AMAT Sym3 Y/Z Magnum, TEL Tactras|TEL Certas LEAGA, Hitachi DCR 9060 |
|핵심 문헌 |Kanarik 2015 (JVST A), Kanarik 2018 (JPC Lett.) |Fischer 2021 (JVST A), George 2020 (Acc. Chem. Res.) |


> **📘 용어: Ion-neutral synergy**
> Plasma ALE의 핵심 개념입니다. 중성 반응종(radical)만 쏘거나 이온만 쏠 때는 거의 식각이 안 일어나지만, **두 개를 번갈아 쏘면** 표면이 깎이는 현상. Kanarik et al.(2017)이 이를 정량화해서 “synergy 값 = 80–100%일 때 이상적 ALE”라고 정의했습니다.

> **📘 용어: ALE window**
> Plasma ALE에서 두 번째 단계(이온 충격)의 에너지 범위. 너무 낮으면 변형된 층이 안 떨어지고, 너무 높으면 아래 bulk까지 손상됩니다. 이 좁은 에너지 “창문” 안에서만 self-limiting이 성립합니다.

> **📘 용어: Fluorination + Ligand-exchange**
> Thermal ALE의 두 단계 반응.
>
> - **Fluorination**: HF가 금속 산화물 표면과 반응해 metal fluoride (예: HfO₂ → HfF₄-like layer)로 바꿉니다.
> - **Ligand-exchange**: TMA(Trimethylaluminum) 같은 분자가 와서 F를 methyl로 교환하는데, 이때 생기는 복합체가 휘발성을 가져 떠나갑니다. 순수한 화학 반응으로만 원자 한 층이 벗겨집니다.

**핵심 포인트**: Plasma ALE는 2010년대 중반 Lam Research를 중심으로 산업 표준이 됐고, Thermal ALE는 George 교수 그룹(CU Boulder)이 2015–2018년에 메커니즘을 체계화한 뒤 2022년 Fischer et al.이 3D NAND HfO₂ HAR 구조에서 **0.6 nm/cycle uniform etch**를 보여주면서 HVM(양산) 진입 단계에 들어섰습니다 **(공식, JVST A 40, 022603, 2022)**.

### 2.2 방향성 관점의 분류

- **Directional ALE**: Plasma ALE의 일반형. 이온이 sheath에서 가속되어 수직으로 입사 → FinFET fin etch, gate etch, contact open 등에 사용.
- **Isotropic ALE**: Thermal ALE가 대표적. 또는 원격 플라즈마에서 이온을 걸러내고 radical만 보내는 방식(AMAT Selectra 구조와 유사). GAA SiGe recess나 inner spacer 형성에 사용.
- **Quasi-ALE / Pseudo-ALE**: self-limiting까지 완전 포화시키지 않고 시간으로 제어하지만 ALE에 준하는 정밀도를 얻는 방식. 생산성을 높이기 위해 실제 양산 라인에서 자주 채택됩니다.

### 2.3 Selective Etch — 선택성은 어떻게 얻어지는가

Selective Etch의 “선택비”는 원리적으로 세 가지 방식으로 만들어집니다.

1. **Chemical selectivity (화학적 선택성)**
- 예: HF + NH₃ 조합(**SiCoNi 계열**)은 native oxide(SiO₂)를 선택적으로 제거하되 Si는 거의 건드리지 않습니다.
- 예: ClF₃는 W의 fluoride(WF₆, 휘발성)와 Ti의 fluoride(TiF₄, 덜 휘발성) 사이의 휘발성 차이를 이용합니다.
1. **Thermodynamic selectivity (열역학적 선택성)**
- Thermal ALE의 핵심. 각 재료의 fluoride ligand exchange에서 ΔG_rxn(반응 깁스 에너지)이 다르므로, TMA를 보냈을 때 어떤 재료만 휘발하는지가 결정됩니다.
- 예: HfO₂는 DMAC와 반응해 HfF₄가 휘발하지만, SiO₂는 같은 조건에서 거의 반응하지 않음 → **HfO₂ : SiO₂ > 100 : 1** **(공식, 문헌 기준)**.
1. **Plasma-modulated selectivity**
- 원격 플라즈마를 만든 뒤 이온을 **그리드(grid)** 로 걸러내고 radical만 웨이퍼에 도달시키는 방식. AMAT Producer Selectra가 이 구조입니다.
- SiGe가 Si보다 F radical과 빠르게 반응하는 특성을 이용 → **SiGe : Si ≈ 수백 : 1 (공식 비공개 — 추정, 학술 문헌 기준)**.

> **📘 용어: SiCoNi**
> AMAT이 만든 선택 식각 chemistry의 별명. **Si + Co(balt) + Ni** 가 아니라 “**Si**licon, **Co**mplex **Ni**trogen-fluorine”의 약어로, NH₃ + NF₃ 원격 플라즈마로 native SiO₂를 건식 제거합니다. FinFET pre-clean 때부터 널리 쓰였습니다.

-----

## 3. 글로벌 장비사 현황

### 3.1 Lam Research

**한 줄 요약**: ALE 이론의 산업화를 주도한 회사. Plasma ALE·Cryogenic Etch·Thermal ALE 모두 독자 기술.

#### 주요 플랫폼

**Sense.i® 플랫폼 (2020.3 출시)**

- 기존 Kiyo·Flex module을 계승한 차세대 etch platform.
- **Equipment Intelligence®** — 챔버당 수백 개의 센서에서 받은 데이터를 ML 모델이 실시간 분석해 공정 편차를 자동 보정하는 구조.
- Kiyo, Flex, Vantex, Akara가 모두 이 Sense.i 위에서 동작.

**Kiyo® Product Family (2004~현재)**

- **Conductor etch**(금속·Si·hard mask 식각)의 주력.
- 누적 설치 **30,000 chamber 이상** **(공식, Lam Akara 제품 페이지·press, 2025.2)**.
- Metal gate, high-k, FinFET/GAA fin etch, double patterning에 사용.
- ALE capability 공식 명시.

**Flex®**

- **Dielectric etch**(SiO₂/Si₃N₄) 주력. 3D NAND channel hole 핵심.
- 전 세계 메모리 제조사에서 광범위하게 사용 중. Cryogenic etch 구성도 이 계열을 기반으로 함 **(공식 press, 2024.7.31)**.

**Vantex® (2021.1 발표)**

- Sense.i 플랫폼 전용 신규 dielectric etcher. RF pulsing 기술 고도화로 3D NAND·DRAM HAR 대응.

**Akara® (2025.2.19 발표)** — 이번 세대의 주력 발표

- Conductor etch의 차세대 **플래그십**.
- **DirectDrive® technology** 탑재 — “이전 플라즈마 소스 대비 100배 이상 빠른 응답” **(공식, Akara 제품 페이지)**.
- **2nm logic GAA 및 advanced planar DRAM에서 production tool-of-record 채택** 확인 **(공식)**.

> **📘 용어: Tool-of-Record (TOR)**
> 양산 라인에서 “이 공정에는 이 장비를 쓴다”고 공식 선정된 장비. 한 번 TOR가 되면 수년간 바뀌지 않아, 장비사에게는 매우 중요한 공식 지표입니다.

**Lam Cryo™ 3.0 (2024.7.31 발표)**

- Cryogenic dielectric etch의 **3세대**. 영하 수십 도에서 high-power confined plasma와 신규 chemistry 결합.
- 공식 스펙 **(Lam press release 2024.7.31 기준)**:
- **profile deviation <0.1% at AR >50:1**
- 최대 **10 μm 관통 깊이**
- 기존 대비 etch rate **2.5×**
- **cryogenic etch 기반 누적 500만 wafer** 생산 실적
- **“~1,000 chamber 설치”는 공식 press release에 명시되어 있지 않음 (공식 비공개 — 업계 추정)**. 원 자료에 기재된 누적 생산 규모는 500만 wafer입니다.
- 2019년 세계 최초 cryo 1세대 production 도입 이후 축적된 자산.

> **📘 용어: Cryogenic Etch (극저온 식각)**
> 웨이퍼 척(chuck) 온도를 영하 수십 도 이하로 냉각해서 식각하는 방식. 저온에서 측벽에 passivation layer가 더 안정적으로 형성되어, **깊은 구멍을 뚫을 때 측벽이 덜 깎이고 profile이 직선에 가깝게 유지됩니다.** 3D NAND layer가 200, 300, 400으로 늘어날수록 거의 필수.

**Coronus®, Corvus®**: 웨이퍼 가장자리(bevel/edge) 영역 전담.
**Syndion, Versys Metal**: TSV(Through-Silicon Via) 및 specialty metal etch.

**Argos® + Prevos® + Selis® — Selective Etch Portfolio (2022.2.9 공식 출시)**

Lam은 conductor/dielectric 외에도 **dedicated Selective Etch 제품군**을 2022년부터 공식 보유하고 있으며, lamresearch.com에 **Selective Etch Product Family 전용 카테고리**를 운영 중입니다 **(공식)**. 세 개의 서로 보완적인 제품으로 구성됩니다.

| 제품 | 핵심 기술 | 주 용도 |
|---|---|---|
| **Argos®** | MARS™ (Metastable Activated Radical Source) — ultra-gentle radical 플라즈마 | Wafer 표면의 선택적 수식·디콘타미네이션. Advanced logic의 surface property modification |
| **Prevos®** | Chemical vapor reactor + 신규 chemistry catalyst + 민첩 온도 제어 | Oxide/Si/metal에 대한 **atomic-layer precision ultra-high selectivity etch**. Native oxide breakthrough, precision trim/recess |
| **Selis®** | **Radical + Thermal etch 혼합**, low-energy radical source로 tuning | 3D 구조에서 top-to-bottom 균일 선택 식각. **GAA용 critical SiGe selective etch** 직접 타깃 — Si layer를 손상·거칠기 없이 SiGe만 제거 |

- **Prevos + Selis는 single integrated tool로도 공급** 가능 — multi-layer selective etching, queue-time 제어, 생산 유연성 향상 **(공식)**.
- **Samsung 양산 채택**: 2022.2 공식 press에서 Samsung 반도체 R&D Center Master Keun Hee Bai가 "우리는 selective etch의 혁신 역량에 의존해 GAA 및 그 이후의 logic device roadmap을 가속한다"고 직접 언급 **(공식 인용)**. Lam 공식 문구는 *"already being used in the fabs of industry leaders like Samsung Electronics"*.
- **Lam Research Korea의 3개 국내 제조시설**에서 이 selective etch tool을 생산 **(공식, AEI Dempa 보도 인용)**.
- **2025년 Edison Awards 수상** — Lam Next-Generation Selective Etch Portfolio (Argos, Prevos, Selis).
- **학문적 기반**: 이미 References에 포함된 Fischer et al. thermal ALE 연구 (JVST A 39, 030801, 2021; JVST A 40, 022603, 2022)가 **Prevos/Selis의 R&D 백본**. Thermal ALE 학계 리더십이 상용 제품으로 그대로 연결된 구조입니다.

> **📘 용어: MARS™ (Metastable Activated Radical Source)**
> Lam Argos의 핵심 소스 기술. "metastable" 상태의 radical을 생성해 이온 에너지는 거의 없이 표면 반응만 유도 — 기존 플라즈마 source로는 불가능한 수준의 **low damage, ultra-gentle surface treatment**를 가능하게 합니다.

**ALTUS® Halo (2025.2.19 발표)** — 사용자 관심 영역

- ALE는 아니지만 **세계 최초 molybdenum ALD 툴** **(공식, Lam press release 2025.2)**.
- Akara와 같은 날 발표. **3D NAND / DRAM / Logic용 barrier-free Mo 금속화** 타깃.
- W를 Mo로 대체하는 흐름에서 첫 번째 상용 장비.

#### 공식 announcements 요약

| 연도 | 제품/기술 | 핵심 포인트 |
|---|---|---|
| 2020.3 | Sense.i® | Smart etch 플랫폼, Kiyo/Flex 계승 + Equipment Intelligence® |
| 2021.1 | Vantex® | Sense.i 전용 HAR dielectric etcher |
| 2022.2 | **Argos® + Prevos® + Selis®** | **Dedicated Selective Etch 3-제품 포트폴리오**. Argos(MARS radical source 표면 처리), Prevos(atomic-layer precision selective etch), Selis(radical + thermal 혼합, GAA SiGe 선택 식각). **Samsung GAA 양산 채택 공식 확인** |
| 2024.7 | Lam Cryo™ 3.0 | 3세대 cryogenic dielectric etch, profile dev <0.1% @ AR >50:1, 3D NAND 1,000-layer 로드맵 |
| 2025.2 | Akara® | Conductor etch 플래그십, DirectDrive 100× faster plasma, 2nm GAA TOR |
| 2025.2 | ALTUS® Halo | 세계 최초 molybdenum ALD 툴, barrier-free Mo 금속화 |

#### 주요 고객 (10-K FY2024 공식 공시)

Micron, Samsung Electronics, SK hynix, TSMC가 **“most significant customers”** 로 명시 **(공식)**.

#### 차별화 포인트

- **ALE 이론의 산업화 1세대 공급사**. Kanarik 그룹이 plasma ALE의 정식 정의와 synergy 이론을 Lam 내부에서 정립.
- **Thermal ALE 이론·장비 내재화**: Fischer·Lill은 Lam Research 소속이면서 George(CU Boulder)와 공저. 이 R&D가 **Prevos/Selis 상용 제품**으로 연결.
- **Dedicated Selective Etch 포트폴리오 보유** (Argos/Prevos/Selis, 2022~) — Samsung GAA 양산 채택 공식 확인.
- **Cryogenic etch**의 사실상 독점적 production 지위 (2019~).

-----

### 3.2 Applied Materials (AMAT)

**한 줄 요약**: Selective Etch의 de facto 표준(Producer Selectra). EUV patterning co-optimization에서 구조적 차별화.

#### 주요 플랫폼

**Centris® Sym3® (2015 출시) → Sym3® Y → Sym3® Y Magnum → Sym3® Z Magnum**

- Conductor etch 계보. **매우 넓은 installed base를 보유한 플래그십** (AMAT 공식 제품 페이지 및 보도에서 반복 언급) **(공식, 다만 정확 chamber 수치는 공식 비공개)**.
- Sym3의 특징은 “high-conductance chamber” — 반응 부산물(by-product)을 빠르게 배출해 재침착(redeposition)을 줄이는 구조 **(공식, Sym3 Y 제품 페이지)**.

**Sym3® Y Magnum™ (2024.2.26 SPIE에서 발표)**

- 이름의 “Magnum”은 전력 강화를 의미하는 브랜딩.
- 핵심 기능: **같은 chamber 안에서 Dep(증착)과 Etch(식각)를 순차적으로 수행**. EUV로 만든 line edge roughness를 dep으로 채우고 etch로 다시 깎아 **매끈하게** 만듭니다 **(공식, AMAT 2024.2.26 press release)**.
- AMAT 공식 포지셔닝: DRAM EUV patterning 영역을 주력 타깃으로 자리매김 **(공식)**.

> **📘 용어: Line Edge Roughness (LER)**
> 포토리소그래피로 만든 선의 가장자리가 얼마나 울퉁불퉁한지. EUV처럼 짧은 파장 노광은 photon shot noise 때문에 LER가 커지는데, 이게 크면 소자 편차가 커져 성능이 떨어집니다. Sym3 Y Magnum의 in-chamber Dep+Etch는 이 LER를 완화합니다.

**Sym3® Z Magnum™ (2026.2 발표)**

- **2세대 Pulsed Voltage Technology (PVT2)** 탑재.
- Ion directionality(방향성)와 plasma density(밀도)의 trade-off를 깨뜨린 구조.
- **2nm logic tool-of-record, 250 chamber 이상 설치** 확인 **(공식, AMAT 2026.2)**.

**Producer® Selectra™ Etch (2016 공식 출시)** — Selective Etch의 상징

- 표준 F/Cl gas 사용, **ion-filtering grid**로 이온을 차단하고 radical만 wafer에 도달시키는 구조.
- AMAT 공식: radical 기반 chemistry로 다양한 dielectrics/metal/semiconductor에 대한 **extreme selectivity, atomic-level precision etch**를 달성 **(공식, Selectra 제품 페이지)**. 적용 공정은 FinFET, 3D NAND, GAA.
- **“1,000+ chamber installed base” 같은 정확한 수치는 AMAT 공식 press/제품 페이지에서 직접 확인되지 않음 (공식 비공개 — 추정)**. 실무적으로 “수백~수천 챔버 규모의 광범위 installed base”로 이해하면 됩니다.
- GAA 공정에서 **SiGe 선택 recess**로 inner spacer cavity를 만들고 nanosheet 끝을 정리하는 핵심 장비.

> **📘 용어: Inner Spacer / Nanosheet End Removal**
> GAA nanosheet 구조를 만들 때, Si sheet 양 끝에서 SiGe를 일부만 옆으로(lateral) 파낸 뒤 dielectric을 채워 넣는 작은 구조. 이 “spacer”가 source/drain과 gate 사이의 용량을 줄이는 데 결정적입니다. Producer Selectra의 대표 application.

**Centura® Sculpta® (2023.2 발표, 2024 확대)**: Pattern-shaping tool. EUV double patterning을 한 번 생략할 수 있게 해줍니다. Intel·Samsung 공식 채택 언급.

**Producer® XP Pioneer® (2024.2 발표)**: 고밀도 carbon hard mask CVD.

**Centris™ Spectral™ Molybdenum ALD (2026.2 발표)** — 사용자 관심 영역

- Mo **monocrystalline** contact 형성을 위한 2nm wiring용 ALD **(공식, AMAT 2026.2)**.
- **Viva™ radical treatment (2026.2)**: ultra-pure radical을 이용해 **2nm GAA nanosheet 채널 거칠기를 앙스트롬 스케일로 smoothing** **(공식, AMAT 2026.2)**.

#### 주요 고객

TSMC (N2 GAA), Samsung (3GAE/3GAP, 2nm), Intel (Sculpta 공식 채택).

#### 차별화 포인트

- **Selective Etch의 de facto 표준**: Producer Selectra가 GAA SiGe recess에서 사실상 독점.
- **In-chamber Dep+Etch** (Sym3 Y Magnum): 타사에 없는 구조.
- **Integrated Materials Solution (IMS)**: high-vacuum transfer로 epi → selective etch → cleaning을 공기 노출 없이 연계.

#### 재무

- **FY2024 전사 매출 $27.18B, Semiconductor Systems $19.91B** **(공식, 10-K)**.

-----

### 3.3 Tokyo Electron (TEL)

**한 줄 요약**: Cryogenic etch(Tactras)와 Chemical Dry Etch(Certas)의 양 축. Coater/Developer 92% 점유와 함께 front-end 종합 coverage.

#### 주요 플랫폼

**Tactras™ (2006~)**

- Dielectric/Conductor plasma RIE 주력.
- 2021년 Tactras-UDEMAE (power device 전용), 2023년 cryogenic etch 옵션 추가.

**Cryogenic Etch on Tactras (2023.6.9 발표)** **(공식, TEL press release)**

- 3D NAND **400+ layer** memory channel hole용.
- 메모리 채널 홀을 **10 μm 깊이, 33분** 내에 식각.
- 기존 공정 대비 **GWP(global warming potential) 84% 감축** **(공식)**.
- **HF gas 기반 chemistry**로 CF(탄화불소)계를 대체. 공식 발표는 “HF 기반으로의 전환”과 “GWP 84% 감소”를 명시하며, **CF계 사용량 감소율 자체는 “수치 형태로 공식 공개되어 있지 않음”**. 업계·국내 보도에서는 “CF계 약 90% 수준 대체”로 언급되나, TEL 공식 보도자료 본문에서 해당 % 수치는 본 분석에서 확인되지 않아 **(공식 비공개 — 추정)**.
- Low-volume 생산 2025, **HVM 2026 목표**.
- 2023 VLSI Symposium에서 Y. Kihara et al. 발표.

**Certas™ LEAGA™** — TEL의 selective etch 핵심

- **Chemical Dry Etch (CDE, plasma-free solution)**. “gas chemical etch”로 플라즈마 및 액체 없이 식각 **(공식, tel.com/product/certas_leaga.html)**.
- isotropic 선택 recess. SiO₂ 계열에 대한 unique selectivity, Si contact pre-clean, 3D 구조 내 selective recess.
- Thermal ALE와 가까운 원리.

> **📘 용어: Chemical Dry Etch (CDE)**
> 플라즈마를 쓰지 않고 **가스 화학 반응만으로** 식각하는 방식. 이온 충격이 없어 웨이퍼 손상이 적고, 표면 전체가 골고루 식각(isotropic)됩니다. Thermal ALE와 비슷한 영역에서 쓰입니다.

**Episode™ UL (2020 발표, 2021.1.14 공식)**

- 최대 12 chamber 집적 가능한 플래그십 plasma etch.
- ※ TEL “Episode” 브랜드는 Etch(Episode UL)와 Deposition(Episode 1/2 DMR/QMR, 2024.7.8 발표) 양쪽에 쓰이므로 혼동 주의.

**참고 — 공식 확인 불가 항목**

- 원래 조사 범위에 있던 **“Tactras Vigus”** 와 **“Certas GeAce”** 는 tel.com 공식 제품 페이지에서 확인되지 않습니다. Secondary 중개상/브로커 표기는 TEL 공식 제품명이 아닙니다. **(공식 확인 불가)**

#### 재무·시장

- **FY2024 연결매출 ¥1.83조**, FY2025 ~¥2.43조 **(공식, TEL IR)**.
- **CY2024 Dry Etch market share 27% (2위)**, Coater/Developer 92% (1위) — **Gartner 인용, TEL Investor Guide 및 FY25 Q4 presentation 수록 (공식 인용)**.

#### 주요 고객

Samsung, SK hynix, TSMC, Intel, Micron, Kioxia, YMTC. Cryogenic etch는 “일부 고객 development POR 확보”로만 공식 언급.

-----

### 3.4 ASM International

**결론: ASMI는 Etch 장비를 제조하지 않습니다.**

공식 사이트(asm.com/our-technology-products) 기준 카테고리는 **ALD, Epitaxy, PECVD, Vertical Furnace** 네 개로 구성되어 있고 Etch 카테고리는 없습니다 **(공식, 2024–2026 시점 확인)**.

#### Etch-인접 기능

- **Previum® preclean module**: Epi 라인 내 보조 pre-clean 모듈입니다. Previum V3(native oxide removal), Previum NEXT(oxide + carbon + silicon etching), Previum VP(HAR cleaning). standalone etch tool이 아니라 **Epi 직전의 표면 준비용**.
- **Area-Selective Deposition(ASD)** 공정 내 보정용 etch-back supercycle이 학술 문헌에서 논의되지만, “selective etch tool”로 포지셔닝된 ASMI 상용 제품은 없습니다.

#### Reno Sub-Systems 인수

- **공식 발표: 2022년 3월 14일** (asm.com press release, GlobeNewswire 보도) **(공식)**.
- 대상: Reno Sub-Systems Inc. (NJ, 미국), RF matching sub-systems.
- 목적: “plasma products and solutions 강화” — 즉 **PEALD·PECVD의 RF match 성능 향상**. Etch 사업 진입 아님.

-----

### 3.5 Hitachi High-Tech

**한 줄 요약**: ECR microwave plasma conductor etch의 전통 강자. 2024년 DCR 9060으로 thermal-like ALE 영역에 공식 진입.

#### 주요 플랫폼

**DCR Etch System 9060 Series (2024.11.27 공식 런칭)** **(공식, Hitachi 보도자료)**

- **Dry Chemical Removal**. 공식 표현은 고종횡비 3D 구조용 **“isotropic etching at the atomic-layer level”**.
- wafer heating/cooling + plasma 기술을 조합해 radical 흡착 ↔ thermal desorption cycle로 원자 단위 형상 제어.
- Plasma etch와 in-line 결합 가능.
- **3D NAND, 3D DRAM 등 advanced 3D memory/logic** 타겟.

→ 사실상 thermal/radical cyclic ALE 급 상용 장비로, Hitachi HT의 기존 플라즈마 제품군과는 성격이 다릅니다.

> **📘 용어: ECR (Electron Cyclotron Resonance) Plasma**
> 마이크로파(2.45 GHz)와 자기장을 이용해 저압·고밀도 플라즈마를 만드는 방식. Hitachi HT의 M-series가 이 기술 기반이며, 하드마스크·깊은 Si 트렌치 식각에 강점.

**Conductor Etch M-8000 Series**

- Microwave ECR plasma. 공식: **“hard mask and silicon etching for 32 nm and beyond”** **(공식, hitachi-hightech.com 제품 페이지)**.

**Conductor Etch M-600 / 6000 Series, 9000 Series, EMCP Etch Chamber**

- Deep Si trench (power device), 20 nm 이하 double patterning, 비휘발성 금속(MRAM/FeRAM·HDD thin-film head).

> **참고 — 공식 확인 불가**: 원 task에 언급된 **“M5000”** 은 hitachi-hightech.com 공식에서 확인되지 않으며 공식 M-시리즈는 M-600/6000, M-8000입니다. **(공식 확인 불가)**

#### 재무·확장

- Hitachi High-Tech FY2023 매출 **~¥723.1B**.
- **Kudamatsu Kasado 신규 Etch 생산동 (2023.4.18)**: 약 ¥240억 투자, FY2025 가동, 생산능력 2배.

-----

### 3.6 글로벌 Players 비교표

|Company |Platform |Process Type |Key Feature |Source (Year) |
|-----------------|--------------------------------|---------------------------------------|---------------------------------------------------------------|-------------------------------------|
|Lam Research |Sense.i + Kiyo/Flex/Vantex/Akara|Conductor/Dielectric Plasma ALE |Equipment Intelligence®, DirectDrive, Kiyo 30k+ chamber |Lam product pages / press (2020–2025)|
|Lam Research |Lam Cryo™ 3.0 |Cryogenic Dielectric Etch |profile dev <0.1% @ AR >50:1, 500만 wafer 실적, 1000-layer 로드맵 |Lam press (2024.7.31) |
|Lam Research |Argos / Prevos / Selis |Selective Etch (radical + thermal) |Samsung GAA 양산 채택, Selis가 critical SiGe 선택 식각 타깃 |Lam press (2022.2.9), lamresearch.com/product/selective-etch-product-family |
|Applied Materials|Centris Sym3 Y Magnum |In-chamber Dep+Etch conductor |EUV LER healing, DRAM 주력 |AMAT press (2024.2.26) |
|Applied Materials|Centris Sym3 Z Magnum |PVT2 conductor etch |2nm logic TOR, 250+ chambers |AMAT press (2026.2) |
|Applied Materials|Producer Selectra |Selective Etch (radical-filtered) |Extreme selectivity, atomic-level precision, GAA SiGe recess 표준|AMAT product page |
|Tokyo Electron |Tactras + Cryogenic |Plasma RIE + Cryo |HF 기반, 10 μm/33분, GWP 84% 감축 |TEL press (2023.6.9) |
|Tokyo Electron |Certas LEAGA |Chemical Dry Etch (plasma-free) |Isotropic selective, 3D recess |tel.com/product/certas_leaga |
|Tokyo Electron |Episode UL |Plasma Etch |12-chamber cluster |TEL press (2021.1.14) |
|ASM International|— |Etch 장비 제조 안 함 |Deposition 전문 |asm.com |
|Hitachi High-Tech|DCR 9060 |Isotropic etching at atomic-layer level|3D NAND/3D DRAM 대응 |Hitachi press (2024.11.27) |
|Hitachi High-Tech|M-8000 / 9000 / M-6000 |Microwave ECR Conductor Plasma |32 nm 이하 hard mask/Si |hitachi-hightech.com |

-----

## 4. 국내 장비사 현황

### 4.1 PSK Holdings (PSK Inc.)

**한 줄 요약**: 세계 1위 Dry Strip 전문기업. Selective removal 영역에서 한국 유일 글로벌 공급사.

#### 제품 포트폴리오 (pskinc.com 공식)

1. **Dry Strip (SUPRA 시리즈)** — PSK 공식: **“greatest market share worldwide”** **(공식, pskinc.com)**. **PR strip 점유율 2016년 37%, 2017년 53% (Gartner, PSK IR 슬라이드 기재) (공식 인용)**.
1. **Dry Cleaning (POC, Plasma Oxide Cleaning)** — Si 표면 native oxide 제거.
1. **New Hard Mask (NHM) Strip** — oxide/nitride 대비 선택비가 높은 강한 etch-resistant film의 선택 제거.
1. **Edge Clean** — 웨이퍼 가장자리 film 제거.
1. **3D IC Packaging** — plasma source, reflow, hot DI, plasma surface treatment.

**경영 목표**: 2030년 USD 1B 기업 (pskholding.com 공식).

### 4.2 주성엔지니어링 (Jusung Engineering)

- **본업**: ALD/CVD (SDP CVD, TSD CVD, UHV CVD, ALD) 중심. DRAM/3D NAND/Logic 증착 + 디스플레이 PECVD/ALD + Solar cell.
- **Etch**: 회사 소개에 “DRY ETCH” 항목 포함. poly etcher 언급이 보도자료에 있으나 **2024–2026년 시점 공식 상용 flagship 모델명은 공식 사이트에서 특정되지 않음 (공식 확인 불가)**.

### 4.3 원익IPS (Wonik IPS)

- **본업**: PE-CVD (반도체 장비 mix의 60–70%), ALD/Diffusion/Furnace. 3D NAND Mold CVD, 10 nm DRAM High-K.
- **Etch**: Display back-plane용 dry etcher. 반도체 dielectric/conductor etch는 주력 아님.

### 4.4 테스 (TES)

- **본업**: PECVD, Dry Etch(**GPE, Gas Phase Etch**), Thermal CVD. 3D NAND cell gate 및 peripheral 전공정 장비.
- 공식 사이트 기준 **GPE**가 대표 dry etch 제품군. SiGe·Poly-Si selective etch 및 residue cleaning에 사용.

### 4.5 유진테크 (Eugene Technology)

- **본업**: LPCVD, ALD, Batch ALD, mini-batch CVD. 300 mm LPCVD 세계 2위권.
- **Etch**: 공식 홈페이지에 standalone etch 제품 없음 **(공식)**.

### 4.6 국내 Players 비교표

|Company |Platform |Process Type |Key Feature |
|------------------|----------------------|-----------------------------|------------------------------------------------------|
|PSK Holdings |SUPRA Series |Dry Strip |세계 1위, 37% (2016) → 53% (2017) share (Gartner, PSK IR)|
|PSK Holdings |POC, NHM Strip |Selective removal / Dry clean|한국 유일 글로벌 selective removal 공급사 |
|Jusung Engineering|SDP/TSD/UHV CVD·ALD |ALD/CVD 중심 + 일부 etch |2024 중국 비중 높음 (DART 확인) |
|Wonik IPS |PE-CVD / ALD / Furnace|Deposition 중심 |3D NAND mold CVD |
|Wonik IPS |Display Dry Etcher |Display back-plane |TFT 공정용 |
|TES |GPE |Selective dry etch |SiGe/Poly-Si, residue clean |
|Eugene Technology |LPCVD / ALD |Deposition only |standalone etch 없음 |

-----

## 5. 경쟁 구도

### 5.1 ALE Top 3 (근거 포함)

1. **Lam Research** — Kanarik·Fischer·Lill 등 이론의 산업화 1세대. Plasma ALE synergy 정의와 Akara·Kiyo·Vantex HVM tool 기반. Cryo 3.0 독보.
1. **Applied Materials** — Sym3 Y/Sym3 Y Magnum/Sym3 Z Magnum 계열로 conductor ALE 추격. EUV patterning co-optimization (Sculpta·Pioneer·Sym3 Y Magnum) 구조적 차별.
1. **Tokyo Electron** — Tactras cryogenic, Certas LEAGA selective에서 차별화. Dry Etch 27% share로 Top 3 확정.

판단 근거: (a) 세 회사의 공식 press release에서 “ALE” 표기 빈도, (b) Kanarik·Fischer·Lill 논문의 소속 기관(Lam), (c) CY2024 Gartner Dry Etch share Top 3.

### 5.2 Selective Etch Top 3

1. **Applied Materials (Producer Selectra)** — 2016년 출시 이후 가장 긴 양산 이력. TSMC/Samsung/Intel GAA SiGe recess의 de facto 표준. 광범위 installed base.
2. **Lam Research (Argos + Prevos + Selis)** — 2022.2 공식 dedicated selective etch 포트폴리오 출시. Samsung GAA 양산 채택 공식 확인 **(공식 인용)**. Selis는 SiGe 선택 식각을 직접 타깃하며, Thermal ALE 학계 리더십(Fischer et al.)이 상용 제품의 기술 백본. Lam Research Korea 3개 제조시설에서 생산.
3. **Tokyo Electron (Certas LEAGA)** — Plasma-free Chemical Dry Etch의 유일 대형 공급사. Isotropic selective recess·oxide 선택 제거에서 오랜 양산 성숙도.

**명예 언급 #4 — Hitachi High-Tech (DCR 9060 Series)**: 2024.11.27 공식 런칭한 신규 entrant로, "atomic-layer level isotropic etching"을 공식 표방하며 3D NAND/3D DRAM 타깃. 기술 방향성은 매우 유망하나 양산 이력·installed base가 아직 Lam·TEL·AMAT에 미치지 못해 Top 3 바로 아래 순위로 조정.

**순위 판단 근거**: (a) dedicated selective etch 제품군 공식 출시 여부, (b) 양산 tier-1 고객 공식 채택 여부, (c) installed base 및 양산 이력, (d) 관련 학계 리더십. AMAT는 (a)(b)(c)에서 가장 성숙, Lam은 (a)(b)에서 공식 확인됨과 동시에 (d)에서 독보적(Fischer·Lill thermal ALE 리뷰 + HfO₂ HAR 선택 식각 실증), TEL은 (c) 이력에서 강점.

### 5.3 기술 성숙도·노드·상용화 비교

|Category |Plasma ALE |Thermal ALE |Selective Etch |
|-----------|----------------------------------------------|----------------------------------------------|--------------------------------------------------|
|**성숙도** |HVM production-proven (10년+) |HVM 진입 초기 (2022~) |HVM 대규모 production (2016~) |
|**주요 플레이어** |Lam, AMAT, TEL, Hitachi HT |Lam(R&D 주도 + Prevos/Selis 상용), TEL(Certas), Hitachi HT(DCR 9060) |AMAT(Selectra), Lam(Argos/Prevos/Selis), TEL(Certas), Hitachi HT |
|**적용 노드** |N5/N3/N2 GAA, DRAM 1a/1b/1c, V-NAND 200+ layer|DRAM HKMG, 3D NAND word-line, GAA inner spacer|GAA SiGe recess, 3D NAND W recess, FinFET fin trim|
|**상용화 수준** |Multi-billion USD tool base |**수백 chamber 수준 (공식 비공개 — 추정)** |tier-1 foundry/memory 표준, **정확 chamber 수는 공식 비공개**|

### 5.4 시장점유율 (CY2024, Gartner 인용)

- **Dry Etch System**: Lam 1위, TEL 27% 2위, AMAT 3위, Hitachi HT / AMEC 후속 **(공식 인용, TEL IR 기재)**.
- **ALE 전용 share는 시장조사 기관 공식 non-disclosure**. Gartner 등은 dry etch 전체 시장 점유율만 제공하며, ALE 전용 시장 점유율이나 각 장비별 precise installed base는 공개하지 않음. Kiyo 30k+ chamber(Lam 공식)만 구체 수치로 확인되며, 그 외 installed base는 **공식 비공개 — 간접 추정**.

-----

## 6. 최신 공정 개발 동향

### 6.1 GAA SiGe/Si 선택 ALE (TSMC N2, Samsung 2nm/3nm)

GAA nanosheet 공정의 핵심 플로우는 다음과 같습니다.

1. **Si/SiGe super-lattice epi** (Centura Prime Epi) — 얇은 Si와 SiGe 층을 교대로 쌓음. 층 두께는 약 35 atoms 수준.
1. **STI → dummy gate → spacer** 형성.
1. **SiGe 끝 lateral 제거** (**Producer Selectra Etch**) — nanosheet 끝 부분에서 SiGe만 옆으로 파내어 inner spacer cavity 생성.
1. **PROvision eBeam metrology** — recess 균일도 측정.
1. **Dielectric fill** — inner spacer 채움.
1. **Si nanosheet 끝 제거** (Producer Selectra Edge).
1. **Centura Prime** — S/D selective epi.
1. **Replacement Metal Gate (RMG)** flow: dummy gate etch → Selectra로 남은 SiGe 최종 제거 → **채널이 공중에 떠서 gate가 4면에서 둘러쌈** (= GAA 완성).

Lam은 이 flow 전반에서 **Akara 기반 conductor etch**와 **Selis®를 통한 critical SiGe selective etch**를 병행 제공합니다. Selis는 2022년 출시 이후 Samsung GAA 양산에 채택된 것이 Lam 공식 press release에서 확인됩니다 **(공식, 2022.2.9)**. 즉 Samsung 3GAE/3GAP(MBCFET) → 2nm 양산 경로에서 SiGe 선택 식각 공정은 **AMAT Producer Selectra와 Lam Selis가 이중 공급 또는 부분 분담** 구도로 동작할 가능성이 높습니다 **(정확한 공정 스텝별 tool-of-record 분담은 고객사 비공개 — 추정)**. Lam Akara도 2025.2에 2nm GAA conductor etch에서 tool-of-record 확보 **(공식)**. TSMC N2는 2025년 양산 진입.

**SiGe : Si 선택비**는 공식 벤더 수치 비공개, 학술 문헌 기준 수백 : 1 수준 **(공식 비공개 — 추정)**.

### 6.2 3D NAND 200+ Layer HAR 공정

3D NAND의 layer 수가 늘어날수록 channel hole이 깊어집니다. 200 layer 시대까지는 기존 plasma etch로 가능했지만, **300–400 layer로 가면서 cryogenic etch가 사실상 필수**가 됐습니다.

- **Lam Cryo 3.0 (2024.7)**: Vantex·Flex chamber에서 운용. profile deviation <0.1%, AR >50:1, 채널 홀 10 μm 깊이, etch rate 2.5×, 누적 **500만 wafer 생산 실적 (공식)**. **2030년 1,000-layer 로드맵** 공식.
- **TEL Tactras Cryogenic (2023.6)**: 400+ layer memory channel hole용. 10 μm 깊이 33분 식각, **GWP 84% 감축 (공식)**, HF gas 기반으로 CF계 대체. HVM 2026 목표. VLSI 2023에서 Y. Kihara et al. 발표.
- **AMAT Sym3 Y Magnum (2024.2)**: 주력은 DRAM EUV이나 3D NAND conductor etch 영역 확장.

고객사: Samsung V-NAND, SK hynix 321-layer, Micron G9 NAND, Kioxia/WD 등 모든 메이저 메모리 메이커가 layer count 증가 + string-stacking 확대 진행 중.

### 6.3 DRAM 트렌드

- **HKMG peripheral**, **4F² cell 전환**, **3D DRAM 로드맵**.
- AMAT Sym3 Y Magnum이 DRAM EUV patterning 영역에서 AMAT의 주력 포지셔닝 **(공식, 2024.2)**.
- Lam Akara는 advanced planar DRAM에서 tool-of-record 확보 **(공식, 2025.2)**.

> **📘 용어: 4F² Cell**
> DRAM의 단위 셀 면적을 표현하는 표준 단위. F는 최소 피처 크기(minimum feature size). 기존 6F² → 4F²로 줄이면 같은 칩 면적에 1.5배 더 많은 셀을 넣을 수 있지만, 주변부 구조가 훨씬 복잡해져서 etch 정밀도 요구가 크게 높아집니다.

### 6.4 학회 하이라이트 (2023–2025)

- **VLSI Symposium 2023**: Y. Kihara et al. (TEL Miyagi), cryogenic memory channel hole etch. 공식 출처: tel.com/news/product/2023/20230609_001.html
- **SPIE Advanced Lithography + Patterning 2024.2.26**: AMAT Sym3 Y Magnum, Pioneer CVD, Sculpta 확장, Aselta contour metrology 발표.
- **AVS 2023/2024**: JVST A의 Thermal ALE special collection (2021~)을 잇는 후속 연구 다수. Fischer et al. HfO₂ 3D NAND (JVST A 40, 022603, 2022) 등. AVS 2024 session 세부 프로그램 URL은 **(공식 확인 불가)**.
- **IEDM 2023/2024, VLSI 2024**: GAA/3D NAND etch integration paper 다수. 개별 paper number/title은 **(공식 확인 불가)**.
- **Semicon Korea 2024/2025**: 각 vendor keynote. 세부 session은 **(공식 확인 불가)**.

### 6.5 Mo/MoN Thermal ALE

MoN/Mo 박막 공정과 관련성이 높은 최신 흐름을 정리합니다.

**문헌 측면**

- **Fischer et al., JVST A 39, 030801 (2021)** — thermal ALE review에서 metal oxide ALE 일반 (MoO₃ 포함) 메커니즘 분류 **(공식)**.
- **George group 연속 논문 (CU Boulder)** — fluorination + ligand-exchange의 metal oxide 전반 적용. 구체 Mo ALE 단독 논문은 본 분석 검색 범위에서 직접 확인되지 않음 **(공식 확인 불가)**.

**업계 시사점**

- **Lam ALTUS Halo** (세계 최초 molybdenum ALD 툴, 2025.2)와 **AMAT Centris Spectral** (Mo ALD, 2026.2) 모두 **Mo contact·word-line 상용 채택**을 명시 **(공식)**. 두 장비 모두 공식 명칭은 **“Mo ALD”이며 “ALE”가 아님**.
- 즉 Mo 박막은 2025년부터 양산 공정에 실제로 들어가기 시작했으며, 이에 대응하는 **Mo 및 MoN thermal ALE process 개발**이 차세대 R&D 핵심 이슈로 부상할 가능성이 매우 높습니다.
- **현재 Mo/MoN 전용 ALE 상용 장비는 공식 출시가 없음** (2026.4 기준). 초기에는 기존 thermal ALE chamber(Certas LEAGA, DCR 9060, Lam thermal chamber)에서 chemistry 커스터마이징으로 대응할 가능성이 큽니다 **(공식 확인 불가 — 추정)**.

-----

## 7. References

### 학술 논문 (Peer-reviewed)

| # | 저자 / 제목 | 연도 | 출처 | 핵심 내용 |
|---|---|---|---|---|
| 1 | **Kanarik et al.** — "Overview of atomic layer etching in the semiconductor industry" | 2015 | [J. Vac. Sci. Technol. A 33, 020802](https://doi.org/10.1116/1.4913379) | Plasma ALE 정의·분류·역사·synergy window를 정리한 산업 표준 review |
| 2 | **Kanarik, Tan, Gottscho** — "Atomic Layer Etching: Rethinking the Art of Etch" | 2018 | [J. Phys. Chem. Lett. 9, 4814](https://doi.org/10.1021/acs.jpclett.8b00997) | ALE smoothing effect, 강결합 재료(C/Ta/W/Ru) 유리성, ALD+ALE combo 논의 |
| 3 | **Kanarik et al.** — "Predicting synergy in atomic layer etching" | 2017 | [J. Vac. Sci. Technol. A 35, 05C302](https://doi.org/10.1116/1.4979019) | ALE synergy의 정량적 예측 모델 |
| 4 | **Fischer, Routzahn, George, Lill** — "Thermal atomic layer etching: A review" | 2021 | [J. Vac. Sci. Technol. A 39, 030801](https://doi.org/10.1116/6.0000894) | Thermal ALE의 thermodynamics·kinetics·material별 reactant 정리 |
| 5 | **Fischer et al.** — "Control of etch profiles in high aspect ratio holes via precise reactant dosing in thermal atomic layer etching" | 2022 | [J. Vac. Sci. Technol. A 40, 022603](https://doi.org/10.1116/6.0001691) | 3D NAND test 구조(AR >50:1)에서 HfO₂ thermal ALE, EPC ~0.6 nm/cycle 시연 |
| 6 | **George** — "Mechanisms of Thermal Atomic Layer Etching" | 2020 | [Acc. Chem. Res. 53, 1151](https://doi.org/10.1021/acs.accounts.0c00084) | Thermal ALE 4가지 메커니즘 정리 |

### Lam Research

| # | 자료 유형 | 제목 | 연도 | URL | 참고 내용 |
|---|---|---|---|---|---|
| 7 | 제품 페이지 | Akara® | 2025 | [lamresearch.com/product/akara](https://www.lamresearch.com/product/akara/) | Akara 공식 제품 페이지. DirectDrive 100× 이상 빠른 플라즈마 응답, Kiyo 30k+ chamber 계보, 2nm GAA TOR 명시 |
| 8 | Press release | Lam Cryo™ 3.0 | 2024.7.31 | [investor.lamresearch.com](https://investor.lamresearch.com/2024-07-31-Lam-Research-Introduces-Lam-Cryo-TM-3-0-Cryogenic-Etch-Technology-to-Accelerate-Scaling-of-3D-NAND-for-the-AI-Era) | Cryo 3.0 공식 발표. Profile deviation <0.1%, AR >50:1, 10 μm 관통, etch rate >2×, cryo 기반 누적 500만 wafer |
| 9 | Press release | ALTUS® Halo (Mo ALD) | 2025.2.19 | [newsroom.lamresearch.com](https://newsroom.lamresearch.com/2025-02-19-Lam-Research-Ushers-in-New-Era-of-Semiconductor-Metallization-with-ALTUS-R-Halo-for-Molybdenum-Atomic-Layer-Deposition) | 세계 최초 Mo ALD 툴 공식 발표, barrier-free Mo 금속화 |
| 10 | Press release | Akara® Conductor Etch | 2025.2.19 | [investor.lamresearch.com](https://investor.lamresearch.com/2025-02-19-Lam-Research-Unveils-Industrys-Most-Advanced-Conductor-Etch-Technology-to-Date) | Akara 공식 발표 (ALTUS Halo와 동시 공개) |
| 11 | 제품 페이지 | Selective Etch Product Family | 2022~ | [lamresearch.com/product/selective-etch-product-family](https://www.lamresearch.com/product/selective-etch-product-family/) | Argos/Prevos/Selis 3-제품 공식 카테고리, ultra-high selectivity + angstrom-scale precision |
| 12 | Press release | Argos® + Prevos® + Selis® 출시 | 2022.2.9 | [GlobeNewswire](https://www.globenewswire.com/news-release/2022/02/09/2381975/0/en/Lam-Research-Introduces-Groundbreaking-Suite-of-Selective-Etch-Tools-to-Accelerate-Chipmakers-3D-Roadmaps.html) | Dedicated Selective Etch 3-제품 공식 출시. Samsung R&D Center Master Keun Hee Bai quote 수록, "already being used in fabs of industry leaders like Samsung" 명시 |
| 13 | Newsroom blog | "Accelerating the path to 3D: Introducing Lam precision selective etch solutions" | 2022 | [newsroom.lamresearch.com](https://newsroom.lamresearch.com/accelerating-the-path-to-3d-introducing-lam-precision-selective-etch-solutions) | Argos/Prevos/Selis 기술 원리 상세 해설. Selis의 "critical SiGe selective etch without damaging Si layers" 공식 명시 |
| 14 | SEC 공시 | Form 10-K FY2024 (6.30 종료) | 2024 | [sec.gov](https://www.sec.gov/Archives/edgar/data/0000707549/000070754924000106/lrcx-20240630.htm) | FY2024 매출 $14.91B. 주요 고객 Micron, Samsung, SK hynix, TSMC 명시 |

### Applied Materials

| # | 자료 유형 | 제목 | 연도 | URL | 참고 내용 |
|---|---|---|---|---|---|
| 15 | Press release | Sym3 Y Magnum + Pioneer + Sculpta | 2024.2.26 | [ir.appliedmaterials.com](https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-expands-patterning-solutions-portfolio) | In-chamber Dep+Etch, DRAM EUV 주력 |
| 16 | Press release | Sym3 Z Magnum + Viva + Spectral Mo ALD | 2026.2 | [ir.appliedmaterials.com](https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-unveils-transistor-and-wiring-innovations) | PVT2, 2nm TOR, 250+ chambers, Mo monocrystalline contact ALD |
| 17 | 제품 페이지 | Producer Selectra Etch | 2016~ | [appliedmaterials.com](https://www.appliedmaterials.com/us/en/product-library/producer-selectra-etch.html) | Radical 기반 extreme selectivity, atomic-level precision. FinFET/3D NAND/GAA 적용 |
| 18 | 제품 페이지 | Centris Sym3 Y Etch | — | [appliedmaterials.com](https://www.appliedmaterials.com/us/en/product-library/centris-sym3-y-etch.html) | High-conductance chamber, pulsed RF, EUV patterning/critical conductor etch |
| 19 | SEC 공시 | Form 10-K FY2024 (10.27 종료) | 2024 | [sec.gov](https://www.sec.gov/Archives/edgar/data/0000006951/000000695124000044/amat-20241027.htm) | FY2024 전사 $27.18B, Semiconductor Systems $19.91B |

### Tokyo Electron

| # | 자료 유형 | 제목 | 연도 | URL | 참고 내용 |
|---|---|---|---|---|---|
| 20 | Press release | Cryogenic Memory Channel Hole Etch (400+ layer, HF, GWP -84%) | 2023.6.9 | [tel.com](https://www.tel.com/news/product/2023/20230609_001.html) | 10 μm / 33분, 400+ layer, HF 기반, GWP 84% 감축. VLSI 2023 Y. Kihara et al. 발표 |
| 21 | 제품 페이지 | Etch Certas™ Series (LEAGA) | — | [tel.com/product/certas_leaga](https://www.tel.com/product/certas_leaga.html) | Chemical Dry Etch, plasma-free solution, isotropic selective |
| 22 | 제품 페이지 | Etch Tactras™ Series | — | [tel.com/product/tactras](https://www.tel.com/product/tactras.html) | Dielectric/Conductor plasma RIE, cryogenic etch 옵션 |
| 23 | 제품 페이지 | Etch Episode™ UL Series | 2021.1 | [tel.com/product/episode_ul](https://www.tel.com/product/episode_ul.html) | 최대 12 chamber 플래그십 plasma etch |
| 24 | IR 자료 | FY25 Q4 Investor Presentation | 2025.4 | [tel.com IR](https://www.tel.com/ir/library/report/l8gqgo00000000gl-att/fy25q4presentations-e.pdf) | CY2024 Gartner Dry Etch 27% (2위), Coater/Developer 92% (1위) 수록 |
| 25 | IR 자료 | Investors' Guide | 2026 | [tel.com IR](https://www.tel.com/ir/library/corporate-update/hq95qj0000000734-att/InvestorsGuide_E20260213_rev01.pdf) | 시장점유율·세그먼트 데이터 갱신본 |

### ASM International

| # | 자료 유형 | 제목 | 연도 | URL | 참고 내용 |
|---|---|---|---|---|---|
| 26 | 제품 overview | ASM "Our Technology & Products" | — | [asm.com](https://www.asm.com/our-technology-products) | ALD/Epi/PECVD/Furnace만 공식 카테고리, **Etch 없음** |
| 27 | Press release | Reno Sub-Systems 인수 | 2022.3.14 | [NTB press](https://kommunikasjon.ntb.no/pressemelding/17928635/asm-international-announces-acquisition-of-reno-sub-systems) | 2022.3.14 공식 발표. Plasma deposition 강화 목적, Etch 사업 진입 아님 |

### Hitachi High-Tech

| # | 자료 유형 | 제목 | 연도 | URL | 참고 내용 |
|---|---|---|---|---|---|
| 28 | Press release | DCR Etch System 9060 Series 런칭 | 2024.11.27 | [hitachi.com](https://www.hitachi.com/en/press/articles/2024/11/1127a/) | "Isotropic etching at the atomic-layer level" 공식 명시. 3D NAND/3D DRAM 대응 |
| 29 | 제품 페이지 | Conductor Etch M-8000 Series | — | [hitachi-hightech.com](https://www.hitachi-hightech.com/us/en/products/semiconductor-manufacturing/dry-etch-systems/conductor/m8000.html) | Microwave ECR plasma, "hard mask and silicon etching for 32 nm and beyond" |

### 국내 업체 · 기타

| # | 자료 유형 | 제목 | 연도 | URL | 참고 내용 |
|---|---|---|---|---|---|
| 30 | 제품 페이지 | PSK Inc. "Products Overview" | — | [pskinc.com](https://www.pskinc.com/producttech/products_overview.php) | SUPRA dry strip (세계 1위), POC dry cleaning, NHM strip, edge clean |
| 31 | 제품 페이지 | PSK SUPRA XP Dry Strip | — | [pskinc.com](https://www.pskinc.com/producttech/dry_strip.php) | "greatest market share worldwide" 명시 |
| 32 | 제품 페이지 | 주성엔지니어링 "Semiconductor Products" | — | [jusung.com](https://www.jusung.com/document/semiconductor) | SDP/TSD/UHV CVD·ALD + Dry Etch 라인업. |
| 33 | Corporate | 원익IPS | — | [wonik-ips.com](https://www.wonik-ips.com) | PE-CVD, ALD, Display dry etcher. |
| 34 | Corporate | TES Co., Ltd. | — | [tes.co.kr](https://www.tes.co.kr) | PECVD, Gas Phase Etch (GPE). |
| 35 | Corporate | Eugene Technology | — | [eugenetech.com](https://www.eugenetech.com) | LPCVD, ALD, Batch CVD. standalone etch 제품 없음 |

-----
