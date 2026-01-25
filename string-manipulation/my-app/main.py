import datetime,math,os,json,http.client,subprocess,hashlib,csv
from calculator import add,substract,multiply,divide
from pprint import pprint


#test

print("Addition: ",add(5,10))
print("Substraction: ",substract(10,2))
print("Multiply: ",multiply(8,3))
print("Devide: ",divide(30,6))


# built-in modules

current_date = datetime.datetime.now()
print(current_date.today())
print(current_date.date())
print(current_date.weekday())
print(current_date.year)
print(current_date.timetz())


# Math

print(math.sqrt(49))
print(math.ceil(4.67))
print(round(45.634))


# OS

print(os.cpu_count())
print(os.name)
print(os.getcwd())
print(os.listdir())


# JSON

student_obj = {"name": "Abu Bakkar", "age": 21}
student_obj_str = json.dumps(student_obj,indent=4)

print(type(student_obj_str))
print(type(student_obj))


# HTTP Request

connection = http.client.HTTPSConnection("jsonplaceholder.typicode.com")

# sent request

connection.request("GET","/users")

# Get response

response = connection.getresponse()
status_code = response.status
users_str = response.read().decode()
users = json.loads(users_str)

print("status: ", status_code)
# print("Data", users[0])
# pprint(users)


# for user in users:
#     print(user['name'])


# Subprocess - working with command

result = subprocess.run(["python","--version"],capture_output=True,text=True)
print("Result: ",result.stdout)

exit_code = subprocess.call(["ls"])
print("Exit code:", exit_code)


password = "aklabalok321" 
text = b'adfdkd' 
hashed_pass = hashlib.sha256(password.encode()).hexdigest() #encode for convert bytetext
hashed_text = hashlib.md5(text).hexdigest();
# hashed_pass = hash(password)

print(hashed_pass)
print(hashed_text)
