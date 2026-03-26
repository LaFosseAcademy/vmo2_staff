# OOP Python Challenges: Employee, Manager, and Developer

These object-oriented programming challenges will help you practice:

- creating classes
- inheritance
- parent and child classes
- shared class variables
- instance attributes
- instance methods
- static methods
- creating objects from multiple classes

You will build a small employee system with:

- `Employee` as the parent class
- `Manager` as a child class
- `Developer` as a child class

---

## Overview

You should end up with:

- **1 parent class**: `Employee`
- **2 child classes**: `Manager` and `Developer`

Each class should have a clear purpose, and you should create several instances to test your code.

---

## Challenge 1: Create the Parent Class

Create a class called `Employee`.

### Requirements

Add these **shared class variables**:

- `company_name` = `"TechStars"`
- `employee_count` = `0`
- `raise_rate` = `1.05`

Add an `__init__` method that stores:

- `name`
- `salary`
- `department`

Every time a new `Employee` (or child object) is created, increase `employee_count` by 1.

### Instance Methods

Create these methods:

1. `display_info()`
   - Returns a string with the employee's name, department, and salary

2. `apply_raise()`
   - Increases the employee's salary using the class `raise_rate`

### Static Method

Create a static method called `is_valid_salary(amount)` that:

- returns `True` if the salary is greater than 0
- returns `False` otherwise

### Test

Create at least **2 Employee objects** and:

- print their info
- test the salary validation static method
- print the total employee count

---

## Challenge 2: Create the Manager Child Class

Create a class called `Manager` that inherits from `Employee`.

### Additional Attribute

Managers should also have:

- `team_size`

### Shared Class Variable

Add a class variable:

- `raise_rate` = `1.10`

This means managers get a higher raise than regular employees.

### Instance Method

Create a method called `manage_team()` that returns a message like:

```python
"Alice manages a team of 8 people."
```

### Static Method

Create a static method called `manager_title()` that returns:

```python
"Management Staff"
```

### Test

Create at least **2 Manager objects** and:

- print their info
- call `manage_team()`
- apply a raise
- print the new salary

---

## Challenge 3: Create the Developer Child Class

Create a class called `Developer` that inherits from `Employee`.

### Additional Attributes

Developers should also have:

- `programming_language`
- `level` (for example: `"Junior"`, `"Mid"`, `"Senior"`)

### Shared Class Variable

Add a class variable:

- `raise_rate` = `1.15`

### Instance Method

Create a method called `write_code()` that returns a message like:

```python
"Ben is writing Python code."
```

### Static Method

Create a static method called `is_valid_level(level)` that returns `True` only if the level is one of:

- `"Junior"`
- `"Mid"`
- `"Senior"`

Otherwise it should return `False`.

### Test

Create at least **2 Developer objects** and:

- print their info
- call `write_code()`
- apply a raise
- print the new salary
- test the level validation static method

---

## Challenge 4: Create Instances of All Classes

Create the following objects:

### Employees
- one employee in HR
- one employee in Finance

### Managers
- one manager for Engineering
- one manager for Sales

### Developers
- one Python developer
- one JavaScript developer

Store them in a list.

Loop through the list and print each person's info.

At the end, print:

- the company name
- the total number of employees created

---

## Challenge 5: Compare Class Variables

Print the `raise_rate` for:

- `Employee`
- `Manager`
- `Developer`

Then create one object from each class and apply a raise to see the difference.

Example idea:

```python
print(Employee.raise_rate)
print(Manager.raise_rate)
print(Developer.raise_rate)
```

Then show the salary before and after the raise.

---

## Challenge 6: Use Static Methods Properly

Test all static methods directly from the class.

### Required tests

- `Employee.is_valid_salary(50000)`
- `Employee.is_valid_salary(-20)`
- `Manager.manager_title()`
- `Developer.is_valid_level("Senior")`
- `Developer.is_valid_level("Intern")`

Print the results.

---

## Challenge 7: Add Your Own Improvement

Choose one extra feature to add. For example:

- add an email attribute
- add a method that returns yearly bonus
- add a method to change department
- add a method to promote a developer from Junior to Mid
- add a method to increase a manager's team size

---

# Example Structure

This is one possible structure for your classes:

```python
class Employee:
    company_name = "TechStars"
    employee_count = 0
    raise_rate = 1.05

    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department
        Employee.employee_count += 1


class Manager(Employee):
    raise_rate = 1.10

    def __init__(self, name, salary, department, team_size):
        super().__init__(name, salary, department)
        self.team_size = team_size


class Developer(Employee):
    raise_rate = 1.15

    def __init__(self, name, salary, department, programming_language, level):
        super().__init__(name, salary, department)
        self.programming_language = programming_language
        self.level = level
```

You still need to add the required methods yourself.

---

# Final Practice Task

After building everything, write code that creates these objects:

```python
emp1 = Employee("Anna", 40000, "HR")
emp2 = Employee("Tom", 42000, "Finance")

mgr1 = Manager("Sarah", 60000, "Engineering", 10)
mgr2 = Manager("James", 58000, "Sales", 6)

dev1 = Developer("Mia", 50000, "Engineering", "Python", "Junior")
dev2 = Developer("Leo", 55000, "Engineering", "JavaScript", "Mid")
```

Then test:

- `display_info()`
- raises
- static methods
- total employee count

---

# Reflection Questions

When you finish, think about these:

1. Why is `Employee` a good parent class?
2. What do `Manager` and `Developer` inherit from `Employee`?
3. Why use a class variable like `employee_count` instead of an instance variable?
4. When is a static method useful?
5. Why might each child class have a different `raise_rate`?

---

Good luck — this is great practice for learning inheritance and class design in Python.

