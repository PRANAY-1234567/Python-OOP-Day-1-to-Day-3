# How to create Empty Class
'''class ClassName:
    pass'''

# How to create Object


'''class student:
    name = "Rohit"
    rno=32
    branch='CS'
s=student() ''' #s is an reference variable

#NameError: name 'name' is not defined
#Accsessing class data outside by using ClassName

'''print(student.name)
print(student.rno)
print(student.branch)'''

#Use this method
'''print(f'student name is {student.name}')
print(f'student rno is {student.rno}')
print(f'student branch is {student.branch}')

print(student.__dict__)

#ID ADDRESS
class Hii:
    x=100
    y=200
h=Hii()
h1=Hii()'''
''' 
1) If we done any modification in mainclass it will effected for both object 

syntax:----> ClassName.var_name=value

print("Before Modification Data")
print(Hii.x)
print(h.x)
print(h1.x)
print("After Modification Data")
Hii.x=700
print(Hii.x)
print(h.x)
print(h1.x)'''

'''
2)If We done any modification in one object it will won't effected 
for main class and other object 
Syntax:--> object.var_name=value

print("Before Modification in Object")
print(Hii.x)
print(h.x)
print(h1.x)

print("After Modification in Object")
h.x='Python'
print(Hii.x)
print(h.x)
print(h1.x)'''

'''
3) Again if we done any modification in main class
it will effected for main class and it will effected
for other object but it will won't effected for previous Modification object because
when we done separate modificationn it will create seperate memory
means we loss the connection
syntax :---> ClassName.var_name=value

Hii.x="SQl"
print(Hii.x)
print(h.x)
print(h1.x)'''

#================================DAY 2 for OOPS============================================
# class Employee:
#     """Employee Information"""  #DOC STRING-Discription of the class
#     name ="ABC"
#     role="Analytics"
#     eid="A123"
#     sal=24500
# e=Employee()
# '''print(Employee.__doc__)'''   #TO print doc string

# help(Employee)

#-------------Method------------
"""Method is a function present inside the class
Method will accept one parameter (Self)
class A:
     def spam(self):
     ....
a=A()
Methood Types-
1) Instance Method
* It is nothing but object 
* Instance method only working for object data
* A method it will accept first argument of an object address then we can call it as a Instance method
Syntax-
class ClassName:
     def method-name(self):
           Statement
object=ClassName()

way-01--> By using object
syntax
object.method_name()

way-2-->By using ClassName


2) class Method
3) static Method
A function is a block of code it will exectute when we call function name
Function will won't except any default parameter
"""
'''
class Evening:
    def demo(self):
        print("Welcome to all")

e=Evening()
#By calling Object
e.demo() #objecct.method_name()

#By calling ClassName
Evening.demo(e)'''

'''class Evening:
    def demo(self):
        print(self)

e=Evening()
print(e)
e.demo()'''

'''class Evening:
    def demo(x):
        print(x)

e=Evening()
print(e)
e.demo()'''

'''#Instace variable 
syntax-
       self.new_variable=value'''


'''class Student:
    def Information(self):
        self.name="XYZ"
        self.age=21
        self.Rno=101
        self.clg="ABC"
        print(f'Student name is {self.name}\n'
            f'Student current age is {self.age}\n'
            f'Student class roll no is {self.Rno}\n'
            f'Student college name is {self.clg}\n' )

s=Student()
s.Information()'''

'''class Bank:
    def AccountInformation(self,HolderName,acc_num,bank_name,bal):
        self.Holdername=HolderName
        self.acc_num=acc_num
        self.bank_name=bank_name
        self.bal=bal
        print(f'Account Hoder name is {self.Holdername}\n'
              f'account number is {self.acc_num}\n'
              f'Bank name is {self.bank_name}\n'
              f'Total Balance is {self.bal}')

b=Bank()
b.AccountInformation("ABC",12345,"Jai Hind",3045555)
print()
b.AccountInformation("CBI",1223345,"KAm",3345555)
print()'''



#==============================Day 3================

"""class Employee:
    name = 'ABC'
    age = 23
    def  information(self):
        print(f'employee name is {name}')
        print(f'Employee Current Age is {age}')
    e=Employee()
    e.information()"""

#HOW TO ACCESS CLASS VAIABLE INTO THE INSTANCE METHOD
# WAY 1
#BY USING OBJECT--------->SELF
#MANDATORY
'''
class Employee:
        name = 'ABC'
        age = 23
        def  information(self):
            print(f'employee name is {self.name}')
            print(f'Employee Current Age is {self.age}')
e=Employee()
e.information()'''



'''
NOT MANDATORY
class Employee:
        name = 'ABC'
        age = 23
        def  information(self):
            print(f'employee name is {e.name}')
            print(f'Employee Current Age is {e.age}')
e=Employee()
e.information()'''

#HOW TO ACCESS CLASS VAIABLE INTO THE INSTANCE METHOD
# WAY 2
#BY USING ClassName--------->Employee
'''class Employee:
        name = 'ABC' #classvariable
        age = 23
        def  information(self):#---->Instance method
            print(f'employee name is {Employee.name}')
            print(f'Employee Current Age is {Employee.age}')
e=Employee()
e.information()'''

'''class Amazon:
    product_name="Iphone" #class variable
    color = "white"#class variable
    Total_product = 3#class variable
    add="Pune"

    def Product_Information(self):
        print(f'My Product Name is {self.product_name}')
        print(f'My Product color is {self.product_name}')
        print(f'Total Product is {self.product_name}')

    def address(self):
        print(f'Current Address is {self.add}')

a=Amazon()
a.Product_Information()
print()
a.address()'''


'''#Class variable modification by using object
class Amazon:
    product_name="Iphone" #class variable
    color = "white"#class variable
    Total_product = 3#class variable
    add="Pune"

    def Product_Information(self):
        print(f'My Product Name is {self.product_name}')
        print(f'My Product color is {self.product_name}')
        print(f'Total Product is {self.Total_product}')

    def address(self):
        print(f'Current Address is {self.add}')

a=Amazon()
a.product_name='Laptop'
a.Total_product=30
a.Product_Information()
print()
a.address()'''

#Class variable modification by using ClassName
'''class Amazon:
    product_name="Iphone" #class variable
    color = "white"#class variable
    Total_product = 3#class variable
    add="Pune"

    def Product_Information(self):
        print(f'My Product Name is {self.product_name}')
        print(f'My Product color is {self.color}')
        print(f'Total Product is {self.Total_product}')

    def address(self):
        print(f'Current Address is {self.add}')

a=Amazon()
#Class_name=Value
Amazon.product_name='Mobile'
Amazon.color='Red'
Amazon.Total_product=300
a.Product_Information()
print()
a.address()'''