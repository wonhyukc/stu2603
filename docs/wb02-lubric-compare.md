# E트랙 루브릭 구조 문제 분석 및 개선 기록

**작성일**: 2026-03-07
**분석 대상**:
- `web-output/curriculum-qa-rubric.md`
- `web-output/wb01-lecture-slide-rubric.md`
- `web-output/wb01-remaining-rubric.md`
**참조 파일**: `web-output/web-curriculum.md`

---

## 발견된 문제 목록

### 문제 1 — `lecture-script.md` 이중 평가 [심각]

**현상**
`wb01-lecture-slide-rubric.md` (파트 A, 65점)와 `wb01-remaining-rubric.md` (파트 A, 50점)가 동일 파일인 `lecture-script.md`를 각각 독립적으로 평가하고 있다. 두 루브릭 모두 PASS 기준에 파트 A 하한을 요구하므로, lecture-script.md 하나로 두 번의 판정을 받아야 하는 구조가 되었다.

**원인**
K트랙 `py0n-remaining-rubric.md` 패턴을 그대로 가져오면서 E트랙 전용 `lecture_slide` 루브릭과 역할 분리가 이루어지지 않았다.

**해결**
- `wb01-lecture-slide-rubric.md` → lecture.md + lecture-script.md + slides.md 전담 (변경 없음)
- `wb01-remaining-rubric.md` → **lecture-script.md 제거**, handout.md + course-notice.md 전담으로 재편

---

### 문제 2 — 교육안 루브릭 언어 기준과 현 파일 불일치 [중간]

**현상**
`curriculum-qa-rubric.md` 영역 1-2는 "100% 한국어 작성"을 3점 만점 기준으로 삼는다. 그러나 현재 `web-curriculum.md`는 전체가 한국어/영어 Bilingual로 작성되어 있어, 루브릭 적용 시 1-2에서 자동으로 1점밖에 받지 못한다.

**원인**
신규 E트랙 언어 방침(교육안은 초안~QA 단계에서 한국어 단독 작성)이 확정된 후 루브릭이 먼저 새 기준으로 작성되었으나, 기존 교육안 파일은 이미 bilingual 상태였다.

**해결**
루브릭 기준은 새 방침(한국어 단독 = 3점)으로 유지한다. 현 교육안 파일이 기준 미달 상태임을 명시하고, 교육안 파일을 한국어 단독으로 재작성한 후 QA를 진행해야 한다. 루브릭은 수정하지 않는다.

---

### 문제 3 — 교육안 루브릭 4-4 태그 명칭 불일치 [중간]

**현상**
`curriculum-qa-rubric.md` 영역 4-4는 `[S1]`, `[S2]`, `[S3]` 태그가 명확히 분리·태깅되어 있는지를 평가한다. 그러나 실제 교육안의 주차 테이블은 `**[이론]**`, `**[조작]**`, `**[AI리뷰]**` 3파트로 구성되어 있다.

**원인**
S1/S2/S3는 `lecture-script.md`에서 사용하는 섹션 번호 체계이다. 교육안 레벨에서는 이론/조작/AI리뷰가 올바른 명칭이다.

**해결**
영역 4-4의 평가 기준을 `[이론]/[조작]/[AI리뷰]` 3파트 구분으로 교체한다.

---

### 문제 4 — 영역 3 시험 주간(8·15주차) 예외 처리 누락 [경미]

**현상**
영역 3은 "목표 3개 이상, 행동 서술어" 기준을 14개 강의 주차에 일괄 적용한다. 14개 주차 계산에 15주차(기말고사)가 포함되지만, 15주차는 학습 목표가 아닌 평가 안내로 구성되어 있어 기준 적용 시 자동 감점된다.

**해결**
영역 3 주석에 "8주차(중간고사)·15주차(기말고사)는 시험 안내 구조 특성상 목표 개수 기준에서 제외한다"는 예외를 추가한다. 환산 대상 주차를 1~7주, 9~14주(13개)로 명시한다.

---

### 문제 5 — `wb01_remaining` 파일명과 대상 파일 불일치 [경미]

**현상**
파일명이 "나머지 산출물" 루브릭임에도 불구하고 `lecture-script.md`를 파트 A의 주 평가 대상으로 포함하고 있어 파일명과 내용이 어긋난다. 문제 1의 해결로 lecture-script.md를 제거하면 자연스럽게 해소된다.

---

## 개선 적용 요약

| 루브릭 파일 | 변경 내용 |
|:------------|:---------|
| `curriculum-qa-rubric.md` | 영역 3 시험 주간 예외 추가, 영역 4-4 태그명 교체 |
| `wb01-lecture-slide-rubric.md` | 역할 명시 주석 추가 (lecture-script 단독 담당 명시) |
| `wb01-remaining-rubric.md` | lecture-script 파트 A 제거, handout+course-notice 전담으로 재편, 배점 재조정 |

---

## wb02 이후 루브릭 제작 가이드라인

위 문제를 반복하지 않기 위한 체크리스트:

```
[ ] lecture-script.md는 lecture_slide_루브릭.md에서만 평가한다
[ ] remaining_루브릭.md는 handout.md + course-notice.md만 포함한다
[ ] 교육안 루브릭의 주차 범위는 시험 주간을 명시적으로 제외한다
[ ] 교육안 수준에서 섹션 태그는 [이론]/[조작]/[AI리뷰], 스크립트 수준에서는 S1/S2/S3를 사용한다
[ ] 교육안 파일은 반드시 한국어 단독으로 작성 후 QA, 통과 후 /to-bilingual 실행한다
```
