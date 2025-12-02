# fruits = ("apple","banana","cherry")
# for x in fruits[2]:
#     print(x)
# for x in fruits:
#     print(x)
# for x in "banana":
#     print(x)

# #will stop when it gets banana
# fruits = ("apple", "cherry", "banana", "watermelon", "mango")
# for x in fruits:
#     print(x)
#     if x == "banana":
#         break

# fruits = ("apple","banana","watermelon","mango")
# for x in fruits:
#     if x=="banana":
#      print(x)
#      break


# fruits = ("apple", "banana","mango")
# for x in fruits:
#     if x == "banana":
#         continue
#     print(x)

# #range fuction
# for x in range(9):
#     print(x)
# #specifing the start value
# for x in range(2,5):
#     print(x)

# #specifying the increment by default 1 number increses
# #but you can specify the increment
# for x in range(2,10,2):
#     print(x)

# for x in range(20):
#     if x ==4:break
#     print(x)
# else:
#     print("the loop has ended")#usign break will not print else in bw

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
# for x in adj:
#     for y in fruits:
#         print(x,y)

# tuple =(1,2,3,5,65,67,7,87,5)
# num = int(input("Enter the number "))
# index = 0
# for x in tuple:
#     if x == num:
#         print("The number is found at index",tuple.index(num))
#         break
# else:
#     print("This number is not in the tuple")

# for x in range(100,1,-1):
#     print(x)
# i = 100
# while i>=0:
#     print(i)
#     i-=1

# i = 1
# num =int(input("Enter your number "))
# while i<=10:
#     print(num * i)
#     i += 1

# num = int(input("Enter your number "))
# for x in range(1,11):
#     print(x*num)

# colors = ["red","blue","orange","banana"]
# for word in colors:
#     print(word)
#     for i in word:
#         print(i)

# i = int(input("Enter the number to start "))
# while i<=20:
#     num =  int(input("Enter your number "))
#     if num<=10:
#         print("The number is less than 10",num )
#     else:
#         print("the number is greater than 10",num)
#     i+=1
# print("End of loop")

value = int(input("press any number to start "))
while value!=5:
    value = int(input("Enter the right number "))
    print("You are wrong try again")
print("End of the loop")
