#!/usr/bin/env bash
python3 -m venv .venv
source .venv/bin/activate
pip install playwright markdown
playwright install chromium
echo "환율 설정이 끝났습니다. source .venv/bin/activate 로 가상환경 진입 후 python ecampus_uploader.py 명령을 실행해 보세요."
