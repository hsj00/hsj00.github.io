---
title: "특허 읽기: '원자층 증착 장치 및 이를 이용한 박막 형성 방법' (10-2019-0002987)"
layout: post
date: 2020-11-23 19:30
tag:
    - Chemical Engineering
    - SEC
    - Samsung Electronics Co., LTD.
    - ALD
    - Atomic Layer Deposition
    - CVD
    - Chemical Vapor Deposition
    - Semiconductor
    - Patent
    - Study
    - Note
headerImage: false
image:
description: 201123 `Apparatus for Atomic Layer Deposition and Method for Forming Thin Film using the Same` patent review
category: blog
author: hsj00
externalLink: true
published: true
comments: true
share: true
use_math: false
---

# 들어가면서

요즘 특허만 읽느라 정작 읽으려고 모아둔 논문이나 프로그래밍 공부 내용은 올리고 있질 못하다. 12월까지 정신없을텐데, 이 시기를 잘 버틴후에 다시 프로그래밍 공부나 취미 생활도 포스팅할 수 있었으면 좋겠다.

이번에는 삼성전자 특허다. 얼마전에 [KIPRIS][00] 삼성전자 특허들을 검색해보다가 ALD 장비 관련된 특허가 눈에 띄어서 읽어보았다. 발명자 세 분 이름이 올라와있는데, 추측해보기로는 반도체연구소 아니면 생산기술연구소 소속이 아니실까 싶다.

특허를 읽어보면 읽어볼수록 내가 대학원 때 배운 ALD가 얼마나 기초적이었는지, 현업에서 사용되는 ALD/CVD는 얼마나 고도화 되어있는지 느끼게 된다. 초미세공정에 필요한 공정과 장비라면 박막의 품질만큼 중요한 것이 유무형의 비용을 줄이는 것일텐데, 산업에서 쓰이는 ALD 장비들은 확실히 그런 부분에서 연구실 장비들과 확실한 차이가 있는 것 같다. 이쯤되면 반도체 산업도 일종의 종합예술로 볼 수 있지 않을까?

ToC는 다음과 같다.
- [들어가면서](#들어가면서)
  - [원자층 증착 장치 및 이를 이용한 박막 형성 방법 (Apparatus for Atomic Layer Deposition and Method for Forming Thin Film using the Same)](#원자층-증착-장치-및-이를-이용한-박막-형성-방법-apparatus-for-atomic-layer-deposition-and-method-for-forming-thin-film-using-the-same)
    - [요약](#요약)
    - [청구범위](#청구범위)
    - [발명의 설명](#발명의-설명)
      - [기술분야](#기술분야)
      - [배경기술](#배경기술)
      - [발명의 내용](#발명의-내용)
        - [해결하려는 과제](#해결하려는-과제)
        - [과제의 해결 수단](#과제의-해결-수단)
      - [발명의 효과](#발명의-효과)
      - [도면의 간단한 설명](#도면의-간단한-설명)
        - [도면1](#도면1)
        - [도면2](#도면2)
        - [도면3](#도면3)
        - [도면4](#도면4)
        - [도면5](#도면5)
        - [도면6](#도면6)
        - [도면7a-7g](#도면7a-7g)
        - [도면16](#도면16)
        - [도면19a-19d](#도면19a-19d)
      - [발명을 실시하기 위한 구체적인 내용](#발명을-실시하기-위한-구체적인-내용)
  - [읽고난 후 메모](#읽고난-후-메모)

----------

## 원자층 증착 장치 및 이를 이용한 박막 형성 방법 (Apparatus for Atomic Layer Deposition and Method for Forming Thin Film using the Same)

| 발명의 명칭 | 원자층 증착 장치 및 이를 이용한 박막 형성 방법 |
| ----------- | ---------------------------------------------- |
| 출원번호    | 10-2019-0002987                                |
| 등록번호    |                                                |
| DOI         | https://doi.org/10.8080/1020190002987          |

----------

### 요약
해당 특허는 각 챔버별로 공정을 달리하여 한 장비 내에서 여러 공정을 동시에 수행할 수 있는 장비와 그 방법에 대한 내용으로 보인다. 요약에는 3개의 증착 공정, 1개의 표면 처리 챔버, 1개의 열처리 챔버로 구성으로 설명하고있다.

1. 제1 공정 챔버
   - 제1 소스 가스 공급 -> 제1 물질막 흡착 유도
2. 제2 공정 챔버
   - 제1 소스 가스 + 제2 소스 가스 공급 -> 제2 물질막 흡착 유도
3. 제3 공정 챔버
   - 제1 소스 가스 + 제2 소스 가스 + 제3 소스 가스 공급 -> 제3 물질막 흡착 유도
4. 표면처리 챔버
   - 제1 or 제3 물질막 각각에 표면 처리 공정을 수행
   - 반응 부산물을 제거
5. 열처리 챔버
   - 제1 or 제3 물질막이 소정의 순서에 따라 흡착된 기판에 열처리 공정 수행
   - 제1 or 제3 물질막을 단일 화합물 박막으로 형성

<center>
<img src="http://kpat.kipris.or.kr/kpat/remoteFile.do?method=bigFrontDraw&applno=1020190002987" alt="대표도면" title="대표도면">
<br>
<figure><figcaption><b>원자층 증착 장치의 개략도</b></figcaption></figure>
</center>

### 청구범위
청구항은 총 20항으로 이뤄져있다. 아직 등록되지 않은 특허라서 최종 등록시 청구항에 변화가 있을수도 있다.

- 01항: 각 챔버별 역할 정의
  - 제1 공정 챔버: 제1 소스 가스 공급 -> 제1 물질막 흡착 유도
  - 제2 공정 챔버: 제1 소스 가스 + 제2 소스 가스 공급 -> 제2 물질막 흡착 유도
  - 제3 공정 챔버: 제1 소스 가스 + 제2 소스 가스 + 제3 소스 가스 공급 -> 제3 물질막 흡착 유도
  - 표면처리 챔버: 제1 or 제3 물질막 각각에 표면 처리 공정 수행 -> 반응 부산물 제거
  - 열처리 챔버: 제1 or 제3 물질막이 소정의 순서에 따라 흡착된 기판에 열처리 공정 수행 -> 제1 or 제3 물질막을 단일 화합물 박막으로 형성

  - 02항: 표면처리 챔버의 종류
    - 표면처리 챔버: 매엽식(single wafer type), 상부에서 기판 윗면 방향으로 광원 조사하는 광원 조사부 포함

    - 03항: 표면처리 챔버의 특징
      - 표면처리 챔버: 투명 재질의 챔버 상부, 광원을 이용해 반응 부산물을 제거하는 표면처리 공정 수행

      - 04항: 표면처리 챔버의 광원 종류
        - 적외선, 자외선, 레이저 중 하나

  - 05항: 열처리 챔버 구성
    - 열처리 챔버: 매엽식(single wafer type)
      - 광원조사부: 상부에서 기판 상면으로 광원을 조사
      - 기판지지부: 하부에서 기판을 지지하고, 기판 하면 방향으로 열원 공급
        - 기판 온도는 제1 or 제3 공정 챔버보다 열처리 챔버에서 더 높음
    - 
    - 06항: 열처리 챔버의 특징
      - 열처리 챔버: 투명 재질의 챔버 상부, 광원 및 열원을 이용해 단일 화합물 박막을 형성하는 열처리 공정을 수행

  - 07항: 제1 or 제3 챔버 역할
    - 제1 or 제3 물질막 흡착을 유도 -> 퍼지 공정을 수행하며 흡착되지 않은 제1 or 제3 소스 가스 및 반응 부산물을 제거

  - 08항: 챔버간 기판 이송 수행
    - 제1 or 제3 공정 챔버, 표면처리 챔버, 열처리 챔버 사이에서 트랙 or 레일을 이용하여 수행
    - 진공 상태에서 기판 이송 수행

    - 09항: 물질막 배치 순서 구현을 위한 기판 이송 수행
      - 제2 및 제3 물질막 바로 아래에는 제1 물질막이 배치되도록 기판 이송 수행

    - 10항: 표면처리 챔버의 배치
      - 제1 or 제3 공정 챔버 각각과 실질적으로 동일한 간격으로 이웃하여 배치

- 11항: 각 공정별 역할 정의
  - 공정 챔버    
    - 소정의 순서를 따라서 기판에 제1 or 제3 소스 가스를 공급
    - 소정의 순서를 따라서 기판 상에 제1 or 제3 물질막 흡착을 유도
  - 표면처리 챔버
    - 제1 or 제3 물질막 각각에 표면처리 공정 수행
    - 반응 부산물 제거
  - 열처리 챔버
    - 제1 or 제3 물질막이 흡착된 기판에 열처리 공정 수행
    - 제1 or 제3 물질막을 단일 화합물 박막으로 형성

  - 12항: 광원 조사부 구성 및 광원의 전력 밀도 정의
    - 제1 광원의 전력 밀도 < 제2 광원의 전력 밀도
    - 표면처리 챔버: 챔버 상부에서 기판 윗면 방향으로 제1 광원을 조사 (제1 광원 조사부)
    - 열처리 챔버: 챔버 상부에서 기판 윗면 방향으로 제2 광원을 조사 (제2 광원 조사부)

    - 13항: 순차적 공정 수행 단계 (공정 챔버 -> 표면처리 챔버)
      - 공정 챔버에서 제1 or 제3 물질막 흡착 유도
      - 퍼지 공정 수행
      - 표면처리 챔버로 기판 이송
      - 표면처리 챔버에서 제1 광원을 이용해 반응 부산물 제거

      - 14항: 물질막 배치 순서 및 이를 위한 기판 이송 수행
        - 제2 및 제3 물질막 바로 아래에는 제1 물질막이 배치
        - 소정의 순서를 따라서 기판 상에 제1 or 제3 물질막이 흡착되도록 기판 이송 수행

        - 15항: 챔버의 특징
          - 각각의 챔버들은 매엽식(single wafer type)
          - 각각의 챔버들 사이에서 기판 이송은 모두 진공 상태에서 수행

- 16항: 유닛 모듈로 구성된 증착 장치 구성
  - 공정 챔버 및 표면처리 챔버를 각각 포함하는 복수의 유닛 모듈
    - 복수의 유닛 모듈에 포함되는 각각의 공정 챔버
      - 각각의 기판에 제1 or 제3 소스 가스를 소정의 순서에 따라 공급
      - 소정의 순서를 따라서 각각의 기판 상에 제1 or 제3 물질막 흡착 유도
    - 복수의 유닛 모듈에 포함되는 각각의 표면처리 챔버
      - 제1 or 제3 물질막 각각에 표면처리 공정을 수행
      - 반응 부산물 제거
  - 복수의 유닛 모듈로부터 복수의 기판을 공급받는 열처리 챔버
    - 소정의 순서를 따라서 제1 or 제3 물질막이 흡착된 복수의 기판에 열처리 공정 수행
    - 제1 or 제3 물질막을 단일 화합물 박막으로 형성

  - 17항: 복수의 유닛 모듈에 포함되는 표면처리 챔버 특징
    - 표면처리 챔버: 매엽식(single wafer type)
    - 광원 조사부: 상부에서 기판 윗면 방향으로 광원을 조사

    - 18항: 복수의 유닛 모듈에서의 공정 수행 및 기판 이송 과정
      - 복수의 유닛 모듈
        - 공정 챔버: 제1 or 제3 물질막 중 어느 하나의 흡착을 유도하는 공정 수행 후 퍼지 공정 수행
        - 기판을 표면처리 챔버로 이송
        - 표면처리 챔버: 광원을 이용해 반응 부산물을 제거하는 공정 수행

  - 19항: 열처리 챔버의 특징
    - 열처리 챔버: 배치 타입(batch type)
    - 히터부: 복수의 기판에 열원을 공급

  - 20항: 각 챔버의 배치
    - 열처리 챔버를 중심으로 복수의 유닛 모듈이 원형으로 배치


### 발명의 설명
#### 기술분야
원자층 증착 장치 및 이를 이용한 박막 형성 공정에 대한 내용을 담고있는 특허다. 챔버별 공정을 반복해서 여러층의 박막이 규칙적으로 형성되는 내용을 담고있는 것으로 파악된다.

#### 배경기술
명세서에 나온 내용을 그대로 옮겨본다.
> 원자층 증착 공정은 반응 전구체(reaction precursor)를 개별적으로 분리하여 반도체 기판 상에 유동시킴으로써, 반도체 기판 표면에 반응 물질의 포화 표면 반응(saturated surface reaction)에 의한 화학적 흡착과 탈착을 이용한 박막 형성 공정이다. 반응 전구체가 단위 시간 동안 반도체 기판 상에 유동하면서 원자층의 박막을 형성할 수 있다. 반응 물질 중 일부는 박막을 성장시키는 성분으로 사용되고, 나머지 일부는 리간드(ligand) 등을 제거하여 후속 반응을 도와주는 성분으로 사용될 수 있다.

-> 내가 이해한 바로는, 전구체 A와 B를 번갈아 공급하면서 반응 자리를 계속 만들어주는 ALD의 기초적인 내용을 길게 풀어놓은 내용이다.

#### 발명의 내용
##### 해결하려는 과제
1. 박막 내부에 포획될 수 있는 원치 않는 반응 부산물을 효과적으로 차단
2. 흡착된 박막들에 열처리 공정을 한 번에 수행하여 박막 품질 향상

##### 과제의 해결 수단
청구항 내용을 길게 풀어써놓은 것이라 생략한다.

#### 발명의 효과
원치 않는 반응 부산물을 효과적으로 차단해 박막 내부에 포획되지 않도록 하고, 일련의 순서에 따라 흡착 박막에 열처리 공정을 한 번에 수행하여 막질을 향상시킴으로써 반도체 소자의 신뢰성 및 생산성을 향상

#### 도면의 간단한 설명
[Google Patents][01]에서 패밀리 특허인 미국 [16/522,372][02] 특허를 살펴보면 도면 하나하나 그림 파일로 확인할 수 있다.

##### 도면1
실시예에 따른 원자층 증착 장치(10) 개략도
##### 도면2
실시예에 따른 원자층 증착 장치(10)의 동작 과정 흐름도
##### 도면3
실시예에 따른 공정 챔버 단면도
##### 도면4
실시예에 따른 표면처리 챔버 단면도
##### 도면5
실시예에 따른 열처리 챔버 단면도
##### 도면6 
실시예에 따른 이송 챔버 단면도
##### 도면7a-7g
실시예에 따른 원자층 증착 장치를 이용한 박막 형성 공정 단면도
##### 도면16
실시예에 따른 원자층 증착 장치를 이용한 박막 형성 방법의 순서도
##### 도면19a-19d
실시예에 따른 박막 형성 방법을 이용한 반도체 소자 제조 방법 단면도

#### 발명을 실시하기 위한 구체적인 내용
각 챔버별 상세 구성, 공정별 역할에 대해 도면을 바탕으로 설명하고 있다. Si 프리커서가 사용예로 언급되어있고, 비활성기체를 캐리어 가스로 사용한다는 내용이 있다. 박막 내부에 포획될 수 있는 원치 않는 반응 부산물을 표면처리를 통해 효과적으로 차단하고, 일련의 순서를 따라 흡착된 박막들을 최종 단계에서 일괄적으로, 한 번에 열처리 함으로써 원치 않는 조성의 상(phase) 형성을 막고, 써멀 버짓을 관리하여 소자에 사용되는 박막 품질을 향상하는 것을 목적으로 한다는 내용도 포함되어있다.

도면6을 보면 각 기판 이송시에 스프라켓에 연결된 체인이 나와있는데, 챔버간 이동시에 사용되는 것으로 보인다. 체인이 반복적으로 움직이며 기판을 옮기다보면 마찰이나 소음, 진동에 의한 파손이 일어날 수 있을 것 같은데 그 부분은 어떻게 해결했을지 궁금하다. 예전에 본 한국알박 특허중에 디스플레이용 대면적 기판를 옮길 때 자기부상 원리를 이용해서 기판의 파손을 방지하는 장치가 있었던 것 같은데 그런걸 적용해볼 여지는 없을까?

열처리 챔버를 중심으로 각 챔버들이 구성된다는 설명이 있는데, 박막 증착이 가능한 챔버를 여러개 배열하여 순차적으로 이동하며 정해진 공정을 거치도록 구성한 다음에 열처리를 최종 단계로 두는 형태가 아닐까 추측해본다. 박막이 증착된 기판이 순차적으로 열처리 챔버에 들어와서 공정이 마무리 되고 나오면 매엽식 반응기여도 단위 공정당 소요 시간을 줄일 수 있는 방법이 되지 않을까 싶다. 실제 챔버 구성과 공정의 설계 의도를 알면 좀 더 이해할 수 있을 것 같은데 내 깜냥으론 아직 거기까지는 안될 것 같다. 각 챔버가 모듈 형태로 구성되어있으니 기본적인 룰을 지키는 선에서 공정 설계 방향에 맞게 모듈을 배열하고 레시피를 짜는 형태가 아닐까? 궁금하다.

----------

## 읽고난 후 메모
메모는 다른 곳에 따로 써뒀다. 개인적인 사정이 있어서 12월이 지난 후 해당 내용을 추가하려고 한다.

---
<!-- references -->
[^00]: <http://www.thelec.kr/news/articleView.html?idxno=7375>{: target="\_blank"}
[^01]: <http://www.thelec.kr/news/articleView.html?idxno=8299>{: target="\_blank"}
[^02]: <http://www.wonik.com/story/dreamTeam/612>{: target="\_blank"}

<!-- links -->
[00]: <http://www.ips.co.kr/ko/business/product.php?board_code=product&page=2&product_category=Semiconductor&page_type=view&idx=337>
[01]: <https://patents.google.com/patent/US20200216953A1/en?oq=16522372>
[02]: <https://patentimages.storage.googleapis.com/a8/00/a0/c40be4e1a1dcbb/US20200216953A1.pdf>


---

<!-- pictures -->