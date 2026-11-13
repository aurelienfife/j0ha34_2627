# Bubble Sort

## Explanation

Bubble sort is a comparison-based sorting algorithm for a list.
Going through every element in the list, if they are in the correct order, leave them as-is. Otherwise swap them over.

Repeat overall process until no swaps occur.

## Pseudocode

```
numbers -> list of elements
flag -> boolean, set to true

repeat while flag is true
    set flag to false
    loop from second element to last element of numbers
        if current element is lower than previous element
            swap them
            set flag to true
        end if
    next 
next
```

## Python implementation

```python
```
