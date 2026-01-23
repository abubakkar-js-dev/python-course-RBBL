#  All python concepts
# 1. Variables and Data Types
# 2. Control Flow (if, for, while)
# 3. Functions and Modules
# 4. Data Structures (lists, tuples, dictionaries, sets)
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

while True:
    name = input("Enter your name: ");
    if name.capitalize() in names:
        print("Welcome back,", name)
        break
    else:
        print("Name not found, try again.")
