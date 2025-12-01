# # thisislist = [1, 2, 3, 4, 5]
# # print(thisislist)

# # #getting type of list
# # mylist = ["apple ", "banana", "cherry"]
# # print (type(mylist))

# # #Remove list items
# # a = ["12","apple","banana","mango"]
# # a.remove("banana")
# # print(len(a))

# # #pop method
# # a = ["12","apple","banana","mango"]
# # a.pop(1)
# # print(len(a))

# # #If item exists
# # a = ["12","apple","banana","mango"]
# # if "apple" in a:
# #     print ("yes," "apple is in the list")

# # #with
# # a = input("Enter your word: ")
# # if "orange" in a:
# #     print ("yes," "orange is in the list")
# # else:
# #     print("no","This is not present in the list")

# # b = "hello world"
# # print(b[2:5])

# # list = ["apple","banana","cherry","pineapple"]
# # print(list[2:5])


# # mylist = ["apple","banana","cherry"]
# # mylist.append("apple")
# # print(mylist)
# # mylist = ["apple","banana","cherry"]
# # mylist1 = ["mango","cherrry","limejuice","coconut"]
# # mylist.extend(mylist1)
# # print(mylist)

# #=--------revision TT
# thislist = ["apple","banana","mango"]
# print(type(thislist))

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[1:5])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# if "apple" in thislist:
#     print("yes apple is available")
# else:
#     print("no it is not available")

# data = [4, 2, 4, 5, 2, 7, 9, 7]
# unique = []
# for x in data:
#     if x not in unique:
#         unique.append(x)

# print("Original:", data)
# print("Unique:", unique)

# list = [1,2,3,5,6]
# list.append(8)
# print(list)

# list = [5,7,867,53,86]
# list.sort()
# print(list)

# #------string methods
# name = "john"
# replace = name.replace("john","anthony")
# print(replace)
# # print(name.replace("john","anthony"))
# capitalize = replace.capitalize()
# upper = name.upper()
# print(name)
# print(capitalize)
# print(upper)

# title ="hello world"
# print(title.startswith("hello"))

import time
timestamp =time.strftime("%H:%M:%S")
numeric = int(timestamp.replace(":",""))
print(numeric)
print(type(numeric))
time = int(input("Enter your time "))
if numeric>=8 and numeric<12:
    print("good morning")
elif numeric>=12 and numeric<1:
    print("good afternoon")
elif numeric>=17 and numeric<20:
    print("good evening")
else:
    print("good night")