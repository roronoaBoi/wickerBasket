"""basic lists with python"""
# pylint: disable=invalid-name
items = ['item1','item2','item3']
print('item 2 is actually ' + items[2])

lil = [['yes','you'],'are','getting','it...']
print(lil[0][0] + ' ' + lil[0][1] + ' ' + lil[1] + ' ' + lil[2] + ' ' + lil[3])

negs = items[-1]
print(negs + ' is item3 because it is the last in items')

all_these = ['0','1','2','3','4']
yorbs = all_these[0:3] #zbi, includes last one...
print(yorbs)
