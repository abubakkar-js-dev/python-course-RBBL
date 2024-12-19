input_num1=input("Enter the first number: ")
operator=input("Enter the operator which calculation you want: ")
input_num2=input("Enter the second number: ")

print("The program is running")

num1=int(input_num1)
num2=int(input_num2)

try: 
    if(operator == '+'):
        result= num1+num2
    elif operator == '-':
        result=num1-num2
    elif operator=='*':
        result=num1*num2
    elif operator=='/':
        result=num1/num2
    else:
        print('Ivalid input')
except Exception as e:
    print(e)


print(result)