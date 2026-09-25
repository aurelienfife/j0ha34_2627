# Unit 4 (week 5): Iteration — practical exercises

**J0HA 34 Computer Programming - HNC Cybersecurity - September 2026**

**Harder mode at the end of handout (if you know the basics already)**

Start by reproducing the examples, then adapt them and have a go at the challenges. Keep the handout nearby. Use the hints if you get stuck.

## Before you start

Advice: a separate Python file for each exercise. You will use variables, `print()`, user input and some of the selection from Week 3.

Remember that `input()` returns strings (text). Use `int()` for a conversion to intgers count and `float()` for numbers with decimals. For example:

```python
repetitions = int(input("How many repetitions? "))
price = float(input("Enter a price: "))
```

Enter a valid number when asked. If you enter an invalid input, it will crash, but the extension activity tries to address this (we'll do it later for the Scripting Unit). For prices, enter `2.50`, without a currency sign.

Tip: predict the result before running each test. Each row in a test table is a separate run. Where a row contains several entries, type them one at a time at successive prompts. Record whether your actual result matches the expected result.

## A. `for` loops

### 1. Try the code an modify it

Type and run this code:

```python
for check in range(1, 4):
    print("Check number:", check)

print("All checks complete")
```

1. Check that it prints check numbers 1, 2 and 3, then the final message once.
2. Change the range so it prints check numbers 1 to 5, including 5.
3. Ask the user how many checks to run. Convert the answer to an integer called `checks`.
4. Adapt the range so the numbering begins at 1 and ends at the requested number.

| Requested checks | Expected result |
| --- | --- |
| 1 | Check number 1, then the final message |
| 3 | Check numbers 1, 2, 3, then the final message |
| 0 | Only the final message |

Add a comment explaining why the stop value in your range is one greater than the last number printed. Assume the user enters a non-negative integer.

**Hint:** `range()` excludes the stop value. For a reminder, see [W3Schools: for loops](https://www.w3schools.com/python/python_for_loops.asp).

### 2. Code challenge: count up, then count down

Write a program that asks for a positive whole number and stores it in `limit`.

- Use a `for` loop to print the numbers from 1 to `limit`, inclusive.
- Print `Counting down` after that loop.
- Use a second `for` loop to print from `limit` down to 1.
- Print `Finished` once at the end.

Put the two loops one after the other. Do not put one inside the other.

**Check:** entering 3 should produce 1, 2, 3, then `Counting down`, then 3, 2, 1, then `Finished`. Entering 1 should print 1 on each side of the countdown message.

**Hints:** use a negative step for the second loop. The stop value is excluded even when counting down. Revisit the `range()` examples in the handout.

**Note**: you can validate your input by ending the program if a negative value is entered. You can use the `exit()` function.

## B. Counting and accumulation

### 3. Try and mofidy:

Type and run this code demonstrating the use of an accumulator:

```python
total = 0.0

for item in range(3):
    price = float(input("Enter a price: "))
    total = total + price

print("Total:", total)
```

1. Enter 2.50, 3.00 and 1.50. The total should be 7.0.
2. Add a counter called `expensive_items`, starting at zero before the loop.
3. Inside the loop, use an `if` to increase the counter when the current price is strictly greater than £5.
4. After the loop, print the count as well as the total.

| Three prices | Expected total | Expected count above £5 |
| --- | --- | --- |
| 2.50, 3.00, 1.50 | 7.00 | 0 |
| 5.00, 5.50, 6.00 | 16.50 | 2 |
| 0, 0, 0 | 0.00 | 0 |

**Hints:** the total increases by the current price; the counter increases by 1. Use two indentation levels for an `if` inside a loop. See [W3Schools: Python operators](https://www.w3schools.com/python/python_operators.asp) for `+=` if you want to try the shorter update form.


### 4. Somehow cyber-related scenario ;) : summarise login outcomes

Imagine you are checking a small batch of simulated login results. Write a program that asks for exactly five outcomes, one at a time. For this activity, enter only `success` or `failure`.

- Start a failure counter at zero before the loop.
- Use a `for` loop to ask for five outcomes.
- Count each failure.
- After the loop, print the failure count.
- If there are three or more failures, also print `Review these login results`. Otherwise, print `No review flag for this batch`.

This is an example classroom rule for flagging a batch of results.

| Outcomes, entered in order | Failure count | Final message |
| --- | --- | --- |
| success, success, success, success, success | 0 | No review flag for this batch |
| failure, success, failure, success, success | 2 | No review flag for this batch |
| failure, success, failure, success, failure | 3 | Review these login results |

**Hints:**

- Use `outcome = input("Login outcome (success/failure): ")` to read each answer, then compare `outcome` with `"failure"`.
- For now, type `success` or `failure` exactly as shown: lowercase, with no spaces before or after the word. Python treats `"Failure"` and `"failure"` as different strings. We have not covered `strip()` or `lower()` yet, so you do not need them for this exercise. However, you can give them a try :)
- The failure check belongs inside the loop. The final review decision belongs after the loop, once all five answers have been counted.
- Start by getting the count right, then add the review message.
- Use [W3Schools: for loops](https://www.w3schools.com/python/python_for_loops.asp) and [Python conditions](https://www.w3schools.com/python/python_conditions.asp) if needed.

## C. `while` loops

### 5. Reproduce, then adapt: enter the password

Write a program that keeps asking for a password until the correct one is entered. Use the made-up password below for this classroom example; do not enter a real password. This demonstrates a loop, not a complete login system.

Type and run this code:

```python
expected_password = "python123"
password = input("Enter the password: ")

while password != expected_password:
    print("Incorrect password. Try again.")
    password = input("Enter the password: ")

print("Access granted")
```

The first prompt gives `password` a value before the condition is checked. The prompt inside the loop updates that value after a wrong answer. Once the two strings match, the condition becomes false and the program continues after the loop.

1. Enter `wrong`, then `python123`. Check that you see one incorrect-password message, followed by `Access granted`.
2. Run it again and enter `python123` straight away. The loop body should run zero times.
3. Try `Python123`, then `python123`. Explain why the capital letter makes a difference.
4. Adapt the program to count all attempts, including the successful one. Print the attempt count after access is granted.
5. Add a comment explaining why the second `input()` is needed. Compare this with Exercise 2: here, you do not know in advance how many repetitions will be needed.

**Check your adapted version:** entering the correct password straight away should give 1 attempt; `wrong`, then `python123` should give 2; `wrong`, `Python123`, then `python123` should give 3.

**Hints:**

- Keep the password as a string. You do not need `int()` or `float()` for this input.
- Compare the text exactly as entered. You do not need `strip()` or `lower()`; capital letters and spaces change the answer.
- The first input is already one attempt, so initialise your counter to 1 after that prompt. Increase it each time another password is entered inside the loop.
- Keep `Access granted` and the final count outside the loop. Do not print the entered password to trace the program; trace the attempt count instead.
- If you accidentally create an endless loop, use Stop in your editor or Ctrl+C in a terminal. See [W3Schools: while loops](https://www.w3schools.com/python/python_while_loops.asp).

### 6. Code challenge: keep a running total until zero

Ask the user for amounts until they enter 0. Accept positive or negative numeric amounts; 0 is the stop signal and must not count as an entry.

Your program should:

- Initialise `total` to 0.0 and `count` to 0 before the loop.
- Read the first amount using `float(input(...))` before the condition is checked.
- Use `while` to keep processing non-zero amounts.
- Add each amount to the total and increase the count.
- Read another amount before the body ends.
- Print the count and total after the loop.

| Inputs, in order | Expected count | Expected total |
| --- | --- | --- |
| 4, 6, 0 | 2 | 10 |
| 0 | 0 | 0 |
| 2.50, -1.00, 0 | 2 | 1.50 |

**Hints:**

- The condition should test whether the current amount is different from the sentinel.
- You need an input before the loop and another inside it. Without the second one, you will keep adding the same amount.
- Keep the final output outside the loop.
- Sketch the return arrow in a flowchart before coding if it helps. See [W3Schools: while loops](https://www.w3schools.com/python/python_while_loops.asp).

### 7. Find the bug: where did the total go?

This code runs, but the total is wrong. Reproduce it and enter 2, 3 and 4.

```python
for item in range(3):
    total = 0.0
    price = float(input("Enter a price: "))
    total = total + price

print("Total:", total)
```

1. Write down what it prints and what it should print.
2. Trace the value of `total` at the start and end of each iteration.
3. Fix the code so it adds all three prices.
4. Test 2, 3, 4 again: the total should be 9. Then test 0, 5, 0: the total should be 5.
5. Add a comment explaining which statement should run once and which should repeat.

**Hint:** the assignment to zero is valid Python. The problem is where it happens. Look back at the initialisation and update in Exercise 3.

## D. A different application: turtle graphics

### 8. Reproduce, then adapt: draw a regular polygon

Use a Python environment that supports turtle graphics and can open a drawing window. Save the file as `polygon_loop.py`, not `turtle.py`. If the window cannot open, ask for help with the environment and use the text-only fallback below.

Start by reproducing this square:

```python
import turtle

turtle.shape("turtle")
turtle.pensize(3)

for side in range(4):
    turtle.forward(80)
    turtle.right(90)

turtle.done()
```

Each iteration draws one side and turns ready for the next side. Four repetitions close the square. `forward(80)` draws 80 pixels; `right(90)` turns clockwise by 90 degrees. `done()` keeps the window open until you close it.

Now use this starter for a shape with a user-selected number of sides:

```python
import turtle

sides = int(input("Number of sides (3 to 8): "))
turtle.shape("turtle")
turtle.pensize(3)

# PLACEHOLDER CODE HERE: replace this comment with your decision and loop.

turtle.done()
```

The line beginning `# PLACEHOLDER CODE HERE` is a comment marking where to write your code. Delete that line and put your decision and loop in its place.

- If `sides` is below 3 or above 8, print `Choose between 3 and 8 sides` and do not draw a polygon.
- Otherwise, calculate `angle = 360 / sides` and use a `for` loop to draw that many sides.
- Inside the loop, move forward 80 pixels and turn right by `angle` degrees.

The turtle must turn through a full 360 degrees to return to its original direction. Dividing that turn equally between the sides gives the exterior turning angle. This is why a square uses 90 degrees and a triangle uses 120 degrees.

**Check:** 3 should draw a triangle; 4 a square; 6 a hexagon. Inputs 2 and 9 should print the message and draw no polygon. Close the window between runs and enter the next side count in the console.

**Hints:**

- Check the allowed range before calculating the angle or starting the loop.
- Put the loop inside the valid-input branch, with the drawing commands indented inside the loop.
- The stop value `sides` gives exactly that many repetitions when the range starts at zero.
- See [Python documentation: turtle graphics](https://docs.python.org/3/library/turtle.html) and [W3Schools: for loops](https://www.w3schools.com/python/python_for_loops.asp).

**Text-only fallback:** keep the input, decision and loop, but remove the turtle commands. Inside the loop, print the side number and the calculated turning angle. For 3 sides, you should see three lines with a turn of 120 degrees.



## For the Brave (or non-beginners) 

These introduce functions, lists, automated checks and exception handling. If those are new to you, keep practising the core exercises first.

### Extension 1. Handle mistyped readings without losing the total

Extend Exercise 6 so the user can enter `q` to finish. Zero is now an ordinary reading and must be counted. Accept positive, negative and zero numeric readings; ignore surrounding spaces and accept uppercase `Q`.

- Check for the quit command before converting the input.
- Use `try/except ValueError` to catch text such as `hello` that cannot be converted with `float()`.
- Print a helpful message for an invalid entry and ask again.
- Do not add rejected entries to the total or count them.
- At the end, print count and total. Print the mean only if at least one reading was accepted; otherwise print `No readings entered`.

| Inputs | Expected result |
| --- | --- |
| 2, hello, 4, q | Reject hello; count 2, total 6, mean 3 |
| 0, q | Count 1, total 0, mean 0 |
| q | Count 0, total 0, No readings entered |
| -2, 2, Q | Count 2, total 0, mean 0 |

**Hints:** keep the running values outside the loop. Place updates only after successful conversion, and make sure every path through the loop reaches another input or exits. See [W3Schools: try/except](https://www.w3schools.com/python/python_try_except.asp).


### Extension 2. Write and test a readings summary - requires knowledge of functions

Write `summarise(readings)`, accepting a list of numbers. Use a loop to calculate the count and total, then return `(count, total, mean)`.

- Do not use `sum()` or `len()` to do the counting and accumulation for you.
- For an empty list, return `(0, 0, None)` because there is no mean.
- Keep input and printing outside the function.
- Write assertions for `[2, 4, 6]`, `[0]`, `[-2, 2]` and `[]`.

Expected results are `(3, 12, 4)`, `(1, 0, 0)`, `(2, 0, 0)` and `(0, 0, None)` respectively.

**Hints:** initialise before the loop, update for every reading, and calculate the mean afterwards. Check for zero count before dividing. An assertion can look like `assert summarise([2, 4, 6]) == (3, 12, 4)`. See [W3Schools: functions](https://www.w3schools.com/python/python_functions.asp).

#### What is an assertion?

An assertion is a check you write in code: “I expect this condition to be true.” Instead of printing a result and checking it yourself, you let Python compare the actual result with the expected one.

Once you have written `summarise`, put this test below the function definition, outside its indented body:

```python
result = summarise([2, 4, 6])
assert result == (3, 12, 4), "Check the count, total and mean"
print("Test passed")
```

Here, we expect three readings, a total of 12 and a mean of 4. The `==` comparison produces a Boolean, just like the conditions we used last week.

- If the comparison is true, the assertion produces no output and Python carries on to `print("Test passed")`.
- If it is false, Python raises an `AssertionError` with the message after the comma. Unless that error is handled, the program stops there. Use the failure to investigate your calculation.

This is a first step towards **unit testing**: checking a small part of a program, such as one function, independently. Each test supplies known input and checks the expected output. Your four test cases check different situations, including an empty list. Passing them shows that those cases work; it does not prove the function is correct for every possible input.

Have a look at [W3Schools: Python assert, with examples you can try](https://www.w3schools.com/python/ref_keyword_assert.asp). For a later look at organising several tests and reporting their results, see [Python's unittest tutorial: basic example](https://docs.python.org/3/library/unittest.html#basic-example). You do not need to use the `unittest` framework for this exercise.

Use assertions here to check your code. Keep the user-input checks from Extension 1 as normal conditions and exception handling: assertions can be disabled when Python runs with optimisation.

