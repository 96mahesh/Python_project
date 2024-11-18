# Approach 1
import sys
sys.path.append("C:/Users/Admin/PycharmProjects/pythonProject/Day9/PackageA")
sys.path.append("C:/Users/Admin/PycharmProjects/pythonProject/Day9/PackageB")
# import Emp;
#
# empobj = Emp.Employe(101,"Mahesh",95000);
# empobj.displayEmp()
#
# import std
#
# stdobj = std.Student(111,"Pawan",'A')
# stdobj.displayStd()


# Approach 1
from Emp import Employe
empobj = Employe(101,"Mahesh",95000)
empobj.displayEmp()

from std import Student
stdobj =  Student(111,"Pawan",'A')
stdobj.displayStd()
