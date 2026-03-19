# Workflows
These are predefined workflows and instructions to interact with the project repository and external systems efficiently.

## Index
1. [Auto-Create eCampus Assignment (Peer Eval)](#auto-create-ecampus-assignment-peer-eval)

---

### Auto-Create eCampus Assignment (Peer Eval)
**Name:** eCampus 상호평가 과제 게시판 자동 생성

**Description:** 
eCampus(Moodle) 시스템의 '가져오기(Import)' 기능을 사용 시, 다른 주차 영상이나 불필요한 파일이 함께 복사되는 문제를 방지하기 위해 AI(브라우저 에이전트)에게 수작업과 동일한 게시판 생성을 위임하는 지시어 가이드.

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
