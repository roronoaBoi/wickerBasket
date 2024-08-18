"""basic lists with python"""
# pylint: disable=invalid-name
items = ['item1','item2','item3']
print('py list indexing:')
print('item 2 is actually ' + items[2])

lil = [['yes','you'],'are','getting','it...']
print(lil[0][0] + ' ' + lil[0][1] + ' ' + lil[1] + ' ' + lil[2] + ' ' + lil[3])

negs = items[-1]
print(negs + ' is item3 because it is the last in items')

print('py slices:')
all_these = ['0','1','2','3','4']
yorbs = all_these[0:3] #zbi, includes last one...
print(yorbs)

#len and updating
print('len and updating:')
gorbs = ['1','2','3']
gorbs_mix = ['seven', 2, 3]
gorbs[0] = 'seven'
print(len(gorbs))
print(gorbs_mix)

#pushing lists into lists
print('list into list')
list_one = [1,2,3]
list_two = [4,5,6]
list_three = list_one + list_two
print(list_three)

#deleting values from list
print('py del')
del list_one[0]
print(list_one)
