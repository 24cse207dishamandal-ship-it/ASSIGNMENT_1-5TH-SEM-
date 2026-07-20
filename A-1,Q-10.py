class Employee:

    def __init__(self):
        self.empid = int(input("Enter Employee ID: "))
        self.name = input("Enter Employee Name: ")
        self.basic_pay = float(input("Enter Basic Pay: "))
        self.ta = float(input("Enter TA: "))
        self.da = float(input("Enter DA: "))

    def calc(self):
        self.gross_pay = self.basic_pay + (0.10 * self.ta) + (0.40 * self.da)

    def display(self):
        print("\nEmployee Details")
        print("Employee ID:", self.empid)
        print("Employee Name:", self.name)
        print("Basic Pay:", self.basic_pay)
        print("TA:", self.ta)
        print("DA:", self.da)
        print("Gross Pay:", self.gross_pay)


e = Employee()
e.calc()
e.display()
