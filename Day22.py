# Talk about Dictionary
# dictionary name = {keys : values}

Basket = {}
print(Basket)

Students = {
	'Name' : 'sara',
	'Id' : 191919 ,
	'age' : '21'

}
print(Students)
print('-------------------------------')

# Access Items
# by referring to its key name inside square brackets [].
print(Students['Id'])
# also a method get() will give me the same result.
value = Students.get('Name')
print(value)
print('-------------------------------')

# Change Values
# by referring to its key name.

Students['age'] = 23
print(Students)

print('-------------------------------')
#  Use for loop
# print all keys
for i in Students:
	print(i)

# print all values
for x in Students:
	print(Students[x])

# also here print all values
for y in Students.values():
	print(y)

print('-------------------------------')

print(Students.values())

for n, z in Students.items():
	print(n,z)

print(Students.items())