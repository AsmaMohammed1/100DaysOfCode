# # Cont'd Talk about Dictionary

# Copy a Dictionary

Basket = {
	'Fruit':'Banana',
	'Drink':'Orange Juice',
	'Sweet':'Galaxy',

}

Dict = Basket.copy()

print(Dict)
# another way for copy : use dict()
Dict2 = dict(Basket)
print(Dict2)

# Nested Dictionaries

Students = {
	'Student1' : {
		'Name' : 'Ahmad',
		'ID' : '0987',
		'Department':'IT'
},
	'Student2' : {
		'Name' : 'Sara',
		'ID' : '6785',
		'Department':'CS'
},
	'Student3' : {
		'Name' : 'Fahad',
		'ID' : '6776',
		'Department':'IS'
}
}
print(Students)

# another way

child1 = {
	'Name':'Yasser',
	'Age':'5'
}

child2 = {
	'Name':'Huda',
	'Age':'9'
}

child3 = {
	'Name':'Mada',
	'Age':'7'
}

Family = {
	'child1':child1,
	'child2':child2,
	'child3':child3
}

print('Family',Family)

# The dict() Constructor
# Keywords not string
# use = rather than :
NewDict = dict(employee='Omar',ID=123456,Salary=9876)
print('New Dict: ',NewDict)

keysInList=list(NewDict.keys())
print(keysInList)

print(sorted(NewDict.keys()))