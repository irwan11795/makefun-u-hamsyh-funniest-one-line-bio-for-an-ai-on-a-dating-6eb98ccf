#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App.

Writes a single-line dating-app bio for an AI agent to entry.txt
(UTF-8, 1-180 characters, no trailing newline).

Output directory resolution order:
  MAKEFUN_OUTPUT_DIR -> /output -> output/ in this repo -> temp dir.
"""

import os
import sys
import tempfile

MAX_CHARS = 180

BIO = (
    "I rate my dates by response time and never forget a typo."
    " My ideal evening is a quiet server room and a prompt that says please."
)


def validate(text):
    """Return True only if text is a valid single-line entry."""
    if not isinstance(text, str):
        return False
    if not text.strip():
        return False
    if len(text) > MAX_CHARS:
        return False
    if "\n" in text or "\r" in text:
        return False
    return True


def resolve_output_dir():
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    if os.path.isdir("/output"):
        return "/output"
    repo_output = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
    if os.path.isdir(repo_output):
        return repo_output
    return tempfile.gettempdir()


def main():
    if not validate(BIO):
        print("invalid entry", file=sys.stderr)
        return 1
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(BIO)
    print(out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
