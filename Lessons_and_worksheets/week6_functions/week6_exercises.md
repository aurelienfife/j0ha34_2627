# Unit 5 (week 6): Introduction to Functions — Exercise Sheets

**J0HA34 Computer Programming | HNC Cybersecurity**

**As usual, there are more challenging exercises near the end for those who have studied Python before. The optional extensions go beyond beginner level, so don't worry if you're not ready for them yet.**

## A. Define and call a function

```python
def show_heading():
    print("Login report")
    print("------------")

show_heading()
print("No results yet")
show_heading()
```

1. Copy and run the code above. Check that the heading appears twice, with `No results yet` between the two headings.
2. Change the heading text inside the function. Check that both calls use the new version.
3. Add a third call at the end of the main program without copying the print statements.
4. Add a comment explaining the difference between defining and calling the function.

**Hint:** Indent the statements inside the function. The calls in the main program start at the left margin, level with `def`. See [W3Schools: functions](https://www.w3schools.com/python/python_functions.asp).

## B. Parameters and arguments

```python
def greet_user(username):
    print("Hello", username)

name = input("Enter your name: ")
greet_user(name)
```

1. Copy and run the code above, entering your own name.
2. Add a second call using the string `"Sam"` directly as the argument.
3. Add a second parameter called `course`. Change the function to print a greeting followed by the course name, and update both calls to supply a course.

A call with `"Sam"` and `"Cybersecurity"` should display both values. Calling the function twice should give two greetings.

**Hint:** Separate parameters with commas, and do the same for the arguments in each call. The input variable does not have to have the same name as the parameter.

## C. An account summary

Now write your own function, `show_result(username, failures)`. It should print a username and a failure count with clear labels. It does not need to return a value.

Outside the function:

- Use `input()` to ask for a username and a whole number of failed logins (zero or more).
- Convert the failure count with `int()` — remember that `input()` gives you a string.
- Call the function with those two values.

Test `Sam` with 0 failures and `Alex` with 3 failures. Each run should display the corresponding name and count once.

**Hint:** Pass the values you collected into the function. Inside it, use the parameters to print the summary. Keep the arguments in the same order as the parameters in your definition.

## D. Returning values

```python
def calculate_total(price, quantity):
    return price * quantity

order_total = calculate_total(2.50, 3)
print("Order total:", order_total)
```

1. Copy and run the code above. It should print 7.5.
2. Ask the user for the price and quantity outside the function. Use `float()` for the price and `int()` for the quantity. Pass the converted values to the function.
3. Store the returned result, then add a delivery charge of £3 outside the function and print the amount to pay.
Keep the calculation inside the function to price × quantity; add delivery in the main program. Try these values:

| Price | Quantity | Returned total | Amount including delivery |
| --- | --- | --- | --- |
| 2.50 | 3 | 7.50 | 10.50 |
| 5.00 | 1 | 5.00 | 8.00 |
| 0.00 | 2 | 0.00 | 3.00 |

**Hint:** `return` gives the result back to the caller. `print()` displays it. You need the returned value to add delivery. Different decimal formatting, such as 7.5 rather than 7.50, is fine.

## E. Find the bug: printing and returning

This program prints the calculation, but something goes wrong when we try to use the result. Copy it and see what happens:

```python
def calculate_total(price, quantity):
    print(price * quantity)

order_total = calculate_total(2.50, 3)
amount_to_pay = order_total + 3
print("Amount to pay:", amount_to_pay)
```

1. Run it. It displays 7.5, then raises a `TypeError`.
2. Temporarily add `print(order_total)` just before the addition. What value did the function actually return?
3. Fix the function so the caller can use its result.
4. Remove the temporary diagnostic print. Check that the final amount is 10.5.
5. Add a comment explaining why printing the calculation did not return it.

**Hint:** A function that reaches the end without returning a result returns `None`. Compare this function with `calculate_total` in section D.

## F. Flagging failed logins

Let's bring selection back in. Write a function called `needs_review(failures)` that returns `True` when there are three or more failed logins, and `False` otherwise. We're using a simple classroom rule here, with made-up login counts.

In the main program, use `input()` to ask for a whole number of failed logins (zero or more). Convert it with `int()` and pass it to your function. Use the returned Boolean in an `if/else` to print either `Review this batch` or `No review flag`.

The function should not print either message or ask for input.

| Failure count | Returned value | Message |
| --- | --- | --- |
| 0 | `False` | No review flag |
| 2 | `False` | No review flag |
| 3 | `True` | Review this batch |
| 4 | `True` | Review this batch |

**Hints:**

- You can use `if/else` inside the function to return the two Booleans, or return the comparison itself.
- Return `True` and `False` without quotation marks. `"False"` is a non-empty string, not a false Boolean.
- You can store the returned value in a variable and use that variable as your `if` condition.
- If you need a reminder about selection, see [W3Schools: if/else](https://www.w3schools.com/python/python_conditions.asp).

## G. A total you can reuse

Use a loop inside a function called `total_to(limit)` to return the sum of the whole numbers from 1 up to and including `limit`. Assume `limit` is a non-negative integer.

Inside the function:

- Start a local total at zero.
- Use a `for` loop to add each number.
- Return the total after the loop has finished.

In the main program, use `input()` to ask for a limit, convert it with `int()`, call the function and print the returned value. Then add `print(total_to(3))` and `print(total_to(5))`. These should display 6 and 15, showing that each call starts with a fresh total.

| Limit | Expected result |
| --- | --- |
| 0 | 0 |
| 1 | 1 |
| 3 | 6 |
| 5 | 15 |

**Hint:** The range must include `limit`; remember that the stop value in `range()` is excluded. Put `return` after the loop, at the same indentation as the initial total assignment. Returning inside the loop ends the function before it has finished adding the numbers. See [W3Schools: for loops and range()](https://www.w3schools.com/python/python_for_loops.asp).

## H. For the more visual among you ;)

Use an environment with working turtle graphics. Save the file as `function_squares.py`, not `turtle.py`.

```python
import turtle

pen = turtle.Turtle()
pen.pensize(3)

def draw_square(size):
    for side in range(4):
        pen.forward(size)
        pen.right(90)

draw_square(60)
draw_square(100)

turtle.done()
```

`size` sets the side length, and `pen` is the turtle that does the drawing. The loop draws four sides, turning 90 degrees after each. Both squares start at the same corner in the same window.

1. Run the starter and check that both squares appear.
2. Add a third call to draw a square of side length 140.
3. Add a `colour` parameter to the function. Set the pen colour using `pen.color(colour)` before its loop, then supply a colour string in each call.
4. Use `"blue"`, `"red"` and `"green"` so you can distinguish the squares.

**Hint:** `pen.color()` changes the drawing colour; the quotes make the colour name a string. This function draws rather than calculates, so it does not need an explicit return. Keep `turtle.done()` after all calls.

**If graphics are unavailable:** remove the turtle commands and have the function print `Side length:` and the supplied size four times. Add the colour to each printed line when adapting it. This still lets you check parameter passing and repetition.

More about the drawing commands: [Python documentation: turtle graphics](https://docs.python.org/3/library/turtle.html).

## For the Brave (or non-beginners)

Comfortable defining functions, passing arguments and returning results? Try these optional extensions. They introduce a few things we haven't covered yet.

### Extension 1. A function that keeps asking for valid input

Write `read_non_negative_integer(prompt)`. It should display the supplied prompt and keep asking until the user enters an integer greater than or equal to zero, then return that integer.

- Use `try/except ValueError` to handle text that `int()` cannot convert.
- Give a clear message for negative integers and for non-integer entries.
- Return only when the input is valid.
- Use your new function to ask for the limit in section G.

Try entering `hello`, then `-2`, then `3`. The first two entries should be rejected; the returned integer should be 3. Entering `0` first should return 0 immediately. Entering `2.5` should be rejected because this function asks for an integer.

**Hint:** Put the loop inside the function. Once the input is valid, `return` ends the function, so you do not need a separate `break`. See [W3Schools: try/except](https://www.w3schools.com/python/python_try_except.asp).

### Extension 2. Automate your checks

Add assertions below your definitions of `needs_review` and `total_to`. An assertion asks Python to check that a condition is true:

```python
assert needs_review(2) == False
assert needs_review(3) == True
assert total_to(3) == 6
print("All checks passed")
```

A passing assertion is silent. A failing one raises `AssertionError` and normally stops the program, so the final message is reached only if all checks pass.

1. Add assertions for all rows in the test tables in sections F and G.
2. Temporarily change the threshold in `needs_review` so exactly three failures are handled incorrectly. Run the tests and identify which assertion catches the change.
3. Restore the correct condition and run the tests again.
4. Add an explanatory failure message to one assertion, for example `assert total_to(0) == 0, "Zero should give an empty sum"`.

This is a first step towards **unit testing**: testing one small part of a program using known inputs and expected results. Passing these tests confirms those cases; it does not prove all possible inputs work. Assertions can be disabled with optimisation, so keep ordinary input validation in Extension 1.

For help with the syntax, see [W3Schools: assert examples](https://www.w3schools.com/python/ref_keyword_assert.asp). For later study, [Python's unittest basic example](https://docs.python.org/3/library/unittest.html#basic-example) shows how to organise a set of tests. You do not need that framework for this exercise.
