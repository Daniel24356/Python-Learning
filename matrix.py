import numpy as np


# A = np.array([[1,2], [3,4]]) # 2 - D
# B = np.array([5,6], [7,8])
# print(A + B)
# print(2 * A)
# print(A.T)
# print(A.dot(B))
# print(np.linalg.det(A))
# print(np.linalg.inv(A))

arr = np.array([1,2,3,4]) #1 - D
arr = np.array((45)) #0 - D
print(arr)
print(arr.ndim)
arr = np.array([1,2,3,4], ndmin=6)
print(arr.ndim)

fruits = np.array(["mango","apple","lemon"])
print(fruits.dtype)

arr = np.array([10,20,30,40,50])
newArr = arr.asType('i')
print(newArr)
print(newArr.dtype)

arr = np.array([[1,2], [3,4], [40,30,50]]) # 3 - D
print(arr.shape)
print(arr.size)

print(arr[0,0])

print(np.random.rand(1,10))

sales = np.array([
    [50,30,20],
    [60,20,10],
    [94,15,60],
    [78,88,22],
    [36,30,8]
])

print("Total sales \n", sales)
print("Total per product",sales.sum(axis = 1))
print("Average egg per day",sales[::,2].mean())

days = [1,2,3,4,5]
sales = [50,60,55,70,65]

plt.plot(days,sales,marker='o')
plt.title("Sales over 5 days")
plt.xlabel("Day")
plt.ylabel("Unit Sold")
plt.show()
 


