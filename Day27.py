# Talk about Conditions and If statements
w = 'HI'
w1 = 'HI'
print('Yes') if w == w1 else print('No')
print("-- Ticket's Movies --")
print('\n\t1: Show Movies')
print('\t2: Exit')

UserInput = int(input('\nYour Choice:'))
while True:
	if UserInput == 1:
		print('\n\t Movies List:\n\t-1. The Bourne Identity.\n\t-2. FearLess.\n\t-3. Fast Five.')
		input2 = int(input('\nYour Choice:'))
		if input2 == 1 or input2 == 2 or input2 == 3:
			print('\n\t\tDone!.')
			exit()
		else:
			print('Try Again!')
			input2 = int(input('\nYour Choice:'))
	elif UserInput==2:
		print('GoodBye!')
		exit()
	else:
		print('Try Again!')
		UserInput = int(input('\nYour Choice:'))
