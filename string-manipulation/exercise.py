#  All python concepts
# 1. Variables and Data Types
# 2. Control Flow (if, for, while)
# 4. Data Structures (lists, tuples, dictionaries, sets)
# 3. Functions and Modules
# 5. Exception Handling (try, except)
# 6. File Handling (reading and writing files)
# 7. Object-Oriented Programming (classes and objects)
# 8. Libraries and Frameworks (e.g., NumPy, Pandas, Flask
# 9. Debugging and Testing (using pdb, unittest)
# 10. Virtual Environments and Package Management (venv, pip)
# 11. Advanced Topics (generators, decorators, context managers)
# 12. Best Practices and Coding Standards (PEP 8, code reviews)



# Variable and data types
name = "John Doe" # String
age = 30         # Integer
height = 5.9     # Float
is_student = False # Boolean
fruits = ["apple", "Banana", "cherry"] # List
person = {"name": "Alice", "age": 25} # dictionary
numbers = (1,2,3,4,5) # Tuple
unique_numbers = {1,2,3,4,5} # Set

# String Manipulation
fName = "Abu Bakkar"
lName = "Siddik"

full_name = fName + " " + lName
print(full_name);
greeting = f"Hello, {full_name}! Welcome to the python world.";
print(greeting);

# String Methods
text = " Hello, World! Welcome to Python programming. "

print(text.strip()) # Remove leading/trailing whitespace
print(text.upper()) # Convert to uppercase
print(text.lower()) # Convert to lowercase
print(text.replace("World", "Universe")) # Replace substring
print(text.split(","))
print("-".join(["2024", "06", "15"])) # Join list into string

# Number methods
num = 15.42342
num2 = 33.9876
print(round(num)) # Round to nearest integer
print(int(num)) # Convert to integer
print(float(num2)) # Convert to float
print(abs(num)) # Absolute value
print(pow(2,4)) # power function
print("another power: ", 2 ** 4) # power operator



# Immutable vs Mutable Types
# Immutable types: int, float, str, tuple, frozenset
# Mutable types: list, dict, set




# Control Flow
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"    

# print("Your grade is: ", grade) 

# Loops 
scores = [85,50, 92, 78, 90, 88,70]

for i in scores:
    if(i >= 90):
        print(f"Score: {i}, Grade: A")
    elif(i >= 80):
        print(f"Score: {i}, Grade: B")
    elif(i >= 70):
        print(f"Score: {i}, Grade: C")
    else:
        print(f"Score: {i}, Grade: F")


# while loop
count = 0
while count < 5:
    print("Count is: ", count)
    count += 1

print("Counting finished!",count)


# do while loop simulation
names = ["Alice", "Bob", "Charlie"]

# while True:
#     name = input("Enter your name: ");
#     if name.capitalize() in names:
#         print("Welcome back,", name)
#         break
#     else:
#         print("Name not found, try again.")


# Data Structures
# List
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits);
fruits.remove("banana")
fruits[0] = "kiwi"
print(fruits)
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
print(fruits[1:3]) # Slicing
print(len(fruits)) # Length
print(fruits.index("kiwi")) # Index of element
print("cherry" in fruits) # Membership test

# Tuple
numbers = (1, 2, 3, 4, 5)
languages = ("Python", "Java", "C++")
print(numbers)
print(numbers[2])
print(len(numbers))
print(3 in numbers)
print(numbers.count(2))
print(numbers.index(4))
print(languages)
print(languages.count("Java"))

# Dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}
print(person)
print(person["name"])
person["age"] = 30
print(person)
person["job"] = "Engineer"
print(person)
del person["city"]
print(person)
print(person.keys())
print(person.values())
print(person.items())
print(person.get("name"))
print(person.values())
person.update({"age": 28, "city": "San Francisco"})
print(person);


# Set
unique_numbers = {8,1,2,3,4,5,3,5}
unique_numbers2 = {4,5,6,7,8,9}
new_numbers = unique_numbers.copy()
print("new_numbers:", new_numbers)
# unique_numbers.add(6)
# unique_numbers.remove(2)
# unique_numbers.discard(1) # No error if not found
# unique_numbers.pop()
print(unique_numbers.union(unique_numbers2))
print(unique_numbers.intersection(unique_numbers2))
print(unique_numbers)
print("Different: ",unique_numbers.difference(unique_numbers2))


#  Frozen Set
frozen_set1 = frozenset([1,2,3,4,5])
frozen_set2 = frozenset([4,5,6,7,8])

# Same methods as set but no modification methods
print("Frozen Set Union: ", frozen_set1.union(frozen_set2))
print("Frozen Set Intersection: ", frozen_set1.intersection(frozen_set2))
print("Frozen Set Difference: ", frozen_set1.difference(frozen_set2))
print(frozen_set1)

# Array
import array
import zipfile

arr = array.array('i', [1, 2, 3, 4])

arr.append(5)          # [1, 2, 3, 4, 5]
arr.insert(1, 10)      # [1, 10, 2, 3, 4, 5]
arr.remove(3)          # [1, 10, 2, 4, 5]
print(arr.pop())       # removes last → 5
print(arr.index(10))   # 1
print(arr.count(2))    # 1
arr.reverse()          # [4, 2, 10, 1]
print(arr.tolist())    # [4, 2, 10, 1]



#  Functions

def greet():
    name = input("Enter your name:")
    return f"Welcome to python journey, {name.capitalize()}"

# print(greet())

def calculate_area(radius):
    pi = 3.1416
    area = pi * (radius ** 2)
    return round(area, 2)

circle_area = calculate_area(5)
print("Area of circle with radius 5:", circle_area)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print("Factorial of 5:", factorial(5))


def fibonacci(n):
    if(n <= 0):
        return []
    if(n == 1):
        return [0]
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_fib)
    return fib_sequence[:n]

print("Fibonacci sequence of 10 terms:", fibonacci(10))

square = lambda x: x ** 2
print("Square of 7 using lambda:", square(7))

def outer_function(msg):
    def inner_function():
        return f"Inner says: {msg}"
    return inner_function()

print(outer_function("Hello from nested function!"))

x = 10

def modify_global():
    global x
    x = 20
modify_global()
print("Modified global x:", x)

# Decorators
def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function

@decorator_function
def display():
    print("Display function executed")
display()

# with open("./string-manipulation/hello.txt", "w") as file:
#     file.write("Hello, World!\nWelcome to Python file handling.")

# with open("./string-manipulation/hello.txt", "r") as file:
#     content = file.read()
#     print("File Content:\n", content)

import os

# os.rename("./string-manipulation/hello.txt", "./string-manipulation/greetings.txt");
# os.remove("./hello.c");

if not os.path.exists('./string-manipulation/new_folder'):
    os.mkdir('./string-manipulation/new_folder')
# os.rmdir('./string-manipulation/new_folder')

# with open("./string-manipulation/new_folder/greetings.txt","w") as file:
#     file.write("This is a new line added to the greetings file.\n")

listGreet = os.listdir('./string-manipulation/new_folder')


for item in listGreet:
    print("Item in new_folder:", item)

print("Current Working Directory:", os.getcwd())
# print("Directory Listing of './string-manipulation':", listdirec)


#  zip and unzip files
import zipfile

# with zipfile.ZipFile("./string-manipulation/test.zip","w") as zipf:
#     zipf.write("./string-manipulation/greetings.txt", arcname= "greetings.txt")
#     zipf.write("./string-manipulation/exercise.py", arcname= "exercise.py")


# with zipfile.ZipFile("./string-manipulation/test.zip","r") as zipf:
#     zipf.extractall("./string-manipulation/unzipped_folder")

# import shutil

# archive =  shutil.make_archive("./string-manipulation/archive_folder","zip","./string-manipulation/new_folder")
# print("Archive created:", archive)


#  working with CSV files
import csv

students = [
    {"id": 1, "name": "Alice Johnson", "age": 20, "grade": "A", "major": "Computer Science"},
    {"id": 2, "name": "Bob Smith", "age": 22, "grade": "B+", "major": "Economics"},
    {"id": 3, "name": "Charlie Brown", "age": 19, "grade": "A-", "major": "Mathematics"},
    {"id": 4, "name": "Diana Prince", "age": 21, "grade": "B", "major": "History"},
    {"id": 5, "name": "Ethan Hunt", "age": 23, "grade": "C+", "major": "Physics"},
    {"id": 6, "name": "Fiona Gallagher", "age": 20, "grade": "A", "major": "Biology"},
    {"id": 7, "name": "George Lopez", "age": 22, "grade": "B-", "major": "Chemistry"},
    {"id": 8, "name": "Hannah Baker", "age": 19, "grade": "A+", "major": "English"},
]

fileName = "./string-manipulation/students.csv"

header = students[0].keys()
print("Header:", header)

# with open(fileName, 'w', newline='') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=header)
#     writer.writeheader()
#     writer.writerows(students)

# print("Csv file created:", fileName);

# with open(fileName, 'r') as csvfile:
#     content = csv.reader(csvfile)
#     for row in content:
#         print("Row:", row)
    


# Exception Handling

try:
    with open("./string-manipulation/none.txt", "r") as file:
        content = file.read()
        result = 10 / int(content)
        print("Result:", result)

# except FileNotFoundError:
#     print("Error: The file was not found.")
# except ValueError:
#     print("Error: Could not convert data to an integer.")
# except TypeError:
#     print("Error: Invalid type encountered.")
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
except Exception as e:
    print("An unexpected error occurred:", str(e))

finally:
    print("Execution completed.")




# working with json
import json

person = {
  "name": "Emily Johnson",
  "age": 29,
  "gender": "Female",
  "email": "emily.johnson@example.com",
  "phone": "+1-202-555-0147",
  "address": {
    "street": "123 Maple Street",
    "city": "Seattle",
    "state": "WA",
    "zip": "98101"
  },
  "is_student": False,
  "skills": ["Python", "Data Analysis", "Machine Learning"],
  "hobbies": ["Reading", "Hiking", "Photography"]
}

# # Object to JSON string
# person_json = json.dumps(person, indent=4)
# print("JSON String:\n", person_json)


## JSON string to Object
# person_json_str = ''' {
#   "name": "Emily Johnson",
#   "age": 29,
#   "gender": "Female",
#   "email": "emily.johnson@example.com",
#   "phone": "+1-202-555-0147",
#   "address": {
#     "street": "123 Maple Street",
#     "city": "Seattle",
#     "state": "WA",
#     "zip": "98101"
#   },
#   "is_student": false,
#   "skills": ["Python", "Data Analysis", "Machine Learning"],
#   "hobbies": ["Reading", "Hiking", "Photography"]
# } '''

# person_obj = json.loads(person_json_str)
# print("Person Object:\n", person_obj)


# Person object to json file

# with open("./string-manipulation/person.json", "w") as person_json_file:
#     json.dump(person, person_json_file, indent=4)


# Person json file to object
with open("./string-manipulation/person.json", "r") as person_json_file:
    person_obj = json.load(person_json_file)
    print("Person Object from JSON file:\n", person_obj)


# Working with date time
import datetime

current_time = datetime.datetime.now()
formated_date = current_time.strftime("%d-%m-%Y %H:%M:%S")
print("Formate date: ",formated_date)

# print(current_time)
# print(current_time.year)
# print(current_time.month)
# print(current_time.day)
# print(current_time.hour)
# print(current_time.time(),' Time')
# print(current_time.minute)
# print(current_time.second)
# print(current_time.microsecond)
# print(current_time.date)
# print(current_time.weekday)


# Working with math
import math

print(math.sqrt(49))
print(math.floor(4.53))
print(math.ceil(4.53))
print(math.pow(2,4))


date_1 = datetime.datetime(2025,8,22)
date_2 = datetime.datetime(2026,1,24)

difference = date_2 - date_1
print("Difference between dates:", difference.days, "days")

new_date = date_1 + datetime.timedelta(days=20)
print("New date after adding 20 days:", new_date.strftime("%d-%m-%Y"))




# OOP - Classes and Objects
class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def substract(self):
        return self.a - self.b
    def multiply(self):
        return self.a * self.b
    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Error: Division by zero"
        

calc = Calculator(20,8)
calc2 = Calculator(15,3)
print("Addition:", calc.add())
print("Substraction:", calc.substract())
print("Multiplication:", calc.multiply())
print("Division:", calc.divide())

print(calc2.add())


class MyObject:
    x = 10
    y = 20
    def __init__(self,a,b):
        self.a = a
        self.x = b
    def addSum(self):
        return self.a + self.x + self.y

obj = MyObject(100, 5)
print("Sum from MyObject:", obj.addSum())



# Single in heritance
class GrandParent:
    family_name = "Mondol Bari"
    def show_family_name(self):
        return self.family_name

class Parent(GrandParent):
    bank_amount = 100000
    @staticmethod
    def static_show_bank_amount():
        return Parent.bank_amount
    def show_bank_amount(self):
        return self.bank_amount


class Child(Parent):
    def __init__(self, name):
        self.name = name
    def display_info(self):
        return f"Child Name: {self.name}, Inherited Bank Amount: {self.show_bank_amount()}"
    

child = Child("Alice")
# print(child.display_info())
# print(child.show_bank_amount())
# print(Parent.bank_amount)
# print(Child.bank_amount)
# print(Parent.static_show_bank_amount())

# Multi-level Inheritance (GrandParent -> Parent -> Child) demonstrated above.
print("Family Name from Child:", child.show_family_name())


#  Multiple Inheritance
class Father:
    def father_property(self):
        return "This is father Property."

class Mother:
    def mother_property(self):
        return "This is mother Property."

class Son_property(Father, Mother):
    pass
    # def son_info(self):
    #     return "This is son class method."

son = Son_property()
print(son.father_property())
print(son.mother_property())
# print(son.son_info())

# Accecing in class methods and properties

"""
1. access when parents have constructor but child has no constructor
2. access when child has constructor but parents have no constructor
3. access when both parents and child have constructors
4. access parent class methods and properties using super()

"""

class A:
    a = 10
    b = 20
    print("Parent class properties initialized.")

class B(A):
    def __init__(self):
        super().__init__()
        print("Child constructor called.")
        self.x = 100
        self.y = 200

# result = B()
result2 = A()

print("Accessing parent class properties from child instance:", result2.a, result2.b)