class Person:
    def __init__(self,name,id,salary,department):
        self.name=name
        self.id = id
        self.salary=salary
        self.department=department
        
    def assign_department(self):
        x = str(input("是否更換部門(請輸入是or否):"))
        if x == "是":
            Change = input("更改部門:")
            self.department=Change
        else:
            self.department=self.department

    def print_employee_details(self):
        print(self.name,self.id,self.salary,self.department)

    def calculate_emp_salary(self):
        hour = int(input("時數:"))
        if hour > 50:
            overtime = hour - 50
            overtime_amount = self.salary+(overtime * (self.salary / 50))
            print("加薪後:",overtime_amount)
        else:
            print("薪水:",self.salary)

Person1 = Person("ADAMS", "E7876", 50000, "ACCOUNTING")
Person2 = Person("JONES", "E7499", 45000, "RESEARCH")
Person3 = Person("MARTIN", "E7900", 50000, "SALES")
Person4 = Person("SMITH", "E7698", 55000, "OPERATIONS")

Person1.assign_department()
Person1.print_employee_details()
Person1.calculate_emp_salary()

Person2.assign_department()
Person2.print_employee_details()
Person2.calculate_emp_salary()

Person3.assign_department()
Person3.print_employee_details()
Person3.calculate_emp_salary()

Person4.assign_department()
Person4.print_employee_details()
Person4.calculate_emp_salary()
