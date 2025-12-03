def myfunc():
    return "hello from function"

msg = myfunc()
print(msg)

def myfunc1():
    return 1+2
sum_fn = myfunc1
print(sum_fn())

def myfunc(fname,lname):
    return fname,"  ",lname
name = myfunc
print("emil","karun")

name2 = myfunc
print("karun","sarun")

def my_function(name = "friend"):
    print("hello",name)

my_function("Emil")
my_function("tobias")
my_function()
my_function("linus")

#-------------------
def calc(a, b):
    return a + b, a - b

add_result, sub_result = calc(10, 3)
print("Add:", add_result)
print("Subtract:", sub_result)


def double(x):
    return x * 2

def triple_and_double(y):
    return double(y) + y * 3

print(triple_and_double(4))


def myfunc(country = "didnt tell"):
    print("hellow",country)

myfunc("norway")

def myfunc(owner,dog):
    print("i have a ",dog)
    print("i am the owner",owner)

myfunc(owner = "mohit",dog = "sheero")

# ----------positional arguments
def myfunc(owner,dog):
    print("i am ",owner)
    print("my pet name is",dog)

myfunc("naru","sheero")
#switching the order changes the result

def myfunc1(animal,age,dog):
    print("i have a pet ",dog)

def my_func(fruits):
    for fruit in fruits:
        print(fruit)
myfruits = ["apple","banana","cherry"]
my_func(myfruits)

myfruits = ["apple","bnann","mango"]
my_func(myfruits)

def my_func(person):
    print("name:",person["name"])
    print("age:",person["age"])

my_person ={"name":"Emil","age":25}
my_func(my_person)

def myfunction(x,y):
    return x+y

result = myfunction(5,3)
print(result)

def myfunc(fname):
    print(fname+ "refsnes")

myfunc("Emil")
myfunc("Tobias")
myfunc("linus")

def my_function(country ="norway"):
    print("i am from",country)

my_function("sweden")
my_function("india")
my_function()
my_function("brazil")

def my_function(country ="norway"):
    print("i am from ",country)

my_function("sweden")
my_function("india")
my_function()
my_function("brazil")

def my_function(animal,name,age):
    print("i have ",age,"year old",animal,"named",name)

my_function("dog",name = "buddy",age =5)


