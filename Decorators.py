#1 Decorators

# Decorators in python is way to modify and enhanced the functionality of function without changing their
#original source code. decorators wrap the function in another function and allows to modify another function.


def decor(fun):
    B = 20
    def inner():
        A = fun()
        C = A + B
        print(C)
        return C
    return inner

def fun():
    return 10

obj = decor(fun)
obj()


#2
def emp_name():
    emp_Name = ["A","B","C","D","E"]
    return emp_Name

def emp_number():
    total_emp = [i+1 for i in range(5)]
    return total_emp

def total(emp_name,emp_number):
    A = emp_name()
    B = emp_number()
    for i, n in zip(A, B):
        print(i,n)

obj1 = total(emp_name,emp_number)


"""3) List and Dict Comprehansios"""
# list and dict comprehensions are concise and powerfull construct that allows to develove or
# create new list or dict in single line respectively based on existing sequence and iterable
#they provide expressive to transfer data



A=[i+1 for i in range(10)]
print(A)
B = [n if n%2 == 0 else "Odd" for n in range(10)]
print(B)

C= {c:(c if c%3==0 else "Even") for c in range(10)}
print(C)

"""3) Lambda function and anonymous function"""
print("-------------------------------------------------------------------------------------------------------")

values = lambda x,y:x+y
print(values(5,6))

print("-------------------------------------------------------------------------------------------------------")

"""Que - iterate even number using lambda fun"""

X = filter(lambda x:x%2 == 0, range(10))
for i in X:
    print(i)

"""4)  Deep copy and Shalow Copy"""

import copy

Z = [1, 2, [3, 4], 5]

X = copy.deepcopy(Z)
X.insert(5,6)
print(X)
print(Z)

Q = copy.copy(Z)

Q[2][1]= 30
print(Q)
print(Z)

Z= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("------------------------------")

"""Generators"""
#Ex.1
def yen():
    for i in range(10+1):
        if i%2==0:
            yield i

obj=yen()
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))

for u in obj:
    print(u)
print("-----------------------------------------")

#ex.2
def fun(j,l):
    yield (j+l)
    yield (j-l)

obj2=fun(5,6)
print(next(obj2))
print(next(obj2))
print("-----------------------------------------")

"""*args and **kwargs

*args allows function to accept number of non-key-worded arguments as tuple and **kwargs allows function to 
accept number of key-worded arguments as dict..both are providing a flexibility to use number of argument with 
single variable name 
"""

def my_fun(*args):
        print(args)
my_fun("avi","is","great")

print("-----------------------------------------")

def name(**kwargs):
    print(kwargs)

name(name="avi")

print("-----------------------------------------")

def my_arg(*args):
    for m in args:
        print(m)

my_arg("avi","ramesh","patil")
print("-----------------------------------------")

def my_arg2(**kwargs):
    for i,j in kwargs.items():
        print(i,":",j)

my_arg2(name="avinash",sirname="patil")
print("-----------------------------------------")

def my_kwarg(**kwargs):
    name=kwargs.get('nm','anonymous')
    age=kwargs.get('ag','unknown')
    print("this is my name",name,"and this is my age",age)

my_kwarg(nm="avi",ag=28)

print("-----------------------------------------")






