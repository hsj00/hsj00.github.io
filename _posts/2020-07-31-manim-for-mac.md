---
title: "MAC에서 Manim 설치하기"
layout: post
date: 2020-07-31 20:30
tag:
    - Python
    - Mac
    - Manim
    - Programming
    - Mathmatics
    - Graph
    - Animation
    - Study
    - Note
headerImage: false
image:
description: 200731 `MANIM FOR MAC`
category: blog
author: hsj00
externalLink: true
published: true
comments: true
share: true
use_math: false
---

# Manim? Mathmatics Animation!
수학 유튜브 채널 [3Blue1Brown][01]의 영상을 파이썬으로 만들었다는 이야기를 [WikiDocs][02]에서 보았다. WikiDocs 내용을 보고 개발환경 설정을 하고 공부해려고 했더니 Mac용 개발환경 설치는 안나와있어서 인터넷을 찾아보고 시행착오 끝에 설정을 완료했다. 해당 내용을 정리해두고 나중에 참고하기 위해 블로그 포스팅으로 남겨본다. 자세한 내용은 [이 글][03]과 [저 글][04]을 참고했다.

- [Manim? Mathmatics Animation!](#manim-mathmatics-animation)
  - [How to Install Manim for MAC?](#how-to-install-manim-for-mac)
    - [01 `Homebrew` 설치와 `Python`, `PIP` 설치하기](#01-homebrew-설치와-python-pip-설치하기)
    - [02 패키지 설치](#02-패키지-설치)
    - [03 `MacTex` 설치](#03-mactex-설치)
    - [04 `Manim` 라이브러리 다운로드 및 가상개발환경 설정](#04-manim-라이브러리-다운로드-및-가상개발환경-설정)
    - [05 결과물을 저장할 폴더를 만들어주고 설정하기](#05-결과물을-저장할-폴더를-만들어주고-설정하기)
    - [06 예제 코드 실행하기](#06-예제-코드-실행하기)
  - [마치며](#마치며)

----------
## How to Install Manim for MAC?
개발환경설정 순서는 다음과 같다.

1. `Homebrew` 설치 후 `Python`과 `Package manager`를 설치한다.
2. 필요한 패키지들을 설치한다.
3. `MacTex`을 설치한다.
4. `GitHub`에서 `Manim` 라이브러리를 다운받고 가상개발환경을 설정한다.
5. 코드를 일부 수정한다.
6. 예제 코드를 실행시켜 제대로 동작하는지 확인한다.

### 01 `Homebrew` 설치와 `Python`, `PIP` 설치하기
`Homebrew` 설치는 [여기][05]를 보면 자세히 나와있다.

일단 터미널에 다음 스크립트를 붙여넣어 실행한다.
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```
설치가 완료됐다면 `brew` 명령어를 이용해 `Python`을 설치해준다.
```
brew install python3
```

### 02 패키지 설치
그 다음으로 `Manim`을 위한 패키지들을 설치해준다
```
brew install cairo pkg-config virtualenv
```
나는 여기에 따로 몇 가지 더 설치를 해줬다. 해도 그만이고 안해도 그만인데 가상개발환경 관리를 위한 패키지들이라 설치하는김에 같이 해줬다.
```
brew install pyenv pyenv-virtualenv
```
`pyenv`는 `Python` 버전을 관리해주는 패키지고, `pyenv-virtualenv`는 `pyenv`의 플러그인이라고 하는데 버전을 세분화해서 여러 개발 환경으로 구분하여 관리하는 기능을 제공한다나? 잘은 모르지만 일단 깔고본다.

### 03 `MacTex` 설치
다 했으면 이제 `MacTex`을 설치해준다.
```
brew cask install mactex
```
그러면 뭐라뭐라 세 가지?의 선택지가 뜨는데, 설치 용량이나 구성과 관련된 내용이다. 나는 일단 몰라서 전체 설치로 진행했다.
[요기][04]를 보면 `MikTex` 콘솔을 다운로드 받아서 어쩌고 저쩌고 하는 내용이 있는데, 이 사람도 `MacTex`으로 설치했다고 써놨다. `MacTex`으로 해도 예제는 잘 돌아가더라.

### 04 `Manim` 라이브러리 다운로드 및 가상개발환경 설정
그 다음으로 이제 `Manim` 라이브러리 다운받고 설정해준다.
다운로드할 폴더를 만들어주고, 터미널에서 그 경로로 이동해준 다음에 다음 명령어를 실행한다.
그러면 `GitHub`에서 `Manim` repository로부터 라이브러리를 다운로드한다.
```
git clone https://github.com/3b1b/manim.git
```
다운로드가 완료되면 이제 다운로드가 완료된 `Manim` 폴더로 이동해서 가상개발환경을 활성화해준다.
```
virtualenv venv
source venv/bin/activate
```
그 다음에 `Python` 패키지들도 같이 설치해준다.
```
pip3 install latex sox ffmpeg pycairo
pip3 install -r requirements.txt
```
마지막 명령은 `requirements.txt` 내용을 읽어들여 패키지를 일괄적으로 설치해주는 내용이다.

여기까지 했으면 거의 다 끝났다. 나머지는 예제 파일 실행되는지 확인하고 그런것만 남았다.

### 05 결과물을 저장할 폴더를 만들어주고 설정하기
나는 `Manim` 라이브러리가 다운로드된 폴더 안에 `output`이란 이름으로 폴더를 만들어줬다. 여기에 결과물들이 저장된다.
그걸 반영해주기 위해서 코드를 일부 수정해줘야 하는데, `manimlib/constants.py` 파일을 찾아서 고치면 된다.

원본 코드는 다음과 같다.
```py
# manimlib/constants.py
# 26번째 코드의 경로 수정
        else:
            MEDIA_DIR = os.path.join(
                os.path.expanduser('~'),
                "Dropbox (3Blue1Brown)/3Blue1Brown Team Folder"
            )
```

이렇게 바꿔준다.
```py
# manimlib/constants.py
# 26번째 코드의 경로에 `output` 폴더 경로 입력하기
        else:
            MEDIA_DIR = os.path.join(
                os.path.expanduser('~'),
                "/Users/anartanimal/Documents/manim/manim/output"
            )
```
여기까지 했으면 테스트만 남았다.

### 06 예제 코드 실행하기
```
python3 -m manim example_scenes.py

1: OpeningManimExample
2: SquareToCircle
3: UpdatersExample
4: WarpSquare
5: WriteStuff

Choose number corresponding to desired scene/arguments.
(Use comma separated list for multiple entries)
Choice(s): 2
```
이렇게 해주면 사각형이 원으로 바뀌는 영상을 `mp4` 확장자 파일로 만들어준다. [2번의 예제 파일][06]도 같이 올려본다.

```
python3 -m manim example_scenes.py

1: OpeningManimExample
2: SquareToCircle
3: UpdatersExample
4: WarpSquare
5: WriteStuff

Choose number corresponding to desired scene/arguments.
(Use comma separated list for multiple entries)
Choice(s): 5
```
이렇게 하면 `TeX`이 제대로 작동하는지 알 수 있는 것 같다.
[5번의 예제 파일][07]도 링크를 올려본다.

----------

## 마치며
`WikiDocs`에 올라온 강의를 보면서 따라하는 일만 남았다. 쉽진 않을 것 같은데 재밌을 것 같으니 소소한 결과물이라도 꾸준히 만들어볼 수 있었으면 좋겠다.

---
[01]: https://www.youtube.com/c/3blue1brown/featured
[02]: https://wikidocs.net/book/4381
[03]: http://bhowell4.com/manic-install-tutorial-for-mac/
[04]: https://caffae.wordpress.com/2019/09/01/how-to-install-manim-for-mac/
[05]: https://brew.sh/index_ko
[06]: /assets/files/posts/2020-07-31/SquareToCircle.mp4
[07]: /assets/files/posts/2020-07-31/WriteStuff.mp4