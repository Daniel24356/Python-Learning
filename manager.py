from employee import Employee

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department =  department

    def show_details(self):
        super().show_details()
        print(f"Your department is {self.department}")

    def calculate_bonus(self):
        return self.salary * 0.10    
