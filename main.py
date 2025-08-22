import datetime
from message import get_user_name
import platform

# print(get_user_name("Daniel"))
# pf = platform.system()
# print(pf)
# pf = dir(platform)
# print(pf)

# print(user["age"])
dt = datetime.datetime.now()
print(dt.year)
print(dt.hour)
print(dt.second)
print(dt.strftime("%d"))

