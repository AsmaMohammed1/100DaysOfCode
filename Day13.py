# Talk about List
# List : is a collection which is ordered and changeable. Allows duplicate members.
# can be string with numbers in same List

# Ex:
List = ['one', 'Two', 1, 2]
print(List)

FloatList =[2.3, 6.5, 34.345, 099897.23232]
print('Float Numbers: ',FloatList)

# Access the list items by referring to the index number
# start with 0 for first , start with -1 for end

print('Access for item 4', List[3])

# using a for loop for print all items in the list, one by one.
print('All items in List:\n')
for i in FloatList:
	print(i)

# To change the value of a specific item, refer to the index number.
print('Change items in my Lists:\n')
List[1] = 'Three'
FloatList[3] = 7
print(List, ',', FloatList)

# 'del' keyword removes the specified index or all list
print('delete item in List:\n')
del List[1]
# del FloatList < this remove all List items
print('List with delete item', List)


# Add/Remove
print('Add & Remove items for my List:\n')
List.append('Five')
FloatList.remove(7)
print(List, ',', FloatList)

# Sort / Reverse
FloatList.sort()
print('List with sort: ', FloatList)
FloatList.reverse()
print('List with reverse: ', FloatList)


#userInput = list(map(str,input("enter five number").split()))

