role='back end developer'

print(role[3])
print(role[5])
print(role[-1])


print(role[1:3]) # start:stop using to slice a string

print(role[5:9])

# ommit one value will be siced all after/before start/end

print(role[5:])
print(role[:4])

print(role[0::3])

print(role[::-2])


#  Hacks:   [start:end:step]

# STRING REPEATATION AND CONCATANATION

'''
    USECASE:
    - Builing dynamic message
    - Url Construction
    - File Paths
    - Template Strings
    - Data Formatting
    - Generating Patterns
    - Formatting, Initialization
    - Creating Repeated Message
'''

'''
    1. using + sign
    2. using .join method
    3. using .formate method
    4. using % modulas operator
'''

str1='hello '
str2='world'


repeated_str=str1 * 20

# print(repeated_str)


concate1=str1+str2
concate2= str1+ ''.join(str2)
concate3='{} {} !'.format(str1,str2)

print(concate3)





