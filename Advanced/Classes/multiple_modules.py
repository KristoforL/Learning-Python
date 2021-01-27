from users import Users
from admin import Admin

JQ = Users('JQ', 'L', 26, 'Georgia')
KN = Admin('K', 'N', 25, 'Mississippi')
KN.privileges = ['Can add people', 'Can delete people']
TMC = Users('T', 'MC', 21, 'Georgia')

JQ.describe_user()
JQ.greet_user()

KN.describe_user()
KN.greet_user()
KN.show_privileges()

TMC.describe_user()
TMC.greet_user()

