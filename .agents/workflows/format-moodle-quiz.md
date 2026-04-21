# format-moodle-quiz

Moodle 퀴즈 파일(`mid-eval-q.md`)의 문항 제목(Title)과 본문, 선택지 등을 가독성과 Moodle Import 시 복사-붙여넣기 편의성을 극대화하기 위해 특정 포맷으로 자동 변환하는 워크플로우입니다.

## 적용 포맷 및 작성 규칙 (최신)

지금까지의 대화에서 정립된 **최종 Moodle 퀴즈 작성 규칙**을 따릅니다. 각 항목 간에는 반드시 한 줄씩 공백(Empty Line)을 두어 더블클릭 복사가 쉽도록 합니다.

### 1. 요소의 배치 순서 (Moodle 입력 폼 순서와 일치)
1. `[Question name]` (문항 이름, 주차, 난이도)
2. `## 제목 ##`
3. `[Question type]` (문제 유형 명시)
4. `[Question text]` (문제 본문 시작)
5. **`[General feedback]` (피드백을 선택지/정답보다 먼저 배치)**
6. `[Choice 1...]` 또는 `[Answer]` (선택지 혹은 단답형 정답)
7. `[Korean]` (문제 본문 한국어 번역 - 코드 생략)

### 2. 문제 유형별 특수 규칙
* **객관식 (Multiple Choice)**: 
  * 정답은 `[Choice X (정답 100%)]`로 표기하며, 하단에 별도의 `[Answer X]` 태그나 정답 번호를 따로 표기하지 않습니다.
* **단답형 (Short Answer)**:
  * 무들 특수 문법(Cloze syntax, `{1:SHORTANSWER:=...}`)을 **절대 사용하지 않습니다.**
  * 복사하기 쉽도록 `정답 X:` 텍스트 바로 아래에 줄바꿈을 하여 정답 값을 작성합니다.
    ```markdown
    [Answer]
    
    정답 1:
    flex (100%)
    
    정답 2:
    flex; (100%)
    ```

### 3. 코드 블록(HTML/CSS) 인라인 스타일링 적용
마크다운 기본 코드 블록(```` ```html ````)을 사용하면 Moodle 에디터에 붙여넣을 때 서식이 깨집니다. 따라서 모든 코드 블록은 다음과 같은 인라인 CSS가 포함된 HTML 태그로 변환합니다. (내부의 `<`, `>` 기호는 `&lt;`, `&gt;`로 이스케이프 처리해야 합니다.)
```html
<pre style="background-color: #f4f4f4; padding: 15px; border: 1px solid #ccc; border-radius: 4px; white-space: pre-wrap; font-family: 'Courier New', Courier, monospace;"><code>...</code></pre>
```

---

**요구되는 최종 포맷 예시**
```markdown
[Question name] Q01 (wb02) [Medium]

## StackBlitz HTML Rendering ##

[Question type] multiple choice

[Question text] 

Run the following exact code in a StackBlitz HTML project. Do not modify the code.

<pre style="background-color: #f4f4f4; padding: 15px; border: 1px solid #ccc; border-radius: 4px; white-space: pre-wrap; font-family: 'Courier New', Courier, monospace;"><code>&lt;!DOCTYPE html&gt;...</code></pre>

When you open this in the StackBlitz preview...

[General feedback]

In HTML5, placing a block-level `<div>` inside an inline `<a>` tag is valid...

[Choice 1 (정답 100%)]

It navigates to google.com

[Choice 2]

It navigates to apple.com

[Korean]
StackBlitz HTML 프로젝트에서 다음 코드를 그대로 실행하세요. (코드 생략) StackBlitz 미리보기에서...
```

## 사용 방법

에이전트에게 `/format-moodle-quiz`를 호출하거나 대상 파일을 명시하여 "이 파일을 최신 Moodle 퀴즈 포맷으로 변환해줘"라고 요청합니다.

## 작동 방식 (AI 에이전트 지침)

AI 에이전트는 이 워크플로우를 호출받으면 다음 단계를 수행합니다:
1. 대상 마크다운 파일(`mid-eval-q.md` 등)을 읽습니다.
2. 각 퀴즈 문항 블록들을 순서대로 파싱하며 문항 번호를 정렬합니다.
3. 마크다운 코드 블록을 추출하여 이스케이프 처리 후 `<pre style="..."><code>` 태그로 변환합니다.
4. `[Question type]` 태그를 `[Question text]` 직전에 추가합니다.
5. 객관식의 경우 `[Answer X]` 블록을 일괄 삭제합니다.
6. 단답형의 경우 Cloze 구문을 읽기 쉬운 플레인 텍스트(줄바꿈 포함) 구조로 분해하여 재작성합니다.
7. Moodle 폼 순서에 맞게 `[General feedback]`을 정답/선택지 블록 위로 끌어올립니다.
8. 각 문항의 맨 마지막 줄(`---` 직전)에 `[Korean]` 태그를 달고 문제 본문의 한국어 번역을 추가합니다.
9. 작업 완료 후 사용자에게 변환 포맷팅 결과를 보고합니다.
