import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["John", "Korode", "Danile"],
    "Age": [25, 30, 28],
    "City": ["Rivers", "Imo", "Lagos"]
}

df = pd.DataFrame(data)
print(df)

school = {
    "Name": ["Mike", "David", "Daniel", "Korede", "Stephanie", "Frank"],
    "Study Hours": [5, 3, 8, 2, 7, 4],
    "Sleep Hours": [7, 6, 6, 5, 8, 7],
    "Score": [80, 60, 72, 55, 88, 72]
}

df = pd.DataFrame(school)
print(df)
# # print(df.info)
# # print(df.describe)

# df = pd.read_csv("data.csv")
# # print(df.head())
# # print("Data")
# # print(df.tail())
# print(df.shape)
# print(df["City"])


# df = pd.read_csv("car data.csv")
# print(df.info())
# print(df.describe())
# print(df.head())
# print(df["Year"])
# print(df.tail())
# print(df.shape)

# name= df["Car_Name"]
# year = df["Year"]

# plt.plot(name, year, marker='o')
# plt.title("Cars Produced over the Years")
# plt.ylabel("Year")
# plt.xlabel("Car Name")
# plt.show()

# print(df.isnull().sum())
# print(df["Age"].fillna(df["Age"].median(),inplace = True))
# print(df.drop('cabin', axis= 1, inplace= True))
# print(df["Embarked"].fillna(df["Embarked"].mode()[0], inplace= True))
# df["Sex"] = df["Sex"].map({"male":0},{"Female":1})
# df.drop(["PassengerId", "Ticket", "Name"], axis= 1, inplace=True)