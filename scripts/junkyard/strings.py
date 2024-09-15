"""
quick reference on string interpolation and f strings.
f strings are like template literals in js `hello ${name}`
"""
#pylint: disable=invalid-name


identifier = '1234'
status = 'SUCCESS'
#interpolation
# print('record no. %s process status: %s' %(identifier, status))

#f-string
print(f'record no. {identifier} process status: {status}')
