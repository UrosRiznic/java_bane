import datetime
from oop1 import Employee
from oop11 import Developer

def main():
    emp_1 = Employee("Uros", "Riznic", 100000)
    emp_2 = Employee("Marko", "Markovic", 90000)
    dev_01 = Developer("Stefan", "Stefanovic", 100000, "Software Developer")
    Employee.set_raise_amount(1.05)
    #print(emp_1)

    my_date = datetime.date(2022, 12, 19)
    #print(Employee.is_workday(my_date))

    

if __name__ == "__main__":
    main()