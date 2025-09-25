import matplotlib.pyplot as plt

days = [1,2,3,4,5]
sales = [50,60,55,70,65]

plt.plot(days,sales,marker='o')
plt.title("Sales over 5 days")
plt.xlabel("Day")
plt.ylabel("Unit Sold")
plt.show()

products = ["Bread","Milk","Eggs"]
unit_sold = [300,220,180]

plt.bar(products, unit_sold, color=['blue','green','orange'])

# plt.title("Sales over 5 days")
# plt.xlabel("Unit sold per product")
# plt.ylabel("Units")
# plt.show()

