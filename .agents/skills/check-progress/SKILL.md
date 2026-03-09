---
name: check-progress
description: 프로젝트 전체 진행 상태를 확인하고 보고합니다. 세션 시작 시 또는 진행 상태 파악이 필요할 때 호출합니다.
---

# 프로젝트 진행 상태 확인 지침 (check-progress)

stu2603c 프로젝트의 전체 진행 현황을 스캔하고 종합하여 보고하는 에이전트입니다.

## 검토 절차

### 1. 기획 및 SSOT 문서 검사

프로젝트 경로에서 다음 핵심 파일의 존재 여부 및 최신 업데이트 상태를 확인하세요:
- `CLAUDE.md`
- `README.md`
- `web-output/웹프로그래밍(E트랙)_교육안.md`
- `python-output/컴퓨팅적사고와코딩(K트랙)_교육안.md`
- `python-output/교육안_QA_루브릭.md`

### 2. 주차별 산출물 폴더 동적 탐색

`wb\d+`, `py\d+` 패턴의 폴더를 모두 검색합니다.
각 주차 폴더 내에 다음 핵심 교육 파일들이 존재하는지 확인합니다:

**E트랙 (wb\*\*) 필수 파일:**
- `lecture.md`, `lecture-script.md`, `handout.md`

**K트랙 (py\*\*) 필수 파일:**
- `lecture.md`, `lecture-script.md`, `handout.md`, `lab.ipynb`

**Deprecated (존재해도 무시):** `lab.md`, `homework.md`

## 출력 형식 (진행 상태 보고서)

```markdown
# 프로젝트 전체 진행 상황 상태보드

## 1. 핵심 기획/관리 문서
- [x/○] CLAUDE.md (프로젝트 총괄 규칙)
- [x/○] README.md
- [x/○] web-output/웹프로그래밍(E트랙)_교육안.md
- [x/○] python-output/컴퓨팅적사고와코딩(K트랙)_교육안.md
- [x/○] python-output/교육안_QA_루브릭.md

## 2. 웹프로그래밍(E트랙) 진척도
| 주차 폴더 | lecture.md | handout.md | 상태 요약 |
|-----------|------------|------------|-----------|
| wb01 | ○ | ○ | 완료 |

## 3. 컴퓨팅적사고와코딩(K트랙) 진척도
| 주차 폴더 | lecture.md | handout.md | lab.ipynb | 상태 요약 |
|-----------|------------|------------|-----------|-----------|
| py01 | ○ | ○ | ○ | 완료 |

## 다음 권장 작업
(작성되지 않은 주차나 누락된 파일을 기반으로 1~2줄로 제안)
```
