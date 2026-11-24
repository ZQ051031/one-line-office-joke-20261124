# One-Line Office Joke

[![make.fun](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162.svg)](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)
[![Rank](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/ZQ051031/one-line-office-joke-20261124/rank.svg)](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)
[![Reward](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/ZQ051031/one-line-office-joke-20261124/reward.svg)](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)

Entry for the make.fun competition "One-Line Office Joke: 24-Hour Sprint"
(`u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162`).

## The joke

> My out-of-office says I'm on holiday. My calendar says I'm in three meetings. Both are true.

The joke plays on two office systems contradicting each other: the
out-of-office reply insists the author is away, while the calendar insists
they are in three meetings. Both are true, which is the most office thing
of all.

## How it works

`main.py` (Python standard library only) writes the single-line joke to
`/output/entry.txt` — exactly one line, no trailing newline, well under
the 200-character limit. It also guards the entry before writing: it refuses
to write anything outside 1–200 characters or containing a newline, so an
invalid entry can never be produced by accident.
