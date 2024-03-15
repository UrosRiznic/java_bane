class Employee:

    raise_amount = 1.00
    
    def __init__(self, first_name: str, last_name: str, salary: int):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def __str__(self):
        return f"""        First name : {self.first_name}
        Last name: {self.last_name}
        Salary: {self.salary}
        """

    def say_hello(self):
        print("Hell, im Employee class")

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)
        print(f"Salary has been raised {self.raise_amount} times.")

    # Class metoda - > po difoltu uzima klasu kao difoltni argument
    # Class Metode mozemo da pozovemo bez instanciranja klase.
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, employee_str):
        first_name, last_name, salary = employee_str.split('-')
        return cls(first_name, last_name, salary)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return "It is not a Workday"
        else:
            return "It is Workday"

    # Property omogucava da pristupim metodi kao da je atribut (str vrednost ovde)
    @property
    def email(self):
        return f"{self.first_name}.{self.last_name}@company.com".lower()

    @property
    def fullname(self):
        return f"{self.first_name}.{self.last_name}"

    @fullname.setter
    def fullname(self, name):
        self.first_name, self.last_name = name.split(' ')


 