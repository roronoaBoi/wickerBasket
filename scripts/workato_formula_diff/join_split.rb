# simple comparison for workato formula mode

string = 'Axe'
list = ['Axe']

string_to_list = string.split

list_to_string = list.join # or list.first

puts string_to_list.inspect #inspect shows the detail... in this case, that it is a list.
puts list_to_string
