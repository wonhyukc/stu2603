---
description: QA가 완료된 E트랙 강사용 문서를 한국어/영어 Bilingual(문단별 교차) 형식으로 변환합니다. "to-bilingual wb01" 또는 "to-bilingual 교육안" 형태로 호출합니다.
---

# E트랙 Bilingual 변환 지침

**중요**: 이 커맨드는 QA PASS 이후 최종 단계에서만 실행한다. QA가 완료되지 않은 파일에는 실행하지 않는다.

## 변환 규칙

**Bilingual 문단 교차 형식**
- 한국어 문단 → 바로 아래 영어 번역 문단 순서로 배치
- 문단 단위로 교차 (문장 단위 혼합 금지)
- 헤딩(#, ##, ###)은 `한국어 / English` 병기 형식: `## 섹션 제목 / Section Title`
- 코드 블록, 표, 목록은 영어로만 유지 (이중 표기 불필요)
- 학생 배포 문서(handout.md, lab 파일)는 **절대 변환하지 않는다** — 영어 단독 유지

## 대상 파일 (강사용만)

| 파일 | 변환 여부 |
|:-----|:---------|
| `lecture.md` | ✅ 변환 |
| `lecture-script.md` | ✅ 변환 |
| `slides.md` | ✅ 변환 |
| `course-notice.md` | ✅ 변환 |
| `handout.md` | ❌ 영어 유지 (학생 배포) |
| `lab` (HTML/JS 등) | ❌ 영어 유지 (학생 배포) |

## 호출 형식

```
/to-bilingual wb01
```
→ `web-output/wb01/` 폴더의 강사용 문서 4종 변환

```
/to-bilingual 교육안
```
→ `web-output/web-curriculum.md` 변환

## 실행 절차

1. `$ARGUMENTS` 파싱
   - `교육안` → `web-output/web-curriculum.md` 단일 파일
   - `wb0N` 형태 → `web-output/wb0N/` 폴더의 강사용 파일 4종
2. 대상 파일을 순서대로 읽고, 문단별 교차 Bilingual 형식으로 변환해 덮어쓴다
   - **[주의: Max Token 대처법]** 파일 변환 시 분량이 2배 이상 증가하므로 단일 응답에서 최대 출력 토큰 한계(Max Output Tokens)를 초과할 가능성이 매우 높습니다.
   - 따라서 전체 문서를 한 번의 도구 호출로 치환하려 하지 말고, 파일 전체를 상/중/하 등 **여러 청크(Chunk) 단위로 분할하여 `multi_replace_file_content`를 통해 순차적으로 변환**하세요. 
3. 변환 완료 후 변경된 파일 목록과 각 파일의 섹션 수를 요약 보고한다
