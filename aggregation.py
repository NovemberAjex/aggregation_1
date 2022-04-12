class salary():
    def __init__(self,pay,annual_pay):
        self.pay  = pay
        self.annual_pay  = annual_pay

    def bonus_calc(self):
        self.bonus_1  = self.annual_pay - self.pay
        print(f"your bnous is {self.bonus_1}")
class emp():
    def __init__(self,name,age,salary):
        self.name  = name
        self.age = age
        self.obj_salary = salary
    def emp_salary(self):
        # return self.name,self.age
        return self.obj_salary.bonus_calc
s1 = salary(1000,12000)
s1.bonus_calc()
e1  = emp("ali",21,s1)
e1.emp_salary()

