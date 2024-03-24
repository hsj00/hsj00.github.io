---
title: "특허 읽기: '지르코늄 금속을 함유하는 신규한 유기금속화합물 및 그 제조방법' (10-1263454)"
layout: post
date: 2020-06-16 19:30
tag:
    - Chemistry
    - Chemical Engineering
    - Precursor
    - Atomic Layer Deposition
    - ALD
    - Thin Film Deposition
    - Semiconductor
    - Patent
    - Study
    - Note
headerImage: false
image:
description: 200616 `A novel organometallic compounds containing Zirconium metal and the preparation thereof` patent review
category: blog
author: hsj00
externalLink: true
published: true
comments: true
share: true
use_math: false
---

# 들어가면서

학부생 연구원 때부터 전구체는 [메카로][01]에서 주문해서 썼었다. [CCTBA][02]나 [TiCl4][03], [TMA][04], [DEZ][05]등 어지간한 유기금속화합물은 메카로 제품만 사용한 이유가 있었다. 연구 주제였던 ZnO ALD에 사용했던 전구체가 [DEZ][05]였는데, 처음에 썼던 제품은 메카로에서 구입한게 아니었다. 국내 모 회사에서 주문해서 사용했는데 불순물이 많았던건지 ALD window도, GPC도 확인이 안될만큼 성장 거동이 너무 제멋대로여서 증착 조건을 잡을 수 없을 정도였다. 그런데 메카로 제품을 사용하니깐 그런 문제가 단 1도 없었다. 졸업할 때까지 메카로에서 구매한 [DEZ][05]가 서너 캐니스터는 될 것이다.

전공을 살려 반도체 산업분야에서 일하고 싶은 마음에 계속 공부도 하고 산업 동향도 찾아보다가 예전에 봤던 메카로 기사[^01]가 생각나서 다시 찾아보았다.

> "_반도체 장비부품·화학소재 전문업체 메카로는 자사 지르코늄 프리커서(전구체)인 'ZM40' 제조 기술이 특허청 주관 '2018년 상반기 특허기술상 충무공상'을 받았다고 27일 밝혔다._"

기사에 나온 `ZM40` 전구체가 국내에서 최초로 개발/상용화 된 high-k 전구체라고 한다. 기사들을 훑어보니 [SK Hynix에서 DRAM 제조 공정][06]에 쓰인 것 같다. 이 제품으로 2018년 상반기까지 발생한 매출이 약 1100억 수준이라고 하니 대단한 발명이란 생각이 든다.

해당 제품의 특허를 [Kipris][07]에서 찾아보니 출원번호 10-2011-0022615로, 등록된지는 7년이 넘었다.

해당 특허 내용을 좀 읽어보고 청구항 구성은 어떻게 되어있는지, 발명의 내용과 참고하고있는 선행기술문헌들이 무엇인지 확인해볼 생각이다.

ToC는 다음과 같다.

- [들어가면서](#들어가면서)
  - [지르코늄 금속을 함유하는 신규한 유기금속화합물 및 그 제조방법 (A novel organometallic compounds containing Zirconium metal and the preparation thereof)](#지르코늄-금속을-함유하는-신규한-유기금속화합물-및-그-제조방법-a-novel-organometallic-compounds-containing-zirconium-metal-and-the-preparation-thereof)
    - [요약](#요약)
    - [특허 청구의 범위](#특허-청구의-범위)
    - [명세서](#명세서)
      - [기술분야](#기술분야)
      - [배경기술](#배경기술)
    - [선행기술문헌](#선행기술문헌)
      - [특허문헌](#특허문헌)
      - [비특허문헌](#비특허문헌)
    - [발명의 내용](#발명의-내용)
      - [해결하려는 과제](#해결하려는-과제)
      - [과제의 해결 수단](#과제의-해결-수단)
      - [실시예](#실시예)
        - [실시예1](#실시예1)
        - [실시예2](#실시예2)
        - [실시예3](#실시예3)
        - [실시예4](#실시예4)
  - [읽고난 후 메모](#읽고난-후-메모)

---

## 지르코늄 금속을 함유하는 신규한 유기금속화합물 및 그 제조방법 (A novel organometallic compounds containing Zirconium metal and the preparation thereof)

| 발명의 명칭 | 지르코늄 금속을 함유하는 신규한 유기금속화합물 및 그 제조방법 |
| ----------- | ------------------------------------------------------------- |
| 출원번호    | 10-2011-0022615                                               |
| 등록번호    | 10-1263454                                                    |
| DOI         | https://doi.org/10.8080/1020110022615                         |

---

### 요약

특허공보 맨 처음에는 특허 서지정보와 발명의 간단한 설명, 대표도면이 나온다.

이 특허는 ALD/CVD에 사용할 수 있는 Zr 전구체 발명에 대한 내용이라고 맨 처음 설명이 나오고, 전구체의 화학식과 TGA 분석 그래프가 실려있다. `TEMAZ`와 `CpTDMAZ`보다 중량이 절반이 될 때의 온도가 더 높은 것으로 볼 때 기존 Zr 전구체들보다 열적 안정성이 개선된 제품으로 보인다.

<center>
<img src="http://kpat.kipris.or.kr/kpat/remoteFile.do?method=bigFrontDraw&applno=1020110022615" alt="대표도면" title="대표도면">
<br>
<figure><figcaption><b>TEMAZ, CpTDMAZ, 실시예1, 실시예2 화합물의 TGA 분석 비교</b></figcaption></figure>
</center>

### 특허 청구의 범위

심사 청구항 27개중에 27번 청구항을 제외하고 전부 살아있다.
심사 청구항들의 종속 관계와 내용 요약을 다음과 같이 대략적으로 분류해보았다. 물론 정확한건 아니고 그냥 내 임의적인 판단이다.
이렇게 구조화해서 청구항을 살펴보면 각 청구항이 어떤 의미를 가지면서 서로 얽혀있는지 전체적인 그림을 파악하는데 도움이 되는 것 같다.

-   1: 유기금속 화합물의 기본 구조를 나타내는 화학식과 알킬기의 탄소수 범위 (R<sup>1</sup>: C1-C4 / R<sup>2</sup>, R<sup>3</sup>: C1-C6)
    -   2: 1항의 화학식에서 알킬기 R<sup>1</sup>, R<sup>2</sup>, R<sup>3</sup>가 서로 독립적으로 메틸, 에틸, 프로필
        -   3: 2항에서 알킬기 R<sup>1</sup>, R<sup>2</sup>, R<sup>3</sup>가 서로 독립적으로 메틸, 에틸
            -   4: 3항에서 알킬기 R<sup>1</sup>, R<sup>2</sup>, R<sup>3</sup>가 모두 메틸
            -   5: 3항에서 R<sup>1</sup>, R<sup>2</sup>는 모두 메틸, R<sup>3</sup>는 에틸
    -   6: 청구항 2번 이하에서 서술하고있는 조건을 만족하는 화합물의 분자식 36개를 나열
        -   12: 1항이나 6항에서 어느 한 항을 따르는 유기금속 화합물중 하나 또는 둘 이상을 기화시켜 기판 위에 지르코늄 함유 박막을 형성
            -   13: 12항의 박막 형성 방법으로 MOCVD 또는 ALD 사용
                -   25: ALD를 사용하는 박막 형성 방법의 순차적 단계
                    -   26: ALD 공정에서 사용하는 purge gas 종류
            -   14: 박막 형성에 사용하는 에너지원 종류
                -   15: 박막 형성이 이뤄지는 온도 범위
            -   16: 유기금속 화학물을 기판 위로 보내주는 이송 방법의 종류
            -   17: 유기금속 화합물을 기판 위로 보낼 때 사용하는 캐리어 가스 종류
            -   18: 반응 가스의 종류 (\* 유기금속 화합물이 기판 위에 증착된 이후에 반응자리 새로 형성하기 위해 사용하는 물질)
            -   19: 기판 위에 증착된 박막이 ZrO<sub>2</sub>이거나 ZrO<sub>2</sub>에 다른 여러 금속 산화물이 포함된 복합 금속 산화물 박막 형성
                -   20: Oxide 박막 증착을 위해 사용하는 반응가스 종류
            -   21: 기판 위에 증착된 박막이 ZrN이거나 ZrN에 다른 여러 금속 질화물이 포함된 복합 금속 질화물 박막 형성
            -   22: 기판 위에 증착된 박막이 ZrC이거나 ZrC에 다른 여러 금속 탄화물이 포함된 복합 금속 탄화물 박막 형성
            -   23: 기판 위에 증착된 박막이 ZrCN이거나 ZrCN에 다른 여러 금속 질화 탄화물이 포함된 복합 금속 질화 탄화물 박막 형성
            -   24: Nitride 박막 형성을 위한 반응 가스 종류
    -   7: 유기금속 화합물 조성에 포함될 수 있는 물질 종류와 내용에 대한 서술
-   8: 유기금속 화합물 합성 반응에 필요한 출발 물질들의 화학식
    -   9: 유기금속 화합물 합성 반응에 필요한 용매 종류
-   10: 유기금속 화학물 합성 반응에 필요한 다른 종류의 출발 물질들 화학식
    -   11: 유기금속 화합물 합성 반응에 필요한 용매 종류

### 명세서

#### 기술분야

특허 명세서에 써있는 내용 그대로 옮겨보겠다.

> "본 발명은 화학 증기 증착(Chemical Vapor Deposition: CVD), 특히 원자층 증착((Atomic Layer Deposition: ALD)에 사용되는 지르코늄 금속을 함유하는 신규한 유기금속 화합물 (신규한 지르코늄 산화물 전구체) 및 그 제조방법에 관한 것이다.

#### 배경기술

배경기술 내용은 중요하다고 생각되는 부분만 추려서 요약해보겠다.

-   막질 저하
-   부반응물 생성
-   낮은 전구체의 증기압

> 염소를 포함하는 전구체들(TiCl<sub>4</sub>, TaCl<sub>5</sub>, ZrCl<sub>4</sub>)의 경우 배선 재료인 알루미늄 부식을 유발하고, 증착 온도가 600℃ 정도로 고온이라 녹는점이 낮은 알루미늄 배선에 적용이 어려움. 그리고 공정중에 암모니아 착물과 암모늄염과 같은 비휘발성 부산물이 생성되어 박막 내에 입자 침착을 유발한다. 그리고 TaCl<sub>5</sub>, ZrCl<sub>4</sub>의 경우, 전구체가 고체화합물이기 때문에 증착에 필요한 충분한 증기압을 공급하지 못함.
>
> ZrO<sub>2</sub> 전구체로 많이 적용된 Zr(NMeEt)<sub>4</sub>(TEMAZ)[^02]의 경우, 상온에서 액체이고 높은 증기압을 갖지만 열적 안정성이 낮아서 단차피복성이 저하되고, 이로 인한 커패시터 누설이 생성되어 공정 적용에 한계를 가짐.
>
> TEMAZ의 대체품으로 CpZr(NMe<sub>2</sub>)<sub>3</sub>(CpTDMAZ)적용한 예[^03]가 있지만 ALD 적용시 부반응물이 생성되는 단점 존재. 캐니스터를 가열하고 이송하는 과정에서 자발적으로 분자간 반응이 발생해 다성분 화합물이 생성되고, 그로인해 박막 두께 조절이 어렵고 박막의 물성 또한 좋지 않음.

### 선행기술문헌

#### 특허문헌

-   ['METHOD OF FORMING HIGH-K DIELECTRIC FILMS BASED ON NOVEL TITANIUM, ZIRCONIUM, AND HAFNIUM PRECURSORS AND THEIR USE FOR SEMICONDUCTOR MANUFACTURING', 2007.12.13, WO/2007/140813][^04]
-   ['지르코늄 산화물 박막 증착용 유기금속 선구물질 및 이의 제조방법', 2007.12.27, 10-2006-0056116][^05]
-   ['ALD/CVD용의 지르코늄, 하프늄, 티타늄 및 규소 전구체', 2010.02.12, 10-2009-7023609][^06]

#### 비특허문헌

-   D.M.Hausmann et al., Chem. Mater., (2002), 14, 4350 [^02]
-   Jaanko Niinisto et al., J. Mater. Chem., (2008), 18, 5243 [^03]

### 발명의 내용

#### 해결하려는 과제

-   TEMAZ 및 CpTDMAZ보다 열적안정성, 단차피복성이 높고, 고온에서 장시간 보관하여도 분해되지 않는 유기금속 화합물 제공
-   해당 발명을 이용하여 CVD 또는 ALD 공정에 적용할 수 있는 Zr 전구체와 그 제조방법, 그리고 이를 사용한 박막 형성 방법 제공

#### 과제의 해결 수단

명세서에서 [0022]부터 [0046]까지는 청구항 내용의 반복이다.

반응식1 내지 3에 따른 Zr 화합물 합성은 다음과 같은 용매를 반응 용매로 사용하여 제조

-   비극성: 헥산, 펜탄, 헵탄, 벤젠, 톨루엔
-   극성: 디에틸에테르, 석유에테르, 테트라히드로퓨란, 1,2-디메톡시에탄

<center>
<img src="https://patentimages.storage.googleapis.com/35/14/5d/4eb6b54f79acf3/112011018610192-pat00016.png" alt="화학식1" title="화학식1">
<br>
<figure><figcaption><b>화학식1</b></figcaption></figure>
</center>

상기 화학식1로 정의되는 지르코늄 화합물은 하기 반응식1의 생성물(화학식2)과 화학식3의 화합물을 반응시켜 제조

<center>
<img src="https://patentimages.storage.googleapis.com/87/df/31/5cbdf1cba4a490/112011018610192-pat00002.png" alt="반응식1" title="반응식1">
<br>
<figure><figcaption><b>반응식1</b></figcaption></figure>
</center>
<center>
<img src="https://patentimages.storage.googleapis.com/4d/02/fc/762e9d23e1c56d/112011018610192-pat00003.png" alt="화학식3" title="화학식3">
<br>
<figure><figcaption><b>화학식3</b></figcaption></figure>
</center>
(상기 식에서, R<sup>1</sup>, R<sup>2</sup> 및 R<sup>3</sup>는 청구항1에서 정의한 바와 동일, X는 염소(Cl), 브롬(Br) 또는 아이오딘(I)을 나타내고, M은 리튬(Li), 소듐(Na) 또는 포타슘(K)을 나타냄)</br>

<br>
상기 반응식1에서 할로겐에틸알킬아민할로겐산염은 문헌 (Organic Syntheses: Wiley: New York, 1943; Collective volume 4, p 333)에 따라 쉽게 제조 (* 검색해보니 참고문헌 서지정보가 잘못된 것 같아서 링크 첨부한다. Org. Synth. 1951, 31, 37[^07])
</br>
<br>

-   화학식2의 화합물은 할로겐에틸알킬아민할로겐산염에 새로 합성된 금속싸이클로펜타디엔닐(metal cyclopentadienyl complex)을 투입하고 이어서 환류하여 반응을 종결
-   생성된 고체염을 여과하고 감압 하에서 용매 제거 후 진공 증류하면 상기의 반응식1에서의 생성물(화학식2)을 쉽게 제조 가능

<center>
<img src="https://patentimages.storage.googleapis.com/6e/c6/94/4fd7c347489590/112011018610192-pat00004.png" alt="반응식2" title="반응식2">
<br>
<figure><figcaption><b>반응식2</b></figcaption></figure>
</center>
(상기 식에서, R<sup>1</sup>, R<sup>2</sup> 및 R<sup>3</sup>는 청구항1에서 정의한 바와 동일)</br>

<br>

-   화학식1의 지르코늄 화합물은 화학식2의 화합물과 화학식3의 화합물을 반응시켜 고수율로 제조
-   테트라키스디알킬아미노지르코늄(IV)(tetrakis(dialkylamino)zirconium(IV))(화학식3)을 저온으로 냉각한 후 싸이클로펜타디엔닐에틸알킬아민(cyclopentadienyl ethyl alkylamine)(화학식2)을 투입하고 상온에서 1시간 교반을 통해 반응 종결
-   감압하에 용매를 제거하고, 생성된 노란색 액체를 진공증류하여 화학식1의 화합물을 쉽게 고수율로 제조
    <br>

-   화학식1의 지르코늄 화합물은 하기 반응식3에 나타낸 바와 같이, 하기 화학식4로 표시되는 화합물(MNR<sup>2</sup>R<sup>3</sup>)을 화학식5로 표시되는 화합물과 반응시켜 제조
-   싸이클로펜타디엔에틸알킬아미드지르코늄(IV) 디할라이드(cyclopentadienyl(ethylmethylamido) zirconium(IV) dihalide)(화학식5)를 반응기에 투입하여 -20℃로 냉각시키고, n-헥산(n-hexane)에 서스펜션 되어있는 금속디알킬아마이드 MNR<sup>2</sup>R<sup>3</sup>(metal dialkylamide MNR<sup>2</sup>R<sup>3</sup>)(화학식4)를 캐뉼라를 이용하여 천천히 첨가한 후 상온에서 15시간동안 교반하여 반응 종결
-   상온에서 정치시킨 후 캐뉼라를 이용하여 상등액을 다른 플라스크로 이송
-   감압 하에서 용매를 제거하고 생성된 노란색 액체를 진공증류하여 화학식1의 화합물을 제조

<center>
<img src="https://patentimages.storage.googleapis.com/85/d8/b5/8463e0ba7c5921/112011018610192-pat00005.png" alt="반응식3" title="반응식3">
<br>
<figure><figcaption><b>반응식3</b></figcaption></figure>
</center>
(상기 식에서, R<sup>1</sup>, R<sup>2</sup> 및 R<sup>3</sup>는 청구항1에서 정의한 바와 동일, X는 염소(Cl), 브롬(Br) 또는 아이오딘(I)을 나타내고, M은 리튬(Li), 소듐(Na) 또는 포타슘(K)을 나타냄)</br>

-   상기 화학식1로 표현되는 유기금속 화합물은 중심금속에 결합하고있는 리간드 중에서 알킬아미드 리간드와 연결된 싸이클로펜타디엔닐 리간드가 중심금속과 강하게 σ-결합, π-결합을 형성하고있어 지속적인 가온에도 열화되지 않는 높은 열적안정성을 갖게되며, 또한 높은 증기압을 유발할 수 있는 2개의 디알킬아미노 리간드가 중심금속과 결합되어있어 높은 증기압을 나타냄
-   대표도면의 TGA 그래프를 보면 해당 발명이 TEMAZ, CpTDMAZ보다 열적 안정성이 향상된 것을 알 수 있음
-   도6의 1H-NMR을 보면, 가열 후의 CpTDMAZ는 가열 전과 비교하여 쉽게 분해되어 불순물 생성된 것을 확인
-   도7의 1H-NMR을 보면 실시예1의 화합물은 가열 전/후 비교시 유의차가 없음을 확인

<center>
<img src="https://patentimages.storage.googleapis.com/35/44/c8/c4a98a2dd2965b/112011018610192-pat00023.png" alt="도6" title="도6">
<br>
<figure><figcaption><b>실시예4에 따른 CpTDMAZ의 가열 전/후 1H-NMR 비교표</b></figcaption></figure>
</center>
<center>
<img src="https://patentimages.storage.googleapis.com/c6/96/16/e16cd1ec47bd63/112011018610192-pat00024.png" alt="도7" title="도7">
<br>
<figure><figcaption><b>실시예4에 따른 실시예1 화합물(CpCH<sub>2</sub>CH<sub>2</sub>NCH<sub>3</sub>Zr(NMe<sub>2</sub>)<sub>2</sub>)의 가열 전/후 1H-NMR 비교표</b></figcaption></figure>
</center>

#### 실시예

-   모든 실험을 글로브 박스와 슐렝크 관(Schlenk line) 기법을 이용하여 불활성 아르곤 분위기에서 수행
-   생성물은 <sup>1</sup>H-NMR, <sup>13</sup>C-NMR을 이용하여 분석

##### 실시예1

-   싸이클로펜타디엔에틸메틸아미드지르코늄(IV)디(디메틸아미드) ((CpCH<sub>2</sub>CH<sub>2</sub>NCH<sub>3</sub>)Zr(NMe<sub>2</sub>)<sub>2</sub>) 합성

<center>
<img src="https://patentimages.storage.googleapis.com/83/be/2a/08aaba86cba0cb/112011018610192-pat00006.png" alt="1단계" title="1단계">
</center>
<center>
<img src="https://patentimages.storage.googleapis.com/28/5e/d3/27612c05236be5/112011018610192-pat00007.png" alt="2단계" title="2단계">
</center>

-   1단계

    -   500ml의 테트라하이드로퓨란(THF)이 들어있는, 불꽃 건조된 2L 슐렝크 플라스크에 문헌(Organic Syntheses: Wiley: New York, 1943; Collective volume 4, p 333)[^07]에 따라 제조된 클로로에틸메틸아민염산염 68.2g(0.524mol, 1.00당량)을 넣고 교반시키면서 0℃로 냉각
    -   새로 합성된 싸이클로펜타디엔닐나트륨(NaCp) 92.3g(1.048mol, 2.00당량)을 30분간 첨가
    -   혼합 반응용액을 상온으로 천천히 승온하고, 4시간동안 환류시킨 후 상온으로 냉각하여 반응 종결
    -   생성된 고체(NaCl)을 여과하고, 이어서 감압 하에서 용매를 완전히 제거
    -   생성된 액체를 감압 하에서 증류(b.p: 25℃ at 0.2mmHg)하여 투명한 액체의 1단계 화합물 32.3g (수율 50%) 수득

-   2단계
    -   80ml 톨루엔이 들어있는, 불꽃 건조된 250ml 슐렝크 플라스크에 테트라키스(디메틸아미노)지르코늄(VI)(tetrakis(dimethylamino)zirconium(IV) 26.8g(0.100mol, 1.00당량)을 넣고 교반시키면서 -20℃로 냉각
    -   1단계에서 합성된 싸이클로펜타디엔닐에틸메틸아민(cyclopentadienyl ethyl methylamine) 12.3g(0.10mol, 1.00당량)을 30분간 투입 후 혼합
    -   혼합 반응용액을 상온에서 1시간동안 교반시켜 반응 종결
    -   감압 하에서 용매를 완전히 제거한 후, 생성된 액체를 감압 하에서 증류(b.p: 85℃ at 0.1mmHg)하여 노란색 액체의 표제 화합물 29.5g (수율 92%) 수득

| NMR type                  | spectrum list                             |
| ------------------------- | ----------------------------------------- |
| <sup>1</sup>H-NMR (C6D6)  | δ 5.96 (t, 2H, C5H4CH2CH2NCH3)            |
|                           | 5.79 (t, 2H, C5H4CH2CH2NCH3)              |
|                           | 3.08 (s, 3H, C5H4CH2CH2NCH3)              |
|                           | 2.93 (s, 12H, 2×N(CH3)2)                  |
|                           | 2.69 (t, 2H, C5H4CH2CH2NCH3)              |
| <sup>13</sup>C-NMR (C6D6) | δ 136.51, 112.41, 106.92 (C5H4CH2CH2NCH3) |
|                           | 71.53 (C5H4CH2CH2NCH3)                    |
|                           | 43.98 N(CH3)2)                            |
|                           | 41.52 (C5H4CH2CH2NCH3)                    |
|                           | 29.51 (C5H4CH2CH2NCH3)                    |

##### 실시예2

-   싸이클로펜타디엔에틸메틸아미드지르코늄(IV) 디(에틸메틸아미드) ((CpCH<sub>2</sub>CH<sub>2</sub>NCH<sub>3</sub>)Zr(NEtMe)<sub>2</sub>) 합성

<center>
<img src="https://patentimages.storage.googleapis.com/14/11/2a/5b0f606f90fc27/112011018610192-pat00008.png" alt="실시예2" title="실시예2">
</center>

-   100ml 톨루엔이 들어있는, 불꽃 건조된 250ml 슐렝크 플라스크에 테트라키스(에틸메틸아미노)지르코늄(VI)(tetrakis(ethylmethylamino)zirconium(IV)) 24.0g(74.2mmol, 1.00당량)을 넣고 교반시키면서 -20℃로 냉각
-   상기 실시예1의 1단계에서 합성된 싸이클로펜타디엔닐에틸메틸아민(cyclopentadienyl ethyl methylamine) 10.0g(81.2mmol, 1.09당량)을 30분간 투입
-   혼합 반응용액을 상온에서 5시간동안 교반시켜 반응 종결
-   감압 하에서 용매를 완전히 제거한 후, 생성된 액체를 감압 하에서 증류(b.p: 97℃ at 0.1mmHg)하여 노란색 액체의 표제 화합물 23g (수율 89%) 수득

| NMR type                  | spectrum list                             |
| ------------------------- | ----------------------------------------- |
| <sup>1</sup>H-NMR (C6D6)  | δ 5.98 (m, 2H, C5H4CH2CH2NCH3)            |
|                           | 5.82 (m, 2H, C5H4CH2CH2NCH3)              |
|                           | 3.68 (t, 2H, C5H4CH2CH2NCH3)              |
|                           | 3.28∼3.10 (m, 4H, 2×N(CH2CH3)(Me))        |
|                           | 3.07 (s, 3H, C5H4CH2CH2NCH3)              |
|                           | 2.98 (s, 6H, 2×N(CH3)(Et))                |
|                           | 2.70 (t, 2H, C5H4CH2CH2NCH3)              |
|                           | 1.07 (s, 6H, 2×N(CH2CH3)(Me))             |
| <sup>13</sup>C-NMR (C6D6) | δ 136.25, 112.14, 106.65 (C5H4CH2CH2NCH3) |
|                           | 71.51 (C5H4CH2CH2NCH3)                    |
|                           | 50.17 (N(CH3)(Et))                        |
|                           | 41.97 (N(CH2CH3)(Me))                     |
|                           | 39.30 (C5H4CH2CH2NCH3)                    |
|                           | 29.57 (C5H4CH2CH2NCH3)                    |
|                           | 15.93 (N(CH2CH3)(Me))                     |

##### 실시예3

-   싸이클로펜타디엔에틸메틸아미드지르코늄(IV) 디(에틸메틸아미드) ((CpCH<sub>2</sub>CH<sub>2</sub>NCH<sub>3</sub>)Zr(NEtMe)<sub>2</sub>) 합성

<center>
<img src="https://patentimages.storage.googleapis.com/76/1d/93/e76562c0b42b17/112011018610192-pat00009.png" alt="실시예3" title="실시예3">
</center>

-   150ml 톨루엔이 들어있는, 불꽃 건조된 1L 슐렝크 플라스크에 싸이클로펜타디엔에틸메틸아미드지르코늄(IV) 디클로라이드 (cyclopentadienyl(ethylmethylamido) zirconium(IV) dichloride) 20.0g(65.9mmol, 1.00당량)을 넣고 교반하면서 -20℃로 냉각
-   350ml 노말 헥산(n-hexane)에 서스펜션 되어있는 리튬에틸메틸아미드(LiNEtMe) 8.57g(131.8mmol, 2.00당량)을 캐뉼라를 이용하여 2시간동안 천천히 첨가한 후 상온에서 15시간동안 교반
-   상온에서 5시간동안 정치시킨 후 상등액을 불꽃 건조된 1L 슐렝크 플라스크에 캐뉼라를 이용하여 이송
-   감압 하에서 용매를 완전히 제거한 후 감압 하에서 증류(b.p: 97℃ at 0.1mmHg)하여 노란색 액체의 표제 화합물 12.9g (수율 50%) 수득

| NMR type                  | spectrum list                             |
| ------------------------- | ----------------------------------------- |
| <sup>1</sup>H-NMR (C6D6)  | δ 5.98 (m, 2H, C5H4CH2CH2NCH3)            |
|                           | 5.82 (m, 2H, C5H4CH2CH2NCH3)              |
|                           | 3.68 (t, 2H, C5H4CH2CH2NCH3)              |
|                           | 3.28∼3.10 (m, 4H, 2×N(CH2CH3)(Me))        |
|                           | 3.07 (s, 3H, C5H4CH2CH2NCH3)              |
|                           | 2.98 (s, 6H, 2×N(CH3)(Et))                |
|                           | 2.70 (t, 2H, C5H4CH2CH2NCH3)              |
|                           | 1.07 (s, 6H, 2×N(CH2CH3)(Me))             |
| <sup>13</sup>C-NMR (C6D6) | δ 136.25, 112.14, 106.65 (C5H4CH2CH2NCH3) |
|                           | 71.51 (C5H4CH2CH2NCH3)                    |
|                           | 50.17 (N(CH3)(Et))                        |
|                           | 41.97 (N(CH2CH3)(Me))                     |
|                           | 39.30 (C5H4CH2CH2NCH3)                    |
|                           | 29.57 (C5H4CH2CH2NCH3)                    |
|                           | 15.93 (N(CH2CH3)(Me))                     |

##### 실시예4

-   Zr 화합물의 열안정성 실험 진행
-   불활성 아르곤으로 치환된 글로브 박스에서 실시예1에서 얻은 싸이클로펜타디엔에틸메틸아미드지르코늄(IV)디(디메틸아미드) (cyclopentadienylethylmethylamidozirconium(IV)di(dimethylamide))와 싸이클로펜타디엔지르코늄(IV)트리스(디메틸아미드) (CpTDMAZ, cyclopentadienylzirconium(IV)tris(dimethylamide))를 각각 마개가 있는 20ml 유리 용기에 10g 씩 투입한 후 마개로 막고 공기와 차단되도록 밀봉
-   상기 2가지 화합물이 채워진 유리용기를 동시에 110℃로 가열된 오일에서 6시간 방치하고, 이어서 150℃에서 2시간 방치 후 상온으로 냉각
-   <sup>1</sup>H-NMR을 통해 각각의 열분해 정도를 비교 (도6, 7)
-   실시예1, 4에서 제조된 각각의 지르코늄 화합물은 TGA법을 이용해 분석 (대표도면)
    -   10℃/min의 속도로 400℃까지 가온시키며 60L/min의 속도로 Ar 가스 주입

---

## 읽고난 후 메모

박막 증착에 사용되는 대부분의 전구체들이 공기나 수분과의 반응성이 크기 때문에 합성 과정도 진공 베이스에서 [`Schlenk method`][08]를 이용해서 합성을 진행하는 것을 알 수 있었다. [`Organic Syntheses`][09]나 기기분석 교재에 있는 `NMR` 내용을 어느정도 알고 있어야 합성뿐만 아니라 합성 후 결과물 분석까지 할 수 있을 것 같다.

반도체 산업군, 특히 CVD/ALD와 연관있는 분야로 이직하고픈 마음이 있기 때문에 이런 부분들도 틈틈이 공부해두면 유익할 것 같다.

다음에는 전구체 사업을 하는 회사들의 특허들을 목록으로 만들어 분류하는 작업을 해볼까 싶다.

<!-- references -->

[^01]: <https://m.etnews.com/20180627000251>{: target="\_blank"}
[^02]: <https://doi.org/10.1021/cm020357x>{: target="\_blank"}
[^03]: <https://doi.org/10.1039/B810922B>{: target="\_blank"}
[^04]: <https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2007140813>{: target="\_blank"}
[^05]: <https://doi.org/10.8080/1020060056116>{: target="\_blank"}
[^06]: <https://doi.org/10.8080/1020097023609>{: target="\_blank"}
[^07]: <https://doi.org/10.15227/orgsyn.031.0037>{: target="\_blank"}

<!-- links -->

[01]: http://www.mecaro.com/
[02]: http://www.ichems.co.kr/images/CCTBA.jpg
[03]: https://en.wikipedia.org/wiki/Titanium_tetrachloride
[04]: https://en.wikipedia.org/wiki/Trimethylaluminium
[05]: https://en.wikipedia.org/wiki/Diethylzinc
[06]: https://m.etnews.com/20180802000100
[07]: https://doi.org/10.8080/1020110022615
[08]: https://en.wikipedia.org/wiki/Schlenk_line
[09]: http://www.orgsyn.org/

---

<!-- pictures -->
