# The GOAT Index

A single number meant to answer, "who's the greatest of all time at the Watermelon Classic?" — combining how fast you were for your age, how well you placed, and how many years you've shown up. It's built from three components that add up to 100:

- **Speed Score** — up to 50 points
- **Dominance Score** — up to 30 points
- **Participation Score** — up to 20 points

## Women's Top 10 GOAT Index

| Rank | Name | Years Raced | Avg Finish Time | Avg Age-Graded % | Speed (/50) | Dominance (/30) | Participation (/20) | GOAT Index | Best Finish |
|------|------|-------------|------------------|------------------|-------------|-----------------|----------------------|------------|-------------|
| 1 | Kelsey Shumate | 3 | 20:11 | 68.99% | 49.54 | 29.88 | 12.00 | **91.43** | 19:35 — 1st / 261 (2021) |
| 2 | Andre Guedez | 5 | 23:49 | 58.62% | 42.10 | 28.55 | 20.00 | **90.65** | 23:28 — 12th / 248 (2022) |
| 3 | Nancy Min | 5 | 28:57 | 63.07% | 45.29 | 22.94 | 20.00 | **88.23** | 27:42 — 41st / 248 (2022) |
| 4 | Audrey Mayatte | 2 | 20:28 | 69.62% | 50.00 | 29.86 | 8.00 | **87.86** | 19:15 — 2nd / 442 (2025) |
| 5 | Dorothy Wofford | 2 | 21:05 | 69.11% | 49.63 | 29.58 | 8.00 | **87.21** | 20:09 — 3rd / 261 (2021) |
| 6 | Elisabeth Gaillet | 4 | 23:34 | 59.16% | 42.48 | 28.62 | 16.00 | **87.11** | 22:35 — 11th / 285 (2023) |
| 7 | Jessica Diamond | 2 | 21:00 | 67.18% | 48.25 | 29.64 | 8.00 | **85.89** | 20:57 — 4th / 261 (2021) |
| 8 | Kara Hankins | 3 | 23:28 | 62.20% | 44.67 | 28.87 | 12.00 | **85.54** | 23:06 — 5th / 347 (2024) |
| 9 | Savannah Turner | 3 | 23:46 | 62.09% | 44.59 | 28.83 | 12.00 | **85.42** | 24:09 — 12th / 347 (2024) |
| 10 | Catherine Holmes | 4 | 28:39 | 63.29% | 45.45 | 23.80 | 16.00 | **85.25** | 27:53 — 45th / 248 (2022) |

*Best Finish is each runner's top result by overall place (time and field size shown for that race).*

## 1. Speed Score (up to 50 points) — "How fast were you, really?"

Raw finish times aren't fair across age and gender — a 50-year-old running 22:00 might be a far more impressive 5K than a 22-year-old running 19:00. So instead of comparing raw times, we use **age-graded percentage**: your time compared to the world-class standard for someone your exact age and gender. A higher percentage means you're closer to "world-class for your age."

The Speed Score takes your average age-graded % across all your Watermelon Classics, then scales it so the single best average performer in the field gets the full 50 points, and everyone else gets a proportional share.

**Worked example — Andre Guedez:** Andre averaged a 58.62% age-graded performance across her 5 years. The top average in the women's field belongs to Audrey Mayatte at 69.62%. So Andre's Speed Score is:

58.62 ÷ 69.62 × 50 = **42.10 / 50**

### How "Age-Graded Percentage" Actually Works

A 19:22 means something very different for a 22-year-old than it does for a 62-year-old. Age grading solves this by converting every finish time into a single, comparable percentage: "how close was this performance to the best a human of this exact age and gender could realistically run?"

**The standard:** For every age (5 to 100) and gender, there's a "standard" 5K time — roughly the world-class benchmark for that age/gender. These come from the Alan Jones 2025 Road Running Standards, the widely-used reference tables in masters and age-group running, updated for 2025.

**The formula:**

```
age-graded % = (standard time for your age & gender) / (your actual time) × 100
```

A result near 100% would be an all-time-great, essentially world-record-level run for that age and gender. 80%+ is considered "national class" — exceptional for a local 5K.

**Worked example — Tony Huffman (83.56%):** Tony is a 62-year-old man. The standard 5K time for a 62-year-old man is 16:11 (971 seconds). Tony actually ran 19:22 (1,162 seconds).

971 ÷ 1,162 × 100 = 83.56%

**Worked example — Jewel Baker (76.07%):** Jewel is a 13-year-old girl. The standard 5K time for a 13-year-old girl is 15:22 (922 seconds). Jewel actually ran 20:12 (1,212 seconds).

922 ÷ 1,212 × 100 = 76.07%

So even though Ethan Kelley's outright 2021 win in 15:44 at age 19 was nearly 4 minutes faster than Tony's (19:22), Tony's run was actually the more impressive performance by age-graded standards (83.56% vs. 81.46%). That's the whole point of age grading — it lets a 62-year-old's "slow" time and a 19-year-old's race-winning time be compared on a level playing field, and sometimes the older runner wins that comparison.

Runners racing multiple years have their age-graded percentages averaged for the Speed Score.

## 2. Dominance Score (up to 30 points) — "How close to the front were you?"

This score throws out time entirely and asks one question: what percentage of the field did you beat? It converts your finishing position into a 0–100% scale where 1st place = 100% and last place = 0%, with everyone else falling in between based on where they landed in the pack.

**The formula:**

```
dominance = 1 - (finish_position - 1) / (field_size - 1)
```

- 1st place: 1 - (1-1)/(field_size-1) = 1.0 (100%)
- Last place: 1 - (field_size-1)/(field_size-1) = 0.0 (0%)
- Dead middle of a 300-person field (150th): 1 - 149/299 ≈ 0.50 (50%)

This is multiplied by 30 to get a per-race score out of 30 points, then your overall Dominance Score is the average across all your races.

**Why percentile instead of raw position?** Field size changes every year (318 men in 2021, 538 in 2025), so "23rd place" means something different depending on the year. Converting to a percentage of the field beaten makes every year directly comparable — finishing 23rd out of 538 is roughly the same accomplishment as finishing 14th out of 318.

**Worked example — Andre Guedez:**

| Year | Time  | Place | Field Size | Dominance | Points (/30) |
|------|-------|-------|------------|-----------|--------------|
| 2021 | 24:06 | 21st  | 261        | 92.31%    | 27.69        |
| 2022 | 23:28 | 12th  | 248        | 95.55%    | 28.66        |
| 2023 | 23:34 | 13th  | 285        | 95.77%    | 28.73        |
| 2024 | 24:14 | 13th  | 347        | 96.53%    | 28.96        |
| 2025 | 23:45 | 20th  | 442        | 95.69%    | 28.71        |

Average dominance across her 5 races: 95.17% → Dominance Score = **28.55 / 30**.

Notice that even her "worst" year (2021, 21st place) was still a top-9% finish — which is why her Dominance Score stays consistently near the max. This is also why Dominance and Speed scores can diverge for the same runner: Andre's age-graded % (58.62%) reflects how she compares to the theoretical best for her age, while her Dominance score (95.17%) reflects how she compares to the actual people who showed up that day — and at the Watermelon Classic, she's consistently near the very front of that pack.

## 3. Participation Score (up to 20 points) — "How many years did you show up?"

This one's the simplest of the three: you get 4 points for every year you raced the Watermelon Classic, up to the full 20 for racing all 5 years.

```
participation score = (years raced / 5) × 20
```

| Years Raced | Participation Score |
|-------------|----------------------|
| 5 | 20 / 20 |
| 4 | 16 / 20 |
| 3 | 12 / 20 |
| 2 (the minimum to appear on this leaderboard) | 8 / 20 |

That's it — no math beyond counting. It exists because the GOAT Index is meant to celebrate the race's regulars, not just someone who happened to run one blistering 5K and never came back. Andre Guedez and Nancy Min, for example, both raced all 5 years and earn the full 20 points here.

## Putting It Together

GOAT Index = Speed (50) + Dominance (30) + Participation (20), for a maximum of 100. Ties are broken first by total appearances, then by your single best age-graded performance.

This is a speed-leaning formula — half the score comes from how fast you were for your age, with dominance and longevity splitting the rest. That means a runner with a blistering average pace and only 2–3 appearances can still outscore a 5-year regular with a more modest pace.

**Full example — Kelsey Shumate (#1 on the women's leaderboard):**

| Component | Score |
|-----------|-------|
| Speed (avg 68.99% age-graded) | 49.54 / 50 |
| Dominance (avg 99.61% of field beaten) | 29.88 / 30 |
| Participation (3/5 years) | 12.00 / 20 |
| **GOAT Index** | **91.43 / 100** |

**Full example — Andre Guedez (#2 on the women's leaderboard):**

| Component | Score |
|-----------|-------|
| Speed (avg 58.62% age-graded) | 42.10 / 50 |
| Dominance (avg 95.17% of field beaten) | 28.55 / 30 |
| Participation (5/5 years) | 20.00 / 20 |
| **GOAT Index** | **90.65 / 100** |

Kelsey's case shows the formula in action: with only 3 appearances, she's giving up 8 of the 20 participation points — but her near-perfect speed and dominance scores are enough to put her at #1, just 0.78 points ahead of Andre Guedez, who raced all 5 years (a full 20/20 on participation) but at a more modest pace. It's a near-perfect illustration of the formula's central tradeoff: a few years of blistering pace vs. steady excellence over the long haul.

## Full Women's GOAT Index Leaderboard

All 291 women with at least 2 appearances, ranked by GOAT Index:

| Rank | Name | Years Raced | Avg Finish Time | Avg Age-Graded % | Speed (/50) | Dominance (/30) | Participation (/20) | GOAT Index |
|------|------|--------------|------------------|-------------------|-------------|-----------------|----------------------|------------|
| 1 | Kelsey Shumate | 3 | 20:11 | 68.99% | 49.54 | 29.88 | 12.00 | 91.43 |
| 2 | Andre Guedez | 5 | 23:49 | 58.62% | 42.10 | 28.55 | 20.00 | 90.65 |
| 3 | Nancy Min | 5 | 28:57 | 63.07% | 45.29 | 22.94 | 20.00 | 88.23 |
| 4 | Audrey Mayatte | 2 | 20:28 | 69.62% | 50.00 | 29.86 | 8.00 | 87.86 |
| 5 | Dorothy Wofford | 2 | 21:05 | 69.11% | 49.63 | 29.58 | 8.00 | 87.21 |
| 6 | Elisabeth Gaillet | 4 | 23:34 | 59.16% | 42.48 | 28.62 | 16.00 | 87.11 |
| 7 | Jessica Diamond | 2 | 21:00 | 67.18% | 48.25 | 29.64 | 8.00 | 85.89 |
| 8 | Kara Hankins | 3 | 23:28 | 62.20% | 44.67 | 28.87 | 12.00 | 85.54 |
| 9 | Savannah Turner | 3 | 23:46 | 62.09% | 44.59 | 28.83 | 12.00 | 85.42 |
| 10 | Catherine Holmes | 4 | 28:39 | 63.29% | 45.45 | 23.80 | 16.00 | 85.25 |
| 11 | Emily Katherine Mattox | 2 | 21:14 | 65.50% | 47.04 | 29.75 | 8.00 | 84.79 |
| 12 | Emily Katherine Dacus | 2 | 21:18 | 65.36% | 46.94 | 29.57 | 8.00 | 84.50 |
| 13 | Ava Sylve | 3 | 23:40 | 60.11% | 43.17 | 28.40 | 12.00 | 83.57 |
| 14 | Kim Pillow | 2 | 25:18 | 65.86% | 47.29 | 28.28 | 8.00 | 83.57 |
| 15 | Charlotte McClellan | 5 | 30:05 | 58.48% | 42.00 | 21.16 | 20.00 | 83.16 |
| 16 | Christie Barber | 2 | 23:39 | 65.12% | 46.76 | 28.29 | 8.00 | 83.05 |
| 17 | Katherine Neal | 3 | 24:34 | 60.08% | 43.15 | 27.88 | 12.00 | 83.02 |
| 18 | Patience Miller | 2 | 21:58 | 63.28% | 45.45 | 29.35 | 8.00 | 82.80 |
| 19 | Wendy Garner | 2 | 25:53 | 66.65% | 47.86 | 26.64 | 8.00 | 82.50 |
| 20 | Marion Geissinger | 2 | 28:31 | 68.86% | 49.45 | 24.93 | 8.00 | 82.39 |
| 21 | Stephanie Weldon | 2 | 25:26 | 65.49% | 47.03 | 27.09 | 8.00 | 82.13 |
| 22 | Anik P. | 2 | 24:42 | 64.81% | 46.54 | 27.09 | 8.00 | 81.64 |
| 23 | Elena Roberts | 2 | 22:44 | 61.27% | 44.00 | 29.42 | 8.00 | 81.43 |
| 24 | Angie Walker | 2 | 24:32 | 62.85% | 45.14 | 27.99 | 8.00 | 81.13 |
| 25 | Frances Lancaster | 2 | 22:58 | 60.80% | 43.66 | 29.42 | 8.00 | 81.08 |
| 26 | Melissa Kaye McCombs | 4 | 26:22 | 53.70% | 38.56 | 26.30 | 16.00 | 80.87 |
| 27 | Virginia Morris | 4 | 26:53 | 53.72% | 38.58 | 25.75 | 16.00 | 80.33 |
| 28 | Melinda Engel | 5 | 29:25 | 53.53% | 38.44 | 21.80 | 20.00 | 80.24 |
| 29 | Rachel Holloway | 3 | 24:59 | 56.12% | 40.30 | 27.89 | 12.00 | 80.19 |
| 30 | Macy Claire Cronin | 2 | 23:02 | 60.53% | 43.47 | 28.70 | 8.00 | 80.17 |
| 31 | Keavy Noblin | 2 | 23:05 | 60.30% | 43.30 | 28.74 | 8.00 | 80.04 |
| 32 | Susan Creegan | 4 | 27:14 | 53.35% | 38.31 | 25.20 | 16.00 | 79.51 |
| 33 | Rosa Whitt | 4 | 27:24 | 53.79% | 38.63 | 24.39 | 16.00 | 79.02 |
| 34 | Jensen Baker | 2 | 24:26 | 58.57% | 42.06 | 28.71 | 8.00 | 78.77 |
| 35 | Sarah Tramel | 4 | 26:51 | 52.31% | 37.57 | 25.11 | 16.00 | 78.68 |
| 36 | Carley Langston | 3 | 25:58 | 54.29% | 38.99 | 27.24 | 12.00 | 78.23 |
| 37 | Lesley Holleman | 5 | 30:29 | 51.57% | 37.04 | 20.90 | 20.00 | 77.93 |
| 38 | Mary Francis Taylor | 3 | 26:22 | 56.05% | 40.26 | 25.56 | 12.00 | 77.82 |
| 39 | Kristi Ishee | 2 | 26:22 | 59.05% | 42.40 | 26.90 | 8.00 | 77.30 |
| 40 | Arin Hawk | 3 | 26:52 | 56.05% | 40.25 | 25.00 | 12.00 | 77.26 |
| 41 | Kristen Thorne | 2 | 25:29 | 57.67% | 41.41 | 27.79 | 8.00 | 77.21 |
| 42 | Mary Brock | 2 | 25:02 | 57.86% | 41.55 | 27.47 | 8.00 | 77.02 |
| 43 | Stephanie Wagner | 3 | 27:08 | 54.56% | 39.18 | 25.84 | 12.00 | 77.02 |
| 44 | Liz White | 3 | 26:43 | 54.55% | 39.18 | 25.77 | 12.00 | 76.95 |
| 45 | Leann Williams | 4 | 30:06 | 56.25% | 40.39 | 20.41 | 16.00 | 76.80 |
| 46 | Sue Nicholson | 5 | 34:53 | 59.11% | 42.45 | 13.93 | 20.00 | 76.38 |
| 47 | Amber Mckenzie | 2 | 26:15 | 58.72% | 42.17 | 26.20 | 8.00 | 76.37 |
| 48 | Christy Barber | 3 | 28:18 | 55.80% | 40.07 | 24.29 | 12.00 | 76.36 |
| 49 | Martha Davis | 3 | 29:32 | 60.49% | 43.44 | 20.87 | 12.00 | 76.32 |
| 50 | Kelsey Ray | 2 | 25:06 | 58.24% | 41.83 | 26.38 | 8.00 | 76.20 |
| 51 | Emma Roberts | 2 | 25:30 | 54.59% | 39.21 | 28.28 | 8.00 | 75.49 |
| 52 | Augusta Craig Whitfield | 4 | 30:20 | 53.87% | 38.68 | 20.76 | 16.00 | 75.44 |
| 53 | Maggie Jones | 2 | 26:34 | 56.13% | 40.31 | 27.12 | 8.00 | 75.43 |
| 54 | Dolly Smith | 2 | 29:18 | 61.97% | 44.50 | 22.56 | 8.00 | 75.06 |
| 55 | Allison Pyles | 3 | 27:00 | 51.67% | 37.10 | 25.87 | 12.00 | 74.98 |
| 56 | Mackenzie Mercer | 2 | 25:30 | 56.23% | 40.38 | 26.49 | 8.00 | 74.87 |
| 57 | Olivia Cook | 2 | 26:38 | 57.12% | 41.02 | 25.63 | 8.00 | 74.64 |
| 58 | Regan Wood | 2 | 25:14 | 55.19% | 39.64 | 26.98 | 8.00 | 74.62 |
| 59 | Alexa Salazar | 2 | 26:02 | 53.61% | 38.50 | 27.60 | 8.00 | 74.10 |
| 60 | Natalie Rodrigues | 3 | 28:32 | 52.81% | 37.93 | 24.09 | 12.00 | 74.02 |
| 61 | Brooke Bell | 2 | 25:38 | 54.46% | 39.11 | 26.70 | 8.00 | 73.80 |
| 62 | Jennifer Neal | 3 | 27:04 | 51.80% | 37.20 | 24.51 | 12.00 | 73.71 |
| 63 | Owenne McNeece | 3 | 29:06 | 53.72% | 38.58 | 22.77 | 12.00 | 73.35 |
| 64 | Nancy Studdard | 3 | 32:59 | 62.79% | 45.10 | 15.94 | 12.00 | 73.03 |
| 65 | Liz Cummings | 4 | 29:01 | 48.56% | 34.87 | 22.12 | 16.00 | 72.99 |
| 66 | Savannah Cavalier | 2 | 26:28 | 52.68% | 37.83 | 27.12 | 8.00 | 72.96 |
| 67 | Johnna Freiman | 2 | 28:22 | 57.50% | 41.30 | 23.55 | 8.00 | 72.84 |
| 68 | Mallary Smith | 2 | 26:32 | 52.44% | 37.66 | 27.06 | 8.00 | 72.72 |
| 69 | Avery Renfrow | 2 | 27:43 | 52.74% | 37.87 | 26.04 | 8.00 | 71.92 |
| 70 | Ginger Gorman | 2 | 27:52 | 53.71% | 38.57 | 25.12 | 8.00 | 71.69 |
| 71 | Erin Polzin | 4 | 30:10 | 48.21% | 34.62 | 20.58 | 16.00 | 71.21 |
| 72 | Anne Marie Obilade | 4 | 31:53 | 51.31% | 36.84 | 18.33 | 16.00 | 71.17 |
| 73 | Kelsey Hairston | 2 | 27:12 | 51.10% | 36.69 | 26.41 | 8.00 | 71.10 |
| 74 | Jessica Young | 2 | 27:35 | 51.36% | 36.88 | 26.02 | 8.00 | 70.91 |
| 75 | Beverly Brower | 2 | 27:31 | 53.64% | 38.52 | 24.26 | 8.00 | 70.78 |
| 76 | Sterling Belle Brock | 2 | 27:59 | 54.42% | 39.08 | 23.69 | 8.00 | 70.77 |
| 77 | Courtney Kern | 2 | 28:07 | 52.49% | 37.70 | 24.86 | 8.00 | 70.56 |
| 78 | Jamere Shelby | 3 | 28:30 | 49.15% | 35.30 | 23.09 | 12.00 | 70.39 |
| 79 | Megan Bell | 2 | 27:58 | 53.92% | 38.72 | 23.41 | 8.00 | 70.14 |
| 80 | Rylee McGee | 3 | 28:27 | 49.33% | 35.43 | 22.66 | 12.00 | 70.09 |
| 81 | Charlene Priester | 3 | 34:59 | 61.25% | 43.99 | 14.08 | 12.00 | 70.07 |
| 82 | Peyton Haecker | 2 | 27:05 | 51.34% | 36.87 | 25.16 | 8.00 | 70.02 |
| 83 | Amy Wright | 2 | 29:47 | 56.58% | 40.63 | 21.36 | 8.00 | 69.99 |
| 84 | Caroline Dyess | 2 | 27:02 | 52.60% | 37.78 | 23.96 | 8.00 | 69.74 |
| 85 | Lex Anna Anderson | 2 | 28:09 | 49.43% | 35.50 | 25.45 | 8.00 | 68.95 |
| 86 | Melissa Lewis | 3 | 30:03 | 48.01% | 34.48 | 22.19 | 12.00 | 68.67 |
| 87 | Doris McKinney | 2 | 30:56 | 57.20% | 41.08 | 19.49 | 8.00 | 68.57 |
| 88 | Hannah Byrd | 2 | 27:42 | 50.22% | 36.06 | 23.88 | 8.00 | 67.94 |
| 89 | Katie Bryant | 2 | 32:08 | 57.55% | 41.33 | 18.60 | 8.00 | 67.93 |
| 90 | Marina Shannon | 3 | 29:37 | 47.08% | 33.81 | 22.11 | 12.00 | 67.92 |
| 91 | Melissa Stevens | 3 | 29:47 | 48.74% | 35.00 | 20.91 | 12.00 | 67.92 |
| 92 | Bradford Seawright Sarah. | 2 | 28:04 | 49.51% | 35.56 | 23.76 | 8.00 | 67.32 |
| 93 | Brooke Hairston | 2 | 29:01 | 47.90% | 34.40 | 24.49 | 8.00 | 66.89 |
| 94 | Nicole Arbour | 4 | 34:24 | 50.56% | 36.31 | 14.57 | 16.00 | 66.87 |
| 95 | Lori Busick | 4 | 33:28 | 48.67% | 34.96 | 15.84 | 16.00 | 66.80 |
| 96 | Parker Reily | 2 | 28:47 | 49.02% | 35.21 | 23.42 | 8.00 | 66.62 |
| 97 | Laura Box | 2 | 28:36 | 49.15% | 35.30 | 22.89 | 8.00 | 66.18 |
| 98 | Nicole Herring | 2 | 29:17 | 47.47% | 34.09 | 24.07 | 8.00 | 66.16 |
| 99 | Emily Essex | 2 | 30:01 | 51.31% | 36.85 | 21.18 | 8.00 | 66.03 |
| 100 | Emiley Welker | 2 | 28:36 | 49.56% | 35.59 | 22.40 | 8.00 | 65.99 |
| 101 | Olivia Field | 2 | 29:02 | 48.28% | 34.67 | 23.29 | 8.00 | 65.96 |
| 102 | Kimberly Williams | 2 | 29:44 | 48.12% | 34.56 | 23.13 | 8.00 | 65.69 |
| 103 | Katie Schipper | 2 | 28:40 | 49.33% | 35.43 | 22.01 | 8.00 | 65.44 |
| 104 | Reese Ruhl | 2 | 29:58 | 49.32% | 35.42 | 21.55 | 8.00 | 64.97 |
| 105 | Ann Heidke | 2 | 32:33 | 54.34% | 39.03 | 17.94 | 8.00 | 64.96 |
| 106 | Antashia Williams | 2 | 30:42 | 51.58% | 37.04 | 19.62 | 8.00 | 64.66 |
| 107 | Teresa Bird | 3 | 33:17 | 51.52% | 37.00 | 15.45 | 12.00 | 64.45 |
| 108 | Molly Albritton | 2 | 29:41 | 46.98% | 33.74 | 22.68 | 8.00 | 64.42 |
| 109 | Natalie Cox | 2 | 29:42 | 46.97% | 33.73 | 22.58 | 8.00 | 64.31 |
| 110 | Trishah Shotts | 2 | 30:13 | 49.06% | 35.23 | 20.99 | 8.00 | 64.22 |
| 111 | Allie Tubby | 2 | 29:58 | 46.62% | 33.48 | 22.65 | 8.00 | 64.13 |
| 112 | Meredith VanDevender | 2 | 29:58 | 47.71% | 34.27 | 21.77 | 8.00 | 64.03 |
| 113 | Elle Pickrell | 2 | 29:58 | 46.43% | 33.34 | 22.64 | 8.00 | 63.99 |
| 114 | Victoria Walker | 2 | 30:45 | 48.18% | 34.60 | 21.17 | 8.00 | 63.77 |
| 115 | Carrie Cook | 2 | 30:24 | 49.58% | 35.61 | 20.12 | 8.00 | 63.72 |
| 116 | Rachel Ford | 3 | 31:13 | 45.99% | 33.03 | 18.52 | 12.00 | 63.54 |
| 117 | Kimberly Hooker | 2 | 32:02 | 50.25% | 36.09 | 18.93 | 8.00 | 63.02 |
| 118 | Amanda Keeton | 3 | 32:33 | 45.14% | 32.42 | 18.24 | 12.00 | 62.66 |
| 119 | Lauren Randle | 2 | 30:48 | 49.22% | 35.35 | 18.98 | 8.00 | 62.33 |
| 120 | Elizabeth Franklin | 4 | 36:58 | 49.07% | 35.24 | 11.02 | 16.00 | 62.26 |
| 121 | Abigail Witt | 2 | 29:54 | 46.52% | 33.41 | 20.77 | 8.00 | 62.18 |
| 122 | Karla Haik | 2 | 30:50 | 47.80% | 34.33 | 19.83 | 8.00 | 62.16 |
| 123 | Cindy Ringler | 2 | 33:41 | 55.21% | 39.65 | 14.51 | 8.00 | 62.15 |
| 124 | Sharon Dowdy | 2 | 33:03 | 51.31% | 36.85 | 17.30 | 8.00 | 62.15 |
| 125 | Cindy Parks | 2 | 30:18 | 47.48% | 34.10 | 19.95 | 8.00 | 62.05 |
| 126 | Livi Hubele | 2 | 30:41 | 45.36% | 32.57 | 21.40 | 8.00 | 61.97 |
| 127 | Kathryn McCullouch | 2 | 30:02 | 46.28% | 33.23 | 20.70 | 8.00 | 61.93 |
| 128 | Maggie Siler | 4 | 33:36 | 41.81% | 30.02 | 15.80 | 16.00 | 61.83 |
| 129 | Jessica Mathews | 4 | 35:18 | 45.12% | 32.40 | 13.37 | 16.00 | 61.77 |
| 130 | Megan Wilson | 3 | 31:57 | 44.17% | 31.72 | 18.03 | 12.00 | 61.75 |
| 131 | Lauren Romine | 2 | 29:58 | 46.71% | 33.54 | 20.04 | 8.00 | 61.58 |
| 132 | SHIRLEY BOURNE | 3 | 37:10 | 53.46% | 38.39 | 11.14 | 12.00 | 61.53 |
| 133 | Chandler Buggage | 2 | 30:28 | 45.77% | 32.87 | 20.55 | 8.00 | 61.42 |
| 134 | Kristen Arrington | 2 | 30:52 | 45.45% | 32.64 | 20.63 | 8.00 | 61.28 |
| 135 | Angie Pailette | 2 | 32:12 | 48.91% | 35.13 | 18.02 | 8.00 | 61.14 |
| 136 | Caroline Ray | 2 | 30:46 | 46.76% | 33.58 | 19.53 | 8.00 | 61.11 |
| 137 | Michelle Dickerson | 3 | 34:51 | 48.65% | 34.94 | 13.80 | 12.00 | 60.74 |
| 138 | Caroline J. | 2 | 32:50 | 48.64% | 34.93 | 17.78 | 8.00 | 60.71 |
| 139 | Chelsey Holmes | 3 | 32:26 | 43.53% | 31.26 | 17.31 | 12.00 | 60.57 |
| 140 | Jenny Woodruff | 2 | 32:24 | 48.65% | 34.93 | 17.45 | 8.00 | 60.39 |
| 141 | Allison Ruhl | 2 | 32:47 | 49.15% | 35.29 | 17.00 | 8.00 | 60.29 |
| 142 | Hannah Laird | 2 | 30:48 | 45.14% | 32.41 | 19.85 | 8.00 | 60.26 |
| 143 | Kimber Riley | 3 | 32:42 | 43.29% | 31.09 | 17.07 | 12.00 | 60.17 |
| 144 | Martini Ford | 3 | 34:29 | 43.96% | 31.57 | 16.43 | 12.00 | 60.00 |
| 145 | Kaitlyn Street | 3 | 32:35 | 42.76% | 30.71 | 17.24 | 12.00 | 59.95 |
| 146 | Shelley Sheppard | 2 | 32:30 | 47.54% | 34.14 | 17.79 | 8.00 | 59.93 |
| 147 | Kendra Johnson | 2 | 32:12 | 47.40% | 34.04 | 17.51 | 8.00 | 59.55 |
| 148 | Kay Bovim | 2 | 33:05 | 49.59% | 35.61 | 15.61 | 8.00 | 59.22 |
| 149 | Kaswana Moore | 2 | 31:42 | 44.27% | 31.79 | 19.32 | 8.00 | 59.11 |
| 150 | Pamela Keys | 4 | 37:05 | 44.94% | 32.28 | 10.71 | 16.00 | 58.99 |
| 151 | AUDREY HAWK | 2 | 31:50 | 45.85% | 32.93 | 17.84 | 8.00 | 58.77 |
| 152 | Lesley Sheppard | 2 | 31:50 | 43.72% | 31.40 | 19.24 | 8.00 | 58.64 |
| 153 | Shannon Evans | 4 | 35:50 | 40.05% | 28.76 | 13.84 | 16.00 | 58.60 |
| 154 | Cortne Robinson | 2 | 32:10 | 44.20% | 31.74 | 18.84 | 8.00 | 58.58 |
| 155 | Joan Ulmer | 3 | 33:24 | 42.08% | 30.22 | 16.31 | 12.00 | 58.53 |
| 156 | Jacqueline Canales | 4 | 42:20 | 51.28% | 36.82 | 5.57 | 16.00 | 58.39 |
| 157 | Mia Parker | 2 | 32:05 | 43.56% | 31.28 | 19.09 | 8.00 | 58.37 |
| 158 | Christine Woodberry | 2 | 33:32 | 46.02% | 33.05 | 17.24 | 8.00 | 58.29 |
| 159 | Xzavier Phillips | 2 | 33:24 | 46.73% | 33.56 | 16.65 | 8.00 | 58.21 |
| 160 | Lyssa Weatherly | 2 | 31:43 | 45.53% | 32.70 | 17.41 | 8.00 | 58.11 |
| 161 | Chris Alexander | 3 | 34:26 | 44.29% | 31.80 | 14.15 | 12.00 | 57.96 |
| 162 | Laura Franey | 2 | 34:02 | 48.36% | 34.73 | 15.09 | 8.00 | 57.82 |
| 163 | Jennifer Ballance | 3 | 34:28 | 43.12% | 30.96 | 14.77 | 12.00 | 57.73 |
| 164 | Jennifer Davis | 4 | 37:07 | 41.55% | 29.84 | 11.21 | 16.00 | 57.04 |
| 165 | Claire Jungling | 2 | 34:10 | 44.23% | 31.77 | 17.19 | 8.00 | 56.95 |
| 166 | Jennifer Stephen | 2 | 33:31 | 47.14% | 33.85 | 15.06 | 8.00 | 56.91 |
| 167 | Tricia Thomas | 4 | 40:36 | 46.76% | 33.58 | 7.24 | 16.00 | 56.82 |
| 168 | Brandi Fairchild | 2 | 32:41 | 43.93% | 31.55 | 17.26 | 8.00 | 56.81 |
| 169 | Kaitlyn Sloan | 2 | 32:04 | 43.58% | 31.30 | 17.18 | 8.00 | 56.48 |
| 170 | Alyse Bullock | 2 | 32:52 | 42.58% | 30.58 | 17.79 | 8.00 | 56.37 |
| 171 | Kelly Shannon | 2 | 33:56 | 46.67% | 33.51 | 14.71 | 8.00 | 56.22 |
| 172 | Ryleigh S. | 3 | 37:14 | 44.63% | 32.05 | 12.05 | 12.00 | 56.10 |
| 173 | Sherry Bullock | 2 | 36:32 | 49.65% | 35.66 | 12.24 | 8.00 | 55.90 |
| 174 | Pepper Ann White | 2 | 33:05 | 42.03% | 30.18 | 17.50 | 8.00 | 55.68 |
| 175 | Kelsey Ford | 5 | 38:27 | 36.28% | 26.06 | 9.61 | 20.00 | 55.67 |
| 176 | Alaina Mathis | 2 | 33:10 | 42.59% | 30.59 | 16.88 | 8.00 | 55.47 |
| 177 | Bonnie Bryant | 3 | 37:33 | 45.17% | 32.44 | 10.95 | 12.00 | 55.39 |
| 178 | Brandi Fournet | 3 | 36:43 | 45.12% | 32.40 | 10.95 | 12.00 | 55.35 |
| 179 | Kelly Liningham | 3 | 35:42 | 41.12% | 29.53 | 13.61 | 12.00 | 55.14 |
| 180 | Juanita Pressley | 3 | 40:29 | 50.20% | 36.05 | 7.03 | 12.00 | 55.08 |
| 181 | Britny Hester | 2 | 33:24 | 44.52% | 31.98 | 15.04 | 8.00 | 55.01 |
| 182 | Alexis Washington | 2 | 34:00 | 42.02% | 30.18 | 16.51 | 8.00 | 54.68 |
| 183 | Rebecca Hardy | 2 | 33:54 | 43.99% | 31.59 | 15.04 | 8.00 | 54.63 |
| 184 | Natalie Parker | 2 | 33:24 | 41.66% | 29.91 | 16.53 | 8.00 | 54.44 |
| 185 | Renee Neal | 4 | 42:18 | 43.34% | 31.13 | 7.24 | 16.00 | 54.37 |
| 186 | Ha Phan | 2 | 33:30 | 41.92% | 30.10 | 16.14 | 8.00 | 54.24 |
| 187 | Laken Stewart | 2 | 34:58 | 43.60% | 31.31 | 14.66 | 8.00 | 53.97 |
| 188 | Michelle Herrington | 2 | 35:37 | 45.19% | 32.45 | 13.52 | 8.00 | 53.97 |
| 189 | Scharla Bivings | 5 | 44:19 | 39.69% | 28.51 | 5.05 | 20.00 | 53.56 |
| 190 | Kai Jenkins | 2 | 33:56 | 43.05% | 30.92 | 14.52 | 8.00 | 53.44 |
| 191 | Haley Conerly | 2 | 33:52 | 41.05% | 29.48 | 15.91 | 8.00 | 53.39 |
| 192 | Maria Smith | 2 | 35:13 | 44.55% | 31.99 | 13.16 | 8.00 | 53.15 |
| 193 | Michelle Wynter | 2 | 34:59 | 43.45% | 31.21 | 13.59 | 8.00 | 52.80 |
| 194 | Jennifer Clark | 4 | 44:49 | 44.94% | 32.28 | 4.27 | 16.00 | 52.55 |
| 195 | Emilye Welch | 5 | 40:39 | 35.15% | 25.24 | 7.13 | 20.00 | 52.37 |
| 196 | Kathleen McNeil | 3 | 40:14 | 45.92% | 32.98 | 7.27 | 12.00 | 52.25 |
| 197 | Olga McDaniel | 4 | 48:22 | 47.10% | 33.83 | 2.41 | 16.00 | 52.23 |
| 198 | Debbie Broadhead | 5 | 47:48 | 39.50% | 28.37 | 3.63 | 20.00 | 51.99 |
| 199 | Susan Rockoff | 2 | 36:52 | 45.58% | 32.73 | 11.12 | 8.00 | 51.85 |
| 200 | KRISTI HAWK | 2 | 41:02 | 43.57% | 31.29 | 12.17 | 8.00 | 51.46 |
| 201 | Kimberly Best | 3 | 39:01 | 38.47% | 27.63 | 11.43 | 12.00 | 51.06 |
| 202 | Chrissy Fortenberry | 4 | 40:03 | 37.27% | 26.77 | 7.89 | 16.00 | 50.66 |
| 203 | Laura Gaddy | 2 | 35:18 | 39.40% | 28.29 | 13.72 | 8.00 | 50.02 |
| 204 | Sylvia Hoffmann | 2 | 35:10 | 39.67% | 28.49 | 13.30 | 8.00 | 49.79 |
| 205 | Tracy Morgan | 3 | 40:20 | 41.93% | 30.11 | 7.64 | 12.00 | 49.75 |
| 206 | Candie Williams | 2 | 36:58 | 43.55% | 31.28 | 10.45 | 8.00 | 49.73 |
| 207 | Heather Usry | 3 | 37:45 | 37.40% | 26.86 | 10.86 | 12.00 | 49.72 |
| 208 | Elizabeth Hamilton | 2 | 35:16 | 40.27% | 28.92 | 12.59 | 8.00 | 49.51 |
| 209 | Donna Norris | 4 | 44:34 | 40.49% | 29.08 | 4.43 | 16.00 | 49.51 |
| 210 | Torrey Robinson | 2 | 35:47 | 38.85% | 27.90 | 13.49 | 8.00 | 49.38 |
| 211 | Keegan Foxx | 2 | 35:42 | 40.86% | 29.35 | 12.02 | 8.00 | 49.37 |
| 212 | Jean Lowrey | 4 | 47:42 | 42.44% | 30.48 | 2.76 | 16.00 | 49.24 |
| 213 | Vicki Husband | 3 | 39:58 | 39.89% | 28.65 | 8.18 | 12.00 | 48.83 |
| 214 | Jetaun Cotten | 2 | 36:04 | 40.77% | 29.28 | 11.49 | 8.00 | 48.77 |
| 215 | Amy Hornback | 4 | 42:48 | 37.86% | 27.19 | 5.42 | 16.00 | 48.61 |
| 216 | Audrey Dean | 3 | 38:01 | 37.35% | 26.82 | 9.74 | 12.00 | 48.56 |
| 217 | Emily Chance | 2 | 37:18 | 39.71% | 28.52 | 11.80 | 8.00 | 48.32 |
| 218 | Abigail S. | 2 | 41:40 | 41.92% | 30.10 | 9.76 | 8.00 | 47.86 |
| 219 | Charla Lewis | 3 | 39:02 | 37.25% | 26.75 | 9.10 | 12.00 | 47.85 |
| 220 | Laura Katherine Buccola | 3 | 38:35 | 37.05% | 26.61 | 9.13 | 12.00 | 47.74 |
| 221 | Harley Smith | 3 | 39:33 | 38.32% | 27.52 | 8.11 | 12.00 | 47.63 |
| 222 | Cissy Mccarty | 2 | 42:19 | 43.37% | 31.14 | 8.42 | 8.00 | 47.57 |
| 223 | Sharon Ezell | 2 | 37:36 | 41.41% | 29.74 | 9.78 | 8.00 | 47.52 |
| 224 | Debra Lovell | 4 | 49:50 | 41.12% | 29.53 | 1.76 | 16.00 | 47.29 |
| 225 | Jeanne Butler | 2 | 39:47 | 43.89% | 31.52 | 7.32 | 8.00 | 46.84 |
| 226 | Deidre Smith | 3 | 40:10 | 38.38% | 27.56 | 7.24 | 12.00 | 46.80 |
| 227 | Amanda Brown | 2 | 37:53 | 38.50% | 27.65 | 11.10 | 8.00 | 46.74 |
| 228 | TAMECKA JOHNSON | 2 | 37:34 | 39.44% | 28.32 | 10.31 | 8.00 | 46.63 |
| 229 | Jennifer Lobos | 2 | 36:38 | 38.61% | 27.73 | 10.87 | 8.00 | 46.59 |
| 230 | Avery McDaniel | 2 | 37:00 | 37.99% | 27.28 | 11.10 | 8.00 | 46.38 |
| 231 | Angela Guice | 2 | 40:32 | 43.19% | 31.02 | 7.11 | 8.00 | 46.13 |
| 232 | Earlene Weathersby | 2 | 40:43 | 43.47% | 31.21 | 6.90 | 8.00 | 46.11 |
| 233 | Alyssa Holly | 2 | 37:06 | 37.58% | 26.99 | 11.01 | 8.00 | 46.00 |
| 234 | Andrea Bonner | 2 | 38:39 | 37.02% | 26.59 | 11.09 | 8.00 | 45.68 |
| 235 | Mecca Chance | 2 | 38:14 | 38.96% | 27.98 | 9.50 | 8.00 | 45.48 |
| 236 | Lexi Brown | 2 | 37:40 | 37.04% | 26.60 | 10.47 | 8.00 | 45.07 |
| 237 | Allie Hart Lyon | 2 | 39:18 | 38.67% | 27.77 | 9.26 | 8.00 | 45.03 |
| 238 | Lori Hill | 2 | 39:51 | 39.52% | 28.38 | 8.63 | 8.00 | 45.01 |
| 239 | Katie Upchurch | 3 | 40:07 | 34.89% | 25.06 | 7.81 | 12.00 | 44.87 |
| 240 | Kayla Soukup | 2 | 38:43 | 37.10% | 26.65 | 10.22 | 8.00 | 44.87 |
| 241 | Jeanna Burns | 2 | 40:10 | 41.25% | 29.62 | 7.23 | 8.00 | 44.85 |
| 242 | Audrika Lewis | 2 | 38:25 | 36.73% | 26.37 | 10.35 | 8.00 | 44.73 |
| 243 | Dyanne Ray | 2 | 41:29 | 42.35% | 30.41 | 6.15 | 8.00 | 44.57 |
| 244 | Amy Earnest | 3 | 42:19 | 37.08% | 26.63 | 5.90 | 12.00 | 44.53 |
| 245 | Katie Seage | 2 | 37:45 | 36.98% | 26.56 | 9.69 | 8.00 | 44.25 |
| 246 | Jacqueline Langston | 2 | 38:55 | 36.50% | 26.22 | 9.94 | 8.00 | 44.15 |
| 247 | Nya Williams | 2 | 38:17 | 36.33% | 26.09 | 9.99 | 8.00 | 44.08 |
| 248 | Jelesia Stokes | 3 | 40:58 | 34.51% | 24.78 | 7.04 | 12.00 | 43.82 |
| 249 | Kelly Russell | 2 | 41:40 | 37.54% | 26.96 | 8.72 | 8.00 | 43.68 |
| 250 | Tracie Archie | 5 | 52:59 | 31.69% | 22.76 | 0.87 | 20.00 | 43.63 |
| 251 | Ashley Peden | 2 | 38:35 | 36.37% | 26.12 | 9.46 | 8.00 | 43.58 |
| 252 | Britney Owens | 2 | 40:32 | 37.42% | 26.88 | 8.52 | 8.00 | 43.39 |
| 253 | Heather Notvest | 3 | 41:18 | 34.54% | 24.80 | 6.43 | 12.00 | 43.24 |
| 254 | Erica Whitlock | 3 | 41:35 | 34.76% | 24.96 | 6.18 | 12.00 | 43.14 |
| 255 | Sally Day Sharp | 2 | 38:22 | 36.39% | 26.13 | 8.89 | 8.00 | 43.03 |
| 256 | Gracie Eubank | 2 | 39:20 | 35.38% | 25.41 | 9.34 | 8.00 | 42.75 |
| 257 | Ana Izaguiree | 3 | 46:11 | 34.44% | 24.73 | 5.86 | 12.00 | 42.60 |
| 258 | Jessica Drenning | 2 | 42:30 | 40.59% | 29.15 | 5.30 | 8.00 | 42.45 |
| 259 | Kimberly Gabriel | 2 | 42:30 | 36.39% | 26.13 | 8.11 | 8.00 | 42.24 |
| 260 | Alicia Arrington | 2 | 41:07 | 37.51% | 26.94 | 7.22 | 8.00 | 42.15 |
| 261 | Tamara Jackson | 2 | 40:38 | 37.52% | 26.94 | 6.96 | 8.00 | 41.90 |
| 262 | Katie Sanders | 2 | 41:49 | 35.78% | 25.70 | 8.17 | 8.00 | 41.87 |
| 263 | Lori Price | 2 | 44:22 | 40.46% | 29.06 | 4.63 | 8.00 | 41.69 |
| 264 | Vanessa Addison | 2 | 44:01 | 40.47% | 29.07 | 4.55 | 8.00 | 41.62 |
| 265 | Diana Hirsch | 2 | 49:52 | 43.52% | 31.26 | 1.97 | 8.00 | 41.22 |
| 266 | Avery Hornback | 4 | 46:24 | 30.86% | 22.16 | 3.04 | 16.00 | 41.20 |
| 267 | Becca Conerly | 2 | 40:00 | 35.14% | 25.24 | 7.51 | 8.00 | 40.75 |
| 268 | Brooke Smith | 2 | 40:19 | 34.52% | 24.79 | 7.88 | 8.00 | 40.67 |
| 269 | Emily Hall | 3 | 43:40 | 32.12% | 23.07 | 5.17 | 12.00 | 40.24 |
| 270 | Karneshe Hibbler | 4 | 50:26 | 31.27% | 22.46 | 1.62 | 16.00 | 40.08 |
| 271 | Ashley Hall | 2 | 43:24 | 33.79% | 24.27 | 7.74 | 8.00 | 40.01 |
| 272 | Janet Higgins | 2 | 47:16 | 38.92% | 27.95 | 3.02 | 8.00 | 38.97 |
| 273 | Edmeisha McGill | 2 | 43:23 | 34.29% | 24.63 | 5.53 | 8.00 | 38.16 |
| 274 | Jane Stevenson | 2 | 51:16 | 39.82% | 28.60 | 1.48 | 8.00 | 38.07 |
| 275 | Jordan Neely | 2 | 42:48 | 33.04% | 23.72 | 5.89 | 8.00 | 37.61 |
| 276 | Nicole Smith-Whitlock | 2 | 45:08 | 32.39% | 23.26 | 5.74 | 8.00 | 37.00 |
| 277 | Laurie Gardner | 2 | 49:26 | 36.77% | 26.41 | 1.99 | 8.00 | 36.40 |
| 278 | Jana Parrish | 2 | 48:55 | 36.37% | 26.12 | 2.14 | 8.00 | 36.26 |
| 279 | Kimberly Loper | 2 | 50:24 | 34.81% | 25.00 | 3.12 | 8.00 | 36.11 |
| 280 | Frankie Clifton-Patton | 2 | 44:20 | 32.92% | 23.64 | 4.32 | 8.00 | 35.96 |
| 281 | Caron Blanton | 2 | 48:20 | 35.71% | 25.64 | 1.76 | 8.00 | 35.40 |
| 282 | Taylor Wiley | 2 | 44:15 | 31.44% | 22.58 | 4.40 | 8.00 | 34.98 |
| 283 | Lauren Baker | 2 | 45:32 | 31.27% | 22.46 | 3.80 | 8.00 | 34.26 |
| 284 | Kailyn Davis | 2 | 44:56 | 31.01% | 22.27 | 3.94 | 8.00 | 34.21 |
| 285 | Heather Chase | 2 | 49:14 | 31.24% | 22.44 | 2.48 | 8.00 | 32.92 |
| 286 | Alliyah Stout | 2 | 46:25 | 29.95% | 21.51 | 3.09 | 8.00 | 32.60 |
| 287 | Alina Lea | 2 | 47:50 | 29.24% | 21.00 | 3.06 | 8.00 | 32.06 |
| 288 | Ramona Pendleton | 2 | 55:08 | 32.47% | 23.32 | 0.45 | 8.00 | 31.76 |
| 289 | Penelope Pendleton | 2 | 51:24 | 27.08% | 19.45 | 1.48 | 8.00 | 28.93 |
| 290 | Victoria Carr | 2 | 52:46 | 27.45% | 19.72 | 1.19 | 8.00 | 28.90 |
| 291 | Bertina McGrew | 2 | 51:32 | 27.01% | 19.39 | 1.45 | 8.00 | 28.84 |
