# Task3 Q2

languages = ('swift', 'python' , "java" )
Word = input('\nPlease Guess the Word!\n').lower()

while True:
	if Word in languages:
		print('Good! The Word Exist.')
		exit()
	else:
		print('Wrong! Please Try Again.')
		Word = input('\nPlease Guess the Word!\n').lower()