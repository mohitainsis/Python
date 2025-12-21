#-----------program to sum even numbers
int = int(input("Enter your number "))
total = 0
for num in range(1,int+1):
    if num%2==0:
        total=total+num
print(total)

#---------------best practice
n = int(input("Enter your number: "))
total = 0

for num in range(1, n + 1):
    if num % 2 == 0:
        total += num

print(total)

