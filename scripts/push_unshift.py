"""modding lists with python (push/unshift)"""

items = ['katana','kunai','bokken']

items.append('buster sword') # works just like a push
items.insert(0,'grass sword') # works just like an unshift, but you need to add index
items.remove('katana') #removing a value from a list
del items[2] #removes bokken due to previous changes

print(items)
