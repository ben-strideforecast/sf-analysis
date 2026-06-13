# The GOAT Index (0–100)

A single number meant to answer, "who's the greatest of all time at the Watermelon Classic?" — combining how fast you were for your age, how well you placed, and how many years you've shown up. It's built from three components that add up to 100:

- **Speed Score** — up to 50 points
- **Dominance Score** — up to 30 points
- **Participation Score** — up to 20 points

## Women's Top 10 GOAT Index

| Rank | Name | Years Raced | Avg Age-Graded % | Speed (/50) | Dominance (/30) | Participation (/20) | GOAT Index | Best Finish |
|------|------|-------------|------------------|-------------|-----------------|----------------------|------------|-------------|
| 1 | Kelsey Shumate | 3 | 68.99% | 49.54 | 29.88 | 12.00 | **91.43** | 19:35 — 1st / 261 (2021) |
| 2 | Andre Guedez | 5 | 58.62% | 42.10 | 28.55 | 20.00 | **90.65** | 23:28 — 12th / 248 (2022) |
| 3 | Nancy Min | 5 | 63.07% | 45.29 | 22.94 | 20.00 | **88.23** | 27:42 — 41st / 248 (2022) |
| 4 | Audrey Mayatte | 2 | 69.62% | 50.00 | 29.86 | 8.00 | **87.86** | 19:15 — 2nd / 442 (2025) |
| 5 | Dorothy Wofford | 2 | 69.11% | 49.63 | 29.58 | 8.00 | **87.21** | 20:09 — 3rd / 261 (2021) |
| 6 | Elisabeth Gaillet | 4 | 59.16% | 42.48 | 28.62 | 16.00 | **87.11** | 22:35 — 11th / 285 (2023) |
| 7 | Jessica Diamond | 2 | 67.18% | 48.25 | 29.64 | 8.00 | **85.89** | 20:57 — 4th / 261 (2021) |
| 8 | Kara Hankins | 3 | 62.20% | 44.67 | 28.87 | 12.00 | **85.54** | 23:06 — 5th / 347 (2024) |
| 9 | Savannah Turner | 3 | 62.09% | 44.59 | 28.83 | 12.00 | **85.42** | 24:09 — 12th / 347 (2024) |
| 10 | Catherine Holmes | 4 | 63.29% | 45.45 | 23.80 | 16.00 | **85.25** | 27:53 — 45th / 248 (2022) |

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

**Worked example — Nathan Tarver:**

| Year | Time  | Place | Field Size | Dominance | Points (/30) |
|------|-------|-------|------------|-----------|--------------|
| 2021 | 18:06 | 10th  | 318        | 97.16%    | 29.1         |
| 2022 | 18:47 | 18th  | 320        | 94.67%    | 28.4         |
| 2023 | 21:36 | 44th  | 363        | 88.12%    | 26.4         |
| 2024 | 19:31 | 21st  | 432        | 95.36%    | 28.6         |
| 2025 | 19:28 | 23rd  | 538        | 95.90%    | 28.8         |

Average dominance across his 5 races: 94.24% → Dominance Score = **28.27 / 30**.

Notice that even his "worst" year (2023, 44th place) was still a top-12% finish — which is why his Dominance Score stays consistently near the max. This is also why Dominance and Speed scores can diverge for the same runner: Nathan's age-graded % (72.97%) reflects how he compares to the theoretical best for his age, while his Dominance score (94.24%) reflects how he compares to the actual people who showed up that day — and at the Watermelon Classic, he's consistently near the very front of that pack.

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

That's it — no math beyond counting. It exists because the GOAT Index is meant to celebrate the race's regulars, not just someone who happened to run one blistering 5K and never came back. Nathan Tarver and Ryan Crandall, for example, both raced all 5 years and earn the full 20 points here.

## Putting It Together

GOAT Index = Speed (50) + Dominance (30) + Participation (20), for a maximum of 100. Ties are broken first by total appearances, then by your single best age-graded performance.

This is a speed-leaning formula — half the score comes from how fast you were for your age, with dominance and longevity splitting the rest. That means a runner with a blistering average pace and only 2–3 appearances can still outscore a 5-year regular with a more modest pace.

**Full example — Nathan Tarver (current #1 men's GOAT):**

| Component | Score |
|-----------|-------|
| Speed (avg 72.97% age-graded) | 44.57 / 50 |
| Dominance (avg 94.24% of field beaten) | 28.27 / 30 |
| Participation (5/5 years) | 20.00 / 20 |
| **GOAT Index** | **92.84 / 100** |

**Full example — Kelsey Shumate (current #1 women's GOAT):**

| Component | Score |
|-----------|-------|
| Speed (avg 68.99% age-graded) | 49.54 / 50 |
| Dominance (avg 99.61% of field beaten) | 29.88 / 30 |
| Participation (3/5 years) | 12.00 / 20 |
| **GOAT Index** | **91.43 / 100** |

Kelsey's case shows the formula in action: with only 3 appearances, she's giving up 8 of the 20 participation points — but her near-perfect speed and dominance scores are enough to put her at #1 on the women's leaderboard, just ahead of Andre Guedez, who raced all 5 years but at a more modest pace.
