# Activity 6: Scope

File: `scope.py`

Two short experiments about which names are visible where.

## Predict

Write down all four lines of output before running anything. Be specific: for
each one, say whether it will be `5`, `10`, `inside` or `outside`.

## Run

Execute it.

## Investigate

- `double_it(value)` clearly doubles something, and yet `value` is still 5
  afterwards. What exactly did the function receive?
- Inside `show_message` there is a line `message = "inside"`. After the function
  has run, the outer `message` is unchanged. Explain that to your partner
  without using the word "scope".
- If you delete the line `message = "inside"` from inside the function, what do
  you think `show_message()` will print? Predict, then try it.

## Modify

- Change `show_message` so that it takes the message as a parameter instead of
  using a name from outside the function. Which version would you rather be
  handed to maintain, and why?
