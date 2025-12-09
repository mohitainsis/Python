# '''join methods
# union adn update() = join all items from both sides
# intersection() = keeps only duplicates
# differnence() = keeps the items from the first set that are not in otherset
# symmeteric_difference() = keeps all items except the duplicates'''

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3= set1.union(set2)
# print(set3)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1.intersection(set2)
# print(set3)

# set1 = {1,2,3,5}
# set2 = {"apple","banana","cherry"}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}
# set5 = set1.union(set2,set3,set4)
# print(set5)

# set1 = {1,2,3,5}
# set2 = {"apple","banana","cherry"}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}
# myset = (set1 | set2 | set3 | set4)
# print(myset)

# # | this works same as union is the operator or union

# set2 = {"apple","banana","cherry"}
# set1 = ("apple","bananna","cherry")
# set3 = set2.union(set1)
# print(set3)

# #union doesnt change the original set it creates new if youwant to save the
# '''unions does not change the origingal set it returs a new set
# if you want to save changes in existing set use updat()
# otherwise use union but will have to create a new variable to storre the value
# '''
# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
# set1.update(set2)
# print(set1)

# #intersection returns a new set 
# #keep only duplicates
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.intersection(set2)
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.intersection_update(set2)
# print(set1)

# #frozenset
# set1 = frozenset({"apple", "banana", "cherry"})
# print(type(set1))


# set1 = {"apple", "banana", "cherry"}
# x = set1.copy()
# print(x)

cities={"delhi","mumbai","haryana","kolkata","pune"}
cities2={"pune","shimla","rajkot","malyalam"}
cities3 = cities.intersection(cities2)
print(cities3)
cities.remove("delhi")
print(cities)
print(len(cities))
