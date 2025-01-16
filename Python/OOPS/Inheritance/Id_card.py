class emp_id_card:
    def __init__(self):
        self.__emp_id = 0
        self.__emp_name = ""
        self.__emp_dept = ""
        self.__emp_desig = ""
        self.__emp_doj = ""

    def setEmp_id(self, emp_id):
        self.__emp_id = emp_id

    def getEmp_id(self):
        return self.__emp_id

    def setEmp_name(self, emp_name):
        self.__emp_name = emp_name

    def getEmp_name(self):
        return self.__emp_name

    def setEmp_dept(self, emp_dept):
        self.__emp_dept = emp_dept

    def getEmp_dept(self):
        return self.__emp_dept

    def setEmp_desig(self, emp_desig):
        self.__emp_desig = emp_desig

    def getEmp_desig(self):
        return self.__emp_desig

    def setEmp_doj(self, emp_doj):
        self.__emp_doj = emp_doj

    def getEmp_doj(self):
        return self.__emp_doj

    def display(self):
        print("Emp_id:", self.__emp_id)
        print("Emp_name:", self.__emp_name)
        print("Emp_dept:", self.__emp_dept)
        print("Emp_desig:", self.__emp_desig)
        print("Emp_doj:", self.__emp_doj)

# Example usage
e = emp_id_card()
e.setEmp_id(101)
e.setEmp_name("Sankar")
e.setEmp_dept("IT")
e.setEmp_desig("Software Engineer")
e.setEmp_doj("01-01-2021")
e.display()


#Output:
# Emp_id: 101
# Emp_name: Sankar
# Emp_dept: IT
# Emp_desig: Software Engineer
# Emp_doj: 01-01-2021
#In the above example, we have defined a class Emp_id_card
# with five private variables __emp_id, __emp_name, __emp_dept, __emp_desig, and __emp_doj.
# We have defined five methods setEmp_id(), getEmp_id(), setEmp_name(), getEmp_name(), setEmp_dept(), getEmp_dept(), setEmp_desig(), getEmp_desig(), setEmp_doj(), and getEmp_doj() to set and get the employee id, name, department, designation, and date of joining.
# We have defined a method display() to display the employee id, name, department, designation, and date of joining.
# We have created an object e of the class Emp_id_card and called the methods to set and get the employee id, name, department, designation, and date of joining.