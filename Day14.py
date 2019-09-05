# Cont'd Talk about List


# Divide List
MyList = ['Asma','Sara','Noura','Huda']

print(MyList[1:3])
print(MyList[:3])
print(MyList[1:])
print(MyList[:])


# Check if Item Exists : Use > in

if "Asma" in MyList:
	print("yes Exist")

# Repeat Item in List : Use > *

MyList = MyList*3
print(MyList)

NewList = [2]*3
print(NewList)

# To add 2 lists or more into one list : Use > +
MyList += NewList
print(MyList)

FloatNumbers = [2.3,56.2,65.434,6.5]
IntNumbers = [1,5,8,3,88]
AllNumbers = FloatNumbers+IntNumbers
print(AllNumbers)
