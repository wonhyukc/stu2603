---
trigger: always_on
---

# Local Project Rules (Override for stu2603)

This document is intended to override some of the user's Global AI Rules. AI agents must apply these rules with the highest priority when working within this project context.

## 1. Relaxation of 4-Document Sync (No Subfolder Sync)

*   **Background**: The existing Global Rule enforces a 'Document-first Sync' policy, requiring the creation and synchronization of four core documents (`1prd.md`, `2todo.md`, `4test.md`) for every work unit and subfolder. However, this policy causes excessive overhead in this project (`stu2603`), so the rule is relaxed.
*   **New Rule**:
    1.  **Manage Root Documents Only**: Project-level scheduling and history are centrally managed using only one document in the root directory: **`1prd.md`**.
    2.  **No Management in Subfolders**: Do not place separate `1prd`, `2todo`, or `4test` documents within each weekly subdirectory (e.g., `wb01/`, `py01/`, etc.).
    3.  **Focus purely on Educational Materials**: Inside each weekly folder, only files necessary for actual lectures and assignments (`lecture.md`, `lab.md`, `homework.md`, etc.) should exist.

## 2. Language Guidelines (Overriding Global Rules)

*   **E-Track (Web Programming)**: 1~8주차 강사용 문서(`lecture.md`, `lecture-script.md`, `course-notice.md`, `slides.md` 등) 초안 작성 시 **반드시 한국어 100% 단일 언어**로만 작성해야 합니다. `CLAUDE.md`의 언어 정책을 최우선으로 따르며, 영어 병기는 향후 별도 워크플로우로 진행하므로 에이전트 생성 시 절대 영한 병기를 적용하지 마세요. 학생 배포 문서인 `handout.md` 등은 영어 우선(또는 영한 병기)으로 작성합니다.
*   **K-Track (Computing Thinking & Coding)**: Write all documentation **exclusively in Korean**. Do not use the bilingual format for K-Track materials.

*(For detailed track-specific language policies, refer to `CLAUDE.md`)*
