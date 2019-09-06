# Cont'd Talk about List
# List Methods

Fruits = ['Apple', 'Orange', 'Banana']


# Length of List
print('Length of List:', len(Fruits))

# To add an item at the specified index
Fruits.insert(1,"Cherry")
print('Length of List:', (Fruits))

# To delete : remove , pop
Fruits.remove('Orange')
Fruits.pop()
Fruits.pop(1)
# Fruits.clear() > delete all items
print('after editing: ',Fruits)

# Copy list : use method Copy()
NewList = Fruits.copy()
print('NewList:', NewList)

# Another way for copy: use list()
NewList3 = list(NewList)
print('Another copy of my List:',NewList3)

# Using the list() constructor to make a list
Colors = list(('Black','Yellow','Red'))
print('Colors:',Colors)