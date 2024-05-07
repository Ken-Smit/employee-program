
class Employee:
    def __init__(self, name, gender, hourly_pay_rate, emp_number):
        self.__name = name
        self.__gender = gender
        self.__hourly_pay_rate = hourly_pay_rate
        self.__emp_number = emp_number

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_gender(self, gender):
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.__hourly_pay_rate = hourly_pay_rate

    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate

    def set_emp_number(self, emp_number):
        self.__emp_number = emp_number

    def get_emp_number(self):
        return self.__emp_number


class ProductionWorker(Employee):
    def __init__(self, name, gender, hourly_pay_rate, emp_number, shift_number):
        super().__init__(name, gender, hourly_pay_rate, emp_number)
        self.__shift_number = shift_number

    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def get_shift_number(self):
        return self.__shift_number


class Main:
    @staticmethod
    def display_employee_info(employee):
        print(f"Employee Name: {employee.get_name()}")
        print(f"Employee Gender: {employee.get_gender()}")
        print(f"Hourly Pay Rate: ${employee.get_hourly_pay_rate():.2f}")
        print(f"Employee Number: {employee.get_emp_number()}")
        print()

    @staticmethod
    def display_production_worker_info(worker):
        Main.display_employee_info(worker)
        print(f"Shift Number: {worker.get_shift_number()}")
        print()

    @staticmethod
    def main():
        # Creating instances of Employee and ProductionWorker
        emp1 = Employee("John Doe", "Male", 20.50, "EMP001")
        emp2 = Employee("Alice Smith", "Female", 18.75, "EMP002")
        worker1 = ProductionWorker("Jane Johnson", "Female", 22.00, "EMP003", 1)
        worker2 = ProductionWorker("Bob Brown", "Male", 19.25, "EMP004", 2)

        # Displaying information
        print("Employee Information:")
        Main.display_employee_info(emp1)
        Main.display_employee_info(emp2)

        print("Production Worker Information:")
        Main.display_production_worker_info(worker1)
        Main.display_production_worker_info(worker2)


# Calling the main method to run the program
Main.main()
