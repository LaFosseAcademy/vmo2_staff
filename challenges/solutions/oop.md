# OOP Python Challenges: Employee, Manager, and Developer — Solutions

These solutions match the main OOP challenges.

---

## Full Solution

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

    def display_info(self):
        return f"Name: {self.name}, Department: {self.department}, Salary: {self.salary}"

    def apply_raise(self):
        self.salary = self.salary * self.raise_rate

    @staticmethod
    def is_valid_salary(amount):
        return amount > 0


class Manager(Employee):
    raise_rate = 1.10

    def __init__(self, name, salary, department, team_size):
        super().__init__(name, salary, department)
        self.team_size = team_size

    def manage_team(self):
        return f"{self.name} manages a team of {self.team_size} people."

    @staticmethod
    def manager_title():
        return "Management Staff"


class Developer(Employee):
    raise_rate = 1.15

    def __init__(self, name, salary, department, programming_language, level):
        super().__init__(name, salary, department)
        self.programming_language = programming_language
        self.level = level

    def write_code(self):
        return f"{self.name} is writing {self.programming_language} code."

    @staticmethod
    def is_valid_level(level):
        return level in ["Junior", "Mid", "Senior"]


# Challenge 1: Employee objects
emp1 = Employee("Anna", 40000, "HR")
emp2 = Employee("Tom", 42000, "Finance")

print(emp1.display_info())
print(emp2.display_info())
print(Employee.is_valid_salary(50000))
print(Employee.is_valid_salary(-100))
print("Employee count:", Employee.employee_count)

print("-" * 40)

# Challenge 2: Manager objects
mgr1 = Manager("Sarah", 60000, "Engineering", 10)
mgr2 = Manager("James", 58000, "Sales", 6)

print(mgr1.display_info())
print(mgr1.manage_team())
mgr1.apply_raise()
print("Sarah new salary:", mgr1.salary)

print(mgr2.display_info())
print(mgr2.manage_team())
mgr2.apply_raise()
print("James new salary:", mgr2.salary)

print("-" * 40)

# Challenge 3: Developer objects
dev1 = Developer("Mia", 50000, "Engineering", "Python", "Junior")
dev2 = Developer("Leo", 55000, "Engineering", "JavaScript", "Mid")

print(dev1.display_info())
print(dev1.write_code())
dev1.apply_raise()
print("Mia new salary:", dev1.salary)

print(dev2.display_info())
print(dev2.write_code())
dev2.apply_raise()
print("Leo new salary:", dev2.salary)

print(Developer.is_valid_level("Senior"))
print(Developer.is_valid_level("Intern"))

print("-" * 40)

# Challenge 4: Store all objects in a list
staff = [emp1, emp2, mgr1, mgr2, dev1, dev2]

for person in staff:
    print(person.display_info())

print("Company name:", Employee.company_name)
print("Total employees created:", Employee.employee_count)

print("-" * 40)

# Challenge 5: Compare raise rates
print("Employee raise rate:", Employee.raise_rate)
print("Manager raise rate:", Manager.raise_rate)
print("Developer raise rate:", Developer.raise_rate)

sample_emp = Employee("Nina", 30000, "Support")
sample_mgr = Manager("Omar", 30000, "Operations", 4)
sample_dev = Developer("Ivy", 30000, "Engineering", "Python", "Senior")

print("Before raise:", sample_emp.salary, sample_mgr.salary, sample_dev.salary)
sample_emp.apply_raise()
sample_mgr.apply_raise()
sample_dev.apply_raise()
print("After raise:", sample_emp.salary, sample_mgr.salary, sample_dev.salary)

print("-" * 40)

# Challenge 6: Test static methods
print(Employee.is_valid_salary(50000))
print(Employee.is_valid_salary(-20))
print(Manager.manager_title())
print(Developer.is_valid_level("Senior"))
print(Developer.is_valid_level("Intern"))

print("-" * 40)

# Challenge 7: One extra feature
# Added a method to increase a manager's team size.

class BetterManager(Manager):
    def increase_team_size(self, amount):
        self.team_size += amount
        return self.team_size


mgr3 = BetterManager("Clara", 65000, "Product", 5)
print(mgr3.manage_team())
mgr3.increase_team_size(3)
print(mgr3.manage_team())
```

---

## Notes

This solution includes:

- a parent class: `Employee`
- two child classes: `Manager` and `Developer`
- shared class variables
- inheritance
- instance methods
- static methods
- multiple created objects


