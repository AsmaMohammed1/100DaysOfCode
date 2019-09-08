# Talk about sets
# not order , unique , not repeat
# can't access items with index because set unorder
# can access with loop for print all values or use "in" to ensure the item in this set
# cannot change items, but can add new items.

colors = {}
print('empty set:',colors)
colors = {'red','blue','black'}
print('set with values:',colors)

MySet = {1,3,6,'Asma','Noura',6,3,'Asma'}
print('set with no repeat values:',MySet)
print('--------------------------')


for x in colors:
	print(x)

print('--------------------------')
if "red" in colors:
	print('Yes')


# Add items : add() , update()
# add() for add one item
colors.add('yellow')
print('set after add one item:',colors)

# update() for add more than one item
colors.update(["Pink","Orange"])
print('set after add more than one item item:', colors)


