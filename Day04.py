# Talk about numbers.
# There is Three numeric Types which are : int , float , complex


import random
# use type() function :

x = 10     #int
y = -20.45 #float
z = 3012345678654324567j #complex , end with "j/J"

print("x is:", x, " and its type", type(x),
      "\ny is:", y, "and its type", type(y),
      "\nz is: ", z, "and its type", type(z))

# convert from one type to another using: int(), float(), and complex() methods.
# complex can't convert to another Types .

a = 11
b = 6.4
c = 55j

a1 = float(a)
b1 = complex(b)
c1 = int(a)

print("a is:", a, ", b is:", b, ", c is:", c)
print(a1, " ", b1)
print(type(a1), type(b1))

# random that can be used to make random numbers

print(random.randrange(1,20))
print(random.random())
print(random.randint(1,6))

