# import datetime
# from message import get_user_name
# import platform

# # print(get_user_name("Daniel"))
# # pf = platform.system()
# # print(pf)
# # pf = dir(platform)
# # print(pf)

# # print(user["age"])
# dt = datetime.datetime.now()
# print(dt.year)
# print(dt.hour)
# print(dt.second)
# print(dt.strftime("%d"))

from bankAccount import BankAccount
from calculator import Calculator
from developer import Developer
from manager import Manager

m = Manager("Mike", 30000, "HR")
d = Developer("Daniel", 50000, "Python")

m.show_details()
print("Manager Bonus",m.calculate_bonus())

d.show_details()
print("Developers Bonus", d.calculate_bonus())

acc = BankAccount('Daniel', 5000)
acc.deposit(2000)
print(acc.get__balance())
print(acc.owner)

calc = Calculator()
print(calc.add(2,3))
print(calc.add(2,3,6,8))
print(calc.add(2,3,1,4,6,7,8))
