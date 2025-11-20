'''class Employee, name ,salary,city
view the name, salary, city'''
class Employee:
    empcount=0
    def __init__(self,name,salary,city):
        self.name=name
        self.salary=salary
        self.city=city
        Employee.empcount+=1

    def printEmployeeName(self):
        print(f"Name of the Employee is ",self.name)
    def printEmployeeSalary(self):
        print(f"SAlary of the Employee is ",self.salary)
    def printEmployeeCity(self):
        print(f"City of the Employee is ",self.city)
    
Emp1 = Employee('JAck',100000,'Singapore')
Emp2 = Employee('Jones',200000,'London')
Emp3 = Employee('Jordan',300000,'Paris')



print(Emp1.empcount)
'''
print(Emp1.printEmployeeName())  
print(Emp1.printEmployeeSalary())
print(Emp1.printEmployeeCity())    


print(Emp2.printEmployeeName())  
print(Emp2.printEmployeeSalary())
print(Emp2.printEmployeeCity())    

print(Emp3.printEmployeeName())  
print(Emp3.printEmployeeSalary())
print(Emp3.printEmployeeCity())    
'''

    