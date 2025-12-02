# i = 1
# while i<9:
#     print(i)
#     i = i+1
#     if i ==3:
#         print(i)
#         break

# i = 1
# while i<9:
#     print(i)
#     i = i+1
#     if i==4:
#         break
    
# i = 1
# while i<9:
#     print(i)
#     i =i+1
#     if i ==3:
#         continue
#         print(i)
    
# i =0
# while i<9:
#     i=i+1
#     if i==3:
#         continue
    
#     print(i)

# i = 1
# while i<9:
#      print(i)
#      i =i+1  
# else:
#     print("out of loop")

# i = [1,2,5,6,87,89,90]

# index = 0
# while index < len(i):
#     print(i[index])
#     index += 1

# n = int(input("Enter your number "))
# i = 1
# while i<=10:
#     print(n*i)
#     i += 1

# i = 1
# while i<=5:
#     if (i == 3):
#         i += 1
#         continue
#     print(i)
#     i += 1

# num = [3,6,67,78,534,34,6,7]
# num.sort()
# find = 78
# for x in num:
#     if x == find:
#         print("found at index",x)
#         break
#     print(x)


# i = int(input("Enter the number to start "))
# while i<=20:
#     num =  int(input("Enter your number "))
#     if num<=10:
#         print("The number is less than 10",num )
#     else:
#         print("the number is greater than 10",num)
#     i+=1
# print("End of loop")

# value = int(input("press any number to start "))
# while value!=5:
#     value = int(input("Enter the right number "))
#     print("You are wrong try again")
# print("End of the loop")

table = range(1,11)
for i in table:
    if i==6:
        break
    print("5 X",i,"=",5*i)