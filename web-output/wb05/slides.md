---
theme: default
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Web Programming Week 5: CSS 기초 및 기본기 생존 훈련
drawings:
  persist: false
title: Web Programming Week 5 - CSS 기초
---

# Web Programming

Week 5: CSS 기초 (옷 입히기!) 및 생존 기본기 훈련

<div class="pt-12">
  <span class="text-gray-500">서울신학대학교 컴퓨터소프트웨어학과</span>
</div>

<div class="pt-4 text-sm font-bold">
  Instructor: Wonhyuk William Chung
</div>

---
layout: section
---

# 핵심 학습 목표 (Week 5)

1. CSS 선택자와 속성을 적용하여 스타일을 입힌다.
2. [Build-up] 명함에 나만의 색상과 폰트 입힌다.
3. 강제 상속 및 스타일 충돌 오류를 수정한다.

---
layout: center
---

# S1. CSS란 무엇일까?

옷 입히기 비유 & 3가지 방법 다루기

---

# CSS: 인테리어이자 패션

HTML이 집의 **콘크리트 뼈대**라면,
CSS는 거기에 **벽지를 바르고 예쁜 가구를 넣는 인테리어** 과정입니다.

* **인라인 (Inline)**
  태그 안에 직접 속성 정의! (급할 때만 사용)
* **내부 요소 (Internal)**
  `<head>` 안에 폰트나 색채 테마를 묶어 넣기
* **외부 파일 (External)**
  `style.css`라는 옷장을 별도로 만들어 연결! (항상 쓰는 방식)

---
layout: center
---

# S2. 기본 스타일링과 선택자

폰트, 색깔, 이름표 달기

---

# 누구를 꾸며줄까? (선택자)

옷 코디를 입힐 타겟을 고르는 기술

* **태그(요소) 선택자**: `h1`, `p`
  - 세상의 모든 태그에 다 똑같이 적용!
* **클래스 (Class, `.`)**: 그룹 이름
  - "이 반 학생들 파란 단체티 통일!"
  - 예: `.my-title { color: blue; }`
* **아이디 (ID, `#`)**: 하나뿐인 개인 이름표
  - 세상에서 하나뿐인 주민등록번호
  - 예: `#main-header { font-size: 24px; }`

---
layout: center
---

# S3. 디버깅 데모 & 생존 특강

안 보이는 글자 고치기 & 쫄지 마, 컴퓨터!

---

# 에러와 소통하는 법 (상속과 멘탈 모델)

* **배경색 = 글자색 버그**
  - 화면이 고장난 게 아닙니다. 우리가 시킨 것일 뿐!
  - `background-color`와 `color`의 차이.
* **강제 상속 (Inheritance)**
  - 가장 상위 부모(예: `body`)에게 준 스타일은 밑에 자식들이 다 물려받는다.
* **[컴맹 탈출 특강] 쫄지 마!**
  - 에러 창 `X` 눌러 끄지 않기 (드래그해서 복사+붙여넣기)
  - `Ctrl + C / V / Z` 필수 단축키와 폴더 구조 이해하기.

---
layout: end
---

# Q&A / 직접 실습해보기!

스택블리츠에서 지난주 명함의 **멋진 컬러**를 입혀보세요.
