# Intermediate Python Challenges (Lists, Tuples, Dictionaries, Functions)

These challenges are slightly more advanced and focus on core Python data structures and functions.

---

## Challenge 1: List Statistics

Write a function that takes a list of numbers and returns:

- the sum
- the average
- the maximum value
- the minimum value

Example:

```python
numbers = [3, 7, 2, 9]

# Expected output:
# (21, 5.25, 9, 2)
```

---

## Challenge 2: Remove Duplicates

Write a function that takes a list and returns a new list with duplicates removed, preserving order.

Example:

```python
[1, 2, 2, 3, 1] → [1, 2, 3]
```

---

## Challenge 3: Tuple Unpacking

You are given a list of tuples:

```python
people = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]
```

Write a function that:

- prints each name and age
- returns the average age

---

## Challenge 4: Dictionary Word Count

Write a function that takes a sentence and returns a dictionary where:

- keys = words
- values = number of times each word appears

Example:

```python
"hello world hello"

# Output:
{"hello": 2, "world": 1}
```

---

## Challenge 5: Student Grades

Create a dictionary where:

- keys = student names
- values = list of their grades

Write a function that:

- returns the average grade for each student
- returns the student with the highest average

---

## Challenge 6: Function with *args

Write a function that takes any number of numbers using *args and returns:

- the sum of the numbers
- how many numbers were passed

Example:

```python
my_func(1, 2, 3, 4)

# Output:
# (10, 4)
```

---

## Challenge 7: Merge Dictionaries

Write a function that takes two dictionaries and merges them.

If a key exists in both, add the values together.

Example:

```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

# Output:
{"a": 1, "b": 5, "c": 4}
```

---

## Challenge 8: Filter Even Numbers

Write a function that:

- takes a list of numbers
- returns a new list containing only even numbers

Try solving this:

- first using a loop
- then using list comprehension

---

## Challenge 9: Inventory System

Create a dictionary representing an inventory:

```python
inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 8
}
```

Write functions to:

1. Add stock
2. Remove stock
3. Check if an item is in stock

---

## Challenge 10: Flexible Calculator

Write a function that:

- takes an operation ("add", "multiply")
- takes any number of values (*args)
- performs the operation

Example:

```python
calc("add", 1, 2, 3) → 6
calc("multiply", 2, 3, 4) → 24
```

---

## Bonus Challenge: Nested Data

You are given:

```python
students = {
    "Alice": {"math": 80, "english": 90},
    "Bob": {"math": 70, "english": 60}
}
```

Write a function that:

- calculates each student's average
- returns the top student

---

## Reflection

- Which data structure felt most natural?
- When would you use a tuple vs list?
- What did *args allow you to do?

Keep building — these patterns show up everywhere in real Python code!

