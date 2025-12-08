# thistuple = ("apple", "banana", "Mango", "banan")
# print(len(thistuple))
# print(type(thistuple))

# thistuple2 = ("kiwi")
# print(type(thistuple2))

#accessign typle items
# thistuple3 = ("apple", "banana", "cherry", "Mango", "banan")
# print(thistuple3[1])

# thistuple = ("apple", "banana", "cherry", "Mango", "banan")
# print(thistuple[1:3])
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-4:-1])

#change the value of the tuple
# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
# print(type(x))
# print(x)

#adding items in the tuple
# x = ("apple", "banana", "cherry")
# y = list(x)
# y.append("orange")
# x = tuple(y)
# print(x)

#unpackign a tuple
# fruits = ("apple", "banana", "cherry")
# (green, yellow, red) = fruits
# print(green)

#checking if the tuple exist or not
# thistuple = ("apple","banana","banana","mango")
# x = input("Enter you fav fruit: ")
# if x in thistuple:
#     print("yes ths is available")
# else:
#     print("no this is not present")
# #loop through the tuple
# thislist = ("apple","banana","mango")
# for x in thislist:
#   print(len(x))

# x = ("apple","mango","cherry")
# i = 0
# while i < len(x):
#    print("yes"[i])
#    i = i+1

#python built in method 
#count()
#index()
# x = ("apple","banana","cherry","apple")
# print(x.count("apple"))

#x is a tuple → it has built-in methods (functions that belong to it).
#You access them with a dot (.).
#count() means “count how many times something appears.”
#x.count("apple") = “Tell x to count how many times 'apple' appears.”

# x = ("apple","banana","mango","cherry")
# print(x.index("mango"))

tup = (1,5,6,7,7,7,56,5,5,5,5,5)
counttup = tup.count(5)
res = tup.index(5)
print("the number 5 is",counttup,"times")
print(res)
change = list(tup)
print(type(change))
print(type(tup))
