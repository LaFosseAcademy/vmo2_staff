# Day 2 & 3

## Customer Class
```python
class Customer:
    def __init__(self, name: str, internet_speed: int, password: str):
        self.name = name
        self.internet_speed = internet_speed
        self._password = password
        self.devices = []
        
    def increase_internet_speed(self, increase: int):
        self.internet_speed += increase
        
    def add_device(self, *devices: str):
        for device in devices:
            self.devices.append(device)
        
paul = Customer("Paul", 200, "seanbean007")
```

## Device Challenge Solution
```python
class Device:
    def __init__(self, name: str, status: str):
        self.name = name
        self._status = status
        
    def update_status(new_status: str):
        self._status = new_status
        
    def display_details(self):
        return f"{self.name} currently has a status of {self._status}" 
    
router = Device("Router", "online")
print(router.display_details())
```

## Customer Class Example
```python
class Customer:
    def __init__(self, name: str, internet_speed: int, password: str):
        self.name = name
        self.internet_speed = internet_speed
        self._password = password
        self.devices = []
        
    def increase_internet_speed(self, increase: int):
        self.internet_speed += increase
        
    def add_device(self, *devices: str):
        for device in devices:
            self.devices.append(device)

        

class BusinessCustomer(Customer):
    def __init__(self, name: str, internet_speed: int, password: str, account_mananger: str):
        super().__init__(name, internet_speed, password)
        self.account_mananger = account_mananger
        
    def generate_invoice(self):
        print("Requesting invoice")
        
    def increase_internet_speed(self, increase: int):
        self.internet_speed += (increase + 10)

    def request_account_support(self):
        print(f"Reaching out to {self.account_mananger} for support")


la_fosse = BusinessCustomer("LaFosse", 300, "courmayeur", "Daniel Whitaker")
```

## Person Class Challenge Solution
```python
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        
    def go_to_work(self):
        print(f"{self.name} is going to work")
        
class Teacher(Person):
    def __init__(self, name: str, age: int, subject_speciality: str):
        super().__init__(name, age)
        self.subject_speciality = subject_speciality
        
    def go_to_work(self):
        print(f"{self.name} is going to work to teach {self.subject_speciality}")

martin.go_to_work()
emile.go_to_work()
```


## Polymorphism starting point
```python
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        
    def go_to_work(self):
        print(f"{self.name} is going to work")
        
class Teacher(Person):
    def __init__(self, name: str, age: int, subject_speciality: str):
        super().__init__(name, age)
        self.subject_speciality = subject_speciality
        
    def go_to_work(self):
        print(f"{self.name} is going to work to teach {self.subject_speciality}")
        

class Chef(Person):
    def __init__(self, name: str, age: int, restuarant: str):
        super().__init__(name, age)
        self.restuarant = restuarant
        
    def go_to_work(self):
        print(f"{self.name} is going to work at {self.restuarant}")   
        
martin = Person("Martin", 31)
emile = Teacher("Emile", 34, "History")
tom_kerridge = Chef("Tom", 52, "The Hand and Flowers")

martin.go_to_work()
emile.go_to_work()
tom_kerridge.go_to_work()
```

## Class Variables Example
```python
class Customer:

    speed_tiers = {
        "standard": 100,
        "fibre": 500,
        "gigabit": 1000
    }

    def __init__(self, name: str, internet_speed: int, password: str):
        self.name = name
        self.internet_speed = internet_speed
        self._password = password
        self.devices = []
        
    def increase_internet_speed(self, increase: int):
        self.internet_speed += increase
        
    def add_device(self, *devices: str):
        for device in devices:
            self.devices.append(device)
            
    def get_tier(self):
        for tier, min_speed in self.speed_tiers.items():
            if self.internet_speed <= min_speed:
                return tier
        return "custom"

    def describe_internet_package(self):
        print(f"{self.name} has a {self.get_tier()} package")            
            
            
emile = Customer("Emile", 200, "gandalf2026")
emile.describe_internet_package()
```

## Class Decorater Starter
```python
class Customer:
    def __init__(self, name: str, speed: int):
        self.name = name
        self._speed = speed

peter = Customer("Peter", 100)

peter._speed = -100
peter._speed = "Gandalf is the greatest wizard

print(peter._speed)
```

## Class Property Decorator complete
```python
class Customer:
    def __init__(self, name: str, speed: int):
        self.name = name
        self._speed = speed

    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, value: int):
        if int(value) < 0:
            print("Speed cannot be negative")
        self._speed = value
        
    @speed.deleter
    def speed(self):
        del self._speed

peter = Customer("Peter", 100)

peter.speed # CALLS GETTER
peter.speed = -100 # CALLS SETTER
del peter.speed # CALLS DELETER
```

## Class and Static Methods
```python
class Customer:
    
    default_speed = 100

    def __init__(self, name: str, speed: int, phone_number: str):
        self.name = name
        self.speed = speed
        # NEW CODE
        if Customer.is_valid_mobile(phone_number):
            self.phone_number = phone_number
            print("Valid phone number")
        else:
            self.phone_number = "Invalid"
            print("Invalid phone number")

    @classmethod
    def with_default_speed(cls, name):
        return cls(name, cls.default_speed)

    @staticmethod
    def is_valid_mobile(number: str):
        return number.startswith("07") and len(number) == 11

peter = Customer("Peter", 200, "07123456789")
```
