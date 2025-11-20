# def myfunction(name = "no name"):
#     return name + "hello"
# #-----------------
# def calc_sum(a,b):
#     sum = a+b
#     print(sum)
#     return sum

# calc_sum(5,10)
# #---------------
# def print_hello():
#     print("hello world")

# print_hello()
#------------
# def average(a,b,c):
#     return (a+b+c) / 3

# result = average(1,2,3)
# print(result)

# def myfunc(animal,name):
#     print("i have a", animal)
#     print("My",animal,"name","is" ,name)
#     return animal , name

# result = myfunc(animal="dog",name="sheru")
# print(result)

# def my_function(animal, name, age):
#   print("I have a", age, "year old", animal, "named", name)

# my_function("dog", name = "Buddy", age = 5)

# def mydict(person):
#     print("name:",person["name"])
#     print("age:",person["age"])

# person ={"name":"ankit", "age":20}
# mydict(person)


#-----------args and kwargs

# def myfunc(*kids):
#     return ("the youngest child is ",kids[0])

# result = myfunc("Amit","rohan","manprett")
# print(result)

#--------------
# def myfunc(*args):
#     print(type(args))
#     print("first argument:",args[0])
#     print("second argument:",args[1])

# myfunc("rohan","mango","cherry","banana")


# def add(*numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total
# print(add(5,6,7,8))

# def add(*numbers):
#     total = 0
#     for num in numbers:
#         total +=num
#     return total
# print(myfunc(2,5,6,7))

# ---------python scope

# def my_func():
#     x =300
#     def myinnerfunc():
#         print(x)
#     myinnerfunc()
# my_func()

# def myfunc():
#     x = 300
#     def myfunction():
#         print(x)
#     myfunction()
# myfunc()

# #------------deocrators
# def changecase(func):
#     def myinner():
#         return func().upper()
#     return myinner

# @changecase
# def myfunc():
#     return "Hello world"

# print(myfunc)

# def changecase(func):
#     def myinner():
#         return func().upper()
#     return myinner

# @changecase
# def myfunction():
#     return "Hello sally"

# @changecase
# def otherfunction():
#     return "i am speeed"

# print(myfunction())
# print(otherfunction())

def changecase(func):
    def myinner(x):
        return func(x).upper()
    return myinner

@changecase
def myfunction(nam):
    return "hello" + nam

print(myfunction("john"))

#-----------------python arrays

matrix = [
    [1,2,4],
    [1,44,5],
    [5,6,7]
]

print(matrix [1][2])

def find_min(lst):
    if len(lst) == 1:
        return lst[0]
    min_rest =find_min(lst[1:])
    return lst[0] if lst[0] < min_rest else min_rest

print(find_min([76,5,6,6,5,7]))
fruits = ["apple", "banana", "cherry"]
for fruits in fruits:
    print(fruits)

#-----------------
def myfunc(a,b):
    return(a+b)

sum = myfunc(1,6)
print(sum)

print(myfunc(5,8))


#---------------------
#calculating the average of 3 numbers functions
def myfunc(a,b,c):
    sum = a+b+c
    avg = sum / 3
    print(avg)
    return avg

myfunc(78,90,56)

#-------------built in functions
#print()
# len()
# type()
# range()

print("hellow world","world 2nd")
print("hello khapra")
def find_min(lst):
    if len(lst) == 1:
        return lst[0]
    min_rest =find_min(lst[1:])
    return lst[0] if lst[0] < min_rest else min_rest

print(find_min([76,5,6,6,5,7]))
fruits = ["apple", "banana", "cherry"]
for fruits in fruits:
    print(fruits)

#-----------------------------------------------------
# default values

default_country ="norway"
print("i am from",default_country)
def myfunc(country = default_country):
    print("i am from",country)