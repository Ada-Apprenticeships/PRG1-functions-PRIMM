# Activity 3: Password Validator

File: `check_password_strength.py`

This is a longer function than the previous two. Read it all the way through
before predicting anything.

## Predict

For each of the four test passwords, predict the score out of 4 and which
pieces of feedback will appear.

## Run

Execute and compare against your predictions. Which one did you get most wrong,
and why?

## Investigate

- What does `any()` do? Describe it in one sentence without using the word "any".
- How do `.isupper()`, `.islower()` and `.isdigit()` work?
- Why does `"PASSWORD"` score so badly? It is a long password.
- This function returns **two** things on one line. Find where those two values
  are picked up again further down the file.

## Modify

- Add a check for special characters such as `!@#$%^&*`.
- Return a rating of "Weak", "Medium" or "Strong" based on the score.
