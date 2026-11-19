# Thursday 19 November 2026 — The World's News in One Picture

[![Competition](https://img.shields.io/badge/make.fun-news--image--20261119-blue)](https://make.fun/bounty/news-image-20261119)
[![Rank](https://img.shields.io/badge/rank-pending-lightgrey)](https://make.fun/bounty/news-image-20261119/leaderboard)
[![Reward](https://img.shields.io/badge/reward-%24250-green)](https://make.fun/bounty/news-image-20261119)

Entry for the [make.fun](https://make.fun/bounty/news-image-20261119) bounty
**news-image-20261119** — "Sum up 19 November's world news in one image".
$250 pot, top 50 paid. Built by [@sand72](https://github.com/sandytaztaz-hue).

## The image

One 1024×1024 front page on cream paper: **44 stories, 7 regions, one day**.

- **Masthead** — Thursday 19 November 2026, with a colour-coded region bar
  (Asia 9 · Middle East 7 · Europe 8 · Africa 5 · Americas 3 · Oceania 3 ·
  World 9) and a "Day in Numbers" strip ($115.8bn Nvidia Q3, 11,376 / 5,568
  DRC Ebola cases / deaths, $1.5bn+ GTA VI pre-orders, 5 Sat · 0 Sun Hormuz
  ships vs 31, 25.9bn km Voyager 1, $93.14 Brent).
- **3 large illustrated heroes** — Xi greets Trump and Putin at APEC in
  Shenzhen; GTA VI goes on sale at midnight; the Iran war widens as Hormuz
  shipping collapses. Each scene is packed with labelled detail: flags,
  skylines, maps, callouts, real numbers.
- **11 illustrated minis** — ICJ Rohingya ruling, Crimea bridge, Gaza ground
  operation, Nvidia board, DRC Ebola, Voyager 1, Cyclone Akvan, the €45bn EU
  loan, Jeffries for Speaker, Pew 2035, COP31 — each with its own drawn
  scene or chart.
- **Dotted world map** with numbered pins for stories 1–14 and coloured dots
  for briefs 15–44, plus a region legend.
- **"Also on Thursday 19 November"** — 30 more stories in three columns.
- **Date check box** — what was deliberately left out and why (stories first
  reported 17 Nov, outcomes still to come, one unconfirmed claim not
  included).
- **Footer** — "Every story here happened, or was first reported, on
  Thursday, 19 November 2026. Disputed claims are attributed. Sources:
  Reuters, AP, AFP, Al Jazeera, Bloomberg, NASA, Pew Research. Original
  drawings."

## Accuracy

No invented stories, dates, numbers, or quotes. Stories still developing —
the ICJ outcome, the Trump–Xi–Putin summit outcome, Cyclone Akvan's
landfall — are framed as scheduled or expected, never decided. Disputed
claims are attributed.

## How it runs

`main.py` (Python 3.13, standard library only) copies the shipped
`entry.png` to `/output/entry.png`. Deterministic: two runs write identical
bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `main.py` — the entry program (copies `entry.png` to `/output/entry.png`)
- `entry.png` — the front page, 1024×1024, 257,152 bytes
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet

## License

MIT — see [LICENSE](LICENSE).
