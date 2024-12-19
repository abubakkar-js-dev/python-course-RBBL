# a=32
# location_a=id(a)
# a=544
# location_b=id(a)

a=32.322
location_a=id(a)
a=544.56
location_b=id(a)


print(location_a)
print(location_b)


str1= 'Hello'
location_str1=id(str1)
str1= 'World'

print(location_str1 == id(str1))


tupes = (1,2,3,4,5,5)
location_tupes= id(tupes)
tupes = (1,2,5)

print(location_tupes == id(tupes))


fronzen1 = frozenset([2,3,4,5])
location_frozen1 = id(fronzen1)
fronzen1 = frozenset([2,3,4])
location_frozen1b = id(fronzen1)

print(location_frozen1)
print(location_frozen1b)
