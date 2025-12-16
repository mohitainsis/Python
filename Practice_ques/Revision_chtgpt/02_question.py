#counting the number without sum function using only for while

number = int(input("Enter your Number "))
count = 0

while number>0:
    number = number//10
    count = count + 1

print(count)
        
