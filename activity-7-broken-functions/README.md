# Activity 7: Broken Functions

File: `broken_functions.py`

Three things in this file are wrong. None of them crash. The code runs, prints
three results, and two of those results are simply incorrect while the third is
not a result at all.

This is what most real faults look like. Code that crashes tells you where to
look. Code that quietly returns the wrong number does not.

## Predict

Read all three functions and the three calls at the bottom. For each call, work
out on paper what the answer **should** be:

- The area of a 4 by 5 rectangle
- £80 with 25% off
- 50 as a percentage of 200

## Run

Execute the file. Compare what you got with what you expected.

## Investigate

For each of the three, work out what went wrong. Be precise: name the line and
say what it does versus what it was meant to do.

Two useful questions:

- One of the outputs is `None`. What does that tell you about the function that
  produced it?
- One of the faults is **not inside a function at all**. Which one, and what
  does that tell you about where faults can live?

## Fault log

Fill this in with your partner. You will do exactly this, marked, in Task 2.

| # | What you saw | What was wrong | How you fixed it |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

## Modify

Fix all three. Run it again. You should get `20`, `60.0` and `25.0`.

## Stretch: swap faults

Optional, and worth reaching if you can.

Write a function with a deliberate fault of your own, of a kind not used here,
and swap with another pair. Can they find it? Can you find theirs? Planting a
fault that survives someone else's reading is harder than it sounds, and it
teaches you a great deal about where your own attention goes when you read.
