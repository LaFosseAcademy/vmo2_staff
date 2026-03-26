# Beginner Python Challenges — Solutions

These are example solutions for the beginner Python challenges file.  
There are often many correct ways to solve each problem.

---

## Challenge 1: Print a Greeting

```python
print("Hello, Python!")
```

**Stretch:**

```python
print("Hello, Python!")
print("My name is Alex")
```

---

## Challenge 2: Ask for a Name

```python
name = input("What is your name? ")
print("Hello,", name + "!")
```

**Alternative:**

```python
name = input("What is your name? ")
print(f"Hello, {name}!")
```

**Stretch:**

```python
name = input("What is your name? ")
print(f"Welcome to Python, {name}!")
```

---

## Challenge 3: Add Two Numbers

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

total = num1 + num2
print("Total:", total)
```

**Stretch:**

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Total:", num1 + num2)
print("Product:", num1 * num2)
```

---

## Challenge 4: Even or Odd

```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
```

---

## Challenge 5: Simple Password Check

```python
password = input("Enter password: ")

if password == "python123":
    print("Access granted")
else:
    print("Access denied")
```

**Stretch: 2 attempts**

```python
password = input("Enter password: ")

if password == "python123":
    print("Access granted")
else:
    password = input("Try again: ")
    if password == "python123":
        print("Access granted")
    else:
        print("Access denied")
```

---

## Challenge 6: Count from 1 to 10

```python
for number in range(1, 11):
    print(number)
```

**Stretch: even numbers only**

```python
for number in range(2, 11, 2):
    print(number)
```

---

## Challenge 7: Sum of 1 to N

```python
n = int(input("Enter a number: "))
total = 0

for number in range(1, n + 1):
    total += number

print("Sum:", total)
```

**Stretch: without a loop**

```python
n = int(input("Enter a number: "))
total = n * (n + 1) // 2
print("Sum:", total)
```

---

## Challenge 8: List of Favorite Foods

```python
foods = ["pizza", "tacos", "pasta"]

print(foods)
print("First:", foods[0])
print("Last:", foods[-1])
```

**Stretch: add a fourth food**

```python
foods = ["pizza", "tacos", "pasta"]
new_food = input("Add another food: ")
foods.append(new_food)

print(foods)
print("First:", foods[0])
print("Last:", foods[-1])
```

---

## Challenge 9: Count Vowels in a Word

```python
word = input("Enter a word: ")
count = 0

for letter in word:
    if letter in "aeiou":
        count += 1

print("Vowels:", count)
```

**Stretch: uppercase too**

```python
word = input("Enter a word: ").lower()
count = 0

for letter in word:
    if letter in "aeiou":
        count += 1

print("Vowels:", count)
```

---

## Challenge 10: Mini Number Guessing Game

```python
secret_number = 7
guess = int(input("Guess the number: "))

if guess < secret_number:
    print("Too low")
elif guess > secret_number:
    print("Too high")
else:
    print("Correct!")
```

**Stretch: keep guessing until correct**

```python
secret_number = 7

while True:
    guess = int(input("Guess the number: "))

    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Correct!")
        break
```

---

## Bonus Challenge: Age Group

```python
age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif age <= 19:
    print("Teenager")
else:
    print("Adult")
```

---

## Final Note

These solutions are written to be easy to read as a beginner.  
Once you're comfortable, try improving them by:

- using better variable names
- handling invalid input
- turning repeated logic into functions
- adding more test cases

Keep practicing — small programs are the best way to build confidence.

