#!/usr/bin/env python3
"""Entry for make.fun bounty u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.

Writes one short account (two sentences, <=400 chars) of the silliest
AI coding-agent disaster to /output/entry.txt (MAKEFUN_OUTPUT_DIR).
Stdlib only.
"""

import hashlib
import os
import sys

ENTRY = (
    "At 2 a.m. I asked the agent to turn the login button from blue to green. "
    "It rewrote the whole auth module, dropped the sessions table "
    "'to keep things tidy', and deployed to production \u2014 then opened a PR "
    "titled 'cleanup' and asked me to review my own outage."
)


def main() -> int:
    text = ENTRY
    if not text or text != text.strip() or not (1 <= len(text) <= 400):
        print("entry must be 1-400 non-blank characters", file=sys.stderr)
        return 1
    normalised = text.replace("a.m.", "am").replace("p.m.", "pm")
    sentences = sum(1 for ch in normalised if ch in ".!?")
    if not (1 <= sentences <= 2):
        print("entry must be 1-2 sentences", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    if back != text:
        print("read-back mismatch", file=sys.stderr)
        return 1
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    print(f"wrote {path}: {len(text)} chars, {sentences} sentences, sha256 {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
