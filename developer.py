#when an object takes or behave many forms is know as polimophism

from employee import Employee

class Developer(Employee):
    def __init__(self, name, salary, languange):
        super().__init__(name, salary)
        self.language = languange

    def show_details(self):
        super().show_details()
        print(f"The language you use is {self.language}")

    def calculate_bonus(self):
        return self.salary * 0.15


