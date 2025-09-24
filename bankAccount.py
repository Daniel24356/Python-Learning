# Encapsulation is the process of bunding data (variables) and the methods (functions)
# that operate on that data into a single unit (class), while restricting direct access to the internal 
# details#

class BankAccount:
    def __init__(self,owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get__balance(self):
        return self.__balance        

      

        