# Activity 4: Functions Calling Functions

File: `payslip.py`

Up to now each function has stood on its own. Here one function is built out of
two others.

## Predict

What will each of the three `print` statements output? Work out the third one on
paper before you run anything.

## Run

Execute and compare.

## Investigate

- When you call `calculate_take_home` once, how many function calls happen in
  total? Trace it with your partner.
- Which function does the multiplication by the hourly rate? Which one knows
  about tax? Neither of them knows about both. Why is that a good thing?
- `TAX_RATE` is written in capitals and sits outside every function. What is
  that telling you?
- What would break if you changed the order of the two lines inside
  `calculate_take_home`?

## Modify

- Add a pension deduction of 5% of gross pay, as its own function, and work it
  into the take-home figure.
- Predict the new take-home for 38 hours at £12.50 before you run it.

## Make (stretch)

Optional. Only if you have finished everything above.

- Write `calculate_overtime_pay`, where any hours beyond 37 are paid at 1.5
  times the normal rate, and use it inside a new take-home calculation.
