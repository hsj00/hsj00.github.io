---
title: "Device Physics for Metal ALD · W2 — 두 물질을 붙이면 밴드가 휜다 (2) pn 접합"
layout: post
date: 2026-08-07 11:00:00+0900
description: "밴드 벤딩의 교과서적 사례인 pn 접합을 본다. 내장 전위의 세 가지 얼굴, 도핑이 정하는 공핍폭, 그리고 공핍층을 커패시터로 읽는 C-V 프로파일링까지 정리한다."
tags:
    - Device physics
    - pn junction
    - Depletion region
    - Built-in potential
    - C-V profiling
categories: Device-Physics
author: hsj00
externalLink: true
published: true
giscus_comments: true
share: true
use_math: true
toc:
  beginning: true
---

<style>
/* 다크 모드에서도 그림이 읽히도록 본문 SVG에 밝은 배경을 준다 */
#markdown-content svg { background:#fbfbf9; border:1px solid #d7dbd5; border-radius:4px; padding:8px; box-sizing:border-box; }
</style>

[1편]({% post_url 2026-08-07-w2a-band-bending %})에서 두 물질을 붙이면 E<sub>F</sub>를 맞추기 위해 밴드가 휜다는 것을 보았다. 이번 2편에서는 그 휘어짐이 가장 깨끗하게 드러나는 사례인 **pn 접합**을 다룬다. 여기서 익히는 내장 전위와 공핍폭의 감각이 [3편의 금속과 반도체 접촉]({% post_url 2026-08-07-w2c-schottky-ohmic %})에서 그대로 쓰인다.

간단히 되짚어 두면, **E<sub>F</sub>(페르미 준위)**는 전자 한 개를 그 위치에 추가하는 데 드는 총비용이고, 평형에서는 접촉한 물질 전체에서 하나로 평평해진다. **일함수 Φ**는 진공 준위에서 E<sub>F</sub>까지의 거리다.

---

## pn 접합, 밴드 벤딩의 교과서적 사례

**도너(donor)**는 전자를 하나 내놓는 불순물(As, P 등)로 n형을 만들고, **억셉터(acceptor)**는 전자를 하나 받는 불순물(B 등)로 p형을 만든다(W1 §04). 내놓거나 받은 뒤 불순물 자신은 이온화되어 **고정된 전하**(도너는 +, 억셉터는 −)로 남는다. 이 "고정 전하"가 이 편의 핵심이다.

p형과 n형을 붙이면 n형의 전자와 p형의 정공이 계면에서 만나 재결합하며 사라진다[^1]. 남는 것은 이온화된 도펀트, 즉 고정 전하뿐인 **공핍 영역(depletion region)**이다. 이 고정 전하가 전기장을 만들고 밴드를 휜다.

1편의 규칙이 그대로 적용된다는 점을 확인해 두자. n형은 E<sub>F</sub>가 높고 p형은 낮으므로 **n측이 전자를 내보내 (+), p측이 받아들여 (−)**가 된다. 다만 금속과 달리 남은 전하가 움직이지 못하는 이온화된 도펀트의 형태로 드러날 뿐이다.

<svg xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto" viewBox="0 0 720 300" role="img" aria-label="pn 접합의 평형 밴드 다이어그램">
  <text x="360" y="18" font-size="12" fill="#4d565e" text-anchor="middle">평형 상태 (인가 전압 0)</text>
  <!-- E_F 평평 -->
  <line x1="60" y1="175" x2="660" y2="175" stroke="#14181c" stroke-width="2" stroke-dasharray="8 4"/>
  <text x="666" y="179" font-size="11.5" fill="#14181c" font-weight="700" font-family="monospace">E_F</text>
  <!-- p측 (좌, 밴드 높음) / n측 (우, 밴드 낮음) -->
  <!-- E_C -->
  <path d="M 60 95 L 250 95 C 300 95, 320 200, 370 200 L 660 200" fill="none" stroke="#2f6fd0" stroke-width="2.4"/>
  <!-- E_V -->
  <path d="M 60 232 L 250 232 C 300 232, 320 285, 370 285 L 660 285" fill="none" stroke="#b8443c" stroke-width="2.4"/>
  <text x="70" y="88" font-size="11" fill="#2f6fd0" font-weight="600" font-family="monospace">E_C</text>
  <text x="70" y="228" font-size="11" fill="#b8443c" font-weight="600" font-family="monospace">E_V</text>
  <text x="620" y="193" font-size="11" fill="#2f6fd0" font-family="monospace">E_C</text>

  <!-- 영역 라벨 -->
  <rect x="60" y="45" width="200" height="12" fill="#b8443c" opacity="0.12"/>
  <rect x="460" y="45" width="200" height="12" fill="#2f6fd0" opacity="0.12"/>
  <rect x="260" y="45" width="200" height="12" fill="#8a4b12" opacity="0.14"/>
  <text x="160" y="40" font-size="12" fill="#b8443c" text-anchor="middle" font-weight="600">p형 (정공)</text>
  <text x="560" y="40" font-size="12" fill="#2f6fd0" text-anchor="middle" font-weight="600">n형 (전자)</text>
  <text x="360" y="40" font-size="11.5" fill="#8a4b12" text-anchor="middle" font-weight="600">공핍 영역</text>

  <!-- qVbi -->
  <line x1="285" y1="95" x2="285" y2="200" stroke="#0d6e66" stroke-width="1.6"/>
  <line x1="280" y1="95" x2="290" y2="95" stroke="#0d6e66" stroke-width="1.6"/>
  <line x1="280" y1="200" x2="290" y2="200" stroke="#0d6e66" stroke-width="1.6"/>
  <text x="294" y="152" font-size="12" fill="#0d6e66" font-weight="700">qV_bi</text>
  <text x="294" y="167" font-size="9.5" fill="#0d6e66">내장 전위 장벽</text>

  <!-- 고정 이온 전하 -->
  <g font-size="13" font-weight="700" text-anchor="middle">
    <text x="300" y="262" fill="#b8443c">&#8722;</text><text x="320" y="262" fill="#b8443c">&#8722;</text><text x="340" y="262" fill="#b8443c">&#8722;</text>
    <text x="380" y="262" fill="#2f6fd0">+</text><text x="400" y="262" fill="#2f6fd0">+</text><text x="420" y="262" fill="#2f6fd0">+</text>
  </g>
  <text x="330" y="280" font-size="9.5" fill="#b8443c" text-anchor="middle">억셉터 이온(&#8722;)</text>
  <text x="400" y="280" font-size="9.5" fill="#2f6fd0" text-anchor="middle">도너 이온(+)</text>
</svg>

**그림 1.** pn 접합의 평형 밴드 다이어그램. **E<sub>F</sub>는 평평하고, 밴드가 휘어 내장 전위 qV<sub>bi</sub>를 만든다.** 공핍 영역에는 이동 가능한 캐리어가 없고 이온화된 도펀트만 남는다. 대칭 도핑(N<sub>a</sub> = N<sub>d</sub> = 10¹⁷)이면 V<sub>bi</sub> ≈ 0.84 V, 공핍폭 ≈ 147 nm다.

### 내장 전위란 무엇인가, 세 가지 얼굴

V<sub>bi</sub>는 W2 전체에서 계속 나오므로 개념을 확실히 잡아두자. 내장 전위는 같은 것을 세 가지 방식으로 볼 수 있다.

1. **페르미 준위의 차이(접촉 전).** 붙이기 전 p측과 n측은 E<sub>F</sub>가 서로 다른 높이에 있었다(도핑이 E<sub>F</sub>를 옮기므로, W1 §04). 그 높이 차이가 곧 qV<sub>bi</sub>다. 붙이면 E<sub>F</sub>가 하나로 정렬되는데, 그 정렬을 위해 밴드가 휜 양이 V<sub>bi</sub>다.
2. **확산을 막는 전위벽.** n측엔 전자가, p측엔 정공이 많다. 농도차 때문에 서로 상대편으로 확산하려 한다. 하지만 넘어갈수록 공핍층의 고정 이온이 만드는 전기장이 되민다(드리프트). V<sub>bi</sub>는 확산하려는 힘을 정확히 상쇄하는 만큼의 전위다.
3. **다이오드의 "켜짐" 기준.** 순바이어스 V를 걸면 장벽이 (V<sub>bi</sub> − V)로 낮아져 확산이 우세해지고 전류가 지수적으로 는다. V<sub>bi</sub>가 다이오드가 켜지는 문턱의 물리적 기준인 이유다.

<svg xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto" viewBox="0 0 720 250" role="img" aria-label="평형에서 드리프트 전류와 확산 전류가 균형을 이루어 내장 전위가 형성됨">
  <text x="360" y="20" font-size="12" fill="#14181c" text-anchor="middle" font-weight="700">평형 = 확산과 드리프트의 균형</text>
  <!-- 공핍층 박스 -->
  <rect x="270" y="50" width="180" height="150" fill="#8a4b12" opacity="0.08" stroke="#d7dbd5"/>
  <rect x="60" y="50" width="210" height="150" fill="#b8443c" opacity="0.06"/>
  <rect x="450" y="50" width="210" height="150" fill="#2f6fd0" opacity="0.06"/>
  <text x="160" y="42" font-size="11" fill="#b8443c" text-anchor="middle" font-weight="600">p측 (정공 多)</text>
  <text x="360" y="42" font-size="10.5" fill="#8a4b12" text-anchor="middle" font-weight="600">공핍층</text>
  <text x="555" y="42" font-size="11" fill="#2f6fd0" text-anchor="middle" font-weight="600">n측 (전자 多)</text>

  <!-- 확산 (농도차 따라, 서로 상대편으로) -->
  <line x1="470" y1="95" x2="300" y2="95" stroke="#2f6fd0" stroke-width="2.4" marker-end="url(#dar)"/>
  <text x="490" y="99" font-size="10.5" fill="#2f6fd0" font-weight="700">전자 확산 &#8594;p</text>
  <line x1="250" y1="120" x2="420" y2="120" stroke="#b8443c" stroke-width="2.4" marker-end="url(#dar2)"/>
  <text x="120" y="124" font-size="10.5" fill="#b8443c" font-weight="700">정공 확산 &#8594;n</text>

  <!-- 드리프트 (전기장 따라, 되미는 방향) -->
  <line x1="300" y1="160" x2="430" y2="160" stroke="#0d6e66" stroke-width="2.4" marker-end="url(#dar3)"/>
  <text x="300" y="180" font-size="10.5" fill="#0d6e66" font-weight="700">전기장(드리프트): 확산을 되민다</text>

  <!-- 전기장 표시 -->
  <text x="360" y="145" font-size="10" fill="#8a4b12" text-anchor="middle">고정이온 전기장 E</text>

  <!-- 균형 표시 -->
  <text x="360" y="215" font-size="11.5" fill="#14181c" text-anchor="middle" font-weight="700">순 전류 = 확산 &#8722; 드리프트 = 0</text>
  <text x="360" y="233" font-size="10" fill="#4d565e" text-anchor="middle">V_bi = 이 균형을 만드는 전위</text>

  <defs>
    <marker id="dar" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="#2f6fd0"/></marker>
    <marker id="dar2" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="#b8443c"/></marker>
    <marker id="dar3" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="#0d6e66"/></marker>
  </defs>
</svg>

**그림 2.** 평형의 실체. 확산(농도차로 서로 상대편으로 가려는 흐름)과 드리프트(공핍층 전기장이 되미는 흐름)가 크기가 같고 방향이 반대여서 순 전류가 0이다. 정지한 것이 아니라 두 흐름이 팽팽히 맞선 동적 균형이며, V<sub>bi</sub>는 이 균형을 만드는 전위다.

> **역설: 있는데 못 잰다**
>
> V<sub>bi</sub>는 실재하는 전위벽인데, 접합 양단에 전압계를 대면 0 V가 나온다. 모순 같지만 아니다. 전압계를 연결하면 그 금속과 반도체의 접촉부에 V<sub>bi</sub>를 정확히 상쇄하는 접촉 전위가 생긴다. 닫힌 회로를 한 바퀴 돌면 전위차의 합은 0이어야 하기 때문이다. 아니면 영구기관이 된다. V<sub>bi</sub>는 **"내부" 전위**다. 존재하지만 외부 단자에서 직접 측정할 수 없고, C-V의 절편이나 광기전력 같은 간접적 방법으로만 접근한다.
>
> "상쇄가 정확히 일어나는" 근본 이유는 따로 있다. W1 §03에서 본 대로 **전압계가 재는 것은 정전 퍼텐셜이 아니라 E<sub>F</sub>(전기화학 퍼텐셜)의 차이**다. 평형에서는 전압계 내부까지 포함한 회로 전체에서 E<sub>F</sub>가 하나의 평평한 선이므로, ΔE<sub>F</sub> = 0이고 전압계는 0 V를 읽을 수밖에 없다. V<sub>bi</sub>는 정전 퍼텐셜의 차이일 뿐 E<sub>F</sub>의 차이가 아니다. 접촉 전위들이 우연히 맞아떨어지는 것이 아니라, **E<sub>F</sub> 평탄이라는 평형 조건이 모든 접촉부의 전위차를 그렇게 되도록 강제하는 것**이다. 전압을 "건다"는 것은 곧 두 단자의 E<sub>F</sub>를 어긋나게 하는 일이며, W3의 게이트 전압이 정확히 이 이야기다.

### 정전 퍼텐셜과 전기화학 퍼텐셜, 전압계는 무엇을 재는가

방금의 역설을 제대로 소화하려면 "전위"라고 뭉뚱그려 부르는 것 안에 서로 다른 두 층이 있다는 것을 구분해야 한다.

- **정전 퍼텐셜 φ.** 전기장만이 만드는 에너지 지형이다. 시험 전하 하나를 그 지점에 두었을 때 전기장 때문에 갖는 위치 에너지이며, 전자는 −qφ다. 공핍층의 고정 이온이 만드는 V<sub>bi</sub>가 바로 이 φ의 언덕이다.
- **화학 퍼텐셜.** 전기장과 무관하게, 입자가 얼마나 빽빽하게 몰려 있고 어떤 상태에 있는가가 주는 에너지 기여다. 농도가 높은 곳의 전자는 그 자체로 "나가고 싶은" 압력을 받는다. 확산의 근원이다.
- **전기화학 퍼텐셜 = E<sub>F</sub>.** 위 둘의 합이다. 전자 한 개를 그 위치에 추가하는 총비용(W1 §03의 "전자의 가격")으로, 전기적 비용과 화학적 비용을 모두 포함한다.

이 구분이 중요한 이유는 하나다. **전류를 모는 것은 φ의 기울기가 아니라 E<sub>F</sub>의 기울기다.** 드리프트(전기장, 즉 φ의 기울기가 밂)와 확산(농도차, 즉 화학 퍼텐셜의 기울기가 밂)을 따로 쓰던 두 항은, 합쳐 놓으면 "전류는 E<sub>F</sub>의 기울기에 비례한다"는 한 줄로 통합된다(아래 S3). 평형에서 E<sub>F</sub>가 평평하다는 것은 곧 순전류가 0이라는 말과 동의어다. φ가 내부에서 0.84 V나 출렁여도 상관이 없다.

> **평형의 실감: 수천 A/cm²가 상쇄되고 있다**
>
> 10¹⁷ 대칭 접합의 공핍층을 가로지르며 전자 농도는 10¹⁷에서 약 9×10²(p측 소수 캐리어)까지 14자릿수 떨어진다. 이 어마어마한 농도 기울기가 미는 확산과, E<sub>max</sub> ≈ 0.11 MV/cm의 전기장이 되미는 드리프트는 위치에 따라 각각 수천에서 수만 A/cm² 스케일이다. 실제 다이오드의 정격 전류밀도(약 1에서 100 A/cm²)보다 큰 흐름 둘이 매 지점에서 정확히 상쇄되어 순전류 0을 만든다. 그림 2의 "동적 균형"이 정량적으로 이 정도라는 뜻이다. 순바이어스가 하는 일은 이 팽팽한 균형을 아주 조금 기울이는 것뿐인데, 상쇄되던 흐름이 워낙 커서 작은 어긋남으로도 큰 순전류가 나온다. 다이오드 전류가 지수적인 또 하나의 이유다.

마지막으로 한 줄 예고. 전압을 걸거나 빛을 쬐어 비평형이 되면 E<sub>F</sub>는 하나로 유지되지 못하고 전자용(E<sub>Fn</sub>)과 정공용(E<sub>Fp</sub>)으로 갈라진다. **유사 페르미 준위(quasi-Fermi level)**라 부르며, 갈라진 폭이 곧 qV다. MOSFET의 채널 전류(W4)와 태양전지, LED를 서술하는 언어가 이것이다.

> **상한은 밴드갭**
>
> 도핑을 올리면 V<sub>bi</sub>가 커지지만(그림 3) 무한정 커지지 않는다. 상한은 대략 E<sub>g</sub>/q = 1.12 V다. 양쪽 E<sub>F</sub>가 각자의 밴드 가장자리에 바싹 붙어도 두 E<sub>F</sub> 차이가 밴드갭을 넘을 수 없기 때문이다. 참고로 볼츠만 근사식(아래 S1)을 축퇴 영역(10¹⁹ 이상)에 그대로 넣으면 V<sub>bi</sub>가 E<sub>g</sub>/q보다 크다는 **비물리적 값**이 나오는데, 이는 그 식이 비축퇴 가정 위에 있기 때문이다. 실제로는 E<sub>g</sub>/q 부근에서 포화한다. **이것이 그림 3에서 V<sub>bi</sub> 곡선이 완만한 근본 이유**다.

> **현장 포인트: V<sub>bi</sub>는 "공짜 장벽"이자 "공짜 공핍층"**
>
> V<sub>bi</sub>는 전압을 걸지 않아도 이미 존재하므로, 소자는 이 내장 장벽과 공핍층을 "공짜로" 얻는다. DRAM 셀 트랜지스터의 off 상태 격리, 소자 간 절연(junction isolation)이 모두 이 내장 공핍층에 기댄다. 반대로 컨택에서는 이 내장 장벽이 방해물이다. 3편에서 축퇴 도핑으로 없애려는 것이 바로 이 장벽의 금속과 반도체 버전이다. 같은 V<sub>bi</sub>가 트랜지스터에선 자산, 컨택에선 부채인 셈이다.

---

## 그 숫자들은 어디서 오고, 무엇을 좌우하는가

V<sub>bi</sub>와 공핍폭 W는 외운다기보다 **어떤 손잡이로 움직이는지**를 아는 것이 중요하다. 두 값 모두 도핑 농도가 지배한다.

> **왜 예제가 하필 10¹⁷인가**
>
> 이 편의 기준 예제(N<sub>A</sub> = N<sub>D</sub> = 10¹⁷ cm⁻³)는 임의의 숫자가 아니다. 세 조건이 겹치는 교차점이다.
>
> 1. **실소자의 전형값.** MOSFET 채널과 웰 도핑이 대략 10¹⁶에서 10¹⁸ 범위이고, 10¹⁷은 그 로그 중앙이다. 교과서용 가공값이 아니라 실제 소자 접합을 대표한다.
> 2. **모든 근사가 깨끗한 "안전지대".** 비축퇴라서 볼츠만 근사(V<sub>bi</sub> 식의 전제)가 유효하고, E<sub>00</sub> = 3.9 meV로 kT보다 훨씬 작아 순수 열전자 방출 영역이며(3편), W = 147 nm로 미세 소자 감각과 맞는 스케일이다. 10¹⁹ 이상이면 식 자체가 흔들리고(위 "상한은 밴드갭" 참조), 10¹⁵ 이하면 W가 μm급이 되어 감각이 멀어진다.
> 3. **손에 잡히는 숫자.** V<sub>bi</sub> ≈ 0.84 V는 다이오드 켜짐 전압(약 0.7 V)과 같은 동네, W ≈ 147 nm는 익숙한 공정 스케일이다. 그림 3을 읽을 때 "내 소자는 어느 구간인가"의 기준점으로 이 값을 쓰면 된다.

<svg xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto" viewBox="0 0 720 300" role="img" aria-label="도핑 농도에 따른 내장 전위와 공핍폭의 변화">
  <text x="365" y="16" font-size="11" fill="#4d565e" text-anchor="middle">대칭 접합 (N_A = N_D) 기준, 공핍폭은 로그축</text>
  <!-- 좌축 Vbi -->
  <line x1="110" y1="45" x2="110" y2="258" stroke="#0d6e66" stroke-width="1.5"/>
  <line x1="102" y1="250" x2="628" y2="250" stroke="#14181c" stroke-width="1.5"/>
  <!-- 우축 W -->
  <line x1="620" y1="45" x2="620" y2="258" stroke="#8a4b12" stroke-width="1.5"/>
  <g stroke="#e6e9e3" stroke-width="1">
    <line x1="110" y1="205" x2="620" y2="205"/><line x1="110" y1="160" x2="620" y2="160"/>
    <line x1="110" y1="115" x2="620" y2="115"/><line x1="110" y1="70" x2="620" y2="70"/>
    <line x1="238" y1="45" x2="238" y2="250"/><line x1="365" y1="45" x2="365" y2="250"/><line x1="492" y1="45" x2="492" y2="250"/>
  </g>
  <!-- 좌축 눈금 Vbi -->
  <g font-size="10" fill="#0d6e66" font-family="monospace" text-anchor="end">
    <text x="104" y="236">0.6</text><text x="104" y="199">0.7</text><text x="104" y="163">0.8</text>
    <text x="104" y="127">0.9</text><text x="104" y="90">1.0</text><text x="104" y="54">1.1</text>
  </g>
  <!-- 우축 눈금 W -->
  <g font-size="10" fill="#8a4b12" font-family="monospace" text-anchor="start">
    <text x="626" y="254">10</text><text x="626" y="167">100</text><text x="626" y="80">1000</text>
  </g>
  <!-- x 눈금 -->
  <g font-size="10.5" fill="#4d565e" font-family="monospace" text-anchor="middle">
    <text x="110" y="266">10¹⁵</text><text x="238" y="266">10¹⁶</text><text x="365" y="266">10¹⁷</text>
    <text x="492" y="266">10¹⁸</text><text x="620" y="266">10¹⁹</text>
  </g>
  <text x="365" y="288" font-size="12" fill="#14181c" text-anchor="middle" font-family="monospace">도핑 농도 N (cm⁻³)</text>
  <text x="40" y="150" font-size="11.5" fill="#0d6e66" text-anchor="middle" transform="rotate(-90 40 150)" font-family="monospace">내장 전위 V_bi (V)</text>
  <text x="690" y="150" font-size="11.5" fill="#8a4b12" text-anchor="middle" transform="rotate(-90 690 150)" font-family="monospace">공핍폭 W (nm)</text>

  <polyline points="110,237 120,234 131,230 141,226 152,223 162,219 172,216 183,212 193,209 204,205 214,202 224,198 235,194 245,191 256,187 266,184 277,180 287,177 297,173 308,170 318,166 329,162 339,159 349,156 360,152 370,148 381,145 391,141 401,138 412,134 422,131 433,127 443,124 453,120 464,116 474,113 485,109 495,106 506,102 516,99 526,95 537,92 547,88 558,84 568,81 578,78 589,74 599,70 610,67 620,63" fill="none" stroke="#0d6e66" stroke-width="3"/>
  <polyline points="110,72 120,75 131,78 141,81 152,85 162,88 172,91 183,95 193,98 204,101 214,104 224,108 235,111 245,114 256,118 266,121 277,124 287,128 297,131 308,134 318,137 329,141 339,144 349,147 360,151 370,154 381,158 391,161 401,164 412,168 422,171 433,174 443,177 453,181 464,184 474,187 485,191 495,194 506,198 516,201 526,204 537,208 547,211 558,215 568,218 578,221 589,225 599,228 610,231 620,235" fill="none" stroke="#8a4b12" stroke-width="3" stroke-dasharray="2 0"/>
  <text x="300" y="188" font-size="12" fill="#0d6e66" font-weight="700">V_bi (완만하게 증가)</text>
  <text x="150" y="74" font-size="12" fill="#8a4b12" font-weight="700">W (급격히 감소)</text>

  <!-- 1e17 마커 -->
  <line x1="365" y1="45" x2="365" y2="250" stroke="#4d565e" stroke-width="0.9" stroke-dasharray="4 3"/>
  <circle cx="365" cy="150" r="4.5" fill="#0d6e66"/>
  <circle cx="365" cy="152" r="4.5" fill="#8a4b12"/>
  <text x="372" y="136" font-size="10.5" fill="#14181c" font-weight="600">10¹⁷: V_bi 0.84 V, W 147 nm</text>
</svg>

**그림 3.** 도핑에 따른 V<sub>bi</sub>와 W. **V<sub>bi</sub>는 로그로 완만히 오르지만(10¹⁵에서 10¹⁹까지 0.60에서 1.07 V), W는 급격히 줄어든다(1243에서 17 nm).** V<sub>bi</sub>는 n<sub>i</sub>가 지수 안에 있어 로그 의존이고, W는 √(1/N)이라 도핑에 민감하다. **고농도일수록 공핍층이 얇다.** 이것이 3편 오믹 컨택(터널링)의 물리적 토대다.

세 가지를 기억하면 된다.

- **V<sub>bi</sub>는 도핑에 둔감하다(로그).** n<sub>i</sub>가 지수 안에 있기 때문이다(아래 S1). ln이 10¹⁴이라는 거대한 비율을 32라는 작은 수로 눌러버린다. 환산 규칙은 **한쪽 도핑 10배에 V<sub>bi</sub> +60 mV**(= kT ln10)다. 10¹⁵에서 10¹⁹까지 4자릿수를 올려도 V<sub>bi</sub>는 0.60에서 1.07 V로 2배가 채 안 된다. 상온 Si pn 접합의 V<sub>bi</sub>는 대체로 **0.6에서 1.0 V 범위**에 갇힌다.
- **W는 도핑에 민감하다(√(1/N)).** 같은 4자릿수 변화에 W는 1243에서 17 nm로 약 75배 줄어든다.
- **대칭 접합이면 공핍폭이 양쪽에 절반씩 걸린다**(x<sub>n</sub> = x<sub>p</sub> = 73.5 nm). 비대칭이면 저농도 쪽으로 쏠린다.

> **교재 간 n<sub>i</sub> 차이의 영향은 이번엔 작다**
>
> W1에서 n<sub>i</sub>가 Sze(9.65×10⁹)와 Neamen(1.5×10¹⁰)으로 갈린다고 했다. V<sub>bi</sub>를 계산하면 각각 0.835 V와 0.812 V로 23 mV 차이, W는 147 nm와 145 nm로 2 nm 차이에 그친다. n<sub>i</sub>가 로그 안에 들어가기 때문이다. 3편의 n<sub>i</sub> 계산과는 정반대 상황인데, 거기선 n<sub>i</sub>가 지수라 50%씩 흔들렸다. **같은 상수라도 식의 어디에 들어가느냐가 민감도를 정한다**는 좋은 예다.

> **현장 포인트: 최대 전기장과 항복**
>
> 공핍층 안의 **최대 전기장은 E<sub>max</sub> = 2V<sub>bi</sub>/W**(삼각형 분포의 꼭짓점으로 접합면에서 최대)이다. 10¹⁷ 대칭 접합의 평형값은 **약 0.11 MV/cm**로, Si 항복 전계(약 0.3 MV/cm)의 0.38배다. 평형에선 안전하다. 그러나 **역바이어스를 걸면 W는 넓어지지만 E<sub>max</sub>는 오히려 커진다**(V = −5 V에서 W 388 nm, E<sub>max</sub> 0.30 MV/cm로 항복 근접). 도핑을 10¹⁹로 올리면 평형에서도 E<sub>max</sub>가 1.3 MV/cm에 달해 **터널링 항복(제너)** 영역에 들어간다. 3편에서 애벌런치 항복과 함께 다룬다. **고농도 접합일수록 전기장이 세다**는 이 사실은 W6의 DRAM 접합 누설과 GIDL에서 다시 만난다.

> **공핍층은 저농도 쪽으로 뻗는다**
>
> 비대칭 접합(예를 들어 p⁺n에서 N<sub>a</sub> = 10¹⁸이 N<sub>d</sub> = 10¹⁵보다 훨씬 큰 경우)에서는 공핍폭의 대부분이 저농도 쪽(n)으로 뻗는다. 전체 전하 중성(N<sub>a</sub>x<sub>p</sub> = N<sub>d</sub>x<sub>n</sub>) 때문이다. 저농도 쪽은 이온이 성기므로 더 넓게 펼쳐져야 같은 전하량을 만든다. 이 사실이 3편 오믹 컨택의 핵심이 된다. **금속 옆 반도체를 고농도로 만들면 공핍층이 얇아진다.**

---

## 공핍층은 곧 커패시터다, 접합 커패시턴스

공핍 영역을 다시 보자. 이동 가능한 캐리어가 없고 고정 전하만 있는 절연층이다. 양쪽에는 캐리어가 풍부한 도체(중성 p 영역과 n 영역)가 있다. 도체와 절연체와 도체, 이것은 정확히 **평판 커패시터**의 구조다. 그래서 pn 접합은 전압을 걸지 않아도 커패시턴스를 갖는다. 단위 면적당 값은 평판 커패시터 공식 그대로다.

$$ C_j = \frac{\varepsilon_s}{W} \qquad (\text{단위 면적당},\ W = \text{공핍폭}) $$

147 nm짜리 공핍층(10¹⁷ 대칭, 평형)을 넣으면 **C<sub>j</sub> ≈ 70 nF/cm²**(= 0.70 fF/μm²)가 나온다. 여기서 결정적인 성질 하나가 따라온다. **W가 전압에 따라 변하므로 C<sub>j</sub>도 전압에 따라 변한다.** 역바이어스를 걸면 W가 넓어지고 C<sub>j</sub>는 줄어든다(10¹⁷에서 0 V부터 −5 V까지 70에서 27 nF/cm²로 2.6배 감소). 전압으로 용량을 조절하는 소자가 바로 이 원리로 동작한다(가변 커패시터, varactor).

<svg xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto" viewBox="0 0 720 300" role="img" aria-label="1/C 제곱 대 전압 그래프의 직선성과 내장 전위 절편, 기울기의 도핑 정보">
  <text x="360" y="16" font-size="11" fill="#4d565e" text-anchor="middle">1/C&#178;을 전압에 대해 그리면 직선, 절편 = V_bi, 기울기 = 도핑 (C&#8211;V 프로파일링)</text>
  <g stroke="#e6e9e3" stroke-width="1">
    <line x1="110" y1="200" x2="600" y2="200"/><line x1="110" y1="150" x2="600" y2="150"/><line x1="110" y1="100" x2="600" y2="100"/>
    <line x1="238" y1="55" x2="238" y2="250"/><line x1="366" y1="55" x2="366" y2="250"/><line x1="493" y1="55" x2="493" y2="250"/>
  </g>
  <line x1="110" y1="55" x2="110" y2="258" stroke="#14181c" stroke-width="1.5"/>
  <line x1="102" y1="250" x2="640" y2="250" stroke="#14181c" stroke-width="1.5"/>
  <g font-size="10.5" fill="#4d565e" font-family="monospace" text-anchor="middle">
    <text x="110" y="266">&#8722;3</text><text x="238" y="266">&#8722;2</text><text x="366" y="266">&#8722;1</text>
    <text x="493" y="266">0</text><text x="600" y="266">V_bi</text>
  </g>
  <text x="360" y="288" font-size="12" fill="#14181c" text-anchor="middle" font-family="monospace">인가 전압 V (역바이어스 &#8592; | &#8594; 순바이어스)</text>
  <text x="40" y="152" font-size="11.5" fill="#14181c" text-anchor="middle" transform="rotate(-90 40 152)" font-family="monospace">1 / C&#178;</text>

  <!-- 직선 -->
  <polyline points="110,55 121,59 132,64 143,68 154,73 166,77 177,82 188,86 199,90 210,95 221,99 232,104 243,108 254,112 266,117 277,121 288,126 299,130 310,135 321,139 332,143 343,148 354,152 365,157 377,161 388,166 399,170 410,174 421,179 432,183 443,188 454,192 465,196 477,201 488,205 499,210 510,214 521,219 532,223 543,227 554,232 565,236 577,241 588,245 599,249" fill="none" stroke="#0d6e66" stroke-width="3.2"/>
  <!-- Vbi 절편 마커 -->
  <circle cx="600" cy="250" r="5.5" fill="none" stroke="#b8443c" stroke-width="2.2"/>
  <line x1="600" y1="250" x2="560" y2="228" stroke="#b8443c" stroke-width="0.9"/>
  <text x="505" y="222" font-size="11" fill="#b8443c" font-weight="700">x절편 = V_bi</text>
  <text x="505" y="235" font-size="9.5" fill="#b8443c">(1/C&#178; &#8594; 0)</text>
  <!-- 기울기 주석 -->
  <line x1="200" y1="90" x2="280" y2="118" stroke="#8a4b12" stroke-width="0.9"/>
  <text x="150" y="86" font-size="11" fill="#8a4b12" font-weight="700">기울기 = 2/(q&#949;N)</text>
  <text x="150" y="99" font-size="9.5" fill="#8a4b12">가파를수록 저농도</text>
  <!-- V=0 점 -->
  <circle cx="493" cy="208" r="4" fill="#0d6e66"/>
  <text x="470" y="200" font-size="9.5" fill="#0d6e66">V=0: C_j=70 nF/cm&#178;</text>
</svg>

**그림 4.** C-V 프로파일링의 원리. 공핍 근사에서 1/C² = (2/qε<sub>s</sub>N)(V<sub>bi</sub> − V)이므로, 1/C²을 전압에 대해 그리면 직선이 된다. 이 직선의 x절편이 V<sub>bi</sub>, 기울기가 도핑 농도 N을 준다. 앞에서 "V<sub>bi</sub>는 내부 전위라 직접 못 잰다"고 했는데, 바로 이 C-V 외삽이 V<sub>bi</sub>에 접근하는 표준 간접 측정법이다. 도핑이 깊이에 따라 달라지면 기울기도 변하므로, C-V로 도핑 프로파일(깊이별 농도)을 얻는다.

> **현장 포인트: C-V는 모든 계면의 진단 도구**
>
> 이 "도체와 절연층과 도체를 커패시터로 보고 C-V로 읽는다"는 발상은 pn 접합을 훌쩍 넘어선다. W3의 MOS 커패시터가 그대로 이 방법으로 EWF와 EOT, 계면 결함을 뽑고, W6의 DRAM 셀 커패시터는 이 C<sub>j</sub>를 최대화하는 것이 목표다(HAR 구조로 면적을 키우고 high-k로 ε를 키운다). 반대로 접합 커패시턴스가 회로에서는 기생 용량으로 속도를 떨어뜨리기도 한다. 같은 C<sub>j</sub>가 저장 소자에선 자산, 논리 회로에선 부채다. V<sub>bi</sub>가 그랬던 것처럼. Metal ALD 관점에서, 우리가 만드는 전극과 유전체의 두께와 ε가 이 C를 직접 정한다.

---

## 2편 정리

- pn 접합에서 남는 것은 **이온화된 도펀트라는 고정 전하**이고, 이것이 전기장을 만들어 밴드를 휜다.
- **V<sub>bi</sub>는 세 가지 얼굴**을 가진다. 접촉 전 E<sub>F</sub> 차이, 확산을 막는 전위벽, 다이오드 켜짐의 기준.
- 전압계는 φ가 아니라 **E<sub>F</sub>의 차이**를 읽는다. 그래서 V<sub>bi</sub>는 존재하지만 단자에서 0 V로 보인다.
- **V<sub>bi</sub>는 도핑에 로그로 둔감**하고(10배에 60 mV), **W는 √(1/N)으로 민감**하다. 고농도일수록 공핍층이 얇다.
- 공핍층은 커패시터이며, **1/C²을 V에 그리면 직선**이 되어 절편에서 V<sub>bi</sub>, 기울기에서 도핑을 얻는다.

다음 [3편]({% post_url 2026-08-07-w2c-schottky-ohmic %})에서는 금속과 반도체를 붙인다. 같은 조합인데 왜 어떤 것은 다이오드가 되고 어떤 것은 저항이 되는지, 그리고 컨택 저항을 낮추는 레버가 왜 금속이 아니라 도핑인지를 본다.

---

## Supplementary, 수식 정리

### S1. 내장 전위와 공핍폭

$$ qV_{bi} = kT \ln\!\left( \frac{N_A N_D}{n_i^2} \right) $$

$$ W = \sqrt{ \frac{2\varepsilon_s (V_{bi}-V)}{q} \left( \frac{1}{N_A} + \frac{1}{N_D} \right) } $$

1/N<sub>A</sub> + 1/N<sub>D</sub> 항이 저농도 쪽이 지배함을 보여준다. 공핍층이 저농도 쪽으로 뻗는 이유다.

#### 워크스루, 기준 예제(10¹⁷ 대칭) 직접 대입

"식을 아는 것"과 "계산할 수 있는 것" 사이를 메우기 위해 숫자를 끝까지 넣어본다.

**1단계, V<sub>bi</sub>**

| 항목 | 계산 | 값 |
|---|---|---|
| kT (300 K) | 8.617×10⁻⁵ eV/K × 300 K | 0.02585 eV |
| N<sub>A</sub>N<sub>D</sub>/n<sub>i</sub>² | 10¹⁷ × 10¹⁷ / (9.65×10⁹)² | 1.074×10¹⁴ |
| ln(…) | ln(1.074×10¹⁴) | 32.31 |
| V<sub>bi</sub> | 0.02585 × 32.31 | 0.835 V |

32.31이라는 값은 분해하면 정체가 보인다. ln(1.074×10¹⁴) = ln(10¹⁴) + ln(1.074) = 14 × 2.303 + 0.07이다. 즉 **ln은 대략 자릿수 곱하기 2.3**이다. 여기서 14는 "도핑 곱(10³⁴)이 n<sub>i</sub>²(약 10²⁰)보다 몇 자릿수 위인가"다. 본문의 "도핑 10배에 +60 mV" 규칙이 바로 이 구조에서 나온다. 자릿수 1개당 kT × 2.303 = 25.9 mV × 2.303 ≈ 60 mV.

**2단계, W**

| 항목 | 계산 | 값 |
|---|---|---|
| 2ε<sub>s</sub>V<sub>bi</sub>/q | 2 × (11.7 × 8.854×10⁻¹² F/m) × 0.835 V / 1.602×10⁻¹⁹ C | 1.080×10⁹ |
| 1/N<sub>A</sub> + 1/N<sub>D</sub> | 2 / 10²³ m⁻³ | 2.0×10⁻²³ m³ |
| 곱 | | 2.160×10⁻¹⁴ m² |
| W = √ | | 1.470×10⁻⁷ m = 147 nm |

> **함정: 단위 변환**
>
> ε<sub>s</sub>는 F/m 단위이므로 도핑 농도를 반드시 cm⁻³에서 m⁻³로(×10⁶) 변환해야 한다. 10¹⁷ cm⁻³ = 10²³ m⁻³다. 이 변환을 빠뜨리면 W가 10³배(√10⁶) 틀린다. 전기장과 커패시턴스 계산에서도 같은 함정이 반복되므로, **계산 전에 모든 양을 SI로 통일하는 습관**이 안전하다.

### S2. 접합 커패시턴스와 C-V

공핍층을 커패시터로 보면 단위 면적당 접합 커패시턴스와 C-V 관계식은 다음과 같다. C<sub>j</sub>는 단위 면적당 커패시턴스(F/cm²), ε<sub>s</sub>는 반도체 유전율이다.

$$ C_j = \frac{\varepsilon_s}{W} \qquad\Longrightarrow\qquad \frac{1}{C_j^{2}} = \frac{2\,(V_{bi}-V)}{q\,\varepsilon_s N} $$

1/C<sub>j</sub>²을 V에 대해 그리면 직선이며, x절편이 V<sub>bi</sub>, 기울기가 2/(qε<sub>s</sub>N)이다(그림 4). 대칭 접합이면 N은 유효 도핑 N<sub>A</sub>N<sub>D</sub>/(N<sub>A</sub>+N<sub>D</sub>)로 대체된다.

### S3. 전류와 전기화학 퍼텐셜, 드리프트와 확산의 통합

전자 전류밀도는 드리프트와 확산의 합이다.

$$ J_n = q\,n\,\mu_n\,\mathcal{E} + q\,D_n \frac{dn}{dx} $$

여기에 아인슈타인 관계 D<sub>n</sub> = μ<sub>n</sub>kT/q(확산계수와 이동도가 독립이 아니라 온도로 묶여 있다는 관계로, 둘 다 같은 산란이 정하기 때문이다)와 n = n<sub>i</sub>exp[(E<sub>F</sub> − E<sub>i</sub>)/kT]를 대입해 정리하면 두 항이 하나로 합쳐진다.

$$ J_n = n\,\mu_n \frac{dE_{Fn}}{dx} $$

전류는 **전기화학 퍼텐셜(E<sub>F</sub>)의 기울기**에 비례한다. 정전 퍼텐셜 φ는 이 식에 직접 등장하지 않는다. φ의 기울기(드리프트)와 농도의 기울기(확산)가 E<sub>F</sub> 안에서 이미 합산되어 있기 때문이다. 평형(dE<sub>F</sub>/dx = 0)이면 J = 0이 자동으로 따라나오고, 전압계가 ΔE<sub>F</sub>/q만 읽는 이유도 이 식이다. 전압계 바늘을 미는 것이 곧 이 전류이기 때문이다. 비평형에서는 E<sub>Fn</sub>, E<sub>Fp</sub>(유사 페르미 준위)로 갈라져 각 캐리어의 전류를 따로 서술한다(정공은 J<sub>p</sub> = pμ<sub>p</sub>dE<sub>Fp</sub>/dx).

---

[^1]: D. A. Neamen, *Semiconductor Physics and Devices*, 4th ed., McGraw-Hill, Ch. 7 (pn Junction).
