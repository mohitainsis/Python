#program to check prime number(primer number are those number who divides only by themselves)
#these numbers only diveded by themselves (gives remainder 0)

num = 55
if num/num == 0:
    print("This is a prime number ")
else:
    print("condition didnt start")

odd = int(input("Enter any number "))
if odd % 2 != 0:
    print("This is odd number ", odd)
else:
    print("This is even number ")


num = 11
num2 =41
if num<1:
    print("Number is not prime ")
else:
    for i in  range(2,11):
        if num%i == 0:
            print("Number is not prime ")
            break
    else:
        print(num,"This is prime")

num = int(input("Enter your 1st number "))
num2 = int(input("Enter your 2nd number "))
for i in (num,num2):
    if i in range(2,)
