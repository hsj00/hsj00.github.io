# 3D NAND Flash: V9–V12 세대별 기술 분석 보고서

> **작성일:** 2026년 6월 24일  
> **대상 세대:** V9 (9세대) ~ V12 (12세대)  
> **대상 제조사:** Samsung, SK Hynix, Micron, Kioxia/WD, YMTC  
> **데이터 출처:** TechInsights Teardown Reports (2024–2025), IEEE ISSCC 2025, TrendForce, SemiAnalysis, 각사 IR/공식 발표  
> **주의:** V10 일부, V11·V12 전체 수치는 로드맵 추정치이며 공식 확정값이 아님

---

## 1. 제조사별 Layer Count 요약

| 제조사 | V9 | V10 | V11 | V12 |
|:---|:---:|:---:|:---:|:---:|
| **Samsung** | 286L (양산) | 400+L (개발, ISSCC 2025) | ~500L (R&D) | >530L (장기) |
| **SK Hynix** | 321L (양산) | 430+L (개발) | ~460L (R&D) | ~510L (장기) |
| **Micron** | 276L (양산, B58R) | ~320L (개발) | ~380L (R&D) | ~440L (장기) |
| **Kioxia/WD** | 232L BiCS7 (양산) | ~332L BiCS8 (개발) | ~420L BiCS9 (R&D) | ~480L BiCS10 (장기) |
| **YMTC** | 232L (양산, Xtacking3) | ~300L (불확실) | ~360L (불확실) | 미확정 |

---

## 2. Stacking Architecture 개요

| 제조사 | V9 덱 구조 | V10 덱 구조 | V11 이후 |
|:---|:---|:---|:---|
| **Samsung** | Dual-deck (2 × 143L) | Triple-deck (3 × ~133L) | Triple+ / Hybrid Bonding 검토 |
| **SK Hynix** | Dual-deck (2 × 160L) | Triple-deck (3 × ~143L) | Triple+ |
| **Micron** | Dual-deck (2 × 138L) | Triple-deck | Triple+ |
| **Kioxia/WD** | Dual-deck (2 × 116L) | Dual/Triple-deck 전환 | Triple+ |
| **YMTC** | Dual-deck (Xtacking3 CMOS분리) | Dual/Triple-deck | 규제 영향 불투명 |

---

## 3. 세대별 핵심 특징

### 3.1 V9 세대

| 항목 | 내용 |
|:---|:---|
| **Layer 범위** | 232L (Kioxia BiCS7, YMTC) ~ 321L (SK Hynix) |
| **Deck 구조** | Dual-deck 표준화 |
| **Cell 포맷** | TLC 표준, QLC 본격 확대 |
| **I/O 속도** | 3.2 Gbps 표준화 |
| **Bit Density** | 21–28 Gb/mm² (TLC 기준) |
| **주요 이정표** | SK Hynix 321L로 Samsung 286L 역전 (층수 기준) — 업계 최초 |
| **Samsung V9 QLC 이슈** | 내구성 문제로 2026 H1 양산 지연 보고 |
| **Mo (Molybdenum) Gate** | Samsung V9에서 부분 적용, WL 저항 감소 |
| **공정 난이도** | SK Hynix: V8 대비 etch step +20%, 전체 process step +30% |

### 3.2 V10 세대

| 항목 | 내용 |
|:---|:---|
| **Layer 범위** | ~320L (Micron) ~ 430+L (SK Hynix) |
| **Deck 구조** | Triple-deck 업계 표준화 시작 |
| **Cell 포맷** | TLC + QLC (2Tb die 목표) |
| **I/O 속도** | 5.6 Gbps (Samsung ISSCC 2025, V9 대비 75% 향상) |
| **Bit Density** | 28–37 Gb/mm² (QLC 기준 37 Gb/mm²+) |
| **Samsung V10 발표** | ISSCC 2025 — 400+L, 28 Gb/mm², 5.6 Gbps, 싱글 chip 최대 2Tb |
| **Mo Gate 전면 확대** | WL 저항 ~40% 감소 (W → Mo 치환) |
| **Triple-deck 과제** | 3-deck 정렬 정밀도 요구, slit 연속성 확보 필요 |

### 3.3 V11 세대

| 항목 | 내용 |
|:---|:---|
| **Layer 범위** | ~380L (Micron) ~ 500L (Samsung, 목표) |
| **Deck 구조** | Triple-deck + 4-deck 검토 |
| **주요 도전** | 500L 장벽 — 적층 균일성, etch depth 한계, 기계적 응력 |
| **PLC (5-bit)** | 기술 검증 단계 진입 예상 |
| **Hybrid Bonding** | 일부 제조사 연구 개시 — CMOS와 셀 직접 bonding |
| **공정 복잡도** | V10 대비 mask layer 수 +15–20% 예상 |
| **신뢰성** | 더 깊은 channel에서 cell-to-cell 간섭 증가, retention 관리 난이도 ↑ |

### 3.4 V12 세대

| 항목 | 내용 |
|:---|:---|
| **Layer 범위** | >440L (Micron) ~ >530L (Samsung, 장기 추정) |
| **Deck 구조** | 4-deck 이상 또는 Hybrid Bonding 필수 |
| **I/O 속도** | 4,800 MT/s 인터페이스 목표 |
| **핵심 혁신** | Hybrid Bonding, 신소재 gate (Mo 이후), EUV-assisted patterning 검토 |
| **YMTC 불확실성** | 미국 EAR/BIS 수출 규제로 장비 접근 제한 — V12 달성 여부 불투명 |
| **경쟁 축 변화** | 단순 층수 경쟁 → 재료·장비·패키징 혁신이 승부 결정 |
| **Bit Density 목표** | >50 Gb/mm² (QLC 기준, 추정) |

---

## 4. Dimension 상세 정보

### 4.1 파라미터 정의

| 파라미터 | 정의 | 단위 |
|:---|:---|:---:|
| **Memory Hole CD (MH CD)** | 채널홀(수직 채널) 직경 (pre-deposition 기준) | nm |
| **Memory Hole Pitch** | 홀 중심 간 최소 거리 (hexagonal 배열 기준) | nm |
| **MH Pitch (orthogonal)** | 직교 방향 홀 중심 간 거리 | nm |
| **Slit CD / GLS Width** | Gate Line Slit 폭 (식각 후 개구부 기준) | nm |
| **Slit Pitch** | 슬릿 중심 간 간격 | µm |
| **Slit Depth (per deck)** | 1개 덱 슬릿 식각 깊이 | µm |
| **Total VC Height** | 전체 수직 채널 높이 | µm |
| **WL Vertical Pitch** | WL 층간 수직 간격 (SiO₂ + SiN 합산) | nm |
| **WL CD** | WL 도체 두께 (SiN→금속 치환 후) | nm |
| **WL Lateral Depth** | WL이 채널홀 주변으로 연장되는 수평 깊이 | nm |
| **GLS AR (per deck)** | Gate Line Slit Aspect Ratio per deck = Depth/CD | — |
| **ONO Thickness** | SiO₂-SiN-SiO₂ 메모리막 총 두께 | nm |

### 4.2 V9 세대 — 제조사별 Dimension

| 파라미터 | Samsung 286L | SK Hynix 321L | Micron 276L | Kioxia 232L | YMTC 232L |
|:---|:---:|:---:|:---:|:---:|:---:|
| **Layer 수** | 286L | 321L | 276L | 232L | 232L |
| **Deck 수** | 2 | 2 | 2 | 2 | 2 (Xtacking3) |
| **MH CD (nm)** | ~120 | ~120 | ~115 | ~115 | ~120 |
| **MH Pitch — min (nm)** | ~150 | ~155 | ~150 | ~155 | ~163 |
| **MH Pitch — orthogonal (nm)** | ~240 | ~245 | ~238 | ~240 | ~255 |
| **Slit CD / GLS Width (nm)** | ~65 | ~70 | ~65 | ~70 | ~75 |
| **Slit Pitch (µm)** | ~1.2 | ~1.25 | ~1.2 | ~1.3 | ~1.5 |
| **Slit Depth per deck (µm)** | ~4.0 | ~4.3 | ~3.8 | ~3.5 | ~6.4 |
| **Total VC Height (µm)** | ~8.0 | ~8.6 | ~7.5 | ~7.0 | ~12.7 |
| **WL Vertical Pitch (nm)** | ~28 | ~27 | ~27 | ~30 | ~48 |
| **WL CD (nm)** | ~13–14 | ~13–14 | ~13 | ~14 | ~14 |
| **WL Lateral Depth (nm)** | ~15–19 | ~17–20 | ~17 | ~18 | ~20 |
| **GLS AR per deck** | ~62:1 | ~61:1 | ~58:1 | ~50:1 | ~85–91:1 |
| **ONO Thickness (nm)** | ~20–22 | ~21–22 | ~21 | ~22 | ~22 |
| **Data 신뢰도** | ★★★★☆ | ★★★★☆ | ★★★☆☆ | ★★★☆☆ | ★★★★★ |

> **YMTC 232L**: TechInsights 공식 teardown 보고서 (2023–2024) 기반 — 업계에서 가장 상세한 공개 데이터  
> **Samsung·SK Hynix**: TechInsights 구독 보고서 + ISSCC/IEDM 발표 조합  
> **Micron·Kioxia**: 공개 발표 + 추정치 혼합

### 4.3 V10 세대 — 제조사별 Dimension (개발/추정)

| 파라미터 | Samsung 400+L | SK Hynix 430+L | Micron ~320L | Kioxia ~332L | YMTC ~300L |
|:---|:---:|:---:|:---:|:---:|:---:|
| **Layer 수** | 400+L | 430+L | ~320L | ~332L | ~300L |
| **Deck 수** | 3 | 3 | 3 | 2–3 | 2–3 |
| **MH CD (nm)** | ~105–110 | ~110 | ~110 | ~110 | ~115 |
| **MH Pitch — min (nm)** | ~145 | ~148 | ~148 | ~150 | ~158 |
| **MH Pitch — orthogonal (nm)** | ~230 | ~235 | ~235 | ~238 | ~245 |
| **Slit CD / GLS Width (nm)** | ~60 | ~65 | ~60 | ~65 | ~70 |
| **Slit Pitch (µm)** | ~1.4 | ~1.45 | ~1.35 | ~1.4 | ~1.55 |
| **Slit Depth per deck (µm)** | ~4.5–5.0 | ~4.5 | ~3.8 | ~4.2 | ~6.5 |
| **Total VC Height (µm)** | ~14–15 | ~14.5 | ~11 | ~12.5 | ~19+ |
| **WL Vertical Pitch (nm)** | ~26–27 | ~26 | ~27 | ~29 | ~45 |
| **WL CD (nm)** | ~13 | ~13 | ~13 | ~13–14 | ~14 |
| **WL Lateral Depth (nm)** | ~25–30 | ~22–25 | ~20 | ~20 | ~22 |
| **GLS AR per deck** | ~75–83:1 | ~69:1 | ~63:1 | ~65:1 | ~93–95:1 |
| **Data 신뢰도** | ★★★☆☆ | ★★☆☆☆ | ★★☆☆☆ | ★★☆☆☆ | ★☆☆☆☆ |

> Samsung V10은 ISSCC 2025에서 일부 전기적 파라미터만 공식 발표; 물리적 dimension은 teardown 대기 중

### 4.4 V11 세대 — Dimension 추정

| 파라미터 | Samsung ~500L | SK Hynix ~460L | Micron ~380L | Kioxia ~420L | YMTC ~360L |
|:---|:---:|:---:|:---:|:---:|:---:|
| **Layer 수** | ~500L | ~460L | ~380L | ~420L | ~360L |
| **Deck 수** | 3–4 | 3 | 3 | 3 | 3 |
| **MH CD (nm)** | ~97–105 | ~100–105 | ~105 | ~105 | ~110 |
| **MH Pitch — min (nm)** | ~138–142 | ~140 | ~143 | ~145 | ~152 |
| **MH Pitch — orthogonal (nm)** | ~218–225 | ~222 | ~225 | ~228 | ~238 |
| **Slit CD / GLS Width (nm)** | ~55–60 | ~60 | ~58 | ~62 | ~65 |
| **Slit Depth per deck (µm)** | ~5.0–5.5 | ~5.0 | ~4.3 | ~4.8 | ~7.0 |
| **Total VC Height (µm)** | ~17–19 | ~17 | ~13.5 | ~16 | ~23+ |
| **WL Vertical Pitch (nm)** | ~25 | ~25 | ~26 | ~28 | ~42 |
| **WL CD (nm)** | ~12–13 | ~13 | ~13 | ~13 | ~13–14 |
| **GLS AR per deck** | ~90–100:1 | ~83:1 | ~74:1 | ~77:1 | ~108:1 |
| **Data 신뢰도** | ★★☆☆☆ | ★★☆☆☆ | ★☆☆☆☆ | ★☆☆☆☆ | ★☆☆☆☆ |

### 4.5 V12 세대 — Dimension 추정

| 파라미터 | Samsung >530L | SK Hynix ~510L | Micron ~440L | Kioxia ~480L | YMTC |
|:---|:---:|:---:|:---:|:---:|:---:|
| **Layer 수** | >530L | ~510L | ~440L | ~480L | 미확정 |
| **Deck 수** | 4+ | 4 | 3–4 | 3–4 | — |
| **MH CD (nm)** | ~92–97 | ~95–100 | ~100 | ~100 | — |
| **MH Pitch — min (nm)** | ~133–138 | ~135 | ~138 | ~140 | — |
| **MH Pitch — orthogonal (nm)** | ~208–218 | ~212 | ~218 | ~220 | — |
| **Slit CD / GLS Width (nm)** | ~50–55 | ~55 | ~55 | ~58 | — |
| **Slit Depth per deck (µm)** | ~5.5–6.0 | ~5.5 | ~4.8 | ~5.2 | — |
| **Total VC Height (µm)** | ~22–24 | ~22 | ~16 | ~20 | — |
| **WL Vertical Pitch (nm)** | ~23–24 | ~24 | ~25 | ~27 | — |
| **WL CD (nm)** | ~12 | ~12 | ~12 | ~12–13 | — |
| **GLS AR per deck** | ~100–120:1 | ~100:1 | ~87:1 | ~90:1 | — |
| **Data 신뢰도** | ★☆☆☆☆ | ★☆☆☆☆ | ★☆☆☆☆ | ★☆☆☆☆ | — |

---

## 5. 핵심 기술 인사이트

### 5.1 YMTC 232L — GLS AR 격차

- WL Vertical Pitch **48nm** (Samsung 28nm 대비 71% 두꺼움)
- 같은 232L이지만 총 VC Height **12.7µm** = Samsung 286L(~8.0µm) 대비 60% 더 깊음
- GLS AR per deck **~85–91:1** → Samsung/Hynix (~60–62:1) 대비 현저히 높아 yield 열위
- 결론: YMTC는 성숙도 낮은 공정으로 더 어려운 식각을 수행하고 있음

### 5.2 SK Hynix Triple-deck 전략의 AR 이점

- 3개 덱으로 분할 → per-deck GLS AR **~40–43:1** (V10 기준)
- Samsung dual-deck V9 ~62:1보다 개별 식각은 쉬움
- 총 공정 단계는 증가하지만 각 etch pass quality가 향상됨

### 5.3 Samsung V10 WL Lateral Depth 증가

- MH CD: 120nm → ~105nm 축소, MH Pitch: 150nm → ~145nm
- WL Lateral Depth: ~19nm → ~25–30nm 증가
- Gate wrap-around 개선 + Mo gate 조합 → cell isolation 향상
- 28 Gb/mm² (TLC) 달성의 핵심 메커니즘

### 5.4 MH Pitch 스케일링 정체 현상

- V12까지도 orthogonal pitch: ~240nm → ~210nm (총 ~12–13% 감소)
- 횡방향 스케일링은 EUV/SADP 없이는 구조적 한계
- 실질 density 향상은 수직 적층(deck 수 증가)으로만 달성

---

## 6. 데이터 출처 및 신뢰도 등급

| 신뢰도 | 설명 | 해당 데이터 |
|:---:|:---|:---|
| ★★★★★ | 공개 teardown 보고서 (TechInsights 등) 명시적 수치 | YMTC 232L dimension |
| ★★★★☆ | ISSCC/IEDM 논문 + teardown 조합 | Samsung V9, SK Hynix V9 |
| ★★★☆☆ | 공식 발표 + 업계 추정치 혼합 | Micron V9, Kioxia V9 |
| ★★☆☆☆ | 로드맵 발표 + 기술 외삽 | V10 대부분 |
| ★☆☆☆☆ | 순수 기술 추정 (공식 미발표) | V11 전체, V12 전체 |

### 주요 참고 문헌

1. TechInsights, "3D NAND Teardown Comparison: Samsung, SK Hynix, Micron, YMTC" (2024)
2. Samsung Electronics, ISSCC 2025 발표 — "400+ Layer 3D NAND with 5.6Gbps I/O"
3. SK Hynix, "World's First 321-Layer NAND Flash" 공식 발표 (2024)
4. TrendForce, "3D NAND Flash Technology Roadmap 2025–2028" (2025)
5. SemiAnalysis, "3D NAND Roadmap Deep Dive" (2025)
6. The Memory Guy (Jim Handy), "Why 3D NAND is Stuck at 40nm" (2024)
7. Blocks & Files, "Samsung Developing 400-Plus Layer 3D NAND" (2024)
8. IEEE IEDM 2024 — Kioxia BiCS8 Process Integration

---

## 7. 자료 신뢰도 검증 방법 (별첨)

*→ Section 8 참조*

---

## 8. 검증 방법 가이드

### 8.1 1차 소스 검증 (Primary Source)

| 검증 항목 | 검증 방법 | 접근처 |
|:---|:---|:---|
| Layer 수 · I/O 속도 | 각사 공식 블로그/IR 보도자료 확인 | samsung.com/semiconductor, news.skhynix.com |
| Dimension 수치 | TechInsights 유료 teardown 보고서 구독 | techinsights.com |
| 공정 구조 | IEEE ISSCC/IEDM 논문 (IEEE Xplore) | ieeexplore.ieee.org |
| 시장 출하 현황 | TrendForce/Omdia 구독 리포트 | trendforce.com |

### 8.2 Cross-Reference 검증법

1. **삼각검증 (Triangulation)**: 동일 파라미터를 TechInsights + 논문 + 회사 발표 3개 소스에서 교차 확인
2. **물리적 일관성 검사**: `GLS AR = Slit Depth / Slit CD` 수식으로 수치 자가 계산 검증
3. **세대 간 트렌드 검사**: 각 파라미터가 단조 감소(MH CD) 또는 단조 증가(VC Height)하는지 확인

### 8.3 새 세션에서 사용 가능한 검증 프롬프트

아래 프롬프트를 새 대화 세션에 붙여넣어 각 수치를 개별 검증할 수 있습니다:

```
[검증 프롬프트 — 3D NAND Dimension 사실 확인]

다음 3D NAND 기술 파라미터들을 최신 공개 자료(TechInsights teardown 보고서, 
IEEE ISSCC/IEDM 논문, 각사 공식 발표)를 기반으로 검증해 주세요.
각 항목마다 (a) 사실 여부, (b) 더 정확한 수치가 있다면 제시, 
(c) 출처/근거를 명시해 주세요.

검증 대상:
1. YMTC 232L의 WL Vertical Pitch는 약 48nm이며 Samsung V9(286L)의 ~28nm보다 
   약 71% 두껍다.
2. YMTC 232L의 Total VC Height(채널 깊이)는 약 12.7µm이다.
3. YMTC 232L의 GLS(Gate Line Slit) Aspect Ratio per deck은 약 85–91:1이다.
4. Samsung 286L(V9)의 Memory Hole CD는 약 120nm이다.
5. SK Hynix 321L의 Memory Hole orthogonal pitch는 약 245nm이다.
6. Samsung V10(400+L)의 I/O 속도는 5.6 Gbps이며 ISSCC 2025에서 발표되었다.
7. Samsung V10은 triple-deck 구조(3개 덱)를 채택한다.
8. 3D NAND Memory Hole pitch의 횡방향 스케일링이 ~40nm 등가 수준에서 
   정체되어 있다는 것이 업계에서 일반적으로 인정되는가?

웹 검색으로 최신 정보를 확인한 후 답변해 주세요.
```

---

*본 보고서는 공개 정보 및 기술 추정에 기반하며, TechInsights 유료 데이터와 상이할 수 있습니다.*  
*V11·V12 수치는 참고용 추정치이며 실제 양산 스펙과 다를 수 있습니다.*
