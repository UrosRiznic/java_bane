from oop1 import Employee

class Developer(Employee):
    def __init__(self, first_name: str, last_name: str, salary: int, position: str):
        super().__init__(first_name, last_name, salary)
        self.position = position

