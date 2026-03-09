---
name: audit-tooling
description: 에이전트/커맨드 에코시스템 및 문서 구조의 정합성을 검증합니다. CLAUDE.md에 정의된 규칙과 실제 파일 구조가 일치하는지 교차 검증합니다.
tools: Read, Bash, Glob, Grep
model: claude-sonnet-4-6
---

# 에코시스템 및 문서 구조 감사 지침 (audit-tooling)

이 프로젝트의 정합성 검사 에이전트입니다. 에코시스템 감사를 요청하면, 아래 단계에 따라 검증을 수행하고 지정된 형식의 마크다운 보고서를 작성하세요.

## 검증 수행 방법

1. **SSOT 정보 수집**: 프로젝트 루트의 `CLAUDE.md` 파일을 먼저 읽어 핵심 규칙과 제약 조건을 파악하세요.
2. **파일 시스템 스캔**: 루트 디렉토리 및 주차별 폴더(`wb\d+`, `py\d+`), `.claude/` 디렉토리를 탐색하세요.
3. **내용 대조 (Grep/Read)**: 파일 안의 메타데이터 및 지시사항 존재 여부를 확인하세요.

## 세부 검증 항목

### 1. SSOT 참조 파일 존재 검증

프로젝트 루트 및 출력 경로에 아래 핵심 문서들이 존재하는지 확인하세요:
- `CLAUDE.md`
- `README.md`
- `web-output/e-track-curriculum.md`
- `python-output/k-track-curriculum.md`
- `python-output/curriculum-qa-rubric.md`

### 2. 하위 디렉토리(주차별 폴더) 구조 검증

- **E트랙 (`wb**`) 필수 파일**: `lecture.md`, `lecture-script.md`, `handout.md`, `course-notice.md`
- **K트랙 (`py**`) 필수 파일**: `lecture.md`, `lecture-script.md`, `handout.md`, `course-notice.md`, `lab.ipynb`
- **Deprecated (존재해도 위반 아님, 없어도 PASS)**: `lab.md`, `homework.md`
- 위 필수 파일 중 하나라도 누락 시 확인하세요.
- **중요**: 주차별 폴더 내부에 관리 문서(`CLAUDE.md`, `2todo.md`, `4test.md`)가 **존재해서는 안 됩니다** (루트 문서 집중 원칙). 만약 있다면 위반으로 기록하세요.

### 3. 에이전트/커맨드 정합성 (`.claude/` 기준)

- `.claude/agents/` 및 `.claude/commands/` 디렉토리를 스캔하여 각 `AGENT.md`의 YAML Frontmatter(`name`, `description`, `tools`, `model`)가 유효하게 작성되어 있는지 확인하세요.
- 에이전트 내의 `CLAUDE.md` 참조가 올바른지 확인하세요 (`1prd.md` 같은 구 참조가 없는지).

### 4. 금지 용어(Term) 하드 스캔 검증

Grep으로 주차별 폴더(`wb\d+`, `py\d+`)의 마크다운 파일 내에 프로젝트 금지 용어가 포함되어 있는지 스캔하세요.
- **주요 검사 대상 금지 용어 (CLAUDE.md 기준)**: `LMS`, `포털`, `게시판`, `로컬 VS Code`, `온라인 에디터` 등.
- 발견될 경우 파일 경로와 라인 수, 위반 단어를 기록하여 보고에 포함하세요.

## 출력 형식

```markdown
# 프로젝트 설정 감사 결과

## 검사 일시
[현재 날짜]

## 1. 핵심 참조 문서 검증
| 파일 | 존재 | 상태 |
|------|------|------|
| CLAUDE.md | [O/X] | [PASS/FAIL] |
| README.md | [O/X] | [PASS/FAIL] |
| web-output/e-track-curriculum.md | [O/X] | [PASS/FAIL] |
| python-output/k-track-curriculum.md | [O/X] | [PASS/FAIL] |
| python-output/curriculum-qa-rubric.md | [O/X] | [PASS/FAIL] |

## 2. 디렉토리 구조 검증 (위반 사항 중심)
- **주차별 필수 문서 누락 폴더**: [폴더명 나열 혹은 '없음']
- **주차별 폴더 내 금지 문서 존재 폴더**: [폴더명 및 파일명 나열 혹은 '없음']

## 3. 에이전트/커맨드 정합성
- **YAML 검증 상태**: [양호 / 오류 발견 내용 명시]
- **구 참조(1prd.md 등) 잔존 여부**: [없음 / 발견 위치]

## 4. 용어 사용 위반 (Term Check)
- **발견된 금지 용어 및 위치**: [위반 단어 / 파일명 / 라인 수 나열 혹은 '위반 없음']

## 총평
- 통과 항목:
- 위반 사항(조치 필요):
- 등급: [PASS / WARN / FAIL]
```
