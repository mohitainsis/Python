num = int(input("enter your number : "))
if num % 2 == 0:
    print("Number is even ")
else:
    print("number is odd")

print(num)

a = int(input("Enter your first number : "))
b = int(input("Enter your second number :"))
c = int(input("Enter your third number :"))

if a>b and a>c:
    print("1st number is greater",a)

elif b>a and b>c:
    print("2nd number is greater",b)

else:
    print("3rd number is greater",c)

num = 14
if num % 7 ==0:
    print("number is multiple of 7")
else:
    print("it is not multiple of 7 ")
