# Cont'd Talk about function

# Passing a List as a Parameter




def func(anyName):
	print(anyName)
	return anyName*2

Colors = ['Red','Blue','Yellow']
func(Colors)
i = func(5)
print(i)

# Keyword Arguments

def tr(n1,n2,n3):
	print('num3 is',n3)


tr(n3=9,n1=2,n2=4)

# Arbitrary Arguments

def method(*para):
	print(para)

method('a','b','c')
method(1,4,3,7,8)


def fact(num):
	if num==0:
		return 1
	else:
		return num*fact(num-1)

print(fact(3))