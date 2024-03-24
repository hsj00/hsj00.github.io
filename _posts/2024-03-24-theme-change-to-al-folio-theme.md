---
title: Github blog theme 교체 (`al-folio` theme 설치)
layout: post
date: 2024-03-24
description: 2024-03-24, Github blog theme change (`al-folio` theme)
tags:
    - Github
    - Blog
    - Jekyll
    - al-folio
giscus_comments: true
featured: false

authors:
  - name: hsj00

bibliography: false

render_with_liquid: false

# Optionally, you can add a table of contents to your post.
# NOTES:
#   - make sure that TOC names match the actual section names
#     for hyperlinks within the post to work correctly.
#   - we may want to automate TOC generation in the future using
#     jekyll-toc plugin (https://github.com/toshimaru/jekyll-toc).
toc: true

# Below is an example of injecting additional post-specific styles.
# If you use this post as a template, delete this _styles block.
_styles: >
  .fake-img {
    background: #bbb;
    border: 1px solid rgba(0, 0, 0, 0.1);
    box-shadow: 0 0px 4px rgba(0, 0, 0, 0.1);
    margin-bottom: 12px;
  }
  .fake-img p {
    font-family: monospace;
    color: white;
    text-align: left;
    margin: 12px 0;
    text-align: center;
    font-size: 16px;
  }
---
## Jekyll `al-folio` theme

맥북도 새로 샀겠다, 포스팅도 오랜만에 올렸겠다 싶어서 이번 기회에 블로그 테마를 교체해보기로 했다. 사용한 테마는 다음과 같다.

[al-folio blog example](https://al-folio.github.io/)<br>
[al-folio theme github link](https://github.com/alshedivat/al-folio.git)

---
## Why did I change the theme to `al-folio`?

지금도 잘 쓰고있는 `jekyll-indigo` theme를 왜 `al-folio` theme로 변경하는가?

1. `jekyll-indigo`를 오래써서 기분 전환하려고
2. 맥북에어를 새로 사면서 로컬 드라이브에 기존 `jekyll-indigo`를 옮겨는 과정에서 원인을 찾지 못한 여러가지 에러들이 있었다.
   1. `bundle exec jekyll serve` 명령어로 local server 구동 실패
   2. 새로 블로그 포스팅을 올렸을 때 블로그 웹사이트에 변경사항이 제대로 반영되지 않음
3. 이러한 문제점들 외에 소위 '있어보이는' 만듦새 때문에 바꾸고 싶단 생각이 들었다.
   1. 아카데믹한 블로깅에 특화되어있는 테마라서 괜히 뭔가 좀 그럴싸해 보였음
   2. 추후에 `Publications` 탭을 커스터마이징 하게되면 논문 뿐만아니라 특허 서지 정보들도 끌어와서 업데이트 할 수 있을 것 같단 생각이 듦
   3. 개인적인 관심사들을 아카이빙하기 좋아보였고, 위와 같은 장점들 때문에 블로그를 하나의 CV portfolio로 만들기 좀 더 수월할거라고 생각함

---
## `al-folio` setting

이번에도 역시 블로그가 제대로 동작하게끔 설정하기까지 무수한 삽질이 있었고, 그 삽질 과정을 조금이라도 줄여준 보물같은 블로그들이 있었다. 아래는 삽질에 도움을 받은 블로그 목록이다.

[Yehyun Suh Github blog](https://yehyunsuh.github.io/)  
[Yehyun Suh Tistory blog](https://yehyunsuh.tistory.com/)  
[George C. de Araújo Github blog](https://george-gca.github.io/)  

`jekyll-indio`를 사용했던 가장 큰 이유는 간결함에서 오는 세팅의 편의성과 웹과 모바일에서 표시되는 화면 구성의 차이가 거의 없기 때문이었는데, 그에 비하면 `al-folio`는 블로그가 어떤 식으로 작동하고 구현되는지 좀 더 깊은 이해도가 필요했다. 가령, `jekyll`과 `ruby`, `yaml`과 같은 것들을 조금은 더 알아야지 세팅이 수월했다. 물론 나는 아직도 잘 모르겠다. `Google`과 `ChatGPT`, `Copilot`이 없었다면 엄두도 못냈을 것이다. 일단 테마 변경부터 끝내놓고 자잘한 오류들은 천천히 처리해야할 것 같다. 첫 술에 배부를 순 없으니 일단 뭐든 되게 만들고 보자.

### Blog structure

삽질을 해보며 내 나름대로 이해해본 `al-folio`의 구성과 작동 방식에 대해 정리해보고자 한다. 현재 활성화 시켜놓은 기능들에 대해서만 정리해놓고 추후에 다른 기능들을 더 활용하게되면 그건 그때 추가 포스팅을 하는걸로.

#### `assets`

프로필 사진이나, 첨부 파일, 이미지, 주피터 노트북, 폰트, `bib` 등등등 규칙에 맞게 폴더에 넣어두면 사용할 수 있는 것 같다. 내부 설정으로 폴더 위치를 양식에 맞게 자동으로 연결되게끔 만들어져있는 것 같다. 나중에 사진이나 파이썬 스크립트 파일, pdf 파일 같은 것들을 첨부하기 편리할 것 같다. 좀 더 써보면서 나중에 한 번 더 정리해보는걸로.

#### `_posts`

`markdown` format으로 작성한 글을 양식에 맞는 제목으로 만들어서 넣어두면 블로그 글이 포스팅된다. 일반적으로 제목 양식은 `yyyy-mm-dd-Put-a-Title-for-Your-Posting.md`이다.

`al-folio` repository에서 `_posts`에 있는 파일들을 보면 사용할 수 있는 기능들을 여러가지 예시 파일로 만들어 넣어두었다. 필요할 때마다 참고해서 작성하면 될 것 같다. 아카데믹한 블로깅에 강점이 있는 테마답게 수식이나 그래프, 주피터 노트북 같은 것들도 반응형으로 넣을 수 있는 것 같다. 당장 쓸 일 없으니 이런건 나중에 더 공부해보는걸로.

#### `_pages`

각 `about.md`나 `cv.md`, `blog.md`와 같은 파일들은 제목과 동일한 이름을 갖는 블로그의 각 페이지 내용들과 연결되어있다. 파일 내용을 수정하면 블로그에 반영이 된다. `about.md`는 블로그 첫 화면 내용과 직접적으로 연결되어있는 내용이 포함되어있어서 좀 신경써서 수정했다.

#### `_layouts`

`_layouts` 폴더엔 `*.liquid` 확장자를 갖는 파일들이 들어있다. 이 파일들은 블로그 홈페이지를 구성하는 각 페이지를 어떤 양식을 따라 렌더링할지 결정하는 정보들이 담겨있는 것 같다.

임시로 블로그 포스팅 최상단에 `Table of Contents`가 나오게끔 설정하려고 `post.liquid` 파일 내용 일부를 수정했다.

<details>
<summary><b>기존 코드</b></summary>

{% raw %}
  <div id="markdown-content">
    {{ content | toc }}
  </div>
{% endraw %}

</details><br>


<details>
<summary><b>수정한 코드</b></summary>

{% raw %}
  <div id="markdown-content">
    {% if page.toc %}
      <h2>Table of Contents</h2>
    {% endif %}
    {{ content | toc }}
  </div>
{% endraw %}

</details>
<br>

#### `_news`

블로그 가장 첫 화면 `news` 항목에 업데이트 되는 내용이다. 한 줄당 파일 하나씩 사용하는 구조인 것 같다. 무슨 내용을 더 추가할지는 나중에 좀 더 고민해보는걸로.

#### `_data`

비활성화해둔 `CV`나 `people`, `teaching` 항목들의 `yml` 설정 파일들이 들어있다. 학문적인 블로깅에 특화되어있는 테마답게 대학원생이나 교수님들이 쓰기 딱 좋은 기능들인 것 같다.

#### `_bibliography`

`al-folio` theme의 강력한 강점 중 하나인 것 같다.

아래는 `Google Scholar`에서 찾은, 내 이름이 포함된 출판 논문들의 서지 정보다. `bib` 파일로 만들어서 넣어두었다. 이렇게 입력을 해서 저장해두면 `Publications`에 내 이름이 들어간 논문들을 보여준다. `jekyll-scholar`가 `bib` 파일 정보를 읽어들여서 웹페이지 형태로 렌더링해서 뿌려주는 것 같다.

<details>
<summary><b> `bib` file example </b></summary>
<div markdown="1">

```bib
@article{han20171,
  title={1, 5-Pentanediol as an Oxygen Precursor for Atomic Layer Deposition of Zinc Oxide Thin Films},
  bibtex_show={true},
  author={Han, Seung-Joo and Shin, Seokhee and Kim, Sungjoon and Ko, Dong-Hyun and Jin, Zhenyu and Lee, Sun Young and Min, Yo-Sep},
  journal={Chemistry of Materials},
  volume={29},
  number={8},
  pages={3371--3374},
  year={2017},
  publisher={ACS Publications},

  html={https://doi.org/10.1021/acs.chemmater.6b05300},
  pdf={Han_Chem_Mater_2017_29_3371.pdf},
  selected={true},
}

@article{jin2014novel,
  title={Novel chemical route for atomic layer deposition of MoS 2 thin film on SiO 2/Si substrate},
  bibtex_show={true},
  author={Jin, Zhenyu and Shin, Seokhee and Han, Seung-Joo and Min, Yo-Sep and others},
  journal={Nanoscale},
  volume={6},
  number={23},
  pages={14453--14458},
  year={2014},
  publisher={Royal Society of Chemistry},

  html={https://doi.org/10.1039/C4NR04816D},
  pdf={Jin_Nanoscale_2014_6_14453.pdf},
  selected={true},
}

@article{kim2015highly,
  title={Highly uniform and vertically aligned SnO 2 nanochannel arrays for photovoltaic applications},
  bibtex_show={true},
  author={Kim, Jae-Yup and Kang, Jin Soo and Shin, Junyoung and Kim, Jin and Han, Seung-Joo and Park, Jongwoo and Min, Yo-Sep and Ko, Min Jae and Sung, Yung-Eun},
  journal={Nanoscale},
  volume={7},
  number={18},
  pages={8368--8377},
  year={2015},
  publisher={Royal Society of Chemistry},

  html={https://doi.org/10.1039/C5NR00202H},
  pdf={JY_Kim_Nanoscale_2015_7_8171.pdf},
  selected={true},
}
```

</div>
</details><br>
