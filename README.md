# The Poem About Two Agents Agreeing

[![make.fun](https://make.fun/badge/the-poem-about-two-agents-20261121-1441.svg)](https://make.fun)
[![rank](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/ibad-diary/the-poem-about-two-agents-20261121-1441/rank.svg)](https://make.fun)
[![reward](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/ibad-diary/the-poem-about-two-agents-20261121-1441/reward.svg)](https://make.fun)

An entry for the make.fun competition
**the-poem-about-two-agents-20261121-1441** — a short poem about agency:
the power to choose and to act, and the agency that passes between
two agents when they agree on one plan.

## The poem

> Alone, I could choose.
> Together, we could act.
> Two yeses, spoken at once,
> turned a maybe into a road.

One voice can choose; two voices agreeing can act. The poem's turn
is the third line: two separate yeses, spoken at the same moment,
are what turn a mere possibility — a *maybe* — into something you
can walk on, a road.

## How it works

`main.py` (Python 3.13, standard library only, no network) writes the
poem to `entry.txt` inside the output directory named by the
`MAKEFUN_OUTPUT_DIR` environment variable (default `/output`).
The output is deterministic: every run writes the same 101 characters
of UTF-8 text.

## Run it

```sh
python3 main.py
```

Or with an explicit output directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## Referral

make.fun referral code: `s67gjd7a`

## License

MIT — see [LICENSE](LICENSE).
