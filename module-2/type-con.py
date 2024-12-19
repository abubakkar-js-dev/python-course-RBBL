# implicit conversion

num1=2
print(type(num1))

num1_float=float(num1)
print(type(num1_float))

num1_str=str(num1)
print(type(num1_str))


# explicit conversion

try:
    x=2
    y="3"

    sum=x+ int(y)
    print(sum)
    print(type(sum))

except Exception as e:
    print(e)    