'''
Using any object oriented language, please define a class model to implement the following specification:
A company has a staffing model which includes Employees, Contractors, and Temporaries.
'''

class Employee():

    def __init__(self, first_name, last_name, pay, vacation_days=0):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.vacation_days = vacation_days

    def get_name(self):
        return "{}, {}".format(self.last_name,self.first_name)

    def get_pay_rate(self):
        return ((self.pay)/24)

    def get_yearly_vacation(self):
        return (self.pay * self.vacation_days)

emp1 = Employee("Permanent", "Employee", 1000, 20)
print emp1.get_name()
print emp1.get_pay_rate()
print emp1.get_yearly_vacation()

class Contractor(Employee):

    def __init__(self, first_name, last_name, pay, agency_name):
        Employee.__init__(self,first_name, last_name, pay)
        # super().__init__(first_name, last_name, pay)
        self.agency_name = agency_name

    def get_agency(self):
        return self.agency_name

    def get_name(self):
        return "{}, {} [C]".format(self.last_name, self.first_name)



c1 = Contractor("Contract", "Employee", 500, agency_name="XYZ")
print c1.get_name()
print c1.get_pay_rate()
print c1.get_yearly_vacation()
print c1.get_agency()

class Temporary(Contractor):

    def __init__(self, first_name, last_name, pay, agency_name):
        Contractor.__init__(self,first_name, last_name, pay, agency_name)

    def get_name(self):
        return "{}, {} [T]".format(self.last_name, self.first_name)



t1 = Temporary("Temporary", "Employee", 300, agency_name="ABC")
print t1.get_name()
print t1.get_pay_rate()
print t1.get_yearly_vacation()
print t1.get_agency()

