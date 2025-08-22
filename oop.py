class Info():
    greet = "How you doin'?"
    num = 500

info1 = Info()
print(info1.num)

class Person():
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName 
        
    
    def __str__(self):
        return f"Fullname: {self.firstName} {self.lastName}"

p1 = Person("Korede", "Zion")
print(p1)   # → Fullname: Korede Zion

class Laptop():
    def __init__(self, model, make, year,):
        self.model = model
        self.make = make
        self.year = year

    def __str__(self):
        return f"{self.make}, {self.model}, {self.year}"
    
laptop1 = Laptop("Victus", "HP", 2025)   
laptop2 = Laptop("Probook", "HP", 2022)   
laptop3 = Laptop("Omen", "HP", 2014)   
laptop4 = Laptop("Pavilon", "HP", 2020)   
laptop5 = Laptop("Elitebook", "HP", 2017)   

print(laptop1)
print(laptop2)
print(laptop3)
print(laptop4)
# print(laptop5)
      