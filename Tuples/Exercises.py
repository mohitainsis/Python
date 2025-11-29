# fruits = ("apple", "banana", "cherry")
# print(len(fruits))

# #2nd
# fruits = ("apple", "banana", "cherry")
# print(fruits[0])

# #3rd
# fruits = ("apple", "banana", "cherry")
# del fruits
# print(fruits)

# #4th
# fruits = ("apple","banana","mango","cherry")
# (x,*y,z) = fruits
# print(y)
# #in this x gets the first and z gets teh last the rest goes to y

# #5th
# for x in ("bananna","cherry", "mango"):
#     print(x)

# #6
# fruits = ("apple", "banana", "cherry")
# i = 0
# while i<len(fruits):
#     print(fruits [i])
#     i = i+1

# #7
# tuple1 = (1,2,3,5,6)
# tuple1 = tuple1*2
# print(tuple1)

# tuple1 = (1,2,3,5,6,76)
# result = tuple(x*2 for x in tuple1)
# print(result)

# tup = (1,2,5,6,7)
# print(len(tup))
# print(type(tup))
# print(tup[1:3])


'''
to find any particular value in the tuple
we can use index method ex..
'''
# tuple = ("apple","banana", 67)
# print(tuple.index("banana"))

#--------question
# movies = []
# movie1st = input("Enter your first  favorite movie:")
# movie2nd = input("Enter your second favorite movie :")
# movie3rd = input("Enter your third favorite movie :")

# movies.append(movie1st)
# movies.append(movie2nd)
# movies.append(movie3rd)

# print(movies)

#---------program to check if the word is palindrome or not
 
# list = [1,2,5]
# list_copy = list.copy()
# list_copy.reverse()

# if list_copy == list:
#     print("palindrome")
# else:
#     print("not palindrome")

#program to count the number of students with a grade

grade =["a","b","c","c","a","a"]
grade.sort()
print(grade)

