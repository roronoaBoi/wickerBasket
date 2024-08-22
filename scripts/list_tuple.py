"""basics of lists and tuples"""

a_list = ['option 1', 'option 2', 'option 3']

a_tuple = ('option 1', 'option 2', 'option 3')

a_list[0] = 'option 0' # changes option 1 for option 0 because lists are mutable
print(a_list) # ['option 0', 'option 2', 'option 3']

# a_tuple[0] = 'option 0' #can't do this! tuples are immutable
# print(a_tuple) #returns error
