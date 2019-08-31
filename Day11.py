# Cont'd Talk about Operators .


# 4 > Logical Operators:
#  used to combine conditional statements.
# Return True , False

Num1 = 4
Num2 = 8
Num3 = Num1
Num4 = 8

print( Num1>2 and Num2<2)
print(Num1 > 2 or Num2 < 2)
print(not (Num1 > 2 and Num2 < 2)) # Reverse the result



# 5 > Identity Operators:
# used to compare the objects
# not if they are equal, but if
# they are actually the same object, with the same memory location.
# is , is not

if Num1 is Num3:
	print('Correct')
if Num2 is Num4:
	print('Good')
if Num1 is not Num3:
	print('Wrong!')

# 6 > Membership Operators:
# used to test if a sequence is presented in an object.
# in , not in

print('---------------------------------')
Colors = ['red', 'blue', 'orange']
UserInput = input("Enter Your Color:")
if UserInput in Colors:
	print("\n\tColor exist,\n\tYour Color: {}".format(UserInput))
else:
	print('\n\tColor not Found.')

print('---------------------------------')
txt = 'Good Morning'
print("oo" in txt)

print('---------------------------------')
# 7 > Bitwise Operators:
# used to compare (binary) numbers.

number1 = 47
print(bin(number1))
number2 = 54
print(bin(number2))

print('& :{}'.format(number1&number2))
print('| :{}'.format(number1|number2))
print('~ :{}'.format(~number1))
print('^ :{}'.format(number1^number2))
