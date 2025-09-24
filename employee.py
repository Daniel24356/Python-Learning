class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Your name is {self.name}") 
        print(f"Your salary is {self.salary}")   