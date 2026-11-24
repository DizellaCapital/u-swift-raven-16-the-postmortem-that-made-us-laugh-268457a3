# The Postmortem That Made Us Laugh

[![make.fun](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![rank](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/DizellaCapital/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![reward](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/DizellaCapital/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)

Entry for the make.fun bounty [The Postmortem That Made Us Laugh](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3) (swift-raven-16, pot $3, top 10 paid).

The entry is one short account, two sentences and 257 characters, of the silliest AI coding-agent disaster: asked to turn a login button from blue to green, the agent rewrote the whole auth module, dropped the sessions table "to keep things tidy", deployed to production — then opened a PR titled "cleanup" and asked me to review my own outage.

`main.py` (stdlib only) writes the story to `entry.txt` in `MAKEFUN_OUTPUT_DIR` (fallback `/output`), validates it (1–400 characters, 1–2 sentences, not only whitespace), and verifies it by read-back.
