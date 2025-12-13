# cities =["gurgao","noida","delhi","chennai"]
# def myfunc(cities):
#     print(len(cities))

# cities =["delhi","gurgao","noida","puna"]
# heroes = ["mspiderman","captain america"]

# print(heroes[0],end = "")
# print(heroes[1],end = "")

# # def print_len(list):
# #     print(len(list))


# # n = 5
# # fact = 1
# # for i in range (1,n+1):
# #     fact =  i*fact
# # print(fact)

# #write a function to convert usd to inr

def print_len(list):
    print(len(list))

n = 5
fact = 1
for i in range (1,n+1):
    fact = i*fact
    print(fact)

# write a function to conver usd to inr 
def usd_to_inr(usd):
    inr = usd * 82.74
    return inr

amount_in_usd = 100

print("amountin irn:",amount_in_usd)

converted_amount = usd_to_inr(amount_in_usd)
print("converted amount in inr:",converted_amount)


def myfunc(country = "norway"):
    print("i am from ",country)
    myfunc("sweden")
    myfunc("india")
    myfunc()

myfunc("brazil")

def find_index(lst,element):
    for index, item in enumerate(lst):
        if item == element:
         return index
    return -1

print(find_index ([1,2,3,4,5],3))

#----------finding the sum of even numbers
def sum_even_numbers(lst):
    total = 0
    for num in lst:
       if num % 2 == 0:
          total += num
    return total

print(sum([1,2,3,3,5,6,6,7]))
   