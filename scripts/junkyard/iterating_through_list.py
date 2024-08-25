"""basic iterations"""
#pylint: disable=consider-using-enumerate
items = ['iron lance','iron sword','devil axe']
for item in range(len(items)):
    print('item ' + str(item + 1) + ' in the list is ' + items[item])

#pylint said to consider enumerate. This would be done like so:
# for index, item in enumerate(items):
#     print(f'Index {index}, Item: {item}')
