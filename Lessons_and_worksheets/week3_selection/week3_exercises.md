# Boolean logic and selection: practical exercises

**SCQF level 7 | Beginner Python**

**Before you start: the optional extensions at the end are not suitable for beginners. They are there for people who already know Python and want an extra challenge. If you are new to Python, focus on Exercises 1–8.**

Work through the exercises in order. Start by reproducing the examples, then adapt them and have a go at the challenges. Keep the handout nearby and use the hints if you get stuck.

## Preparation

This was meant to be for a 2-hour class, but we encourage you to study further and try extra challenges in your own time.

Exercises 1–8 form the beginner route. The two extensions offer additional challenges for learners who already know Python.

| Section | Exercises |
| --- | --- |
| `if`: one conditional action | 1–2 |
| `if/else`: two alternatives | 3–4 |
| `if/elif/else`: several alternatives | 5–7 |
| A different application: turtle graphics | 8 |

You should already be able to create and run a Python file, assign variables and use `print()`. No loops or functions are required for the beginner route. Start a separate file for each exercise, with names such as `exercise_01.py`.

### A reminder about input and types

The reproduce exercises start with values written directly in the code. Run those versions first so you can see what the conditions do. You will then add user input where the instructions ask for it.

**Remember: `input()` always returns a string, even when you type a number.** Convert it before comparing it with a number:

```python
people = int(input("How many people are in the room? "))
```

Here, `input()` asks the question, `int()` converts the answer to a whole number, and `=` stores that number in `people`. Use `float()` instead when you want to accept decimal values, such as a price or temperature. Enter prices as numbers only: `39.50`, without a pound sign.

For yes/no answers, compare the text to create a Boolean:

```python
answer = input("Is the account active? (yes/no): ").strip().lower()
is_active = answer == "yes"
```

`.strip()` removes spaces at the beginning and end; `.lower()` converts the text to lowercase. The comparison produces `True` for `yes` and `False` otherwise. **Do not use `bool(input(...))` to interpret yes/no answers:** a non-empty string such as `"no"` becomes `True`.

For Exercises 1–8, enter a valid number when asked for one, and answer yes/no questions with `yes` or `no`. Checking for mistyped answers is the task in Extension 2. A number can still be outside an exercise's allowed range: for example, `-1` converts successfully to an integer, but the ticket program must reject it as an age.

For each exercise:

1. Predict what will happen before running the program.
2. Run it with each set of test values. Edit the assignment for a fixed-value example, or type the values at the prompts once you have added input. For two-variable tables, use both values from the same row.
3. Compare the actual result with the expected result.
4. Save your code. Where asked, add a short explanation as a comment beginning with `#`.

Use the test tables to check your results. Where a table shows `True` or `False` for a yes/no prompt, enter `yes` or `no`, respectively. Use four spaces for each indentation level.

## A. `if`: run an action when a condition is true

### 1. Reproduce: a low-battery warning

**Focus: a simple comparison and indentation**

Type and run this program:

```python
battery = 15

if battery < 20:
    print("Low battery")

print("Battery check complete")
```

Then:

1. Run it with `battery` set to `15`, `20` and `80`.
2. Identify which message appears every time.
3. Change the condition so that exactly 20 also produces a warning.
4. Replace `battery = 15` with a prompt asking for the battery percentage. Convert the answer with `int()` and repeat the three tests.
5. Add a comment explaining why the last message does not depend on the condition.

**Check your changed program:** 15 and 20 should show the warning; 80 should not. Every run should finish with `Battery check complete`.

### 2. Code challenge: a full room

**Focus: write your own `if`**

A room has a capacity of 24 people. Write a program that:

- Asks the user how many people are currently in the room. Convert the answer to an integer and store it in `people`, using the input example above.
- Prints `Room at or above capacity` if there are 24 or more people.
- Always prints `Room check complete` afterwards.

Use one `if` statement. No alternative message is needed when there is space.

| `people` | Expected output, in order |
| --- | --- |
| `23` | `Room check complete` |
| `24` | `Room at or above capacity`, then `Room check complete` |
| `25` | `Room at or above capacity`, then `Room check complete` |

Add a comment explaining why the test with 24 is important.

**Hint:** choose a comparison that includes 24. Keep the final `print()` at the left margin so that it runs regardless of the comparison's result. For a reminder of assignment syntax, see [W3Schools: Python variables](https://www.w3schools.com/python/python_variables.asp).

## B. `if/else`: choose one of two alternatives

### 3. Reproduce, then adapt: a delivery charge

**Focus: true and false branches**

Type and run this program:

```python
order_total = 25

if order_total >= 30:
    print("Free delivery")
else:
    print("Delivery costs £3")
```

1. Test totals of `29`, `30` and `31`. Exactly one message should appear each time.
2. Change the free-delivery threshold to £40 and the delivery charge to £4.
3. Replace `order_total = 25` with a prompt for the order total. Convert the answer with `float()` so the program accepts pounds and pence.
4. Test your updated version with totals of `39`, `39.99`, `40` and `41`.

**Check:** 39 and 39.99 should produce `Delivery costs £4`; 40 and 41 should produce `Free delivery`.

Add a comment explaining why `else` does not need its own comparison.

### 4. Cybersecurity challenge: an account access check

**Focus: `and` and `not`**

Imagine you are checking whether an account should be allowed into a company portal. For this exercise, the account must be active and must not be suspended. First, build and test the decision using these values:

```python
is_active = True
is_suspended = False
```

Write an `if/else` statement that prints either `Access allowed` or `Access refused`. Use both `and` and `not` in the condition.

Once it works, replace the fixed values with two yes/no prompts: one asking whether the account is active, and one asking whether it is suspended. Convert each answer to a Boolean using the pattern at the top of the worksheet. Repeat all four tests. You are entering simulated account information to test the rule.

| `is_active` | `is_suspended` | Expected output |
| --- | --- | --- |
| `True` | `False` | `Access allowed` |
| `True` | `True` | `Access refused` |
| `False` | `False` | `Access refused` |
| `False` | `True` | `Access refused` |

**Hints:**

- Read `is_active` as “the account is active”. A Boolean variable can be used directly in a condition.
- Use `not` to express “the account is not suspended”.
- Both requirements must be met. Use a single combined condition, followed by an `else` for refused access.
- Review the logical operators in [W3Schools: Python operators](https://www.w3schools.com/python/python_operators.asp).

After testing, add a comment explaining why an active but suspended account must still be refused access.

## C. `if/elif/else`: choose between several alternatives

### 5. Reproduce, then adapt: a temperature message

**Focus: testing conditions in order**

Type and run this program:

```python
temperature = 12

if temperature < 10:
    print("Cold")
elif temperature < 20:
    print("Mild")
else:
    print("Warm")
```

1. Test temperatures of `9`, `10`, `19` and `20`.
2. Add a comment explaining why 9 does not also produce `Mild`.
3. Adapt the program to give the four outcomes below. Use one `if/elif/else` chain.
4. Replace `temperature = 12` with a prompt for the temperature in degrees Celsius. Use `float()` so you can also enter values such as `9.5`.

| Temperature | Required message |
| --- | --- |
| Below 0 | `Freezing` |
| 0 up to, but not including, 10 | `Cold` |
| 10 up to, but not including, 20 | `Mild` |
| 20 or above | `Warm` |

**Check:** test `-1`, `0`, `9`, `10`, `19` and `20`. Each run should print exactly one message.

**Hint:** put the lowest temperature boundary first, then work upwards. Each later condition is reached only when the earlier conditions were false. Revisit [W3Schools: Python conditions](https://www.w3schools.com/python/python_conditions.asp) for the basic selection syntax.

### 6. Find the bug: an unreachable result

**Focus: a logic error rather than a syntax error**

This program runs, but does not follow the intended rule. The rule is:

- 70 or above: `High score`.
- 50 up to, but not including, 70: `Pass`.
- Below 50: `Not yet passed`.

These are example thresholds for this activity, not an assessment grading policy.

**Faulty code — reproduce it before making changes:**

```python
score = 75

if score >= 50:
    print("Pass")
elif score >= 70:
    print("High score")
else:
    print("Not yet passed")
```

1. Predict the output for 75, then run the program.
2. Explain why the high-score branch cannot be reached, even with a score of 100.
3. Fix the program while keeping one `if/elif/else` chain.
4. Test the repaired version against the table by changing `score = 75` for each test. Keep the fixed assignment in this exercise so you can focus on the bug.

| `score` | Expected output |
| --- | --- |
| `49` | `Not yet passed` |
| `50` | `Pass` |
| `69` | `Pass` |
| `70` | `High score` |
| `75` | `High score` |

**Hint:** trace the comparisons from top to bottom. Which condition accepts the widest range of scores? For 75, write down the result of the first comparison and identify what Python does next. Use [W3Schools: Python conditions](https://www.w3schools.com/python/python_conditions.asp) if you need to review how a decision controls the following block.

### 7. Code challenge: choose a ticket price

**Focus: combine comparisons and logical operators**

Write a program that uses an age and a membership status to choose exactly one ticket price. Apply the rules in this order:

1. An age below 0 or above 120 produces `Invalid age`.
2. Otherwise, anyone under 5 enters free, regardless of membership.
3. Otherwise, anyone under 18 **or** anyone who is a member pays £5.
4. Everyone else pays £10.

Start by asking the user two questions:

- Their age in whole years: convert the answer with `int()` and store it in `age`.
- Whether they are a member: ask for `yes` or `no`, then turn the answer into a Boolean called `is_member` using the pattern at the top of the worksheet.

Write your selection code after these prompts. Enter 16 and `no` for your first run.

Use one `if/elif/else` chain. Use `or` where either condition is sufficient. Print one of `Invalid age`, `Free entry`, `Ticket: £5` or `Ticket: £10`.

| `age` | `is_member` | Expected output |
| --- | --- | --- |
| `-1` | `True` | `Invalid age` |
| `4` | `False` | `Free entry` |
| `5` | `False` | `Ticket: £5` |
| `17` | `False` | `Ticket: £5` |
| `18` | `False` | `Ticket: £10` |
| `18` | `True` | `Ticket: £5` |
| `120` | `False` | `Ticket: £10` |
| `121` | `True` | `Invalid age` |

Before coding, write the decisions as a short list or sketch a flowchart. After testing, add a comment explaining why the invalid-age check must come before the price checks.

**Hints:**

- Check the types first: `age` should be an integer and `is_member` should be a Boolean. The string `"False"` is not the same as the Boolean `False`.
- An age can be invalid in two different ways. Write a complete comparison for each and join them with `or`.
- Use one `if`, two `elif` branches and a final `else`, following the rule order above.
- Once the free-entry branch has been ruled out, combine the under-18 comparison with the Boolean variable `is_member`.
- Add and test one branch at a time. Check the comparison and logical operator tables in [W3Schools: Python operators](https://www.w3schools.com/python/python_operators.asp).

## D. A different application: turtle graphics

### 8. Visual challenge: a battery indicator

**Focus: use a condition to change graphical output**

Turtle lets a Python program draw in a window. In this exercise, your selection code will choose a colour and label, then the supplied drawing commands will display them. You do not need to learn loops or write drawing functions.

**Before starting:** use a Python environment that supports turtle graphics, such as a suitably configured desktop installation. Turtle requires Tk support and a graphical display; some browser-based Python editors cannot open its window. Your lecturer can confirm the appropriate environment. Save your file as `battery_indicator.py`, not `turtle.py`.

### Step 1: reproduce the starter

```python
import turtle

battery = 65
colour = "grey"
message = "Battery level"

# PLACEHOLDER CODE HERE: replace this comment with your selection code.

turtle.setup(500, 300)
turtle.hideturtle()
turtle.penup()
turtle.goto(0, 30)
turtle.dot(100, colour)
turtle.goto(0, -60)
turtle.write(message, align="center", font=("Arial", 16, "normal"))
turtle.done()
```

Run it once. You should see a grey circle and the words `Battery level`. Close the drawing window before running the file again.

Now replace `battery = 65` with an `input()` prompt converted using `int()`. Enter the percentage in your editor’s console or terminal when prompted; the drawing window opens afterwards.

### What the unfamiliar code does

| Code | Purpose |
| --- | --- |
| `import turtle` | Makes the drawing commands available. |
| `turtle.setup(500, 300)` | Sets the window size in pixels. |
| `turtle.hideturtle()` | Hides the drawing cursor. |
| `turtle.penup()` | Stops movement from leaving connecting lines. |
| `turtle.goto(x, y)` | Moves to a position; `(0, 0)` is the centre and positive `y` is upwards. |
| `turtle.dot(100, colour)` | Draws a filled circle with a diameter of 100 pixels, using the chosen colour. |
| `turtle.write(...)` | Displays the message with the supplied alignment and font settings. |
| `turtle.done()` | Keeps the window open until you close it. |

### Step 2: add the decision

The line beginning `# PLACEHOLDER CODE HERE` is a **comment marking where you should write your code**. Python ignores it; it does not make a decision. Delete that comment line and write your `if/elif/else` chain in its place, between the initial variable assignments and `turtle.setup(500, 300)`.

In each branch, assign a value to **both** `colour` and `message`. Keep the supplied drawing commands after the complete chain, at the left margin. This draws the circle once, using the values chosen by your branch.

| Battery value | `colour` | `message` |
| --- | --- | --- |
| Below 0 or above 100 | `"grey"` | `"Invalid level"` |
| Otherwise, below 20 | `"red"` | `"Charge now"` |
| Otherwise, below 60 | `"orange"` | `"Battery okay"` |
| Otherwise | `"green"` | `"Battery good"` |

**Hints:**

- Check for an invalid battery value first, using `or` to combine the two ways it can be outside the range.
- Then test the remaining boundaries from lowest to highest, as in Exercise 5.
- Each branch needs two indented assignment statements. For example, the required values `"red"` and `"Charge now"` must be assigned to `colour` and `message`, respectively.
- Keep colour names and messages in quotation marks because they are strings. For assignment help, see [W3Schools: Python variables](https://www.w3schools.com/python/python_variables.asp).
- If the circle stays grey with the original label, check that you have replaced the placeholder comment and saved the file. If no window opens, try the text-only fallback below.

### Step 3: check the picture

Run the program again for each value: `-1`, `0`, `19`, `20`, `59`, `60`, `100` and `101`. Enter the number at the prompt and close the drawing window between runs. Check the label as well as the colour: the meaning should still be clear to someone who cannot distinguish the colours.

**Finished when:** every test displays the expected colour and label, and each run draws just one circle.

**If graphics are unavailable:** complete the same selection code in a normal Python file and use `print(colour, message)` after it. This lets you test the decision before trying the drawing version in a suitable environment.

## Optional extensions: for learners who already know Python

These extensions are **not beginner-level tasks**. Have a go if you already know Python and are ready to work with functions, automated checks and exception handling. Otherwise, keep practising Exercises 1–8.

### Extension 1. Turn the ticket rules into a tested function

**Builds on Exercise 7**

Write a function called `ticket_price(age, is_member)`. Assume `age` is an integer and `is_member` is a Boolean.

- Return `None` for an age outside 0–120.
- Return `0`, `5` or `10` for the valid ticket prices.
- Do not use `input()` in this extension. Call the function with literal test values, such as `ticket_price(18, True)`. Use `return` inside the function instead of printing the result.
- Write `assert` checks for all eight cases in Exercise 7, plus a member aged 4 and a non-member aged 0. `assert` checks that an expression is true and reports a failure otherwise.
- Add a short explanation of how the boundary tests could catch an incorrect `<` or `<=` operator.

**Hints:**

- Start with `def ticket_price(age, is_member):` and indent the selection code inside the function.
- Reuse the rule order from Exercise 7, replacing each output message with the required return value.
- A test can look like `assert ticket_price(18, True) == 5`. For an invalid age, check the result with `is None`.
- Review [W3Schools: Python functions](https://www.w3schools.com/python/python_functions.asp), especially parameters and return values.

**Finished when:** the function returns the correct values and every assertion passes.

### Extension 2. Make the ticket program cope with invalid input

**Builds on Exercise 7 or Extension 1**

Exercise 7 assumes the user enters a whole number and a yes/no answer. Now make it cope when they do not. Keep the prompts, but check the answers before applying the ticket rules. If you completed Extension 1, call your pricing function only after the inputs have passed those checks.

Requirements:

- Accept membership responses `yes` or `no`, ignoring surrounding spaces and capitalisation. Use `.strip().lower()` to normalise the response.
- Use `try/except ValueError` to handle age entries that cannot be converted to an integer.
- Give a clear error message for non-integer ages, ages outside 0–120, or unrecognised membership responses.
- Print a price only when both inputs are valid.
- Handle one customer per run; a loop is not required.

Test at least these entries:

| Age text | Membership text | Expected behaviour |
| --- | --- | --- |
| `18` | ` YES ` | £5 ticket |
| `18` | `no` | £10 ticket |
| `four` | `yes` | Explain that age must be a whole number; no price |
| `18.5` | `no` | Explain that age must be a whole number; no price |
| `121` | `yes` | Explain the valid age range; no price |
| `18` | `maybe` | Explain that the answer must be `yes` or `no`; no price |

**Hints:**

- Separate reading the input, checking it and selecting the price. Do not calculate a price until both inputs have passed their checks.
- Put the age conversion inside `try`; use `except ValueError` for text that `int()` cannot convert. Keep code that depends on a successful conversion out of the error branch.
- After normalising the membership text, check that it is `"yes"` or `"no"`. Only then create a Boolean such as `is_member = membership_text == "yes"`.
- Review [W3Schools: Python try/except](https://www.w3schools.com/python/python_try_except.asp) for handling conversion errors.

**Finished when:** invalid entries produce helpful messages rather than a traceback or an incorrect price.

## Reference links

- [Python documentation: `if` statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
- [Python documentation: Boolean operations](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)
- [Python documentation: turtle graphics](https://docs.python.org/3/library/turtle.html)
- [Python documentation: `input()`](https://docs.python.org/3/library/functions.html#input)
- [Python documentation: handling exceptions](https://docs.python.org/3/tutorial/errors.html#handling-exceptions)
- [W3Schools: Python conditions](https://www.w3schools.com/python/python_conditions.asp)
- [W3Schools: Python operators](https://www.w3schools.com/python/python_operators.asp)
