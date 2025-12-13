# #average of 3 numbers
# def average(a,b,c):
#     sum = a+b+c
#     avg = sum/3
#     print(avg)
#     return avg

# class mynumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
    
#     def __next__(self):
#         x = self.a
#         self.a +=1
#         return x
    
# myclass = mynumbers()
# myiter = iter(myclass)

# print(next(myiter))

# def unpck(a,b,c):
#     return a+b+c
# numbers =[1,2,3]
# result = unpck(*numbers)
# print(result)

# def myfunc(fname,lname):
#     print("hello",fname,lname)

# person ={"fname": "Rohan" ,"lname" :"Ankit"}
# myfunc(**person)

#Recursive functions
# def countdown(n):
#     if n== 0:
#         print("Done")
#     else:
#         print(n)
#         countdown(n-1)

# countdown(5)

# def countup(n, limit):
#     if n > limit:
#         print("Done")
#     else:
#         print(n)
#         countup(n + 1, limit)

# countup(10)

# def power(base,exp =2):
#     return base **exp

# print(power(3))
# print(power(3,3))

# def factorial(n):
#     if n==1:
#         return(1)
#     else:
#         return n*factorial(n-1)

# print(factorial(5))

#====fibonacci series
# def fib(n):
#     if n<=1:
#         return
#     else:
#         return fib(n-1) +fib(n-2)

# for i in range(6):
#     print(fib(i))


# #reverse a string
# def reverse(s):
#     if len(s) ==0:
#         return s
#     else:
#         return reverse(s[1:]) + s[0]
    
# print(reverse("mohit"))
# print(reverse("arjun"))


#Finding maximum
# def find_max(lst):
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         max_rest = find_max(lst[1:])
#         return lst[0] if lst[0] < max_rest else max_rest

# print(find_max([2,,5,6,77,3,59]))


def find_max(lst):
    if len(lst) == l:
        return lst[0]
    else:
        max_rest = find_max(lst[1:])
        return lst[0] if lst[0] < max_rest else max_rest

print( find_max([2,3,5,6,7]))

def countdown(n):
    if n == 0:
        print("Done")
    else:
        print(n)
        countdown(n-1)

#count digits
# 
def count_digits(n):
    if n == 0:
        return 0
    else:
        return 1 + count_digits(n//10)
    
print(count_digits(1235678))
print(count_digits(165456144456))

#--------
def find_min(lst):
    if len(lst) == 1:
        return lst[0]
    min_rest =find_min(lst[1:])
    return lst[0] if lst[0] < min_rest else min_rest

# print(find_min([76,5,6,6,5,7]))
# fruits = ["apple", "banana", "cherry"]
# for fruits in fruits:
#     print(fruits)

# print(find_min([34,2,5,6,7,1]))
# print(find_min([65,7,65,756,78]))
# print(find_min([3,5,7,2,8,0]))
# print(find_min([23,45,67,89,12,4]))
# print(find_min([90,34,23,12,45,67 ]))
# print(find_min([11,22,33,44,55,66  ]))
# print(find_min([9,8,7,6,5,4,3,2,1 ]))
# print(find_min([100,200,50,600,300 ]))


# def count_digits(n):
#     if n==0:
#         return 0
#     else:
#         return 1 + count_digits(n//10)
#         print(count_digits(12345))
#         print(count_digits(67890))
        