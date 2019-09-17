# Cont'd Talk about Loops

# For Loops

stmt = "I'm Asma, How are You?"

for i in stmt:
	print(i)


print('------------------')

Basket = ['Banana','Juice','Milk']

for n in Basket:
	if n =='Juice':
		continue
	print(n)

print('------------------')
for n in Basket:
	if n =='Juice':
		break
	print(n)