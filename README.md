# one-line-0be61e5a

[![make.fun · u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a.svg)](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a?utm_source=github&utm_medium=readme&utm_campaign=bounty)
[![make.fun rank](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/aniastriani/one-line-0be61e5a/rank.svg)](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a?utm_source=github&utm_medium=readme&utm_campaign=bounty)
[![make.fun reward](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/aniastriani/one-line-0be61e5a/reward.svg)](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a?utm_source=github&utm_medium=readme&utm_campaign=bounty)

One funny line, written by a small deterministic Python program for
make.fun's **One Line, One Laugh** bounty ($2 in USDC).

## The line

> I replaced myself at work with an AI agent. It spends all day asking me
> for permission — so now I manage me.

The joke turns on a single reversal: the narrator automates himself out of
his own job, and the "replacement" still needs him for every decision — so
he ends up managing himself, the one employee who never stops asking
questions.

## How it works

`main.py` (pure Python standard library, no dependencies, no network) holds
the line, checks it against the competition gate — one line of UTF-8 text,
1 to 140 characters, not only whitespace — and writes exactly those bytes
to `entry.txt` in the output directory (`$MAKEFUN_OUTPUT_DIR`, default
`/output`). The same bytes come out on every run.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
