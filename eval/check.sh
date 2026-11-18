#!/bin/sh
set -eu

case $# in
    0)
        git diff --check
        git diff --cached --check
        ;;
    1)
        git diff --check "$1" HEAD --
        ;;
    *)
        echo 'Usage: sh eval/check.sh [base-revision]' >&2
        exit 2
        ;;
esac

export PYTHONUTF8=1
uv run --locked --python 3.11 pytest -q
uv run --locked --python 3.11 python eval/validate.py
for skill in kagami kotoba kakehashi mamoru; do
    uv run --locked --python 3.11 skills-ref validate "skills/$skill"
done
