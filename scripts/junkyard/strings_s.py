"""
quick reference on upper . lower. Useful in automations
that leverage standardized parameters that coule be coming
in from another system where cases are not considered. Example:
api requires 'user_type: free', but system data has 'Free'
"""
#pylint: disable=invalid-name

user_data = [
    {
        'name' : 'Marth',
        'u_type' : 'free'
    },
    {
        'name' : 'Roy',
        'u_type' : 'Free'
    }
]

#example of formatting a param in an integration...
for user in user_data:
    if user['u_type'].islower():
        print(f"{user['name']} has been created as {user['u_type']}")
    else:
        new_format = user['u_type'].lower()
        print(f"{user['name']} has been created as {new_format}")
