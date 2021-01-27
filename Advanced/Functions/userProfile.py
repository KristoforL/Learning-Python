#This will take in multiple positional arguments and then arbitrary kayword arguments

#The double asterisk is for creating a dictionary names user_info
#Do not get them confused where one asterisk is for tuples while 2 is for dictionary
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

   
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)