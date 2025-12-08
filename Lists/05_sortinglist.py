# thislist = ["watermelon", "banana", "orange", "kiwi", "mango"]
# thislist.sort()
# print(thislist)

# #numerical sort
# numlist =[100, 50, 65, 82, 23   ]
# numlist.sort()
# print(numlist)

thislist = ["watermelon", "banana", "orange", "kiwi", "mango"]
thislist.sort()
print(thislist)

thislist =["orange","mango","kiwi", "orange", "kiwi", "mango"]
thislist.sort(reverse = True)
print(thislist)

def myfunc(n):
    return abs(n-50)
thislist = [100,39,59,35,65]
thislist.sort(key = myfunc)
print(thislist)

# -----------------list revision -------------------


