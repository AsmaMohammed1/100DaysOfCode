# Cont'd Talk about Dictionary

Person ={
	'Hair':'Black',
	'Tall':'169',
	'weight':'54',
	'Gender':'male'
}

# Check if Key Exists : Use > in

if 'Tall' in Person:
	print('Yes exist')
else:
	print('No')


# Dictionary Length
print('Length of Dictionary:',len(Person))

# Adding Items
# by using a new index key and assigning a value to it.

Person['Jop'] = 'Doctor'
print(Person)

# Remove Items

# 1 : pop() :  removes the item with the specified key name
Person.pop("Hair")
print(Person)
# Person.pop("Hair") > key error


# 2 :  popitem() : removes the last inserted item
Person.popitem()

print(Person)

# 3 : del() : removes the item with the specified key name
del Person['Tall']
print(Person)

# 4 : clear() : remove all items
Person.clear()
print(Person)