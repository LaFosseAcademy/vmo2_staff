## DataTypes

### Integers
```python
# Integer examples
age = 21
temperature = -5
score = 100

print(age)
```

### Floating Point Numbers
```python
# Float examples
price = 9.99
height = 1.75
pi = 3.14159

print(price)
```

### Strings
```python
# String examples
name = "Alice"
message = "Hello, world!"

print(name)
```

### Booleans
```python
# Boolean examples
is_logged_in = True
has_permission = False

print(is_logged_in)
```

## Operators

### Arithmetic Operators
```python
102 + 37 #Add two numbers with +
102 - 37 # Subtract a number with -
4 * 6 # Multiply two numbers with *
22 / 7 # Divide a number by another with /
22 % 7 # Returns 1 # Get the remainder  after division with %
```

### Assignment Operators
```python
a = 5 # Assign a value to a
x = [4,2,3]
x[0] = 1 # Change the value of an item in a list, indexed at position 0
```

### Numeric Comparison Operators
```python
3 == 3 # Test for equality with ==
3 != 3 # Test for inequality with !=
3 > 1 # Test greater than with >
3 >= 3 # Test greater than or equal to with >=
3 < 4 # Test less than with <
3 <= 4 # Test less than or equal to with <=
```

### Logical Operators
```python
not (2 == 2) # Logical NOT with not
(1 != 1) and (1 < 1) # Logical AND with and
(1 >= 1) or (1 < 1) # Logical OR with or
```

## Lists
```python 
# Create lists with [], elements separated by commas
# Define the list 
x = ['a', 'b', 'c', 'd', 'e']

# Select the 0th element in the list
x[0] # 'a'

# Select the last element in the list
x[-1] # 'e'
```

## Dictionaries
```python
# Create a dictionary with {}
a = {'a': 1, 'b': 4, 'c': 9}

# Get a value from a dictionary by specifying the key
a['a'] # 1
```

## Control Flow
```python
# Store the internet speed value (in Mbps, for example)
internet_speed = 100

# Check if the speed is greater than 500
if internet_speed > 500:
    # If true, print that the internet is very fast
    print("very fast internet")

# If the first condition is false, check if speed is greater than 300
elif internet_speed > 300:
    # If true, print that the internet is fast
    print("fast internet")

# If the previous conditions are false, check if speed is greater than 50
elif internet_speed > 50:
    # If true, print that the internet is quick
    print("quick internet")

# If none of the above conditions are true
else:
    # Print that the internet is slow
    print("slow internet")
```

## Loops
```python
# Create a list of fruits
fruits = ["apple", "banana", "orange", "grape"]

# Loop through each item in the list
for fruit in fruits:
    # "fruit" represents the current item from the list during each loop

    # Print the current fruit
    print("Current fruit:", fruit)
```

## Basic Function
```python
# Define a function called greet
def greet():
    # This line runs when the function is called
    print("Hello!")

# Call the function
greet()
```

- def → keyword used to define a function
- greet → the name of the function
- () → parentheses used to pass inputs (parameters) if needed
- : → starts the function block
- The indented code below it is the function body
- greet() → calls the function, making it run


# Beginner Python Challenges 🐍

---

## 1. Print Your Name
Create a variable storing your name and print a greeting.

**Example Output**
```
Hello Ehsan
```

**Hints**
- Use a variable
- Use `print()`

---

## 2. Add Two Numbers
Create two variables containing numbers and print their sum.

Example:
```python
num1 = 5
num2 = 3
```

Expected output:
```
8
```

---

## 3. Even or Odd
Ask the user for a number and print whether it is **even or odd**.

**Example Output**
```
Enter a number: 7
Odd
```

**Hint**
Use the modulus operator `%`.

---

## 4. Loop From 1 to 5
Write a loop that prints numbers from **1 to 5**.

Expected output:
```
1
2
3
4
5
```

**Hint**
Use `range()`.

---

## 5. Print Each Item in a List
Create a list of animals and print each one using a loop.

Example list:
```python
["cat", "dog", "rabbit"]
```

Expected output:
```
cat
dog
rabbit
```

---

## 6. Count to 10 with a While Loop
Write a `while` loop that prints numbers **1 to 10**.

---

## 7. Simple Greeting Function
Create a function called `greet` that prints:

```
Hello!
```

Then call the function.

---

## 8. Function With a Parameter
Create a function that takes a name and prints:

```
Hello Sarah
```

---

## 9. Find the Largest Number
Create two numbers and print which one is larger.

Example output:
```
10 is larger
```

**Hint**
Use an `if` statement.

---

## 10. Total of a List
Create a list of numbers and print the **total**.

Example list:
```python
[2, 4, 6]
```

Expected output:
```
12
```

