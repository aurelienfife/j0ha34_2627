# Lists, strings and dictionaries — Exercise sheet

**J0HA34 Computer Programming | SCQF Level 7 | HNC Cybersecurity**

Note: OpenAI/Codex were used to expand explanations and format the document in markdown, based on existing exercises from the 25/26 sessions.

**The optional extensions at the end go beyond beginner level. They're for those who have studied Python before, so don't worry if you're not ready for them yet.**

**LESSON** = reproduce the code, run it and examine what happens. **TRY** = attempt the task without a supplied solution. Use the theory handout and hints when you need them.

Use a separate file for each activity. `input()` returns a string: keep it as text for names and programme titles; convert it only when you need a number. For the name tasks, “second name” means surname. Use made-up names if you prefer.

## A. LESSON — Days of the week by index

```python
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print(days[2])  # Tuesday
```

1. Reproduce and run the code. Explain why index `2` gives Tuesday.
2. Add statements to print Sunday and Saturday using their positive indices.
3. Add `print(days[-1])` and `print(len(days))`. What does each show?
4. Add this loop and check that all seven days appear in order:

```python
for day in days:
    print(day)
```

**Hint:** The first item has index zero. The loop variable `day` receives each string in turn. See [W3Schools: lists](https://www.w3schools.com/python/python_lists.asp).

## B. TRY — TV programmes list

Ask the user for three TV programme titles, store them in a list called `programmes`, then use a `for` loop to display all three, one per line.

Start by collecting three inputs in separate variables and putting those variables into a list. Once that works, change the input stage to use an empty list, a loop that runs three times and `.append()`.

Try three different titles, then try entering the same title twice. Your list should keep all three entries in the order entered, including duplicates.

**Hint:** Create the empty list before the input loop. Add one title on each repetition. Use a separate loop afterwards to display the completed list. See [W3Schools: adding list items](https://www.w3schools.com/python/python_lists_add.asp).

## C. LESSON — Methods return new text

```python
course = "Cybersecurity"
print(course.upper())
print(course)
course = course.lower()
print(course)
```

Run the code. You should see `CYBERSECURITY`, `Cybersecurity` and `cybersecurity`.

Add a comment explaining why the second line of output still has a capital C. Notice the difference between displaying a changed version and assigning that version to a variable.

## D. TRY — First names in uppercase and lowercase

1. Ask for a first name with `input()` and store it in `first_name`.
2. Display an uppercase version.
3. Display a lowercase version.
4. Display `first_name` itself and check that your original input is still there.

Try `aLeX`: the converted versions should be `ALEX` and `alex`.

**Hint:** Use `.upper()` and `.lower()` with parentheses. See [W3Schools: string methods](https://www.w3schools.com/python/python_strings_methods.asp).

## E. TRY — How many letters? What comes first?

Ask for a first name. Use `len()` to count its characters, store the result in `name_length` and display it with a clear label. Then display the first character.

Use an `if/else` so an empty input displays `Please enter a name` instead of trying to read a character that does not exist.

| Input | Length | First character |
| --- | --- | --- |
| Sam | 3 | S |
| Jo | 2 | J |
| A | 1 | A |
| Empty input | 0 | Display the message instead |

For names containing only letters, the character count is the letter count. Try `Anne-Marie` too: its length is 10 because the hyphen counts.

**Hint:** Use index `0` only after checking that the string is not empty. See [W3Schools: strings](https://www.w3schools.com/python/python_strings.asp).

## F. TRY — First initial and last letter

Ask separately for a first name and a surname. Display the first character of the first name joined to the last character of the surname, with no space between them. Keep the entered case.

For `Sam` and `Jones`, the result should be `Ss`. For `A` and `B`, it should be `AB`.

If either input is empty, display a helpful message instead.

**Hint:** `[-1]` selects the last character. Use `+` to join the two characters. You can check both inputs with `and` before indexing them.

## G. TRY — Username builder

Create a simple username generator for a fictional college account system:

1. Ask separately for a first name and a surname.
2. Check that neither is empty.
3. Convert both to lowercase and build a username in the form `<first initial><surname>`.
4. Store the result in `username` and display it.

`Alex` and `Smith` should produce `asmith`; `SAM` and `JONES` should produce `sjones`. If either input is empty, show a message and do not build a username. Use names without spaces or punctuation for this first version.

**Hint:** You have already used all the operations you need. This is a naming rule for practice; two people can produce the same username. Resolving that is an optional extension below.

## H. TRY — Find the bug

This code is meant to display the first programme in uppercase. It contains two mistakes:

```python
programmes = ["Doctor Who", "The Traitors", "Blue Planet"]
first_programme = programmes[1]
first_programme.upper()
print(first_programme)
```

Run it and compare the output with the intended result, `DOCTOR WHO`. Fix both mistakes, then add a comment explaining each correction.

**Hint:** Check the index first. Then consider what happens to the string returned by `.upper()`.

## I. LESSON — A dictionary of counts

```python
counts = {"yes": 0, "no": 0}
answer = input("Enter yes or no: ").lower()

if answer in counts:
    counts[answer] = counts[answer] + 1
else:
    print("Answer not recognised")

for answer in counts:
    print(answer, counts[answer])
```

1. Reproduce the code and run it with `yes`, `NO` and `maybe` on separate runs.
2. Check that a recognised answer increases only its matching count.
3. Explain why `maybe` does not cause a missing-key error.

Each run starts the counts at zero. This version records one answer per run.

**Hint:** `in` checks dictionary keys. `counts[answer]` uses the value of `answer` as the key. See [W3Schools: dictionaries](https://www.w3schools.com/python/python_dictionaries.asp).

## J. TRY — Counting vowels

Ask the user for their full name in one input. Count how many times each vowel occurs, using a dictionary called `vowels`.

- Start with the keys `"a"`, `"e"`, `"i"`, `"o"` and `"u"`, each with a count of zero.
- Convert the entered name to lowercase so capital and lowercase vowels count together.
- Use a `for` loop to examine each character.
- If the character is a key in your dictionary, increase that count by one.
- After the loop, display all five vowels and their counts, including zeros.

For this task, count only those five unaccented vowels. Ignore spaces, punctuation and other characters.

| Input | a | e | i | o | u |
| --- | --- | --- | --- | --- | --- |
| Anna Bell | 2 | 1 | 0 | 0 | 0 |
| ALEX | 1 | 1 | 0 | 0 | 0 |
| Jo Li | 0 | 0 | 1 | 1 | 0 |
| Empty input | 0 | 0 | 0 | 0 | 0 |

**Hints:**

- Keep the dictionary creation before the character loop so you do not reset the counts.
- The dictionary example above updates one key. Here, the current character tells you which key to update.
- Check membership before reading a count: most characters in a name will not be keys.
- Display the results after counting has finished, using a separate loop over the dictionary.



---


## For the Brave

These are optional. They combine several ideas and ask you to make more decisions about how your program should behave.

### Extension 1. Account names without duplicates

Turn your username builder into a function called `make_username(first_name, surname, existing)` that returns an unused username.

Use `existing = ["asmith", "asmith2"]`. For `Alex` and `Smith`, your function should return `asmith3`. If `sjones` is unused, `Sam` and `Jones` should return `sjones` without a number.

Remove surrounding whitespace from both names using `.strip()`, then convert them to lowercase. If either cleaned name is empty, return `None`. The calling code should display a message for `None`; otherwise it should append the returned username to `existing`. This reserves it for the next call.

**Hints:** `.strip()` returns text without whitespace at either end. Keep the original base username in its own variable. Use a `while` loop to check candidates with `in`, starting suffixes at 2. Convert a numeric suffix with `str()` before joining it to text. See [W3Schools: while loops](https://www.w3schools.com/python/python_while_loops.asp).

Check two consecutive requests for `Alex Smith`: after the first result is added, the next should be `asmith4`.

### Extension 2. Summarise simulated failed logins

Use this list of account names, where each entry represents one failed login:

```python
failed_logins = ["sam", "alex", "sam", "jo", "alex", "sam"]
```

Write a function called `count_failures(accounts)` that returns a dictionary containing the number of failures for each account. It should work with account names not known in advance and return an empty dictionary for an empty list.

In the calling code, display each account and its count. Flag accounts with three or more failures for review. For the supplied list, Sam has 3, Alex has 2 and Jo has 1; only Sam should be flagged. This is simulated data and a classroom review rule.

**Hint:** Begin with an empty dictionary. When a name first appears, give it a count of zero before adding one. For a returning name, increase its existing count. Keep input and printing outside the function.

Add assertions for the supplied list and an empty list. An assertion checks a condition: if it is false, Python raises `AssertionError`; if true, execution continues silently. These checks are a small step towards unit testing, where you compare a function's result with an expected result. See [W3Schools: assert examples](https://www.w3schools.com/python/ref_keyword_assert.asp).
