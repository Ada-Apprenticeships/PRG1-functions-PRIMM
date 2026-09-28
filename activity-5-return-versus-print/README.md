# Activity 5: Return versus Print

File: `return_versus_print.py`

Two functions that look almost identical and behave completely differently. This
one catches nearly everybody, so predict carefully.

## Predict

- How many lines of output will this file produce?
- Write down what each line will say, in order.
- What will `first` hold? What will `second` hold?

## Run

Execute it. Most pairs get the number of lines wrong before they get the content
wrong.

## Investigate

- `add_and_print(2, 3)` produced output. `add_and_return(2, 3)` on the next line
  did not. Why not? The calculation still happened.
- Why does `print(first)` show `None`? Where did `None` come from, given that
  the word `None` appears nowhere in the file?
- The last line multiplies a function call by 10 and it works. Try doing the
  same thing with `add_and_print`. What happens, and why?

## Modify

- Change `add_and_print` so that the last line of the file would work with it
  too. What did you have to add?

> Almost every function you meet from here on returns rather than prints.
> Printing is how a program talks to a person. Returning is how one piece of a
> program talks to another.
