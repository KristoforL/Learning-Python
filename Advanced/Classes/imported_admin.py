#Imports all the functions from the admin module and then creates a class for it to make sure it works

from admin import *

KSC = Admin('JQ','L',26,'GA')
KSC.privileges=['Can add people', 'Can delete people']
KSC.describe_user()
KSC.show_privileges()
