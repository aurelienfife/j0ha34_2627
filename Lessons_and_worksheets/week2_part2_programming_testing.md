# J0HA 34 Computer Programming
# Part 2
# Trace Tables, Programming and Testing

## Learning Outcomes

By the end of Part 2, you will be able to:

- Use trace tables to analyse program execution.
- Follow how variables change during a program.
- Develop simple Python programs using variables and expressions.
- Test and debug simple solutions.

## 1. Understanding Trace Tables

A **trace table** records the values stored in variables as each statement is executed.

Trace tables help programmers:

- Predict outputs.
- Identify logic errors.
- Understand program behaviour.
- Test calculations.

Think of a trace table as a record of the computer's memory as the program runs.

## Worked Example

Consider the following code:

```python
price = 2.50
quantity = 4
total = price * quantity
```

| Statement Executed | price | quantity | total |
|-------------------|-------|----------|-------|
| Start | | | |
| price = 2.50 | 2.50 | | |
| quantity = 4 | 2.50 | 4 | |
| total = price * quantity | 2.50 | 4 | 10.00 |

### What Happened?

**Step 1:** `price` stores 2.50.

**Step 2:** `quantity` stores 4.

**Step 3:** Python calculates `2.50 * 4` and stores the result in `total`.

## Reassignment Example

```python
score = 10
score = score + 5
```

| Statement Executed | score |
|-------------------|-------|
| Start | |
| score = 10 | 10 |
| score = score + 5 | 15 |

The second statement means:

1. Take the current value of `score`.
2. Add 5.
3. Store the new value back into `score`.

## Trace Table Strategy

When completing a trace table:

1. Read one statement.
2. Update any variables affected by that statement.
3. Record the new values.
4. Move to the next statement.
5. Repeat until the program finishes.
6. Always use the most recent values.

**Tip:** Follow the code exactly as Python would execute it.

## Guided Trace Table Activity

```python
minutes = 135
hours = minutes // 60
remaining_minutes = minutes % 60
```

| Statement Executed | minutes | hours | remaining_minutes |
|-------------------|---------|-------|------------------|
| Start | | | |
| minutes = 135 | | | |
| hours = minutes // 60 | | | |
| remaining_minutes = minutes % 60 | | | |

### Analysis Questions

1. Which variable receives a value first?
2. Why must `minutes` be assigned before calculating `hours`?
3. What operation does `//` perform?
4. What operation does `%` perform?
5. What real-world problem is this program solving?

# Practical Programming Task

## Café Order Calculator (lecturer input)

### Before Coding

- Inputs?
- Process?
- Outputs?


```python
item_price = 2.75
quantity = 3

total_cost = item_price * quantity

print(total_cost)

payment = 10

change = payment - total_cost

print(change)
```

# Independent Programming Challenge

Choose ONE task.

## Option A: Travel Cost Calculator

Calculate the cost of a journey using:

- Cost per mile
- Distance travelled

## Option B: Time Converter

Convert minutes into:

- Hours
- Remaining minutes

## Option C: Average Mark Calculator

Calculate the average of three assessment marks.

### Planning Table

| Variable Name | Data Type | Purpose |
|--------------|-----------|---------|
| | | |
| | | |
| | | |
| | | |


# Testing Your Program

| Test Input | Expected Result | Actual Result | Pass/Fail |
|------------|----------------|---------------|-----------|
| | | | |
| | | | |
| | | | |


# Debugging Exercise

The following program contains an error.

```python
price = 2.75
quantity = "3"

total = price * quantity

print(total)
```

### Questions

1. Which variable has an unsuitable data type?
2. What error is likely to occur?
3. How would you correct the program?
4. Why is the corrected version more suitable?


# Final Reflection

1. How did trace tables help you understand program execution?
2. What was the most challenging concept today?
3. Which activity helped your understanding the most?
4. What is one thing you can now do that you could not do before this lesson?




<details>
<summary><strong>Answers: Guided Trace Table Activity</strong></summary>

Completed trace table:

| Statement Executed | minutes | hours | remaining_minutes |
|-------------------|---------|-------|------------------|
| Start | | | |
| minutes = 135 | 135 | | |
| hours = minutes // 60 | 135 | 2 | |
| remaining_minutes = minutes % 60 | 135 | 2 | 15 |

### Analysis Questions

1. `minutes` receives a value first.

2. `hours` depends on the value stored in `minutes`, so `minutes` must exist first.

3. `//` performs integer division.

4. `%` returns the remainder after division.

5. The program converts minutes into hours and minutes.

</details>

<details>
<summary><strong>Answers: Café Order Calculator</strong></summary>

### Inputs

- `item_price`
- `quantity`

### Processing

```python
total_cost = item_price * quantity
```

### Output

```python
print(total_cost)
```

### Evaluation Questions

1. Input variables: `item_price`, `quantity`

2. Result variable: `total_cost`

3. Floats are suitable because money may contain decimal values.

</details>

<details>
<summary><strong>Possible Answers: Planning Table (Average Mark Calculator)</strong></summary>

| Variable Name | Data Type | Purpose |
|--------------|-----------|---------|
| mark1 | Integer | First student mark |
| mark2 | Integer | Second student mark |
| mark3 | Integer | Third student mark |
| average | Float | Stores calculated average |

</details>

<details>
<summary><strong>Answers: Debugging Exercise</strong></summary>

### Question 1

The variable with the unsuitable data type is:

```python
quantity = "3"
```

### Question 2

A TypeError will occur because Python cannot multiply a float by a string in this context.

### Question 3

Correct version:

```python
price = 2.75
quantity = 3

total = price * quantity

print(total)
```

### Question 4

The corrected version is more suitable because `quantity` should be a number, not text.

</details>

<details>
<summary><strong>Example Reflection Answers</strong></summary>

### How did trace tables help?

They showed how variable values changed after each statement and made it easier to follow program execution.

### Most challenging concept?

Example answer: Understanding operator precedence.

### Which activity helped most?

Example answer: Completing the trace table because it showed how values change step by step.

### One thing I can do now?

Example answer: Create and test a simple Python program using variables and calculations.

</details>
