#!/usr/bin/env python3
import os
import re
import sys
import argparse

def check_placeholders(content, filename):
    placeholders = ["[강사 이름]", "[이메일]", "[주차]", "[학번]"]
    found = []
    for p in placeholders:
        if p in content:
            found.append(p)
    return found

def get_micro_assignment_ssot(week_num):
    ssot_path = "docs/assignment-micro.md"
    if not os.path.exists(ssot_path):
        return None

    with open(ssot_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Try to find ## 과제 0.N section
    pattern = rf"## 과제 0\.{int(week_num)}(.*?)(?=## 과제 0\.|\Z)"
    match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return None

def lint_week(week_dir):
    print(f"--- 검증 시작: {week_dir} ---")
    errors = []

    # week_num extraction
    folder_name = os.path.basename(week_dir.rstrip("/"))
    match = re.search(r"(wb|py)(\d+)", folder_name)
    if not match:
        errors.append(f"폴더 네이밍 규칙 위반: {folder_name} (예: py03, wb01)")
        return errors

    track = match.group(1) # 'wb' or 'py'
    week_num = match.group(2)

    # 1. handout.md check
    handout_path = os.path.join(week_dir, "handout.md")
    if os.path.exists(handout_path):
        with open(handout_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Placeholder check
        ph = check_placeholders(content, "handout.md")
        if ph:
            errors.append(f"handout.md 내에 미치환 플레이스홀더 발견: {ph}")

        # Week number consistency
        title_match = re.search(rf"{int(week_num)}\s*주차", content)
        if not title_match:
            # Maybe Assignment 0.X check
            title_match = re.search(rf"Assignment\s*0\.{int(week_num)}", content, re.IGNORECASE)
            if not title_match and int(week_num) > 0:
                errors.append(f"handout.md 제목/내용에 주차({week_num}) 불일치 의심")

        # Micro-assignment SSOT alignment (Simple keyword check)
        ssot_content = get_micro_assignment_ssot(week_num)
        if ssot_content:
            # Extract items from SSOT
            ssot_items = re.findall(r"\d+\.\s+\*\*([^*]+)\*\*", ssot_content)

            # Extract items from handout (Section 3 — supports multiple heading formats)
            # Supported headings: "## Section 3: Assignment", "## 3. Email Assignment",
            #                     "## 3. 마이크로 과제", "## 마이크로과제"
            handout_assignment_section = re.search(
                r"(##\s+(?:Section\s+3[:\s]|3[.\s]+(?:Email\s+)?(?:Assignment|마이크로\s*과제)|마이크로\s*과제).*?)(?=\n## |\Z)",
                content, re.DOTALL | re.IGNORECASE
            )
            handout_items_count = 0
            if handout_assignment_section:
                handout_items_count = len(re.findall(r"\d+\.\s+\*\*", handout_assignment_section.group(1)))

            if len(ssot_items) != handout_items_count:
                errors.append(f"handout.md 과제 개수 불일치: SSOT({len(ssot_items)}개) vs 핸드아웃({handout_items_count}개)")

            for item in ssot_items:
                if item.strip() not in content:
                    # Looser check if bolding is different
                    if item.strip().split()[0] not in content:
                        errors.append(f"handout.md에 SSOT 과제 내용이 누락된 것으로 보임: {item}")
    else:
        errors.append("handout.md 파일이 없습니다.")

    # 2. peer-eval-rubric.md check
    rubric_path = os.path.join(week_dir, "peer-eval-rubric.md")
    if os.path.exists(rubric_path):
        with open(rubric_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Total score check
        score_match = re.search(r"(\d+)\s*점\s*만점", content)
        if score_match:
            expected_score = int(score_match.group(1))
            # Q1 is always 5 points. Other questions are 1 point each.
            # So the number of (Yes 1 / No 0) for other questions should be expected_score - 4
            # OR expected_score directly if Q1 also uses it (not typical, but we'll accept both)
            yes_count = content.count("(Yes 1 / No 0)")
            if yes_count != expected_score and yes_count != (expected_score - 4) and yes_count != (expected_score - 5):
                errors.append(f"루브릭 점수 합계 불일치: 명시된 만점({expected_score}) vs 실제 (Yes 1/No 0) 항목 수({yes_count}) 확인 요망")
        else:
            errors.append("루브릭에 'N점 만점' 표기가 없습니다.")

        # Placeholder check
        ph = check_placeholders(content, "peer-eval-rubric.md")
        if ph:
            errors.append(f"peer-eval-rubric.md 내에 미치환 플레이스홀더 발견: {ph}")
    else:
        errors.append("peer-eval-rubric.md 파일이 없습니다.")

    return errors

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("week_dir", help="검증할 주차 폴더 경로")
    args = parser.parse_args()

    errs = lint_week(args.week_dir)
    if errs:
        print("\n[FAIL] 하네스 검증 실패:")
        for e in errs:
            print(f" - {e}")
        sys.exit(1)
    else:
        print("\n[PASS] 하네스 검증 통과!")
        sys.exit(0)
