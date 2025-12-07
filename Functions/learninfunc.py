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

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum+i
    print("Average is: ",sum / len(numbers))

average(5,6,76,8)