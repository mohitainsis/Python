# # def greet():
# #     print("you called a function")
# # greet() 

# # def welcome():
# #     print("welcome you ran a funciton")
# #     return("you can run it again")

# # welcome()

# # def add(a,b):
# #     print(a+b)
# #     return("the number has been added")
# # print(add(2,3))

# def my_function(fname):
#   print(fname + " Refsnes")
# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

# def my_function(name,lname):
#     print(name,lname, "hello")

# my_function("mohit","verma")
# def myfunc (animal,name):
#     print("my animal is",name)
#     print("i have a", animal)
# myfunc(animal = "dog", name ="harry")

# #----------------
# def square(number): #------this is parameter in parenthesis
#     return(number ** 2)

# result = square(5)
# print(result)
# #this the right way to create or use a function use return to return the valueso that
# #the value doesnt directly get print in in the console 
# #use a variable to store the value of the parameters 

# #function with 2 parameters
# def add(num1,num2):
#     return(num1+num2)

# result = (2,5)
# print(result)

# #example to learn

# def multiply(p1,p2):
#     return(p1*p2)

# result = multiply(8,5)
# # result = multiply('b',5)
# # result = multiply(5,'b')
# print(result)

# def myfunc(a1,a2):
#     return(a1*a2)

# result = myfunc(3,5)
# print(result)

# def myfunc(animal,name):
#     print("I have a",animal)
#     print("My" , animal + "s name  is", name)

# myfunc(name = "Buddy", animal = "dog") 

# def find_max(mylist):
#     if len (mylist)==1:
#         return mylist[0]
    
# print(find_max([2,5,3]))
   
# def my_function(a,b,/,*,c,d):
#     return a+b+c+d
# result = my_function(5,10,c=15,d =20)
# print(result)

# def add(a,b,/):
#     return a+b

# print(add(5,10))

# def multiply(*,x,y):
#     return x*y

# print(multiply(x=5,y=5))

# def myfunc(greeting,*names):
#     for name in names:
#         print(greeting,name)

# myfunc("hello","Emil","Tobias","linus")

# def cube(num):
#     return num**3

# cube = lambda x:x**3
# print(cube(3))

# # def myfunc(x,y):
# #     return x*y
# # result = (myfunc(6,7))
# # print(result)
# # print(myfunc(6,'a'))
# # print(myfunc(5,7))


# def myfunc(*numbers):
#     total = 0
#     for num in numbers:
#         total +=num
#     return total

# print(myfunc(1,2,3))
# print(myfunc(10,20,40))
# print(myfunc(5))

# def myfunc(*numbers):
#     if len(numbers)==0:
#         return None
#     max_num = numbers[0]
#     for num in numbers:
#         if num>max_num:
#             max_num = num
#     return max_num

# print(myfunc(2,5,6,7,1))

# def myfunc(username,**details):
#     print("username",username)
#     print("addtional details")
#     for key, value in details.items():
#         print("",key + ":",value)
# myfunc("emil",age=25, city ="oslo",hobby = "coding")

# def myfunc(a,b,c):
#     return a+b+c

# numbers = [1,2,3]
# result =myfunc(*numbers)
# print(result)
 

# def sum_all(x,num):
#     return x+num

# x = int(input("Enter your number :"))
# num = int(input("Enter your 2nd number: "))
# result = sum_all()
# print(result)


# def my_function(animal,name):
#     print("i have a",animal)
#     print("my",animal + "'s name is",name)

# my_function("dog",'buddy')
# my_function("dog","cat")

# def my_function(animal,name,age):
#     print("i have a ",age,"year old",animal,"named",name)

# my_function("dog",name = "buddy",age = 5)

#-------------------------

# def my_function(fruits):
#     for fruit in fruits:
#         print(fruit)

# my_fruits = ["apple","banana","cherry"]
# my_function(my_fruits)

# def my_function(person):
#     print("name:",person["name"])
#     print("age:",person ["age"])

# my_person ={"name":"emil","age":24}
# my_function(my_person)

# #------------combination ofmixing and positional arguments
# def my_function(animal,name,age):
#    print("i have a ",age, "year old", animal, "named",name)

# my_function("dog",name = "buddy",age = 5)