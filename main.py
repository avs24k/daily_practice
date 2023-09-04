class Values():
    def __init__(self,A,B):
        self.value_a = A
        self.value_b  =B

class Add(Values):
    def total(self):
        C = self.value_a + self.value_b
        print(C)

obj = Add(2,3)
obj.total()

#########################################################################################3
# Parent class
class ParentClass:
    def par_func(self):
         print("I am parent class function")

# Child class
class ChildClass(ParentClass):
    def child_func(self):
         print("I am child class function")

# Driver code
obj1 = ChildClass()
obj1.par_func()
obj1.child_func()
##################################################################################################


class A():
    def __init__(self,value_a):
        self.Value_A = value_a

class B(A):
    def __init__(self,value_b,value_a):
        self.Value_B = value_b
        super().__init__(value_a)
class C(B):
    def __init__(self,value_c,value_b,value_a):
        self.Value_C = value_c
        super().__init__(value_b,value_a)

    def display(self):
        A_Name = "Name of value_a:",self.Value_A
        B_Name = "Name of value_b:",self.Value_B
        C_Name = "Name of value_c:",self.Value_C

        print(A_Name,B_Name,C_Name)
print("----------------------------------------------------------------------------")
obj=C("Parent","intermidate","child")
obj.display()
print(issubclass(B,C))



"""Empty Class"""
class EmptyClassDemo:
   pass
obj=EmptyClassDemo()
obj.sirname="patil"
print(obj.sirname)


func = lambda a, b : (a ** b)
print(func(float(10),20))

fruits = ("apple", "banana", "cherry")
print(len(fruits))





