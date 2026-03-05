## 2026-03-05
*   **[K트랙] `py02-try1` 검증 및 대폭 보완(review-quality)**: 신규 생성된 `py02-try1` 폴더의 산출물을 검증(`review-quality`). 용어 통일성(eCampus, Colab 등)은 준수되었으나 5종 산출물 중 `course-notice.md` 누락 및 `lecture-script.md` 분량 미달(약 470단어)을 적발함. 스크립트를 통해 `course-notice.md`를 신규 생성하고 75분 룰에 맞추어 대본을 대규모 확장(약 10,400단어)하여 최종 `PASS` 등급으로 복구함 (`health-report` 저장).
*   **[K트랙] `py01` 2주차 검증 및 보완(review-quality)**: 품질 검증 스킬(`review-quality`) 결과 산출물 5종 및 용어 사용 완벽 준수(`PASS`). 단, `lecture-script.md` 분량 미달(약 2200단어)을 발견하여 자동 확장 스크립트를 통해 보완(`WARN` -> `PASS` 전환, `health-report` 저장).
*   **[E트랙] 교육안 품질 검증(review-quality)**: `웹프로그래밍(E트랙)_교육안.md`의 용어 통일성(eCampus, StackBlitz 미사용 등) 및 언어 정책(Bilingual 미준수) 위반 사항 발견에 따른 최종 **FAIL** 리포트 산출 (`health-report`에 저장).
*   **[K트랙] `py01` 주차 2주차 강의 자료 생성**: `build-week` 스킬 지침(온라인 유학생 대상, 75분 분량, 한글 전용)에 따라 2주차 파이썬 강의안(`lecture.md`), 대본(`lecture-script.md`), 실습안(`lab.md`), 과제물(`homework.md`), 수강 공지(`course-notice.md`) 제작 완료.
*   **[E트랙] 스크립트 기반 `lecture-script.md` 템플릿 규칙 추가**: 영어-한국어 문단별 교차 병기 및 강사 행동 지침 등 `wb` 폴더에서 사용될 대본 형식의 구체적 제약을 `build-week` 스킬에 적용.
*   **[K트랙] `py01` 강의 자료 전면 갱신**: 업데이트된 75분(25분 x 3섹션) 규칙에 맞추어 1주차 파이썬 강의안(`lecture.md`), 실습안(`lab.md`, Colab 기준), 마이크로 과제물(`homework.md`) 생성 완료.
*   **[K트랙] `py01` 자료 보완(유학생/온라인 룰 적용)**: 인도/베트남 등 유학생 맞춤형 안부 인사, 100% 온라인 수업 등 새로운 컨텍스트 지시에 맞춰 대본(`lecture-script.md`) 도입부 15문장 내외 재작성 구체화 및 요리 비유 도입 (5600+ 단어, 검증 통과).
*   **[K트랙] `py01` 자료 교체(2주차)**: 기존 1주차 내용을 삭제하고 커리큘럼 기준 2주차 내용(개발 환경 및 기초 출력, 에러 파괴 훈련)을 `py01` 폴더 5종 세트(lecture, script, lab, homework, course-notice)에 덮어써 새롭게 생성.
*   **[전체] `build-week` 스킬 고도화**: 대본(`lecture-script.md`) 길이 강제 규칙(75분, 각 섹션 1000자 이상) 추가 및 마크다운 전용 `course-notice.md` 생성 단계 신설.
*   **[K트랙] `py01` 대본 증량 및 공지 추가**: 사용자 피드백을 반영해 75분 분량으로 대본 재작성 및 `course-notice.md` (순수 마크다운) 신규 생성.
*   **[K트랙] `py01` 주차 강의 자료 재생성**: 1주차 파이썬 강의안(`lecture.md`), 대본(`lecture-script.md`), 실습안(`lab.md`), 마이크로 과제(`homework.md`)를 `build-week` 스킬 지침(75분 분량, 한글 전용)에 따라 생성 완료.
*   **[전체] `how-to-skill-agnet.md` 보완**: 사용자가 요청한 워크플로우(`build-week`, `course-work`)별 활용 시기 가이드라인을 구조화하고, 매주 생성 자동화를 위한 **3단계 프롬프트(생성-검증-커밋) 템플릿**을 명문화.
*   **[전체] 강의안 분량 기준 구체화**: 매 주차 핵심 강의안은 학생 개인 실습과 Q&A 시간을 제외하고 오직 강사의 강연 및 코딩 데모 파트로만 총 75분(25분 x 3개 섹션)이 되도록 설계하는 세부 지침을 `1prd.md`와 `build-week` 스킬에 추가.
*   **[K트랙] `py02` 강의 자료 신규 생성 및 품질 검증(review-quality)**: 2주차 파이썬 강의안(`lecture.md`), 실습안(`lab.md`), 마이크로 과제물(`homework.md`) 작성 완료. 품질 검토 후 `AI` 👉 `Agent`, `Homework` 👉 `Weekly Assignment` 용어 일괄 교정 완료 (최종 PASS 등급).

## 2026-03-04
*   **[K트랙] `py01`**: 1주차 강의안(lecture.md), 실습안(lab.md), 과제물(homework.md) 제작 완료.
*   **[전체] 수강 공지 위치 최적화**: 루트에 있던 각 트랙별 수강 공지 파일을 주차별 폴더(`py01/course-notice.md`, `wb01/course-notice.md`)로 이동 및 HTML 최적화.
*   **[전체] `how-to-commit.md` 생성**: 1prd.md 기반의 실전 커밋 워크플로우 가이드 작성 완료.
*   **[E트랙] 교육안 업데이트**: `웹프로그래밍(E트랙)_교육안.md`의 주차별 목표 및 공지 사항 동기화.

## 2026-03-02
*   **[전체] 루트 PRD (`1prd.md`) 대폭 개편**: `tmpCLAUDE.md`에 명시된 원칙들(AI-Native, 클라우드 IDE 우선, SSOT, 워크플로우 등)을 통합해 마스터 문서화 완료.
*   **[전체] `local-rules.md` 생성 및 문서 정책 완화**: 하위 폴더별 4대 문서(1prd, 2todo, 3history, 4test) 동기화 의무를 해제하고 루트(`1prd`, `3history`)에서 통합 관리하는 로컬 예외 규칙 수립.
*   **[전체] 하위 폴더 정리**: 불필요해진 각 주차별 폴더(`wb01`, `py01`, `py02`) 내의 관리용 마크다운 파일(1prd, 3history 등)을 삭제하고 교육 본연의 자료만 남김.
*   **[K트랙] 파이썬 교육안 고도화**: 구글 코랩(Google Colab) 기반의 1~2주차 상세 목표 및 아카이브 섹션 추가.
*   **[E트랙] 웹 교육안 고도화**: 스택브리츠(StackBlitz) 기반의 1주차 상세 목표 및 아카이브 섹션 추가 (Bilingual).
*   **[E트랙] `wb01/lecture-script.md` 생성**: 1주차 웹 강의를 위한 실강용 대본 작성 완료 (Bilingual).

## 2026-03-01 (이전 작업 내역)
*   **[wb01] `wb01/lab.md` 개선**: 환영 인사/OT, AI-Native 마인드셋/질문법, StackBlitz/GitHub 기초 가이드 추가.
*   **[wb01] `wb01/lecture.md` 대폭 개편**: 강사 소개, 소통 정책, Flipped Learning 설명, 0.x 과제 동기화 보강 등.
*   **[wb01] `wb01/script.md` 생성**: 강의 실강 스크립트 작성 완료.
*   **[wb01] Bilingual 정책 적용**: 도입부 및 주요 규칙 한영 병기 완료.
*   **[wb01] `wb01/business-email.md` 생성**: 비즈니스 이메일 작성 규칙 가이드 완료.
