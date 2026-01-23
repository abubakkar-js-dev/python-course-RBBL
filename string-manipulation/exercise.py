#  All python concepts
# 1. Variables and Data Types
# 2. Control Flow (if, for, while)
# 4. Data Structures (lists, tuples, dictionaries, sets)
# 3. Functions and Modules
# 5. Object-Oriented Programming (classes and objects)
# 6. Exception Handling (try, except)
# 7. File Handling (reading and writing files)
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