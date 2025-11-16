thisislist = [1, 2, 3, 4, 5]
print(thisislist)

#getting type of list
mylist = ["apple ", "banana", "cherry"]
print (type(mylist))

#Remove list items
a = ["12","apple","banana","mango"]
a.remove("banana")
print(len(a))

#pop method
a = ["12","apple","banana","mango"]
a.pop(1)
print(len(a))

#If item exists
a = ["12","apple","banana","mango"]
if "apple" in a:
    print ("yes," "apple is in the list")

#with
a = input("Enter your word: ")
if "orange" in a:
    print ("yes," "orange is in the list")
else:
    print("no","This is not present in the list")

b = "hello world"
print(b[2:5])

list = ["apple","banana","cherry","pineapple"]
print(list[2:5])


mylist = ["apple","banana","cherry"]
mylist.append("apple")
print(mylist)
mylist = ["apple","banana","cherry"]
mylist1 = ["mango","cherrry","limejuice","coconut"]
mylist.extend(mylist1)
print(mylist)

