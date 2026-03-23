# How to Use: 에이전트 및 워크플로우 종합 가이드

이 문서는 stu2603 프로젝트에서 교안(커리큘럼)과 주차별 산출물을 제작하고 외부 시스템(eCampus 등)과 연동할 때 사용하는 프롬프트·스킬(에이전트)·커맨드를 총망라한 실무 참고서입니다.

---

## 전체 워크플로우 한눈에 보기

### K트랙 (py0X)

```
[교안 제작] — 전체 한국어
  교육안 초안 작성
      ↓
  /qa-ktrack  ← 교육안 품질 채점 (90점 기준)
      ↓ FAIL
  /ralph-loop ← 자동 보완 반복 → PASS

[주차별 산출물 제작] — 전체 한국어
  루브릭 파일 생성 (py0x-remaining-rubric.md)
      ↓
  build-week 에이전트로 산출물 초안 제작
      ↓
  qa-content 에이전트로 형식·용어 검증
      ↓
  /qa-py-materials py0X  ← 내용 채점 (85점 기준)
      ↓ FAIL
  /ralph-loop ← 자동 보완 반복 → PASS
```

### E트랙 (wb0X)

```
[교안 제작] — 초안은 한국어
  교육안 초안 작성 (한국어)
      ↓
  /qa-ktrack 또는 자체 검토
      ↓ PASS 후 최종화
  /to-bilingual 교육안  ← 한국어 → 한국어/영어 Bilingual 변환

[주차별 산출물 제작]
  강사용 문서 초안 작성 (lecture.md, lecture-script.md, slides.md) — 한국어
  학생 배포 문서 초안 작성 (handout.md, lab 파일) — 영어
      ↓
  qa-content 에이전트로 형식·용어 검증
      ↓
  내용 채점 / QA 완료 → PASS
      ↓ PASS 후 최종화
  /to-bilingual wb0X  ← 강사용 문서 4종을 한국어/영어 Bilingual 형식으로 변환
```

> **E트랙 핵심 규칙**:
> - 학생 배포 문서(handout, lab)는 **처음부터 영어**, QA 후에도 영어 유지
> - 강사용 문서는 **초안~QA까지 한국어**, QA PASS 후 `/to-bilingual`로만 Bilingual 변환

---

## SSOT 파일 위치

| 파일 | 역할 |
|:-----|:-----|
| `CLAUDE.md` | 전체 운영 지침 (언어·파일 규칙·Git 정책 등) |
| `python-output/python-curriculum.md` | K트랙 커리큘럼 마스터 |
| `python-output/curriculum-qa-rubric.md` | K트랙 교육안 채점 기준 |
| `python-output/py0x-remaining-rubric.md` | 주차별 산출물 채점 기준 |

---

## 1. 교안(커리큘럼) 제작

### 1-1. 교육안 초안 작성

교육안 파일이 없거나 새로 써야 할 때 사용하는 프롬프트입니다.

```
K트랙 교육안을 새로 작성해줘.
파일 경로: python-output/python-curriculum.md

작성 기준:
- CLAUDE.md의 핵심 제약 조건 전부 준수
- 대상: 컴퓨터 교육 처음 받는 1학년 (100% 대면 수업, 거꾸로 학습)
- 1~16주차 전체 커리큘럼, 주차별로 학습 목표·강의 내용(S1/S2/S3)·email로 제출 과제 포함
- 교육안 완성 후 /qa-ktrack 으로 자동 채점
```

기존 교육안을 특정 주차만 수정할 때:

```
python-output/python-curriculum.md 의 3주차 내용을 수정해줘.
[수정 내용 구체적으로 기술]
수정 후 /qa-ktrack 으로 재채점해서 점수 변화를 알려줘.
```

---

### 1-2. 교육안 QA — `/qa-ktrack`

**용도**: 교육안이 루브릭 기준(100점 만점, 90점 PASS)을 충족하는지 채점
**대상 파일**: `python-output/python-curriculum.md`
**루브릭 파일**: `python-output/curriculum-qa-rubric.md`

호출 방법:

```
/qa-ktrack
```

채점 결과 예시:

```
| 영역                        | 만점 | 취득 |
| 1. 문서 구조 및 메타데이터   |    5 |    5 |
| 2. 운영 구조 명확성          |   10 |    9 |
| ...                         |      |      |
| 합계                        |  100 |   92 |

최종 판정: PASS
```

---

### 1-3. 교육안 자동 보완 — `/ralph-loop`

`/qa-ktrack` 결과가 FAIL(90점 미만)일 때 자동으로 보완하고 재채점합니다.

```
python-output/python-curriculum.md 를 /qa-ktrack 으로 평가해.
90점 미만이면 /ralph-loop 워크플로우로 보완 항목을 직접 수정하고,
90점 이상이 될 때까지 반복한 뒤 결과만 보고해.
```

---

## 2. 주차별 산출물 제작

### 2-1. 루브릭 파일 생성

산출물 QA에 앞서 반드시 루브릭 파일이 있어야 합니다.
**경로 패턴**: `python-output/py0x-remaining-rubric.md`

py02 루브릭을 참고 템플릿으로 삼아 새 주차 루브릭을 만들 때:

```
python-output/py02-remaining-rubric.md 를 참고해서
py03 용 루브릭을 python-output/py03-remaining-rubric.md 로 생성해줘.
교육안의 3주차 학습 목표(변수·문자열 조작·f-string)에 맞게 파트 A~D 세부 항목을 교체해줘.
```

루브릭 구조 (고정, 변경 금지):

| 파트 | 파일 | 배점 | PASS 하한 |
|:----:|:-----|-----:|----------:|
| A | lecture-script.md | 45 | 38 |
| B | lab.ipynb | 25 | 20 |
| C | handout.md | 20 | 16 |
| **합계** | | **90** | **75** |

---

### 2-2. 산출물 초안 제작 — `build-week`

**용도**: 특정 주차의 전체 산출물(lecture.md, lecture-script.md, handout.md, lab.ipynb)을 교육안 기반으로 초안 생성
**에이전트**: `.agents/skills/build-week/SKILL.md`

호출 방법:

```
build-week py03
```

또는 특정 파일만 생성할 때:

```
python-output/python-curriculum.md 의 3주차 내용을 보고
python-output/py03/lecture-script.md 를 작성해줘.
- 3섹션 × 25분, 총 4,500단어 이상
- 구어체, 볼드체·문단 구분 충분
- Google Colab 실습 환경 기준
- 강사: 정원혁 (wonhyukc@stu.ac.kr)
```

**산출물 파일 목록 (K트랙 기준)**:

| 파일 | 대상 | 필수 |
|:-----|:-----|:----:|
| `lecture.md` | 강사 (진행 순서·체크리스트) | ✅ |
| `lecture-script.md` | 강사 (75분 대본) | ✅ |
| `handout.md` | 학생 (개념 요약+실습 안내+과제) | ✅ |
| `lab.ipynb` | 학생 실습 노트북 | ✅ |
| `slides.md` | 슬라이드 개요 | 선택 |

---

### 2-3. 형식·용어 검증 — `qa-content`

**용도**: 용어 통일, 분량 규정(75분·4,500단어), Bilingual 규칙, 금지 용어 스캔
**에이전트**: `.agents/skills/qa-content/SKILL.md`
**보고서 저장**: `tmp/health-report/YYYY-MM-DD_py0X_quality_report.md`

호출 방법:

```
qa-content 에이전트로 python-output/py03 폴더를 검증해줘.
```

특정 파일만 검증:

```
qa-content 에이전트로 python-output/py03/lecture-script.md 의
분량·어뷰징·볼드체·문단 구분을 점검해줘.
```

---

### 2-4. 내용 채점 — `/qa-py-materials`

**용도**: 루브릭 기준으로 4개 파일의 내용 완전성을 파트별로 채점 (100점, 85점 PASS)
**루브릭**: `python-output/py0x-remaining-rubric.md`
**교차 검증**: `python-output/python-curriculum.md` 해당 주차와 대조

호출 방법:

```
/qa-py-materials py03
```

채점 결과 예시:

```
| 파트 | 항목                  | 만점 | 취득 | 감점 이유 |
| A-1  | 분량 및 품질          |   10 |   10 |           |
| A-2  | S1 내용 완전성        |   12 |   10 | 변수 네이밍 규칙 미흡 |
| ...                                              |
| 합계 |                       |  100 |   89 |           |

PASS 조건: 총점 89 ≥ 85 ✅ / A 43 ≥ 38 ✅ / ...
최종 판정: PASS
```

---

### 2-5. 산출물 자동 보완 — `/ralph-loop`

`/qa-py-materials` 결과가 FAIL(85점 미만 또는 파트 하한 미달)일 때 사용합니다.

```
py03의 lecture-script, lab.ipynb, handout을
/qa-py-materials py03 으로 평가해.
85점 미만이면 /ralph-loop 워크플로우로 보완 항목을 직접 수정하고,
85점 이상이 될 때까지 반복한 뒤 결과만 보고해.
```

---

## 3. 전체 도구 참조표

### Slash Commands (`/커맨드명`)

| 커맨드 | 용도 | 기준 | 호출 예시 |
|:-------|:-----|:----:|:----------|
| `/qa-ktrack` | K트랙 교육안 내용 채점 | 90점 PASS | `/qa-ktrack` |
| `/qa-py-materials` | K트랙 주차 산출물 채점 | 85점 PASS | `/qa-py-materials py02` |
| `/ralph-loop` | Auto-Fix 반복 루프 | PASS까지 | `/ralph-loop` + 지시 프롬프트 |
| `/to-html` | Markdown → HTML 변환 | — | `/to-html py02/handout.md` |
| `/to-bilingual` | E트랙 강사용 문서 Bilingual 변환 (QA PASS 후) | — | `/to-bilingual wb01` |
| `/translate-english` | 한국어 → 영어 번역 | — | `/translate-english` |
| `/optimize-docs` | CLAUDE.md/README.md 최적화 | — | `/optimize-docs` |

### Agents (에이전트)

| 에이전트 | 파일 경로 | 용도 |
|:---------|:---------|:-----|
| `build-week` | `.agents/skills/build-week/SKILL.md` | 주차 전체 산출물 초안 생성 |
| `qa-content` | `.agents/skills/qa-content/SKILL.md` | 형식·용어·분량 검증 |
| `material-creator` | `.agents/workflows/material-creator.md` | 개별 실습·과제 파일 생성 |
| `course-designer` | `.agents/workflows/course-work.md` | 커리큘럼 전체 기획·설계 |
| `check-progress` | `.agents/skills/check-progress/SKILL.md` | 전체 주차 진행 상태 스캔 |
| `audit-structure` | `.agents/skills/audit-structure/SKILL.md` | 에코시스템·폴더 구조 감사 |

### 루브릭 파일

| 파일 | 대상 | PASS 기준 |
|:-----|:-----|:---------|
| `python-output/curriculum-qa-rubric.md` | K트랙 교육안 | 90점 |
| `python-output/py0x-remaining-rubric.md` | 주차별 산출물 4종 | 85점 (파트별 하한 동시 충족) |

---

## 4. 새 주차 제작 체크리스트

새 주차(예: py03)를 처음 만들 때 이 순서를 따라합니다.

```
[ ] 1. 교육안에서 해당 주차 내용 확인
        → python-output/python-curriculum.md

[ ] 2. 루브릭 파일 생성
        → python-output/py03-remaining-rubric.md
        → py02 루브릭을 템플릿으로 주차 내용에 맞게 A-2~A-4 항목 교체

[ ] 3. 산출물 초안 제작
        → "build-week py03" 에이전트 호출
        → 또는 파일별 직접 작성 프롬프트 사용

[ ] 4. 형식 검증
        → "qa-content 에이전트로 python-output/py03 검증해줘"

[ ] 5. 내용 채점
        → /qa-py-materials py03

[ ] 6. FAIL이면 자동 보완
        → /ralph-loop 프롬프트로 85점 PASS까지 반복

[ ] 7. 완료 커밋
        → 브랜치: issue-{번호}-py03-materials
        → 커밋 메시지: docs: py03 주차 산출물 제작 (#이슈번호)
```

---

## 5. 자주 쓰는 프롬프트 패턴

### 교육안 수정 + 즉시 검증

```
교육안 X주차의 [수정 내용]을 반영해줘.
수정 후 /qa-ktrack 으로 채점하고, FAIL이면 바로 보완해서 PASS 달성 후 보고해.
```

### 한 주차 전체 제작 + QA 일괄

```
py0X 폴더가 없어. 교육안의 N주차 내용을 기반으로
build-week py0X 으로 전체 산출물을 만들고,
이어서 /qa-py-materials py0X 으로 채점해줘.
85점 미만이면 /ralph-loop 으로 보완하고 결과만 보고해.
```

### 특정 파일만 재작성

```
python-output/py0X/lecture-script.md 가 루브릭 A-3 기준을 못 충족해.
교육안 N주차 S2 내용을 다시 읽고 lecture-script.md 의 Section 2 를 전면 재작성해줘.
재작성 후 /qa-py-materials py0X 으로 A파트 점수 변화를 확인해줘.
```

### 전체 진행 상황 확인

```
check-progress 에이전트로 현재 K트랙 전체 주차 진행 상태를 스캔해줘.
```

---

## 6. 특수 외부 시스템 연동 워크플로우

### eCampus 상호평가 과제 게시판 자동 생성 (`/ecampus-assign`)

**Description:** 
eCampus(Moodle) 시스템의 '가져오기(Import)' 기능을 사용 시, 다른 주차 영상이나 불필요한 파일이 함께 복사되는 문제를 방지하기 위해 AI(브라우저 에이전트)에게 수작업과 동일한 게시판 생성을 위임하는 지시어 가이드입니다.

**When to use:** 
특정 주차(예: 3주차) eCampus에 제출 후 상호평가(대안 B: 링크+해시값 기반)를 위한 eCampus Assign(과제) 모듈을 새로 만들어야 할 때.

**How to Instruct the AI:**
복사해서 프롬프트에 붙여넣고 `[ ]` 안의 내용만 변경하여 지시하세요.

```text
/ecampus-assign
강좌 URL: [https://ecampus.stu.ac.kr/course/view.php?id=13971]
대상 주차: [3주차]
과제 제목: [3rd Week Lab Submission]
```

**AI's Background Behavior (What the Agent Will Do):**
지시를 받은 AI는 사용자의 권한으로 브라우저에 접속하여 다음 절차를 수행합니다.
1. 지시받은 강좌 URL 접속 및 `편집 모드(Edit Mode)` 활성화
2. 지정한 대상 주차(예: 3주차) 섹션으로 스크롤하여 `활동 또는 자료 추가` 클릭
3. `과제(Assign)` 모듈 선택
4. `과제 제목` 입력
5. `설명(Description)`: 가이드 텍스트 자동 입력 (GitHub 링크, 커밋 해시값 제출 및 동료 평가 안내)
6. `제출 유형(Submission types)`: '첨부파일' 해제 및 '온라인 텍스트(Online text)' 활성화
7. `성적(Grade)`: 최대 점수 3점으로 설정 (제출 1점, URL 1점, 해시값 1점 반영)
8. `저장하고 돌아가기` 클릭 후 생성된 게시판 URL 보고

> **Note:** 분반이 2개(예: E트랙 1분반, 2분반)인 경우, 각각의 강좌 URL을 명시하여 두 번 지시하거나 한 번에 두 URL을 모두 포함해 요청할 수 있습니다.
