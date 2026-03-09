---
description: K트랙 특정 주차의 핵심 산출물(lecture-script, lab.ipynb, handout, course-notice)을 루브릭 기준으로 평가합니다. "qa-py-materials py02" 형태로 호출합니다.
---

# qa-py-materials — K트랙 주차 산출물 평가

## 실행 흐름

1. **ARGUMENTS에서 폴더명 파싱** (예: `py02`)
2. **루브릭 읽기**: `python-output/공통_remaining_루브릭.md`
3. **교육안 읽기** (SSOT 검증용): `python-output/k-track-curriculum.md` — 해당 주차의 학습 목표, S1/S2/S3 세션 내용, 과제 내용 확인
4. **4개 파일 읽기 및 채점**:
   - `python-output/{week}/lecture-script.md`
   - `python-output/{week}/lab.ipynb`
   - `python-output/{week}/handout.md`
   - `python-output/{week}/course-notice.md`
5. **결과 표 출력 + PASS/FAIL 판정**
6. **FAIL 시 보완 항목 목록** (우선순위순) 출력

## 채점 기준

해당 주차 교육안(`k-track-curriculum.md`)의 세션별(S1, S2, S3) 세부 내용을 단일 SSOT(Single Source of Truth)로 삼는다.
루브릭 문서(`공통_remaining_루브릭.md`)의 품질 기준 및 지표에 따라 각 산출물이 **"해당 주차 교육안의 내용을 빠짐없이 그리고 정확하게 담고 있는지"** 검증하며, 누락 시 엄격하게 감점한다.

## 보고 형식

```
### 영역별 채점 결과

| 파트 | 항목 | 만점 | 취득 | 감점 이유 |
|:-----|:-----|-----:|-----:|:---------|
| A-1  | 분량 및 품질 | 10 | ? | ... |
| A-2  | S1 print() 완전성 | 12 | ? | ... |
| A-3  | S2 타입+연산자 완전성 | 13 | ? | ... |
| A-4  | S3 input()+변환+에러 | 10 | ? | ... |
| B-1  | 노트북 기본 구조 | 5 | ? | ... |
| B-2  | S1 print() 실습 | 7 | ? | ... |
| B-3  | S2 타입+연산자 실습 | 8 | ? | ... |
| B-4  | S3 input()+변환 실습 | 5 | ? | ... |
| C-1  | 개념 참고 영역 | 8 | ? | ... |
| C-2  | 실습 섹션 | 5 | ? | ... |
| C-3  | 과제 섹션 | 7 | ? | ... |
| D-1  | 고유 정보 완결성 | 5 | ? | ... |
| D-2  | 포맷 및 중복 방지 | 5 | ? | ... |
| **합계** | | **100** | **?** | |

### PASS 조건 달성 여부

| 조건 | 기준 | 달성 |
|:-----|-----:|:----:|
| 총점 | 85+ | ? |
| A (lecture-script) | 38+ | ? |
| B (lab.ipynb) | 20+ | ? |
| C (handout) | 16+ | ? |
| D (course-notice) | 8+ | ? |

### 최종 판정: PASS / FAIL

### 보완 필요 항목 (FAIL 시)
1. [최우선] ...
2. ...
```
