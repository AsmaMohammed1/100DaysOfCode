# cont'd Talk about Sets

gender = {'F','M'}
print('The Length of my Sets:',len(gender))


# Remove Items : remove() , discard()
Cites = {'Jeddah', 'Makkah', 'Abha', 'Taif'}
Cites.remove('Abha')
Cites.discard('NoValue')
valueDeleted = Cites.pop() # will delete any items because set un order
# Cites.clear() > for delete all items in sets
# del Cites > will remove all items from memory and will become error
print('Cites',Cites)
print('Value delete with pop():',valueDeleted)

# use the set() constructor to make a set.

Grade = set(('A+','A','B','B+','C+','C','D+','D','F'))
Nums = set([3,4,5,6,7])
print(Grade)
print(Nums)
Cop =Grade.copy()
print(Cop)
Dif = Cites.difference(Grade)
print(Dif)
Uni = Cites.union(Grade)
print(Uni)
Intersction = Grade.intersection(Cites)
UserInput = str(input('Please Enter Your Gender!\n\t(F/M):'))

while True:
	if UserInput == 'F' or UserInput =='f':
		print('Your Choice:',UserInput)
		exit()
	elif UserInput == 'M' or UserInput == 'm':
		print('Your Choice',UserInput)
		exit()
	else:
		print('\nWrong!')
		UserInput = input('\n\tPlease Enter Your Gender!\n\t(F/M):')

