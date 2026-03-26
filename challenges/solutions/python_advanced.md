# Intermediate Python Challenges — Solutions

These are example solutions for the intermediate Python challenges.
There are often several correct ways to solve each one.

---

## Challenge 1: List Statistics

```python
def list_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return total, average, maximum, minimum


numbers = [3, 7, 2, 9]
print(list_stats(numbers))
```

---

## Challenge 2: Remove Duplicates

```python
def remove_duplicates(items):
    result = []

    for item in items:
        if item not in result:
            result.append(item)

    return result


print(remove_duplicates([1, 2, 2, 3, 1]))
```

---

## Challenge 3: Tuple Unpacking

```python
def show_people(people):
    total_age = 0

    for name, age in people:
        print(f"{name} is {age} years old")
        total_age += age

    return total_age / len(people)


people = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]
print("Average age:", show_people(people))
```

---

## Challenge 4: Dictionary Word Count

```python
def word_count(sentence):
    counts = {}

    for word in sentence.split():
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


print(word_count("hello world hello"))
```

---

## Challenge 5: Student Grades

```python
def student_averages(grades):
    averages = {}

    for student, scores in grades.items():
        averages[student] = sum(scores) / len(scores)

    top_student = max(averages, key=averages.get)
    return averages, top_student


grades = {
    "Alice": [80, 90, 85],
    "Bob": [70, 75, 72],
    "Charlie": [95, 88, 91]
}

averages, top_student = student_averages(grades)
print("Averages:", averages)
print("Top student:", top_student)
```

---

## Challenge 6: Function with *args

```python
def my_func(*args):
    return sum(args), len(args)


print(my_func(1, 2, 3, 4))
```

---

## Challenge 7: Merge Dictionaries

```python
def merge_dicts(d1, d2):
    result = d1.copy()

    for key, value in d2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value

    return result


d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
print(merge_dicts(d1, d2))
```

---

## Challenge 8: Filter Even Numbers

### Using a loop

```python
def even_numbers_loop(numbers):
    result = []

    for number in numbers:
        if number % 2 == 0:
            result.append(number)

    return result


print(even_numbers_loop([1, 2, 3, 4, 5, 6]))
```

### Using list comprehension

```python
def even_numbers_comprehension(numbers):
    return [number for number in numbers if number % 2 == 0]


print(even_numbers_comprehension([1, 2, 3, 4, 5, 6]))
```

---

## Challenge 9: Inventory System

```python
def add_stock(inventory, item, amount):
    if item in inventory:
        inventory[item] += amount
    else:
        inventory[item] = amount


def remove_stock(inventory, item, amount):
    if item in inventory:
        inventory[item] -= amount
        if inventory[item] < 0:
            inventory[item] = 0


def in_stock(inventory, item):
    return item in inventory and inventory[item] > 0


inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 8
}

add_stock(inventory, "banana", 3)
remove_stock(inventory, "apple", 4)

print(inventory)
print("Banana in stock?", in_stock(inventory, "banana"))
print("Grape in stock?", in_stock(inventory, "grape"))
```

---

## Challenge 10: Flexible Calculator

```python
def calc(operation, *args):
    if operation == "add":
        return sum(args)

    elif operation == "multiply":
        result = 1
        for number in args:
            result *= number
        return result

    else:
        return "Invalid operation"


print(calc("add", 1, 2, 3))
print(calc("multiply", 2, 3, 4))
```

---

## Bonus Challenge: Nested Data

```python
def top_student(students):
    averages = {}

    for student, subjects in students.items():
        scores = subjects.values()
        averages[student] = sum(scores) / len(scores)

    best_student = max(averages, key=averages.get)
    return averages, best_student


students = {
    "Alice": {"math": 80, "english": 90},
    "Bob": {"math": 70, "english": 60}
}

averages, best_student = top_student(students)
print("Averages:", averages)
print("Top student:", best_student)
```

---

## Extra Practice Ideas

Once you understand these solutions, try improving them by:

- handling bad input
- adding comments
- returning clearer error messages
- splitting larger tasks into smaller helper functions
- writing your own test cases

Nice work — these are very useful Python patterns to know.

