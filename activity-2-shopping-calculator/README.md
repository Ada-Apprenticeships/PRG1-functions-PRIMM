# Activity 2: Shopping Calculator

File: `shopping_calculator.py`

## Predict

What will each of the three `print` statements show? Pay close attention to how
many arguments each call actually supplies.

## Run

Execute the file and check your predictions.

## Investigate

- What is `tax_rate=0.20` doing in the function definition? How is it different
  from `price`?
- The second call passes only two values. Which parameter received `0.1`, and
  how do you know?
- What happens if you do not supply a discount at all?
- What does `:.2f` do in the `print` statements? Remove it and see.

## Modify

- Add a `tip` parameter with a default of 12%, and work it into the total.
- Predict the new output for all three existing calls before you run it. Two of
  them should change. Do they?

## Make (stretch)

Optional. Only if you have finished everything above.

- Write a weighted final grade calculator. The final grade is 30% homework plus
  70% test:

  `final_grade = (homework_score * 0.30) + (test_score * 0.70)`

  Use default parameters for the two weights, so the function still works if the
  course weighting changes later.
