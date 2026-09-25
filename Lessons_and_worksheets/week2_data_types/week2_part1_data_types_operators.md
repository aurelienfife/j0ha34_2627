# J0HA 34 Computer Programming
# Week 2: Variables, Data Types and Simple Calculations in Python

# Learning Outcomes

By the end of this lesson, you will be able to:

- Explain the purpose of variables within a Python program.
- Distinguish between integers, floating-point numbers, strings and Boolean values.
- Use assignment statements to store, update and retrieve values.
- Apply arithmetic, comparison and logical operators correctly.
- Predict the outcome of expressions using operator precedence rules.
- Use trace tables to analyse how values change during program execution.
- Design, test and refine a simple Python program that solves a practical problem.


# Part 1
# Variables, Data Types, Operators and Expressions

## 1. Variables

A **variable** is a named reference to a value stored in memory.

### Example

```python
quantity = 3
```

The variable `quantity` stores the value `3`.

Variables can be updated during program execution.

```python
quantity = 3
quantity = 5
```

The value stored in `quantity` is now `5`.

### Think About It

1. Why is `quantity` a better variable name than `x`?
2. What would happen if a program used fixed values instead of variables?
3. Why might a programmer need to change a variable's value?


## 2. Data Types

Different kinds of data require different data types.

| Data Type | Purpose | Example |
|------------|---------|---------|
| Integer (`int`) | Whole numbers | 42 |
| Float (`float`) | Decimal values | 2.75 |
| String (`str`) | Text | "Python" |
| Boolean (`bool`) | True/False values | True |

### Activity 1: Selecting Data Types

What data type is suitable for the following? Why?
- Number of students in a class
- Average mark
- Student name
- Assessment completed


## 3. Arithmetic Operators

Arithmetic operators perform calculations.

| Operator | Meaning |
|-----------|---------|
| + | Addition |
| - | Subtraction |
| * | Multiplication |
| / | Division |
| // | Integer Division |
| % | Modulus (Remainder) |
| ** | Power |

### Practice

What do you think the output of the following will be in Python? 
(Do not write code)

```python
12 + 8
```

Answer: __________

```python
25 - 11
```

Answer: __________

```python
7 * 9
```

Answer: __________

```python
15 % 4
```

Answer: __________

```python
2 ** 5
```

Answer: __________

## 4. Comparison Operators

Comparison operators compare values and produce either `True` or `False`.

| Operator | Meaning |
|-----------|---------|
| == | Equal to |
| != | Not equal to |
| > | Greater than |
| < | Less than |
| >= | Greater than or equal to |
| <= | Less than or equal to |

### Examples

```python
10 > 5
```

Result: `True`

```python
8 == 3
```

Result: `False`

## 5. Logical Operators

Logical operators combine conditions and produce a Boolean result.

| Operator | Meaning |
|-----------|---------|
| and | Both conditions must be true |
| or | At least one condition must be true |
| not | Reverses a condition |


# Truth Tables

## AND Truth Table

| Condition A | Condition B | A and B |
|------------|------------|---------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

### Remember

Both conditions must be true.

```python
age >= 16 and age < 19
```

## OR Truth Table

| Condition A | Condition B | A or B |
|------------|------------|--------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

### Remember

Only one condition needs to be true.

```python
day == "Saturday" or day == "Sunday"
```

## NOT Truth Table

| Condition A | not A |
|------------|-------|
| True | False |
| False | True |

### Example

```python
not (5 > 2)
```

Result: `False`

## Worked Example

Consider the expression:

```python
5 > 3 and 10 < 12
```

Step 1: Evaluate each comparison.

```python
5 > 3
```

Result: `True`

```python
10 < 12
```

Result: `True`

Step 2: Apply the AND truth table.

| Condition A | Condition B | Result |
|------------|------------|--------|
| True | True | True |

Final answer:

```python
True
```

### Activity 2: Logical Operators

| Expression | Result | Explanation |
|------------|---------|-------------|
| True and False | | |
| True or False | | |
| False or False | | |
| not False | | |
| 7 > 3 and 2 > 5 | | |
| 7 > 3 or 2 > 5 | | |

### Challenge

Determine the result of (no code):

```python
(8 > 4 and 3 == 3) or (10 < 5)
```

## 6. Expressions and Calculations

An **expression** combines values, variables and operators to produce a result.

```python
price = 2.75
quantity = 4

total = price * quantity
```

### Questions

1. What value will be stored in `total`?

_____________________________________________________________

2. Which data types are used?

_____________________________________________________________

3. Why is multiplication the correct operator?

_____________________________________________________________

---

## 7. Operator Precedence

Python follows rules that determine the order in which operations are performed.

### Example 1

```python
2 + 3 * 4
```

Answer: **14**

### Example 2

```python
(2 + 3) * 4
```

Answer: **20**

### Practice

| Expression | Predicted Result | Explanation |
|------------|-----------------|-------------|
| 4 + 2 * 5 | | |
| (4 + 2) * 5 | | |
| 20 / 4 + 3 | | |

### Reflection

Why can brackets improve the readability and reliability of a program?

_____________________________________________________________

_____________________________________________________________


# Review 1
1. What is a variable?
2. What is the difference between an integer and a float?
3. What is the purpose of a Boolean value?
4. When would you use the `and` operator?
5. When would you use the `or` operator?
6. Why do programmers use brackets in expressions?



<details>
<summary><strong>Answers: Think About It</strong></summary>

1. `quantity` clearly describes what the variable stores, making the code easier to understand and maintain.

2. Using fixed values would make programs difficult to update because every value would need to be changed manually.

3. Programs often need to update information while running, such as scores, quantities, balances or user input.

</details>

<details>
<summary><strong>Answers: Activity 1 - Selecting Data Types</strong></summary>

| Information | Suitable Data Type | Reason |
|------------|-------------------|---------|
| Number of students in a class | Integer (`int`) | Student counts are whole numbers. |
| Average mark | Float (`float`) | Average values may contain decimals. |
| Student name | String (`str`) | Names are text. |
| Assessment completed | Boolean (`bool`) | The answer is either True or False. |

</details>

<details>
<summary><strong>Answers: Arithmetic Operators Practice</strong></summary>

```python
12 + 8
```

Answer: **20**

```python
25 - 11
```

Answer: **14**

```python
7 * 9
```

Answer: **63**

```python
15 % 4
```

Answer: **3**

```python
2 ** 5
```

Answer: **32**

</details>

<details>
<summary><strong>Answers: Activity 2 - Logical Operators</strong></summary>

| Expression | Result | Explanation |
|------------|---------|-------------|
| True and False | False | Both conditions must be True for AND to return True. |
| True or False | True | At least one condition is True. |
| False or False | False | Neither condition is True. |
| not False | True | NOT reverses the value. |
| 7 > 3 and 2 > 5 | False | True and False gives False. |
| 7 > 3 or 2 > 5 | True | True or False gives True. |

</details>

<details>
<summary><strong>Answers: Challenge</strong></summary>

Expression:

```python
(8 > 4 and 3 == 3) or (10 < 5)
```

Step 1:

```python
8 > 4
```

Result: True

```python
3 == 3
```

Result: True

```python
10 < 5
```

Result: False

Step 2:

```python
True and True
```

Result: True

Step 3:

```python
True or False
```

Result: True

Final Answer:

```python
True
```

</details>

<details>
<summary><strong>Answers: Expressions and Calculations</strong></summary>

### Question 1

Value stored in `total`:

```python
2.75 * 4 = 11.0
```

Answer: **11.0**

### Question 2

Data types used:

- `price` → Float
- `quantity` → Integer
- `total` → Float



</details>

<details>
<summary><strong>Answers: Operator Precedence Practice</strong></summary>

| Expression | Predicted Result | Explanation |
|------------|-----------------|-------------|
| 4 + 2 * 5 | 14 | Multiplication occurs before addition. |
| (4 + 2) * 5 | 30 | Brackets are evaluated first. |
| 20 / 4 + 3 | 8.0 | Division occurs before addition. |

### Reflection

Brackets make the intended order of operations clear and reduce the risk of mistakes.

</details>

<details>
<summary><strong>Answers: End of Part 1 Review</strong></summary>

1. A variable is a named location used to store a value.

2. An integer stores whole numbers, while a float stores decimal numbers.

3. A Boolean stores either `True` or `False`.

4. The `and` operator is used when both conditions must be true.

5. The `or` operator is used when at least one condition must be true.

6. Brackets make expressions easier to read and control the order of operations.

</details>