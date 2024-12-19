nums = [1,2,3,4]
print(id(nums))

nums[0] = 6
print(id(nums))

nums.append(2)
print(nums)

person = {'name':'Mr. Abc','age': 21,'department': 'English','isMarried': False}

print(id(person))

person['age'] = 22
print(id(person))


friends={'Abu Bakkar','Rahim','Karim','Jheltu'}
print(id(friends))
friends.add('Kader')

print(id(friends))
