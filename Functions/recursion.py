def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(4))
fact = factorial(int(input("Enter your number: ")))
# fact = int(input("Enter your number : "))
# print("The factorial of your number is: ",fact)
print(fact)

