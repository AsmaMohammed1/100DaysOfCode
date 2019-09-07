# Task3 Q1

print("\n\t\t-- Welcome To As's Bank --\n")

UserInput = float(input('- press 1 for Deposit'
      '\n- press 2 for Withdraw'
      '\n- press 3 for Show balance'
      '\n- press 4 for EXIT\n'))

balance = []
while True:
	if UserInput == 1:
		Input = float(input('Enter The Amount:\n'))
		balance.append(Input)
		UserInput = float(input('- press 1 for Deposit'
		                        '\n- press 2 for Withdraw'
		                        '\n- press 3 for Show balance'
		                        '\n- press 4 for EXIT\n'))
	elif UserInput == 2:
		if len(balance) == 0:
			print('\n\tYour Account empty, Thank You')
		else:
				Input2 = float(input('\n\tEnter The Amount for Withdraw:\n'))
				if Input2 not in balance:
					print('\n\t\t not exist!')
					exit()
				else:
					balance = balance.remove(Input2)
					print('\n\t\tDone!')
					exit()
	elif UserInput == 3:
		if len(balance) == 0:
			print('\n\tYour Account empty, Thank You')
		else:
			print('\n\tYour Balance: ',sum(balance),'SR')
			exit()
	elif UserInput == 4:
	    print('\n\t\tTHANK YOU!')
	    exit()

