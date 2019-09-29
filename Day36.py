# Cont'd Talk about lambda



def func(num):
	return lambda x : x*num


var = func(2) # 2 to num
print(var(4)) # 4 to x
