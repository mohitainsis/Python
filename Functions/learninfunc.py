# def isgreater(a,b):
#     if a>b:
#         print("a is greater")
#     else:
#         print("b is greater or equal to ")

# isgreater(5,6)
# a = 14
# b = 20
# isgreater(a,b)   

# def myname(fname,middlename ="john", lname="verma"):
#     print("hello",fname,middlename,lname)

# myname("ron")

# def avg(a,b,c):
#     print((a+b+c)/3)

# avg(5,6,7)

# def average(*numbers):
#     sum = 0
#     for i in numbers:
#         sum = sum+i
#         print(sum)
#     return "Average is ",6
#     print("Average is: ",sum / len(numbers))


# avg = average(5,5,5)
# print(avg)
# average(5,6,7,7)

# def myfunc(a,b,c):
#     print(a,b,c)

# numbers = [1,2,3]
# # result = myfunc(*numbers)
# print(*numbers)

# var1 = "this is global variable"
# def func():
#     var2 = "this is local variable"
#     print(var2)
#     print(var1)

# print(var1)
# # print(var2)
# func()

# def myfunc():
#     x = 200
#     def myinnerfunc():
#         print(x)
#     myinnerfunc()
    
# myfunc()

# x = 500
# def func():
#    global x
#    x = 100
#    print(x)
   
# func()
# print(x)
 
# def myfunc(numbers):
#    return numbers**2

# result = myfunc(5)
# print(result)

# def func(num1,num2):
#     sum = num1+num2
#     return sum

# result = func(2,4)
# print(result)

# def multiply(p1,p2):
#     return (p1*p2)

# result = multiply(2,2)
# print(result)


# import math
# def area(radius):
#     area = math.pi * radius * 2
#     circumference = 2*math.pi*radius
#     return area,circumference

# a,b = area(2)
# print("Area:",a,"circumference :",b)


# def func(name = "user"):
#     return "hello " + name

# print(func())

# def func():
#     for i in range(1,10):
#         print(i)
#         if i == 4 :
#            print(" 4 is found")
#     else:
#         print("the loop is completete")

# func()

a = int(input("Enter ur number : "))
for i in range(1,10):
    print(a*i)

