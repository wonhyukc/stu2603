---
description: IPYNB(Jupyter Notebook) 파일의 JSON 문법 무결성을 검증합니다.
---

에이전트 또는 사용자가 `.ipynb` 파일을 수정한 직후 파일 깨짐(Silent Error) 현상을 방지하기 위해 JSON 문법을 빠르게 검증하는 워크플로우입니다.

1. 터미널을 열고 대상 파일에 대해 `jq` 명령어를 실행합니다.
// turbo
2. `jq . [대상_파일_경로] > /dev/null`
   - *실행 예시*: `jq . python-output/py03/lab.ipynb > /dev/null`
3. 에러 출력 없이 종료(exit code 0)되면 파일이 정상입니다.
4. 만약 `parse error: Invalid escape ...` 등의 메시지가 뜬다면, 지적된 라인의 이스케이프 문자(예: 잘못된 따옴표, 백슬래시 오타 등)를 수정한 뒤 다시 2번 단계를 실행하여 통과할 때까지 반복합니다.
