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


def add(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(add(5,6,7,8))

# def add(*numbers):
#     total = 0
#     for num in numbers:
#         total +=num
#     return total
# print(myfunc(2,5,6,7))

# ---------python scope

def my_func():
    x =300
    def myinnerfunc():
        print(x)
    myinnerfunc()
my_func()

def myfunc():
    x = 300
    def myfunction():
        print(x)
    myfunction()
myfunc()

#------------deocrators
def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def myfunc():
    return "Hello world"

print(myfunc)

def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def myfunction():
    return "Hello sally"

@changecase
def otherfunction():
    return "i am speeed"

print(myfunction())
print(otherfunction())